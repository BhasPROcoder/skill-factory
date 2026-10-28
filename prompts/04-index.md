Read AGENTS.md.

TASK: Rebuild indexes and fix routing overlaps for ONE domain.

1. Run `python3 tools/sf.py index --all` and `python3 tools/sf.py router`.
2. Run `python3 tools/sf.py status` and pick the domain named in this line, or the first domain whose INDEX.md you have not reviewed (check `logs/progress.md` for "index-review"): DOMAIN = ______
3. Read only `skills/<DOMAIN>/INDEX.md`.
4. Find pairs of skills whose descriptions or triggers overlap so a model could pick the wrong one.
5. For each overlap, edit ONLY the frontmatter of those two SKILL.md files: sharpen `description`, move ambiguous triggers to the correct skill, add each other's ID to `not_for`.
6. Run `python3 tools/sf.py validate --domain <DOMAIN>` and `python3 tools/sf.py index <DOMAIN>`.
7. Append to `logs/progress.md`: `- index-review: <DOMAIN> — <n> overlaps fixed`.
8. Reply with that line only and stop.
