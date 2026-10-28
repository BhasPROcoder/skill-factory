#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"

AGENT_CMD="${AGENT_CMD:-codex exec --full-auto}"
PROMPT="${1:-prompts/00-auto.md}"
MAX="${2:-500}"
SKIP_AUDIT="${SKIP_AUDIT:-1}"
LOG="logs/run.log"
FAILS=0

left() {
  case "$PROMPT" in
    *taxonomy*) python3 tools/sf.py remaining taxonomy ;;
    *generate*) python3 tools/sf.py remaining generate ;;
    *audit*) python3 tools/sf.py remaining audit ;;
    *)
      t=$(python3 tools/sf.py remaining taxonomy)
      g=$(python3 tools/sf.py remaining generate)
      a=0
      [ "$SKIP_AUDIT" = "1" ] || a=$(python3 tools/sf.py remaining audit)
      echo $((t + g + a)) ;;
  esac
}

for i in $(seq 1 "$MAX"); do
  if [ "$(left)" = "0" ]; then
    python3 tools/sf.py index --all >/dev/null && python3 tools/sf.py router
    echo "$(date '+%F %T') DONE" | tee -a "$LOG"; break
  fi
  echo "$(date '+%F %T') run $i — $(python3 tools/sf.py status | tail -1)" | tee -a "$LOG"
  if timeout 1800 $AGENT_CMD "$(cat "$PROMPT")" >>"$LOG" 2>&1; then
    FAILS=0
  else
    FAILS=$((FAILS + 1))
    echo "$(date '+%F %T') run $i failed ($FAILS in a row)" | tee -a "$LOG"
    [ "$FAILS" -ge 5 ] && { echo "5 failures in a row, stopping" | tee -a "$LOG"; break; }
    sleep $((FAILS * 60))
  fi
done
python3 tools/sf.py status | tee -a "$LOG"
