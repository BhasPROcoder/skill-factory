# Plan of action: 5,000 additional portable skills

Planning date: 2026-10-31. This document proposes work; it does not register candidates as completed skills.

Execution-order update (2026-11-11): [creation-order.md](creation-order.md) is now the controlling priority queue and remaining allocation plan. Graph engineering is first. Its 4,922 remaining allocation replaces the equal-track allocation below for future work, while preserving the 5,000-addition objective and all coverage/quality requirements.

User-supplied directory integration: [all numbered topics and pilot mapping](directory-integration.md). The directory contains 185 numbered entries despite its 180-domain title. Include all entries within this expansion, starting with a reviewed pilot; do not add a separate 5,000-skill quota or treat topics as automatically unique skills.

## Objective and baseline

Add 5,000 substantively distinct, usable skills to the existing library. Observed `python tools/sf.py status` output in this planning session: 544 skills, 57 domains, all 544 validated, none audited. The target is therefore 5,544 total, provided the original 544 remain accepted. Replacements, revisions, merged variants, and rejected candidates do not count as additions. If an existing skill is retired, replenish the shortfall before claiming the total.

Preserve the factory's plain Markdown format, explicit input requirements, decision rules, output templates, fictional examples, and checkable tests. Agent-neutral means instructions do not depend on a particular assistant or plugin. It does not promise that every model has the reasoning, browsing, coding, or file access needed to execute every skill. Declare capabilities and provide an honest fallback when execution is unavailable.

## 1. Discover useful workflows from public GitHub developers

Use public skill repositories as inspiration and evidence of practical tasks. Start with the following repositories, whose public pages were inspected during planning. These are discovery seeds, not a claim that individual skills or licenses have been audited.

