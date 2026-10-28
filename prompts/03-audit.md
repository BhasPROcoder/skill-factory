Read AGENTS.md, SPEC.md and examples/GOLD-SKILL.md (once each).

TASK: Deep-audit 3 skills and upgrade them. The validator only checks structure; you check substance.

1. Run `python3 tools/sf.py next 3 --status failed`. If NONE, run `python3 tools/sf.py next 3 --status validated`. If still NONE, reply "nothing to audit" and stop.
2. For each skill, read its SKILL.md and score it 1–5 on:
   - Expertise: would a senior practitioner agree with every step and threshold?
   - Operability: could a small model follow each step without guessing?
   - Determinism: would two different models produce the same structure and the same key conclusions?
   - Safety/accuracy: any invented facts, citations, numbers? any missing professional boundary?
   - Example quality: is the worked example realistic and fully template-compliant?
3. For every score below 5, edit the file to fix the cause. Typical fixes: replace vague steps with concrete ones, add a missing IF/THEN rule, tighten the output template, replace uncertain specifics with `[VERIFY: ...]`.
4. Bump `version` to 1.1 (or next minor).
5. Run `python3 tools/sf.py validate <IDs>`. Fix until PASS.
6. Run `python3 tools/sf.py mark audited <passing IDs>`.
7. Append to `logs/progress.md`: `- audit: <ID scores before→after>`.
8. Reply with that line only and stop.
