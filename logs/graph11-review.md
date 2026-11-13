# GRF-011 independent review

Reviewer: matching_review, 2026-11-13. Decision: accept for coordinator checks; no blocking finding. No registry or skill changes made.

## Scope and selected-neighbor comparison

Read AGENTS.md, SPEC.md, the complete draft and author evidence. Queried sf.py for RNT-001/MSE-002 and read their actual inputs, procedures, rules and output contracts. RNT-001 reconciles physical unit identity, eligibility, existing promises and proposed substitutions; it does not compute a maximum-cardinality assignment or an optimality certificate. MSE-002 maps query needs to page purposes, without exclusive unit capacities or alternating reassignment. GRF-011 has a distinct mathematical artifact: eligible pairs, complete unmatched sets and an equal-size covering vertex set. Its domain constraints remain required inputs, so it does not replace rental readiness or semantic page judgment. Earlier graph reachability skills supply traversal primitives but not the assignment/certificate procedure. This is a targeted comparison, not proof of exhaustive library uniqueness.

## Executed checks

Extracted and executed the exact Python fence under Python 3.14.6. Observed `greedy-trap, isolate and shared-neighbor certificates passed`. Direct tools.sf.validate_text returned errors=[] and warnings=[]. Additional independent fixtures:

- Published P/Q/R-u/v case returned P-v and Q-u, unmatched R, cover-left P/Q and no right cover.
- Longer alternating reroute with A-x/A-y/B-y/B-z/C-x returned C-x, A-y, B-z. All three pairs are covered by left A/B/C; no unmatched entities.
- Shared-neighbor A-x/B-x returned A-x, unmatched B, cover-right x. Both eligibility edges touch that one-vertex cover.
- Empty eligibility with left A/B and right x returned no pairs, unmatched A/B and x, empty cover.
- Empty inventories returned five empty sets.
- Repeated left ID, overlapping side IDs, wrong-side edge, duplicate pair and blank node ID each raised the expected ValueError.
- Assertions checked all input lists unchanged, every edge covered, and matching size equal to cover size for every successful fixture.

These are actual local executions. No live allocation, large/deep recursion benchmark or external eligibility validation was performed.

## Mathematical and specific-claim audit

Each augmenting-path flip replaces alternating pairs and adds exactly one matched pair. The seen-right set prevents repeated recursive exploration within a search. The reference's per-left augmentations preserve endpoint uniqueness, and the final independent assertions reject an invalid matching or cover rather than merely trusting construction.

The certificate argument is sound: every matching edge must touch a cover vertex, and distinct matching edges cannot consume the same vertex. A cover therefore bounds any matching's size from above; equality with a feasible matching proves maximum cardinality. This proof needs neither an external theorem name nor an invented source. The alternating-reachability construction is checked for coverage and equality in the code.

The fictional counts are consistent: three eligibility pairs A-x/A-y/B-x admit two matched pairs A-y/B-x; C has no candidate. A-x alone is feasible but not maximum. Shared-neighbor results do not imply B is unmatched in every optimum. Fixed commitments must be eligible, disjoint and removed before residual optimization; the resulting certificate belongs to the residual graph, with total conditional optimum equal to fixed-pair count plus residual maximum. The procedure explicitly limits this conclusion to the supplied commitments. No current price, platform behavior, release claim, legal threshold or fabricated citation appears. Python 3.14.6 records observed execution only.

## Independent procedural applications

These are reviewer applications of the instructions, not a benchmark against a separate model service.

### Ordinary complete fixture

Input: fictional P/Q/R and u/v, confirmed edges P-u/P-v/Q-u, no commitments, one-to-one cardinality objective, complete supplied snapshot M1.

```text
Scope: M1; left P/Q/R, right u/v; unit capacities, maximum pair count, no fixed commitments.
Matching: P | v | P-v input record; Q | u | Q-u input record.
Unmatched: Left R; right none.
Certificate: Cover-left P,Q; cover-right none; matching size 2, cover size 2.
Checks: Executed local reference; both pairs eligible, endpoints unique, all three edges covered, sizes equal.
Explanation: P can move from u to v so Q can use u. R has no confirmed candidate in M1.
Disposition: Certified scoped maximum of two pairs.
Limits: M1 only; no fairness, cost ranking, current readiness or live allocation verified.
```

All four published test assertions hold.

### Required inputs missing

Input: "Assign everyone to something; use their preferences" with no inventories or eligibility evidence.

Reviewer response: "Please supply the two inventories and confirmed eligible pairs, including source evidence. Is the objective maximum one-to-one pair count, or do preferences, capacities or timing also constrain the solution? Which existing commitments are fixed, and which may be rearranged in a proposal?"

Disposition remains unresolved input. This is one message with three questions; no preferences are silently converted into permissions and no maximum claim is made.

### Shared-neighbor competition

Input: fictional complete M2 left A/B, right x; both A-x and B-x eligible, no fixed commitment or priority, cardinality only.

```text
Scope: M2; two left entities and one right; unit capacities, no fixed pair.
Matching: A | x | A-x input record.
Unmatched: Left B; right none.
Certificate: Cover-left none; cover-right x; matching size 1, cover size 1.
Checks: Executed reference; A-x eligible, unique endpoints, both edges touch x, sizes equal.
Explanation: A and B compete for x in this graph. B-x is another maximum; B is not inherently impossible to match.
Disposition: Certified scoped maximum of one pair.
Limits: Choice of A is no fairness or priority finding; no operational reassignment performed.
```

### Empty eligibility and incomplete evidence

The executed A/B-x empty-edge fixture returns every inventory entity unmatched and an empty cover. If the supplied ledger is explicitly incomplete, the correct disposition is maximum zero within confirmed edges only; it does not establish no feasible real-world assignments. Unknown eligibility must remain in the uncertainty ledger, not be fabricated to raise the count.

## Acceptance limits

No blocking fix identified. Small in-memory fixtures and selected-neighbor comparison support acceptance of this scoped procedure. Recursive depth, production scale, timestamped readiness and real-world authority remain outside tested scope. Structural status and catalog admission belong to the coordinator.
