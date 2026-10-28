# AGENTS.md — Skill Factory operating rules

You are working inside the Skill Factory repo. Its job is to build a library of 500+ portable skills (instruction files any LLM can follow). Default maintenance sessions are one small job. An explicit user request for a larger batch or sustained work determines the actual scope.

## Files that matter
- `SPEC.md` — the skill format and quality rules. Read it once per session.
- `examples/GOLD-SKILL.md` — the reference skill. Match its depth and structure.
- `registry/macros.json` — list of macro-areas.
- `registry/domains.jsonl` — one domain per line.
- `registry/skills.jsonl` — one planned/written skill per line, with status.
- `skills/<DOMAIN-CODE>/<name>/SKILL.md` — the skills themselves.
- `tools/sf.py` — the only way you query or update the registry.
- `logs/progress.md` — append one line per session.

## Context discipline (most important)
1. Never open or print `registry/*.jsonl` in full. Use `python3 tools/sf.py` commands.
2. During generation, do not read unrelated skills' SKILL.md files. For routing context, use `python3 tools/sf.py show <ID>` (one line). During a requested substantive audit, read the selected skills being reviewed, as required by `prompts/03-audit.md`.
3. After writing a file, do not cat it back. Run the validator instead.
4. Do exactly the batch the prompt asks for. Do not start the next batch.
5. Final message of every session: at most 5 lines. No recaps of file contents.

## Registry statuses
`planned` → `written` → `validated` → `audited`. `failed` = could not pass validation after 2 fix attempts.

## sf.py cheat sheet
- `python3 tools/sf.py status` — counts
- `python3 tools/sf.py macros` — macro-areas with TODO/DONE
- `python3 tools/sf.py codes` — existing domain codes
- `python3 tools/sf.py next 5` — next planned skills (add `--status failed` etc.)
- `python3 tools/sf.py show PRM-001`
- `python3 tools/sf.py check-registry`
- `python3 tools/sf.py validate PRM-001 PRM-002 --mark`
- `python3 tools/sf.py mark written PRM-001 PRM-002`
- `python3 tools/sf.py index --all` and `python3 tools/sf.py router`
- `python3 tools/sf.py testpack PRM-001`
- `python3 tools/sf.py export dist/claude-skills`
- `python3 tools/sf.py ingest staging/<manifest>.json` — serial manifest ingestion; never run concurrent registry writers
- `python3 tools/sf.py quality --all` — mechanical quality gates, not a substantive audit
- `python3 tools/sf.py coverage` and `python3 tools/sf.py overlap`
- `python3 tools/sf.py package dist/portable-skills.zip`

## Accuracy and status
- Teach method and judgment. Do not hardcode current laws, fees, prices, platform rules, deadlines, software versions, or other changing facts.
- Keep specific claims only when certain and stable; otherwise use `[VERIFY: what to check and the authoritative source]` or omit them.
- Never invent sources, URLs, citations, quotes, laws, case names, studies, or statistics.
- Label worked examples fictional and recompute their arithmetic before saving.
- Review every specific claim before saving. When uncertain, prefer a shorter correct instruction.
- Report file status and progress only from `sf.py` output observed in the current session. Structural validation never by itself warrants `audited` status.
- Separate agents own separate domain folders and staging manifests. The coordinating agent ingests manifests serially and performs the combined checks.
