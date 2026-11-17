Read AGENTS.md and SPEC.md.

TASK: Build a cross-skill relationship graph over the validated skill library in `skills/`, and
cluster it into named "chunks" — groups of skills meant to be used together as a pipeline or
stack — so a user (or another agent) can see at a glance which skills combine, in what order,
and why.

This is an explicitly authorized full-corpus task: graph and chunk the entire validated library
(currently 544+ skills across 57+ domains), not a default small batch. Scope is `skills/` only —
the registry-driven, SPEC.md-compliant library. `local-skills/` (the raw gsd/academic-research-
skills/custom/marketplace dump staged on this branch) is out of scope for this pass: it has no
registry entry, no consistent frontmatter, and hasn't been through taxonomy/generation, so
there's nothing graphable about it yet. A future ingest pass could change that; don't do it here.

## 1. Add one new sf.py command: `graph-export`

Add `cmd_graph_export` to `tools/sf.py`, following the existing style of `cmd_overlap`/
`cmd_search` (load the registry once via the existing `load()` helper, print derived lines only —
never the raw rows). It should:
- Iterate every row in `registry/skills.jsonl`, joined to its domain's `macro` and `name` from
  `registry/domains.jsonl`.
- Print one compact JSON line per skill to stdout:
  `{"id","name","domain_code","domain_name","macro","subdomain","description","risk_level",
  "requires","status"}` — fields only, no full SKILL.md body.
- Register it in `CMDS`.

Run `python3 tools/sf.py graph-export > registry/skill-graph-nodes.jsonl` once. Don't cat the
result back; confirm with `wc -l registry/skill-graph-nodes.jsonl` against `sf.py status`'s
validated count.

## 2. Seed candidate edges — don't start from a blank page
Candidate pairs come from three cheap, deterministic sources (none require reading full
SKILL.md bodies):
- **Declared dependencies:** every non-empty `requires` list in the node export is already a
  `requires` edge — port these over as-is, direction `requires: A -> B` meaning A's SKILL.md
  names B's ID.
- **Cross-domain lexical candidates:** `python3 tools/sf.py overlap` already finds cross-domain
  name-word overlap at similarity ≥0.6. Capture its full output — every `REVIEW <score> <id> <>
  <id>` line is a candidate pair for you to classify in step 3.
- **Same-domain/same-subdomain siblings:** from the node export, group by `(domain_code,
  subdomain)` — skills sharing a subdomain are candidate `complements`/`overlaps_with`/
  `alternative_to` pairs. No new tool needed; just group the export you already produced.

Do not attempt all ~544×543 pairs. Classify only candidates from these three sources, plus any
pair you notice while reading one skill's `description` that plainly references another's task
by name.

## 3. Classify each candidate pair into exactly one edge type
Read only the two skills' `description` fields from the node export (not the full SKILL.md) to
decide. If a description alone is ambiguous, check `python3 tools/sf.py show <ID>` for a one-line
summary before opening a file; open a SKILL.md directly only as a last resort, and discard its
content from context once you've classified the edge — don't carry it into later classifications.

Edge types (pick exactly one per pair):
- `requires` — B's procedure has a formal input only A's procedure produces (already seeded from
  the registry; confirm it still makes sense, don't re-derive it from scratch).
- `feeds_into` — A's **output template** is commonly B's **input** in a typical real workflow,
  without a hard `requires` declaration (e.g. a recon brief feeding an ideation skill).
- `complements` — commonly used together in the same project/session, no fixed order between
  them.
- `overlaps_with` — same underlying task from a different angle or depth; a user should pick one,
  not run both for the same request.
- `alternative_to` — mutually exclusive by design (e.g. an India-specific vs. a US-specific
  variant of the same task).
- `generalizes` / `specializes` — one is the general-purpose version, the other a narrower
  variant (country-specific, platform-specific, risk-tier-specific).

Write one JSON line per confirmed edge to `registry/skill-graph-edges.jsonl`:
`{"from":"<ID>","to":"<ID>","type":"<edge type>","confidence":"high|medium|low","reason":"<one
clause, under 20 words>"}`. Discard a candidate pair that turns out unrelated — don't force an
edge to justify having looked at it.

## 4. Chunk the graph
A "chunk" is a named group of 3-10 skills meant to be read/used together, not a domain (domains
already exist in `registry/domains.jsonl`; a chunk crosses domains where the real workflow does).
Build chunks from the edge file, not from intuition:
- Start from dense `feeds_into` chains (A feeds B feeds C...) — these are pipelines. Name the
  chunk after the end-to-end outcome, not the first step (e.g. "Hackathon idea-to-submission
  pipeline", not "hack-recon and friends").
- Add a `complements`-linked skill to the chunk it's most densely connected to, not to every
  chunk it merely touches — a skill belongs to more than one chunk only when it's genuinely a
  hinge between two real workflows, not by default.
- Leave `overlaps_with`/`alternative_to` pairs out of chunk-membership math entirely; note them
  inside whichever chunk contains them as a "pick one" callout instead.
- A skill with no edges above `low` confidence stays unchunked. List it; don't force it into a
  cluster for the sake of coverage.

## 5. Write the output
`logs/skill-graph-chunks.md`, one section per chunk:
```
## <Chunk name>
**Skills (in typical order):** SKI-001 skill-name -> SKI-004 skill-name -> ...
**Why they're linked:** <2-3 sentences>
**Internal choices:** <any overlaps_with/alternative_to pairs inside this chunk, and when to
pick which — omit this line if there are none>
```
End the file with an "## Unchunked" section listing every skill with no edges above `low`
confidence, one per line: `SKI-NNN skill-name — <why nothing connected: niche domain, genuinely
standalone task, etc.>`.

## 6. Verify before logging done
- Every `from`/`to` ID in the edges file must exist in the node export — grep-check this, don't
  eyeball it.
- No duplicate `(from, to, type)` triples in the edges file.
- Every chunk in the output has at least 3 skills and at least one stated order or rationale.

## 7. Log and stop
Append to `logs/progress.md`:
`- skill-graph: <N> nodes, <E> edges (<R> requires, <F> feeds_into, <C> complements, <O>
overlaps/alternative), <K> chunks, <U> unchunked`.

Reply with that line, plus the path to `logs/skill-graph-chunks.md`, and stop. Do not ask the
user anything mid-task — where a classification is genuinely borderline, mark it
`confidence: low` and move on rather than stopping to ask.
