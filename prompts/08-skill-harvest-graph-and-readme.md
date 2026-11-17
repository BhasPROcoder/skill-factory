# COSTAR — Harvest, graph, and document the skill factory

Read `AGENTS.md` and `SPEC.md` first; everything below operates inside those rules
(context discipline, `tools/sf.py` as the only registry writer, no invented facts/URLs/stats,
batch-at-a-time unless this prompt says otherwise — it does, explicitly, per part).

## C — Context

This repo (`skill-factory`) holds two parallel skill collections:
- `skills/<DOMAIN-CODE>/<name>/SKILL.md` — the registry-driven, SPEC.md-compliant library,
  currently 645 validated skills across 81 domains (`python tools/sf.py status`).
- `local-skills/` — a raw, un-registered staging area (`gsd/`, `academic-research-skills/`,
  `custom/`, `marketplace/`) from the owner's personal `~/.claude/skills`, never ingested into
  the registry.

A prior pass (`prompts/07-skill-graph-engineering.md`, output in
`logs/skill-graph-chunks.md` + `registry/skill-graph-{nodes,edges}.jsonl`) built a typed
relationship graph and 28 named workflow "chunks" over the registry skills as they stood at
639 — before the registry grew to 645, and explicitly left 23 newly-merged domains unassessed.
That graph has never been turned into a README.

The owner just pasted six X posts (saved verbatim, with intentionally-truncated URLs, in
`staging/sources/x-posts-github-skill-leads-2026-11.md`) listing ~60 GitHub repos and Claude
Skills other people are using: design/anti-slop skills (Impeccable, Hallmark, Taste Skill,
frontend-design, canvas-design, pptx, theme-factory, ui-ux-pro-max, Stageshow, Make Interfaces
Feel Better...), agent-infra repos (Superpowers, Spec Kit, Context7, Serena, Task Master,
Playwright MCP, GitHub MCP, Aider, cline, Graphiti, buzz, herdr, deer-flow, openviking, pi...),
context/memory-hygiene tools (TokenEconomizer, loom, nomore, stalemap, landmines, Rulebook,
a lean-subagent repo), and design-system/canvas tooling (shadcn/ui, Tailwind, Magic UI, Magic
MCP, Figma Context MCP, Penpot, Excalidraw, tldraw, Lucide, Leonardo, rembg, agent-browser).
Several of these (Serena, Context7, Spec Kit, Playwright MCP, GitHub MCP, Task Master, Aider,
Graphiti, obra/superpowers, Figma Context MCP) already appear, independently verified, in the
owner's GitHub-discovery report from earlier this session — don't re-research those from
scratch, just confirm they're already accounted for.

## O — Objective

Four deliverables, in this order, each gated on the previous one finishing cleanly:

1. **Harvest**: resolve every link in the X-posts source file, decide per item whether it's
   (a) already present in `skills/` or `local-skills/`, (b) a genuine Claude Skill worth adding,
   (c) a tool/library/MCP server that is not itself a skill (note it, don't force it into the
   registry), or (d) unverifiable/dead — then add the genuinely new skills.
2. **Graph**: extend `prompts/07`'s graph and chunks to cover the full current registry
   (645 skills, including the 23 domains that pass explicitly skipped) plus whatever new skills
   step 1 adds.
3. **README**: write a tabular/graphical analysis of the whole skill factory into `README.md`.
4. **Discover**: an open-ended search for additional high-value skills not covered by the X
   posts, not already in the factory, specifically filtered for the owner's own workflow
   (building and maintaining this very skill factory, plus general AI-assisted development).

## S — Style

Operational and evidence-gated, matching `AGENTS.md`'s accuracy rules exactly:
- Resolve every truncated URL (`github.com/owner/repo…`) via WebSearch/WebFetch before acting
  on it. A truncated lead is a hypothesis, not a fact — confirm the real `owner/repo`, that the
  repository exists, and what it actually contains (read its README, don't take the tweet's
  one-line gloss as ground truth).
- Never invent a star count, license, or last-commit date. State "not verified" rather than
  guess, exactly as the owner's own GitHub-discovery report earlier this session did.
- A "Claude Skill" worth adding has a `SKILL.md` (or equivalent instruction file) at its root or
  in a clear subfolder — not every repo on these lists is a skill; most of post 4 and post 5 are
  tools/libraries/MCP servers/context-hygiene utilities, not skills. Don't force them into
  `skills/` or `local-skills/` just because they were on the list — see the disposition table in
  Part 1's output.
- Follow the same dedupe discipline as `logs/claude-migration.md` and
  `prompts/06-ingest-high-leverage-skills.md`: `new` / `covered` / `merged`, one line of
  reasoning each, destination ID or path when `new`.

## A — Audience

The repo owner, who will read the committed `README.md` and `logs/x-posts-harvest.md` directly,
and whoever (human or agent) next opens this repo needing a map of what's here and why.

## R — Response

### Part 1 — Harvest (do this whole part as one batch; it's small)

1. Read `staging/sources/x-posts-github-skill-leads-2026-11.md` once.
2. For each of the ~60 entries, resolve the real URL (WebSearch the owner+repo fragment, or the
   tool's own name, when truncated) and fetch the repo to see what it actually is.
3. Cross-check against what's already here:
   - `python tools/sf.py search <keyword>` for anything that might already be a registry skill.
   - `ls local-skills/custom local-skills/marketplace` (or `find`) for anything already staged.
   - The already-verified entries in this session's earlier GitHub-discovery report (Serena,
     Context7, Spec Kit, Playwright MCP, GitHub MCP, Task Master, Aider, Graphiti,
     obra/superpowers, Figma Context MCP) — mark these `already-known`, don't re-verify from
     zero, just confirm the URL matches.
