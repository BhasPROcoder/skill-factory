Read AGENTS.md.

TASK: Grade cross-model consistency for ONE skill. SKILL ID = ______

Setup (done by the human before this run):
- `python3 tools/sf.py testpack <ID>` created `tests/<ID>/PROMPT.md`.
- The human pasted PROMPT.md into 2+ models and saved each answer as `tests/<ID>/results/<model>.md`.

Steps:
1. Read `tests/<ID>/ASSERTIONS.md` and every file in `tests/<ID>/results/`.
2. For each model, mark each assertion PASS/FAIL with a 1-line reason.
3. Compare the models: same section order? same key conclusions? Note every divergence.
4. For each divergence or FAIL, find the line in the skill that allowed it (vague step, missing rule, loose template).
5. Edit the SKILL.md to close those gaps. Bump the minor version.
6. Run `python3 tools/sf.py validate <ID>`; fix until PASS.
7. Write `tests/<ID>/REPORT.md`: a table (model × assertion), divergences, and the edits made.
8. Append to `logs/progress.md`: `- crossmodel: <ID> — <pass rate per model>`.
9. Reply with that line only and stop.
