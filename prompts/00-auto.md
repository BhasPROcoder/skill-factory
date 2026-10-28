You are running the Skill Factory in this repo. Do ONE batch, then stop.

1. Read AGENTS.md.
2. Run: python3 tools/sf.py remaining taxonomy
   - If > 0 → open prompts/01-taxonomy.md and follow it exactly.
3. Else run: python3 tools/sf.py remaining generate
   - If > 0 → open prompts/02-generate.md and follow it exactly.
4. Else run: python3 tools/sf.py remaining audit
   - If > 0 → open prompts/03-audit.md and follow it exactly.
5. Else → run python3 tools/sf.py index --all && python3 tools/sf.py router, then reply "LIBRARY COMPLETE".

Rules: one prompt file per session. Never ask the user anything; make the reasonable choice and continue. Never read registry/*.jsonl or other skills' SKILL.md files in full. Final reply: one line from logs/progress.md.