4. Write `logs/x-posts-harvest.md`: one table, columns `Lead | Resolved URL | Disposition
   (already-known / new-skill-added / tool-not-a-skill / dead-or-unverifiable) | Where it landed
   or why not | One-line evidence`.
5. For every `new-skill-added` disposition: the repo owner's own skill library lives in
   `~/.claude/skills`, not this factory's SPEC.md-governed `skills/`. Fetch the skill's actual
   `SKILL.md` content and add it there, preserving its own author's format (do not force
   SPEC.md's 11-section structure onto someone else's skill) — matching how `rea-teardown` was
   hand-authored there earlier, but here you're importing an existing skill, not writing a new
   one, so prefer copying its real file if you can fetch it, over paraphrasing.
6. For anything genuinely novel enough to become a *new, original* skill in this factory's own
   `skills/` (rare — most of the list is either an existing skill to import elsewhere, or a tool,
   not a gap in this factory's own taxonomy): follow `prompts/01-taxonomy.md` then
   `prompts/02-generate.md` exactly, same as any other factory skill.
7. `git add` the new files, append one line to `logs/progress.md`, do not commit yet — commit
   once at the end of Part 1 with a message listing counts per disposition.

### Part 2 — Graph (depends on Part 1's final skill count)

1. Run `python tools/sf.py graph-export > registry/skill-graph-nodes.jsonl` fresh (it's stale
   the moment Part 1 adds anything).
2. Re-open `logs/skill-graph-chunks.md`. The 28 existing chunks over the original ~544-639 skills
   stand; don't redo them. Specifically cover what was explicitly left out:
   - The 23 previously-flagged, never-assessed merged domains (ARC, ATR, BID, CLI, DST, EVT, EXP,
     GEO, IPR, IXA, LIR, LRE, PRT, RNT, SDR, SEQ, SHP, SPD, SVC, TBX, UST, VEV, WHS) plus the
     GRF-018..023 extension and any registry growth since (diff the new node export against the
     old one the same way `prompts/07` did for the original merge).
   - Any skills Part 1 added.
   Use the same method `prompts/07` used: declared `requires` first, `sf.py overlap` second,
   same-subdomain siblings third, and your own reading of the one-line descriptions for
   cross-domain bridges — don't force edges where none exist; an honest "unchunked" entry beats a
   fabricated relationship.
3. Append new chunks (numbered onward from 28) and update the node/edge/chunk-count totals at
   the top of `logs/skill-graph-chunks.md` and the bottom "Unchunked" tally. Update
   `registry/skill-graph-edges.jsonl` with the new edges (append, dedupe against existing
   `(from,to,type)` triples exactly like the Part-1-era script did).
4. Verify: every edge's `from`/`to` exists in the node export, no duplicate triples, every chunk
   has ≥3 skills and a stated rationale — same three checks as `prompts/07` step 6.

### Part 3 — README (depends on Part 2's finished graph)

Write (or replace) `README.md` at the repo root with:
- The existing intro content from the current `README.md` (don't delete the "Use a skill" /
  "Accuracy and limits" / "Inspect and validate" sections — fold the new content in alongside
  them, don't replace the operating instructions with only the new tables).
- A **macro/domain table**: macro area | domain count | skill count | validated/audited split,
  generated from `sf.py` output, not hand-counted.
- A **chunk summary table**: chunk name | skill count | link to its section in
  `logs/skill-graph-chunks.md`.
- One **Mermaid diagram** (GitHub renders Mermaid natively in a README, no extra tooling) showing
  the chunk-level graph: one node per chunk (not per skill — 645 individual nodes is unreadable),
  edges between chunks where this pass found a real cross-chunk bridge (e.g. chunk 11 "Startup
  customer validation" → chunk 21 "Startup validation feeds strategy & fundraising"). Keep it to
  one diagram; if it's unreadable at full scale, split by macro area into several smaller
  diagrams rather than one unreadable graph.
- A short **"where things live"** section distinguishing `skills/` (registry-governed) from
  `local-skills/` (raw, unregistered) from whatever Part 1 added to `~/.claude/skills`, so a
  reader doesn't assume they're one thing.
- Every number in the README must come from a command you actually ran this session
  (`sf.py status`, `sf.py macros`, a count over the edges/chunks files) — paste the exact command
  output or the number it produced, not a remembered or estimated figure.

### Part 4 — Discover (independent of Parts 1-3; can run in parallel with them)

Open-ended research, same anti-fabrication rules as the owner's earlier GitHub-discovery report:
find skills (not generic tools) that would materially help the owner's own workflow — building
and maintaining a 650+-skill factory, running multi-session collaborative Claude Code work,
doing the kind of reverse-engineering/graph-engineering/research-report work already seen in
this session — and that are **not** already covered by the six X posts or already present in
`skills/`/`local-skills/`/`~/.claude/skills`. Produce `logs/additional-skill-discoveries.md`:
one entry per find with resolved URL, what it actually does, why it's relevant to *this* owner's
workflow specifically (not a generic "would help any developer" line), and whether you verified
it via WebFetch or are relying on WebSearch snippets only. 8-15 genuinely good finds beats 30
padded ones.

### Final step

Commit everything (Parts 1-3 can be separate commits if that reads better in history; Part 4 is
its own commit since it's independent). Push. Append a final `logs/progress.md` line summarizing
all four parts' counts. Reply with that line and the `README.md`/`logs/*.md` paths, under 10
lines total.
