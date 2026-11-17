# Contributing to Skill Factory

This repo builds a library of 500+ portable, SPEC.md-governed skills under `skills/`, plus
supporting tooling. Contributions of new skills, fixes to existing ones, or tooling
improvements are welcome.

## Before you start

1. Read [AGENTS.md](AGENTS.md) — the operating rules this library is built under (context
   discipline, registry statuses, the `sf.py` cheat sheet).
2. Read [SPEC.md](SPEC.md) — the exact skill format: frontmatter, body sections, length limits,
   and the self-check every skill must pass before it's considered done.
3. Read [`examples/GOLD-SKILL.md`](examples/GOLD-SKILL.md) — the reference skill. Match its
   depth and structure, not just its section headings.

## Adding a new skill

1. Check it doesn't already exist or overlap heavily with one that does:
   ```text
   python tools/sf.py search <task keywords>
   python tools/sf.py codes
   ```
2. If it's a new domain or a planned-but-unwritten skill, add a registry row (see
   `prompts/01-taxonomy.md` for the exact taxonomy process) or pick up an existing planned skill:
   ```text
   python tools/sf.py next 5
   ```
3. Write `skills/<DOMAIN-CODE>/<name>/SKILL.md` to the full SPEC.md format — all 11 body
   sections, real domain expertise, a complete worked example, 3-5 checkable test assertions.
   No filler, no invented facts/citations/statistics (`[VERIFY: ...]` placeholders instead,
   where something needs a current-source check).
4. Validate before opening a PR:
   ```text
   python tools/sf.py mark written <ID>
   python tools/sf.py validate <ID> --mark
   python tools/sf.py quality --all
   python -m unittest discover -s tests -p test_sf.py
   ```
5. Open a PR. Describe what the skill does, why it's not already covered, and link any sources
   the skill's `[VERIFY: ...]` placeholders point to.

## Fixing or improving an existing skill

Same validation steps as above, run against the specific ID(s) you touched. If you're correcting
a factual claim, note what was wrong and why in the PR description — this project's accuracy
bar (see `AGENTS.md`'s "Accuracy and status" section) depends on that trail existing.

## Tooling changes (`tools/sf.py`)

`sf.py` is the only supported way to query or update the registry — don't open or print
`registry/*.jsonl` directly in a script or PR description. New subcommands should follow the
existing style (see `cmd_overlap`/`cmd_search`/`cmd_graph_export` for the pattern: load via the
shared `load()` helper, print derived output only, never dump raw rows).

## What doesn't belong in `skills/`

Generic tools, MCP servers, and personal workflow skills that aren't SPEC.md-shaped portable
instructions belong in your own `~/.claude/skills`, not this repo's registry-governed library.
See `logs/x-posts-harvest.md` for a worked example of that triage decision.

## Code of conduct

Be direct, be accurate, and don't invent facts to fill a gap — "I don't know, verify X" is a
better contribution than a plausible-sounding guess. That standard applies to human and AI
contributors alike.