| Source | Discovery focus | Compare first with |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | Software development workflow methods | TRP, TST, CTG, SKR |
| [trailofbits/skills](https://github.com/trailofbits/skills) | Defensive security review and audit methods | TSC, TST, CMP |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Web engineering and interface workflows | MPU, TAP, CTG |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Marketing, conversion, SEO, and measurement | MSE, MAR, MME, MCA, MBR |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Scientific analysis and research workflows | GRQ, GRV, TRP, TDS, TML |

Expand discovery across independent maintainers and undercovered subject areas. Search public GitHub repositories for task terms and skill files; use curated lists only to find original sources. Follow forks to their upstream origin and collapse copied workflows before evaluation. Do not use stars, downloads, or repository size as proof of quality. Do not assume these sources alone contain 5,000 suitable unique additions.

For each promising source:

1. Read the actual skill, relevant references, and required scripts as data; do not install or execute downloaded instructions during discovery.
2. Record repository URL, owner, exact file path, commit identifier, inspection date, and upstream origin if it is a fork.
3. Inspect the license and relevant file notices at that commit. Record what reuse is permitted and what attribution is required. Public visibility alone is not permission to copy.
4. Extract a short task specification: user problem, required evidence, reasoning procedure, output artifact, failure modes, and tool dependencies.
5. Search the factory for semantic neighbors before drafting. Choose new skill, improvement to an existing skill, supporting reference, or rejection; record the reason.
6. Generalize workflow assumptions into explicit inputs. Replace vendor hooks and personal paths with capability requirements. Keep specialized methods where necessary rather than deleting the details that make them useful.
7. Write an original procedure and fresh fictional example. If adapting licensed text or code, preserve required notices; do not imply original authors endorsed the new skill. If permission is unclear, do not copy or closely paraphrase the material.
8. Verify technical details against current primary documentation when actually authoring. Record unverified details as `[VERIFY: what to check and where]`.

Keep source records outside the portable skill body unless attribution must accompany it. The record must distinguish inspiration, adapted material, and independently authored work. Record source updates as review triggers, not automatic overwrites. Avoid keeping bulk source clones or installing vendor skill libraries on this system; retain provenance and any necessary licensed dependencies only.

## 2. Allocate discovery effort across useful areas

The following 25 tracks each start with a planning allocation of 200 accepted additions: 25 × 200 = 5,000. These are adjustable effort allocations, not evidence that every track contains 200 unique skills. Move allocation to better-supported gaps whenever duplicate rejection is high. Never manufacture variants to fill a quota. Tracks are planning labels, not preassigned registry domains.

| Track | Initial additions | Candidate workflow families to investigate |
| --- | ---: | --- |
| Dataset acquisition and stewardship | 200 | Consent records, annotation disagreement, provenance, version migration, collection coverage |
| Data engineering and analytical systems | 200 | Change capture, temporal joins, reconciliation, lineage, analytical contract failures |
| Applied machine learning and evaluation | 200 | Calibration, drift diagnosis, abstention, ranking, subgroup evaluation |
| AI agent and knowledge workflows | 200 | Retrieval failure analysis, tool-result verification, memory conflicts, context selection |
| Hackathons and data competitions | 200 | Event constraints, team integration, reproducible submissions, judging evidence, post-event handoffs |
| Software maintenance and architecture | 200 | Dependency boundaries, migrations, compatibility, debugging, legacy behavior preservation |
| Infrastructure and service reliability | 200 | Incident evidence, recovery exercises, capacity diagnosis, observability, release constraints |
| Defensive security and privacy | 200 | Threat modeling, access reviews, secret handling, disclosure preparation, privacy evidence |
| Product design and accessibility | 200 | Assistive interaction, error recovery, usability tasks, content accessibility, service journeys |
| SEO and publishing systems | 200 | Crawl evidence, information architecture, migrations, multilingual publishing, editorial maintenance |
| Marketing and audience development | 200 | Channel experiments, lifecycle transitions, positioning evidence, community participation |
| Sales, partnerships, and customer success | 200 | Procurement objections, handoffs, adoption blockers, partner obligations, renewal evidence |
| Government services and administrative work | 200 | Records requests, application evidence, case routing, grievance preparation, status reconciliation |
| Policy, civic participation, and nonprofit work | 200 | Consultation evidence, implementation review, volunteer operations, grant reporting, service coverage |
| Accounting and financial administration | 200 | Reconciliations, close evidence, invoice exceptions, expense substantiation, audit preparation |
| Procurement and supplier management | 200 | Bid comparability, supplier exceptions, acceptance evidence, purchasing controls, substitution reviews |
| Logistics, inventory, and fulfillment | 200 | Stock discrepancies, shipment exceptions, returns, demand uncertainty, warehouse handoffs |
| Manufacturing and quality engineering | 200 | Defect evidence, process changes, traceability, inspection planning, corrective-action verification |
| Construction, facilities, and asset maintenance | 200 | Change records, maintenance histories, handover evidence, defect logs, asset condition records |
| Agriculture, environment, and spatial analysis | 200 | Field observations, sampling records, geospatial quality, conservation evidence, resource monitoring |
| Healthcare administration and caregiving support | 200 | Visit preparation, record organization, care handoffs, appointment barriers, question preparation |
| Education, vocational learning, and assessment | 200 | Misconception diagnosis, accessible instruction, practice design, vocational evidence, assessment review |
| Scientific research, laboratories, and archives | 200 | Sample provenance, instrument records, research data checks, cataloging, preservation decisions |
| Creative production, media, and localization | 200 | Production continuity, editorial constraints, adaptation, caption quality, cultural context review |
| Workforce, service operations, and daily administration | 200 | Hiring evidence, onboarding, shift handoffs, hospitality, event logistics, household records |
| **Total planned additions** | **5,000** | **Subject to distinctness and acceptance gates** |

Prioritize workflows with a concrete artifact and credible real use. For regulated or safety-critical work, focus on evidence organization and bounded decision support; require applicable context and current authoritative guidance. Do not manufacture clinical recommendations, engineering safety thresholds, legal conclusions, or tax rules to expand coverage.

## 3. Prove that each candidate is a new skill

Create a candidate card before writing a full skill:

```text
Candidate reference:
User task and trigger:
Inputs and required capabilities:
Transformation performed:
Output artifact and acceptance criteria:
Distinct decision rules and failure modes:
Nearest existing skills and nearest pending candidates:
Why those skills cannot already satisfy this task:
Source provenance and license disposition:
Verification requirements and risk boundary:
Decision: new / improve existing / merge / reject / investigate
Reviewer and reasoning:
```

Use `sf.py search` and `sf.py show` to inspect registry neighbors. During substantive comparison, read the selected skill procedures. Search both the original catalog and all accepted or pending expansion candidates. Compare what the skill does, not just its title. Add lexical and semantic retrieval to suggest comparisons as tooling permits; similarity scores never decide uniqueness alone.

A candidate qualifies only if it has a coherent independent trigger and requires materially different execution, evidence, decisions, or verification. Document that difference with a fresh task where the nearest skill is insufficient. A different industry, country, platform, audience, file format, or wording is not enough by itself. Put simple variants into existing inputs or edge cases. Separate jurisdiction-specific skills only when verified procedural differences justify them. Do not split a routine checklist into multiple skills merely to increase the count.

Keep a rejection and merge ledger so later agents do not repeatedly propose the same idea. Assign permanent IDs only after scope approval; check codes and names through factory tooling. Revisions to the original 544 are tracked separately from accepted additions.

## 4. Author and review in controlled batches

Use a coordinator plus three workers when four concurrent slots are available. Workers own disjoint domain folders and staging manifests. Rotate authors and reviewers so nobody is the sole judge of their own work. The coordinator owns the cross-track duplicate ledger, serial registry ingestion, release accounting, and shared tooling changes.

Start with authoring batches of 10 skills. Each batch must contain individually approved candidate cards. Writers follow SPEC.md and the accuracy rules; they must not fill a common template with interchangeable domain words. Each procedure needs its own meaningful decisions, artifact, failure cases, and example. Avoid unsupported claims of completed external actions.

Before saving each skill, enumerate its specific factual claims privately. Keep only certain stable facts, verify against primary sources, use a precise verification placeholder, or delete the claim. Recompute fictional arithmetic using a calculator or executable check. Current laws, deadlines, standards, APIs, versions, prices, and platform rules are verification inputs, not assertions of current truth. Technical implementations record the tested environment and runnable verification rather than implying universal compatibility.

Every accepted skill must pass:

1. **Scope review:** useful independent task; concrete distinction from its nearest neighbors.
2. **Accuracy review:** supported specific claims, explicit unknowns, current-source verification steps, checked arithmetic.
3. **Structural checks:** registered metadata, required sections, size limits, templates, references, and mechanical quality gates.
4. **Independent execution:** fresh ordinary request, missing-input request, and edge/failure request, written by a reviewer rather than copied from the author's example.
5. **Artifact review:** the result actually meets the promised output contract. Code is run when execution is required; generated artifacts are opened or inspected using suitable tools. A prose specification is not recorded as a finished binary document.
6. **Neighbor routing:** distinguish this skill from a nearby one on a boundary request. Wrong routing means revise triggers or merge scopes.
7. **Capability review:** missing browsing, file access, or external permissions produces an honest limited result and a clear next step; it never produces fabricated completion.

Keep fixture, actual result, assertions, reviewer, environment, and disposition for each run. Any failed required assertion blocks acceptance until corrected and rerun. Do not call structural validation a substantive audit. Mark audited only with recorded review evidence that satisfies the agreed audit process.

Require three fresh execution cases per addition, giving a planned minimum of 5,000 × 3 = 15,000 execution cases, plus neighbor-routing checks. Pilot a second available model or agent runtime across every active track and every capability class. Record exactly which skills were tested on which systems; do not infer universal compatibility from a sample. If a second system is unavailable, keep that claim explicitly untested.

## 5. Deliver in gated waves

| Wave | Accepted additions in wave | Cumulative additions | Expected total with unchanged baseline | Exit condition |
| --- | ---: | ---: | ---: | --- |
| Preparation | 0 | 0 | 544 | Baseline inventory, source ledger, duplicate rubric, and test evidence format ready |
| Pilot | 100 | 100 | 644 | Ten varied tracks exercised; author/reviewer process and source handling demonstrated |
| Breadth | 400 | 500 | 1,044 | Every viable track represented; duplicate and test failures drive allocation changes |
| Expansion A | 900 | 1,400 | 1,944 | New batches pass cross-track comparison and execution gates |
| Expansion B | 1,200 | 2,600 | 3,144 | Review capacity keeps pace; no unreviewed output counted |
| Expansion C | 1,200 | 3,800 | 4,344 | Remaining gaps prioritized from task evidence rather than title counts |
| Completion | 1,200 | 5,000 | 5,544 | All additions accepted, source notices complete, indexes and portable package verified |

These are proposed milestones, not elapsed-time promises. Measure discovery, authoring, review, correction, and packaging effort during the pilot. Estimate subsequent duration from observed accepted-skill throughput and available reviewer capacity; report assumptions. Slow or stop a production queue when review backlog grows. Replace rejected candidates rather than relaxing gates.

For the first 100, investigate ten candidate families each in procurement, logistics, facilities, accessibility, archives, environmental records, healthcare administration, scientific reproducibility, software maintenance, and administrative casework. Confirm distinctness before turning those families into individual skill titles. This pilot deliberately combines undercovered work with overlap-prone existing areas to test both discovery and rejection discipline.

## 6. Tooling and deliverables

Before scaling, extend factory tooling only where existing commands cannot support the process. Proposed additions are a source provenance ledger, candidate decision ledger, semantic comparison report, behavioral evidence runner, and release acceptance report. These are requirements, not claims that new commands already exist. Preserve the existing registry status vocabulary unless a separately reviewed change is necessary; keep detailed acceptance evidence in linked records.

Use existing `sf.py` commands for registry queries, serial ingestion, validation, quality, coverage, overlap checks, indexes, routing, export, and packaging. Check command usage before invoking unfamiliar options. Add focused regression tests for any new tooling behavior. Keep registry writes serialized even when authors work in parallel.

Produce during implementation:

- Source ledger with pinned provenance, license decisions, upstream relationships, and adaptation notes.
- Candidate queue and rejection/merge ledger with nearest-neighbor reasoning.
- New portable skills inside the existing factory, plus any necessary permitted reference material.
- Per-skill independent test evidence and batch review records.
- A completion report separating baseline, additions, revisions, retirements, failed candidates, validated skills, audited skills, and tested runtimes.
- Updated router and domain indexes; reproducible portable export and integrity-checked archive.
- Reviewable Git checkpoints after accepted batches; commit and push only according to the user's applicable authorization and the environment's permissions.

Report progress from observed `sf.py` output only. Extend its reporting before presenting new acceptance metrics if needed; never substitute generated filenames or proposed titles for finished skill counts. Final acceptance requires 5,000 net additional distinct skills with required evidence, no unresolved blocking findings, and a verified distributable package. If review finds overlap or weak utility, reopen those items and replenish the gap.

## Immediate next actions

1. Establish source and candidate ledgers without importing raw third-party skill packs.
2. Inspect individual skills from the verified seed repositories, pin revisions, and resolve license handling.
3. Compare promising workflows with existing and pending skills; select the first pilot batch from demonstrated gaps.
4. Author and independently test that batch before expanding production.
5. Use pilot evidence to revise track allocations and estimate the remaining work.

This planning deliverable does not itself begin mass skill generation or assert that 5,000 distinct candidates have already been discovered.
