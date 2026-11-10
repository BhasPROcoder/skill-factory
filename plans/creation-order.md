# Ordered creation queue

Updated 2026-11-11 following the user's instruction to prioritize graph engineering.

## Scope and accounting

Observed sf.py checkpoint: 622 validated entries, including the original 544; 78 net additions, 4,922 still required. Target remains 5,544 total. This document orders future work; its candidate names and allocations are not registered or completed skills. Structural validation does not prove semantic uniqueness or behavioral reliability.

This queue supersedes the equal-track allocation and unordered candidate queue in the earlier expansion plan. Keep its accuracy, independent review, public-source provenance, portability, and acceptance requirements. Preserve coverage of every numbered topic in directory-integration.md and directory-topic-ledger.json within the same expansion.

Graph engineering here means graph data models, graph algorithms, graph databases, knowledge graphs, graph retrieval, and graph system operations. Graphical design and plotting remain in their respective tracks.

## Creation order and remaining allocations

Allocations are planning budgets for accepted unique additions, not claims that that many distinct skills have already been discovered. Move unused capacity to documented gaps; never create renamed variants to fill a bucket. Deduct only accepted net additions from the remaining total.

| Order | Workstream | Remaining allocation | Internal creation order |
|---|---|---:|---|
| 1 | **Graph engineering** | 200 | Representation and identity → integrity → traversal and algorithms → storage/query → knowledge graphs → retrieval/learning → operations and domain applications |
| 2 | Datasets, data engineering, analytical systems | 600 | Intake/rights → schemas and quality → transformations → temporal/stream processing → analytical contracts → reproducibility |
| 3 | Software maintenance, architecture, infrastructure, defensive security | 600 | Reproduction/debugging → contracts → migration → verification → deployment/recovery → access/privacy/security review |
| 4 | Applied ML, AI agents, knowledge workflows, hackathons and competitions | 500 | Evaluation data → baselines → error analysis → retrieval/tools/memory → agent evaluation → integration/submission |
| 5 | Product design, accessibility, creative production and localization | 500 | User tasks → interaction/state → accessible implementation → design systems → media/asset production → localization and delivery |
| 6 | SEO, publishing, marketing, sales and customer success | 500 | Audience/evidence → content/site structure → publishing checks → experiments/measurement → sales handoff → adoption/renewal |
| 7 | Procurement, logistics, inventory, manufacturing and quality | 500 | Requirements/supplier evidence → receiving/stock → production/traceability → fulfillment → exceptions → corrective-action verification |
| 8 | Government administration, policy, civic/nonprofit work, accounting administration | 500 | Jurisdiction and authority intake → application/record packets → reconciliation → routing/appeals preparation → reporting and follow-up |
| 9 | Education, research, laboratories, archives, healthcare administration | 500 | Questions/learning outcomes → instruments/materials → evidence collection → analysis/assessment → records/handoffs → review |
| 10 | Construction/facilities, agriculture/environment/spatial work, workforce/services/daily administration | 522 | Asset/site/context evidence → work planning → field/service records → exception handling → handover and maintenance |
| | **Remaining total** | **4,922** | **78 already added + 4,922 remaining = 5,000 additions** |

These groups cover all original 25 planning tracks. Cross-domain candidates have one home and are counted once. Graph applications in later waves must add a new operational procedure, not merely change the dataset or industry.

## Graph engineering: first candidate queue

These are discovery cards, not reserved skill IDs. Work in the following order, checking catalog neighbors and earlier accepted graph cards before authoring. Reuse an existing skill when it already performs the task.

