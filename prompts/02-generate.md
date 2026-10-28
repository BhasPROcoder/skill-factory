Read AGENTS.md, SPEC.md and examples/GOLD-SKILL.md (once each).

TASK: Write the next 5 skills, validate them, and stop.

1. Run `python3 tools/sf.py next 5`. These are your 5 skills (all from one domain). If it prints NONE, reply "nothing planned" and stop.
2. For any ID listed in a skill's `requires`, run `python3 tools/sf.py show <ID>`. Do not open any other SKILL.md.
3. For each skill, write `skills/<CODE>/<name>/SKILL.md` exactly to SPEC.md:
   - `id`, `name`, `description`, `risk_level` match the registry row (you may sharpen the description wording).
   - Real domain expertise: concrete steps, thresholds, frameworks and checks an expert actually uses. No filler.
   - High-risk skills: follow SPEC §5 exactly; use `[VERIFY: ...]` for any specific citation, section number, rate or dose you are not certain of.
   - Worked example is complete and realistic, and follows the Output template exactly.
   - Do not cat the file back after writing.
4. Run `python3 tools/sf.py mark written <the 5 IDs>`.
5. Run `python3 tools/sf.py validate <the 5 IDs> --mark`.
6. For each FAIL, fix only the listed errors and re-run validation for that ID. Fix warnings too if quick. After 2 failed fix attempts on one skill, run `python3 tools/sf.py mark failed <ID>` and move on.
7. Append to `logs/progress.md`: `- generate: <IDs> — <passed>/<5> passed`.
8. Reply with that line only and stop.
