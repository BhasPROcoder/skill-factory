---
name: lit-search
description: Literature search for a ResearchOS project. Use when the user wants to find papers, build or run search queries across Semantic Scholar/OpenAlex/arXiv/Crossref/DBLP/ACL/GitHub, import a known set of papers (DOIs, arXiv ids, titles, BibTeX), snowball references/citations, export BibTeX/CSV, download open-access PDFs, check search recall against a known corpus, or set up weekly monitoring for new papers. Do NOT use for deciding which papers to include (screen-extract), reading or summarising a paper in depth (screen-extract), checking whether a citation in a draft is real (verifier), or a quick "has anyone done X" novelty check before a project exists (idea-scoping).
---

# lit-search

## Purpose
Turn RQs into source-specific boolean queries, run them in parallel (one agent per source), snowball to saturation, dedupe, and log everything so the search section of the paper can be written from the logs. Never invent a paper: every record comes from an API response or a user-supplied identifier that resolved.

## Runtime check
`python -c "import researchos_core"`. If it fails or `python -m researchos_core.lit search ...` returns `status: failed` with a network error for every engine, you are offline/sandboxed: say "API access isn't available here; I'm falling back to web search, so hit counts and coverage are not reproducible", search with WebSearch/WebFetch, and tag every record you add as `retrieval: web_fallback` in conversation. Do not fabricate hit counts.

Keys: OpenAlex needs `OPENALEX_API_KEY` (free, mandatory since Feb 2026). Semantic Scholar works keyless but is throttled; `S2_API_KEY` is recommended. Crossref uses `CROSSREF_MAILTO`. Missing-key errors name the key; relay them verbatim.

## Inputs
- Approved RQs in state (`ros status`). If none, stop and route to research-os.
- Optional seed corpus: a file of DOIs / arXiv ids / titles (one per line), a `.bib`, or a CSV with doi/arxiv/title columns.
- `references/source_access.md` (limits, keys, fallbacks), `references/query_syntax.md` (per-engine boolean syntax).

## Workflow
1. **Seed (if the user has known papers)**
   `python -m researchos_core.lit seed --file <file> --tag gold --status included`
   Report resolved/unresolved. Unresolved entries become an open question; never add them as records.
2. **Concept table.** From each RQ, build a table: concept → synonyms → excluded senses. Show it as a **Review** checkpoint. Weakest-point check: is any concept so broad that a query will exceed 1,000 hits? Narrow it now.
3. **Query plan.** Write `lit/query_plan.json`:
   ```json
   {"version": 1, "year": "2015-2026", "limit": 500, "round": 1,
    "engines": {"semantic_scholar": ["..."], "openalex": ["..."], "arxiv": ["..."], "dblp": ["..."], "acl": ["..."], "crossref": [], "github": []}}
   ```
   One query per concept combination per engine, in that engine's syntax (`references/query_syntax.md`). Use `acl` only for NLP-adjacent topics and `github` only for tool/benchmark papers. Show the plan as an **Approve** checkpoint (mandatory before an SLR search).
4. **Fan-out F1.** `python -m researchos_core.lit plan-fanout --plan lit/query_plan.json`
   It prints one brief per engine. Spawn one subagent per brief **in a single message so they run in parallel** (Agent tool; prompt: "Read the brief at <brief path> and follow it exactly. Do not read other files in that fanout folder."). Each agent runs only its engine's commands.
5. **Merge.** When all agents finish: `python -m researchos_core.lit merge --fanout <fanout_id>`.
   Report: candidates in, new unique, matched existing, failed and partial queries. For each `partial` query (hits > limit) propose a narrower query; for `failed`, re-run once, then accept the gap and log it.
6. **Snowball (F2).** Only from papers whose status is `included` (seeds or after screening).
   `python -m researchos_core.lit snowball --direction both --from-status included --round <n> --out lit/snowball_r<n>.jsonl`
   then `python -m researchos_core.lit merge --files lit/snowball_r<n>.jsonl --method snowball`.
   For large seed sets, split by `--ids` into batches of ≤15 and run each batch as a parallel agent writing its own `--out` file, then merge all files together.
   Saturation: stop when a round's new candidates yield **zero** new inclusions after screening, or after round 4. Snowballing needs screening between rounds; hand off to screen-extract and come back.
7. **Recall check (when a gold set exists).** `python -m researchos_core.lit recall --tag gold`. Below 0.8 recall means the queries miss vocabulary: show the missed titles and add terms. This is the single best evidence that your search is adequate; report it in the methods section.
8. **Export.** `python -m researchos_core.lit export` → `lit/references.bib`, `lit/exports/sources.csv`. Every BibTeX entry carries `note = {ResearchOS S-xxxx}`; never remove it (verifier relies on it).
9. **PDFs.** `python -m researchos_core.lit pdfs --status passed_title_abstract included`. Lists `need_from_user`: ask the user for PDFs they can access through their institution; they save them as `lit/pdfs/<source_id>.pdf`, then `python -m researchos_core.lit attach`.
10. **Monitoring (optional).** Create a weekly scheduled task (scheduling tool, not cron) whose prompt is: "In <project root>, run `python -m researchos_core.lit monitor`, read the abstracts of the new_ids it prints, and flag any that threaten the novelty of the project's RQs with `python -m researchos_core.ros risk add --category novelty ...`. Report the flagged papers." Store its id in state with `ros decide --question "monitoring task" --chosen <task id> ...`.

## Parallel agents
F1 per engine (cooperative), F2 per seed batch (cooperative). Merge rule: union; dedupe by DOI → arXiv id → normalised title + year ±1 (similarity ≥ 0.95); metadata precedence Crossref > OpenAlex > Semantic Scholar > DBLP > ACL > arXiv. Failures: per-host rate limiter with Retry-After and exponential backoff is built in; a failed engine marks the fan-out `partial` and the gap is logged, never filled by guessing.

## Checkpoints
- Concept table → Review.
- Query plan → Approve (mandatory for SLR/mapping).
- After merge → Choose: (A) snowball now (B) screen first (C) add queries for missed vocabulary.

## Outputs
- `registry/sources.jsonl`, `registry/queries.jsonl` (schemas in `research_state.schema.json` `$defs`)
- `lit/query_plan.json`, `lit/references.bib`, `lit/exports/sources.csv`, `lit/pdfs/`, `fanout/F1-*/merge.json`

## Quality gates
- Every executed query appears in `queries.jsonl` with engine, string, date, hits, retrieved, status.
- No `partial` query left unexplained.
- Recall ≥ 0.8 on the gold set when one exists (else state it as a limitation).

## Good vs bad
Bad query (one engine, one string): `AI overreliance`
Good (OpenAlex): `("overreliance" OR "over-reliance" OR "automation bias") AND ("AI" OR "machine learning" OR "decision support") AND ("explanation" OR "explainable")` with year filter, plus a Semantic Scholar bulk version using `+`/`|`, plus an arXiv `abs:` version.

## Failure modes
- OpenAlex key missing → run the other engines, tell the user the key is mandatory and free.
- Semantic Scholar 429s keyless → slower runs; suggest requesting `S2_API_KEY`.
- Query hits 20,000 → don't raise the limit; narrow the query.
- Seed title doesn't resolve → leave it out, ask the user for a DOI.
