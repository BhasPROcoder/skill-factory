Read AGENTS.md and SPEC.md.

TASK: Migrate the external list in `staging/sources/100-high-leverage-ai-skills.md` (~85
named items across 13 categories, plus a "Top 10 Cross-Domain Must-Haves" table that just
re-ranks items already in the list — do not double-count those 10) into the registry and
skills library.

This is an explicitly authorized full-batch task: the repo owner asked to process the whole
list, so do not stop at the default 5-skill batch size from `prompts/02-generate.md`. Work
through every item in this session; only split across sessions if you hit a hard context
limit, and if you do, resume from the exact item you stopped at.

This follows the same method already used for `logs/claude-migration.md`: compare each
source item against the existing 544-skill library, decide `new` / `covered` / `merged`,
and only write new files for genuine gaps. Most items in this list will be `covered` or
`merged` — it is a generic, persona-framed prompt list, and the factory already has
deeper, task-specific equivalents for a lot of it.

1. Run `python3 tools/sf.py status`, `python3 tools/sf.py macros`, and
   `python3 tools/sf.py codes` once each, for orientation. Do not read `registry/*.jsonl`
   in full.
2. Read `staging/sources/100-high-leverage-ai-skills.md` once.
3. For each named item (the bold-titled bullets, not the Top 10 table):
   a. Search the registry by what the task actually does, not its marketing name, e.g.
      `python3 tools/sf.py search <keyword>`.
   b. Decide:
      - `covered` — an existing skill (give its ID) already does this at the required
        depth. No new file.
      - `merged` — fold its scope into a planned-but-unwritten skill rather than creating
        a near-duplicate; note which ID absorbs it.
      - `new` — no equivalent exists. Plan it as a skill.
   c. Drop persona/role-play framing ("as a staff engineer", "explain it to a 12-year-old")
      in favor of an operational task description, and drop any vendor/model name, exactly
      like the Claude migration did (SPEC.md §1.2).
4. For every item marked `new`, add it to the taxonomy per `prompts/01-taxonomy.md` steps
   3–6:
   - Reuse an existing domain `code` when the item fits a domain already in
     `registry/domains.jsonl` (e.g. route the coding-persona items to the existing
     software-engineering domain, not a new one). Only create a new domain if nothing
     existing fits, and keep it inside an existing `macro` from `registry/macros.json`
     when possible.
   - Append rows to `registry/domains.jsonl` (only if a new domain is needed) and to
     `registry/skills.jsonl` with `status: "planned"`.
5. Run `python3 tools/sf.py check-registry` and fix every error before continuing.
6. Write each newly planned skill's `skills/<CODE>/<name>/SKILL.md` to the full SPEC.md
   format — all 11 body sections, frontmatter, a complete worked example, and a test case.
   Do not skip sections to move faster. Use `prompts/02-generate.md`'s per-skill procedure,
   in batches of 5, until every new skill from this list is written.
7. After each batch: `python3 tools/sf.py mark written <IDs>` then
   `python3 tools/sf.py validate <IDs> --mark`. Fix failures (max 2 attempts per skill,
   then `mark failed` and move on).
8. When every source item has a disposition, write `logs/high-leverage-skills-migration.md`
   in the same table format as `logs/claude-migration.md`:
   `| Source item | Disposition | Destination ID(s) | Reason |`.
9. Run `python3 tools/sf.py index --all` and `python3 tools/sf.py router`.
10. Append one line to `logs/progress.md`:
    `- high-leverage-list: <N> source items — <X> new, <Y> covered, <Z> merged; <W> skills written and validated`.
11. Reply with that line only and stop.

Do not ask the user anything mid-task. Make the reasonable domain-fit and generalization
call yourself, using the same judgment already on record in `logs/claude-migration.md`,
and keep going.
