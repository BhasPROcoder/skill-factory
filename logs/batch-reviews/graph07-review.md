# GRF-007 independent review

2026-11-13; reviewer g07_review_resume. Decision: accept for coordinator checks with no blocking findings. No skill or registry changes made.

## Scope and selected-neighbor comparison

Read AGENTS.md, SPEC.md, the complete GRF-007 draft, GRF-004 and the relevant GRF-006 procedure/output contract. GRF-004 checks a supplied rooted-forest constraint and emits incoming-parent violations plus root-unreachable nodes. GRF-006 returns a bounded seed-reachable set, minimum hops and truncation evidence. GRF-007 instead partitions every included node without a depth cap, retains spanning witnesses and identifies observed excluded edges joining projected components. These artifacts and filter-dependent separation decisions are distinct. This is selected-neighbor comparison, not a claim of exhaustive semantic uniqueness across the catalog.

## Actual execution

Extracted and executed the exact Python fence using Python 3.14.6. The snippet printed `filtered partition, isolates and excluded-link comparison passed`. Direct `tools.sf.validate_text` returned errors=[] and warnings=[]. This is draft validation, not registry acceptance.

Additional independently executed fixtures:

- Reverse-arrow: A/B/C with e:B->A returns A/B in component A, C singleton, witness (A,B,e). The witness opposes the source arrow and therefore supports weak connectivity only.
- Filter isolate: A->B of type x and B->C of type y, retaining x, returns A/B together and C singleton; y is the excluded crossing edge.
- Loop and parallel relationships: A->A plus A->B and B->A of type x returns A/B together, C singleton, one spanning edge p; the loop does not create another component.
- Empty inventory and edges return empty membership, empty witnesses and no crossing edges.
- Empty allowed-label set with A->B returns two singleton components and the omitted edge as a crossing witness.
- Duplicate node IDs, unknown endpoint, and duplicate edge ID each raised ValueError as expected.
- Input lists remained unchanged in all five normal fixture calls.
- For each normal fixture, an assertion checked that discovery-edge count equals node count minus component count.
- Published P/Q/R/S test executed: membership P:P,Q:P,R:R,S:S; witness P:(P,Q,x), R/S empty; excluded crossing record y:Q->R of type archived. All expected values asserted.

No remote graph, partial pagination, or external source completeness was tested. The reference deliberately requires tuple-shape prevalidation and implements relation filters with all supplied nodes retained; other projection rules must be materialized first.

## Independent procedural scenarios

These are reviewer applications of the instructions, not a separate model benchmark.

### Ordinary supplied complete fixture

Input: fictional revision T1 with P/Q/R/S, x:P->Q live, y:Q->R archived, all records complete; retain all nodes and live relationships, weak connectivity.

```text
Scope: T1 complete supplied fictional node/edge fixture.
Projection: Weak connectivity; live relations only; all four nodes retained.
Membership: P|P; Q|P; R|R; S|S.
Witnesses: P|x; R|none, singleton; S|none, singleton.
Isolation: R|filter-induced|y is its supplied incident record; S|inventory-only|no incident record in T1.
Excluded links: y|Q->R|P and R|archived relation excluded.
Checks: Executed reference; exact membership and witness values asserted. Every node appears once; x remains internal; x spans P/Q; singleton witnesses need no edges.
Interpretation: Three weak components in this projection. The supplied excluded link joins P/Q to R in the wider fixture. This does not establish a directed Q-to-P path or a source defect.
Next action: Confirm the requested filter supports the decision; no correction justified.
```

All five published assertions hold. Arithmetic: four nodes in one two-node component and two singletons yields three components; one discovery edge equals four minus three.

### Missing required inventory and meaning

Input: "Find disconnected regions" with only an edge A->B, no inventory or connectivity definition.

Response: "Please supply the node inventory and snapshot scope, including any nodes without edges. Do you mean weak/undirected connectivity or directed reachability, and which filters apply? Is the supplied graph complete for that scope, and are excluded records available?"

Three questions in one message; no inferred isolate coverage or connectivity definition. A complete partition remains unperformed until required inputs are resolved.

### Filtered and incomplete edge evidence

Input: fictional observed projection E1 has A/B/C with e:B->A retained; source coverage partial and excluded records unavailable. Weak components requested.

```text
Scope: E1 observed three-node projection; wider edge coverage partial.
Projection: Weak connectivity of the supplied retained records; wider exclusion rules/evidence unavailable.
Membership: A|A; B|A; C|C.
Witnesses: A|e; C|none, singleton.
Isolation: C|unresolved|no supplied incident edge; excluded records unavailable.
Excluded links: Unavailable; none inferred.
Checks: Executed reverse-arrow fixture; coverage and internal-edge checks pass for the observed projection. Witness e links A/B only after ignoring direction.
Interpretation: Two components in E1. Wider-graph separation is unknown; no directed A-to-B route follows from e:B->A.
Next action: Obtain excluded-record and coverage evidence if wider-graph conclusions are required; do not add an artificial bridge.
```

This qualifies the isolation cause instead of treating an observed absence as proof of real separation. Interruption or capped traversal would likewise withhold complete-component status under the explicit decision rule.

## Specific-claim audit

Reviewed weak connectivity versus directed reachability, complete partition/disjointness, spanning discovery witnesses, isolates, projection exclusions, empty graph, and snapshot-local labels. All are stable mathematical/procedural claims, supported by the inspected logic and bounded executions. Worked-example counts are consistent: five nodes form three projected components; adding the supplied excluded link joins the two paired groups, leaving two components. No current API, platform, price, law, invented source or externally changing threshold is asserted. Node-filter behavior is a procedure requirement outside the reference's relation-only fixture, and no unsupported implementation claim is made. No blocking fix identified.