| Position | Candidate task | Concrete deliverable / decision | Prerequisite |
|---|---|---|---|
| G01 | Translate a real workflow into a graph model | Node/edge/property contract with direction, cardinality and excluded relationships | None |
| G02 | Resolve graph identity and duplicate entities | Merge/non-merge decisions with provenance and reversible identity mapping | G01 |
| G03 | Ingest edge lists without losing semantics | Import reconciliation for parallel edges, self-loops, null endpoints and identifiers | G01 |
| G04 | Validate graph structural invariants | Violations and repair proposals for an explicit graph contract | G03 |
| G05 | Preserve graph provenance and temporal meaning | Evidence-linked edges with validity, observation and version distinctions | G01 |
| G06 | Specify traversal boundaries | Visited-state, direction, depth and termination contract with reproducible reachable set | G04 |
| G07 | Diagnose disconnected graph regions | Component membership and justified connectivity findings | G06 |
| G08 | Analyze strongly connected regions | Region condensation and consequences for dependent operations | G06 |
| G09 | Select and validate weighted route computation | Algorithm preconditions, unreachable cases and independently checked path cost | G04, G06 |
| G10 | Model flow and capacity constraints | Feasible flow and bottleneck evidence with conserved quantities | G04 |
| G11 | Formulate graph matching/assignment | Matching constraints, unmatched entities and objective evidence | G04 |
| G12 | Evaluate graph ranking sensitivity | Rank changes under edge/weight/boundary perturbations; interpretation limits | G04 |
| G13 | Assess graph community outputs | Partition comparisons and sensitivity to assumptions | G04 |
| G14 | Implement a graph storage schema | Schema, query workload and migration/validation artifacts | G01–G05 |
| G15 | Diagnose graph-query cardinality and performance | Query-plan evidence and equivalent-result checks | G14 |
| G16 | Apply incremental graph updates | Idempotent update contract, affected regions and consistency checks | G14 |
| G17 | Migrate graph schema and identifiers | Reversible transformation plus preserved relationship checks | G14 |
| G18 | Model a knowledge graph vocabulary | Entity/relation definitions, evidence rules and compatibility decisions | G01, G05 |
| G19 | Map text evidence to candidate relations | Extracted claims, source spans, ambiguity and acceptance review | G18 |
| G20 | Validate knowledge-graph constraints | Contradictions, unsupported inference and repair evidence | G18, G19 |
| G21 | Design graph-assisted retrieval | Retrieval units, evidence paths, baselines and failure checks | G18–G20 |
| G22 | Evaluate graph retrieval and answers | Held-out questions, provenance/coverage errors and baseline comparison | G21 |
| G23 | Prepare graph-learning data splits | Node/edge/time split contract and leakage checks | G05, G14 |
| G24 | Monitor and recover a graph service | Invariant monitoring, recovery evidence and restoration checks | G14, G16 |

G01–G04 form the first review batch; G05–G08 the second. Later batches follow prerequisites, with independent ready cards authored in parallel. Candidate names may be merged, rejected or rewritten after comparison; position is priority, not a promise of acceptance.

Existing overlap anchors: SEQ-001 already provides a prerequisite cycle witness; SEQ-002 a ready-task frontier; SEQ-003 critical-path/slack calculation; TDS-002 provenance mapping; TDS-012 withdrawal lineage impact; SHP-002 affected-lot trace reconciliation. Do not recreate these under graph-themed names. Before G08, distinguish region analysis from a single cycle witness. Before G05/G16, distinguish actual graph semantics/update behavior from generic provenance or reachability.

## How the queue is executed

1. Start with graph engineering. Preserve unfinished TST/GAS drafts for later evaluation; they do not outrank the new graph priority.
2. Discover candidates in the current wave using public developer skills and real task evidence. Record exact inspected source/commit/license when using external inspiration. Do not copy or execute unreviewed source instructions.
3. For each candidate, record nearest accepted and pending neighbors, distinct artifact and failure decisions. Reject duplication before writing a full skill.
4. Author a small ready batch, normally up to four distinct skills, in disjoint files. Keep registry mutations serial.
5. Independently execute ordinary, missing-input and adversarial/edge requests. Run actual technical examples and inspect artifacts. Fix failures and rerun affected checks; no reviewer available means hold acceptance, not waive review.
6. Ingest accepted manifests; validate; update relevant indexes, router, topic ledger, export and package; commit and push that reviewed batch. Verify the remote commit.
7. At each batch boundary, record accepted additions, rejected/merged cards and the next ready cards. Update remaining allocations from sf.py evidence. Do not treat planned allocation as registry status.
8. At each wave boundary, audit all directory topics mapped to the wave. Record supported tasks, gaps and follow-up candidates; a single skill does not establish full topic coverage.
9. If a wave cannot supply additional unique tasks, record the shortfall and redistribute it to documented uncovered needs. Preserve the overall target and all directory coverage; do not pad counts.

The next execution action is comparison and candidate cards for G01–G04. No new skill is claimed by this planning update.
