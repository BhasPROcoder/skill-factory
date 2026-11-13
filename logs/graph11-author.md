# GRF-011 candidate and author evidence

Authored 2026-11-13 by g08_review_resume. Candidate bipartite-matching-certificate is held for independent review; no registry ingestion or status marking performed.

## Scope and selected-neighbor comparison

Used sf.py lexical assignment/allocation/matching searches. Read actual RNT-001, MSE-002 procedure, SHP-001 inputs/procedure and GRF-001 contract design, with graph traversal/component methods already inspected in the preceding review task.

- RNT-001 reconciles promises, physical identities, current eligibility and proposed rental substitutions; it does not compute or certify the global maximum number of pairs. GRF-011 requires that domain evidence as an input and supplies an exact graph solution and certificate, without replacing readiness/custody/authority checks.
- MSE-002 maps semantic query needs to suitable pages, not exclusive unit-capacity matching or an optimality proof.
- SHP-001 reconciles content quantities, package memberships and revision evidence; assignments can be many-to-many and are not an optimization objective.
- GRF-001 establishes model semantics; GRF-006 bounded traversal and GRF-007/008 connectivity partitions do not perform alternating reassignment or produce equal-size cover certificates.

Distinct artifact: eligible matching, complete unmatched sets, a vertex cover touching every eligibility edge, and equality of their sizes. The scope is cardinality-only, bipartite, unit-capacity, with no weighted, preference, fairness, multi-capacity or scheduling claim. Fixed commitments require a residual calculation and explicitly conditional optimum. No external skill code/content was copied; the method and fixture were authored from the approved queue and selected catalog gap.

## Specific-claim review before saving

Checked the augmenting path mechanics: traversing unmatched edges toward the right and matched edges back toward the left permits replacement rather than merely greedy allocation. Each successful augmentation increases cardinality by one. The reference uses a fresh seen-right set per search to terminate and recursively reroutes only existing owners.

Reviewed certificate proof directly: if every eligibility edge touches a cover, every matching edge must consume a distinct cover vertex because matching endpoints cannot repeat. Therefore cover size upper-bounds any feasible matching size. A feasible matching of the same size attains that bound and certifies maximum cardinality. No theorem name or external attribution is needed for this explicit argument. Alternating reachability produces the cover from unreached left and reached right nodes; executed checks verify both edge coverage and equal size rather than assuming the construction succeeded.

The example is fictional: A-x, A-y, B-x contain three allowed pairs; choosing A-y and B-x uses two pairs with two left cover vertices, while C stays unmatched. A-x alone is only one pair and not optimal. Empty-edge and empty-side cases retain all unmatched IDs. Same labels must be namespaced, unresolved eligibility is not invented, and an unmatched node with neighbors can be matched in another optimum. Runtime currency, production scale, real eligibility and execution authority are not asserted.

## Actual execution

Used Python 3.14.6, extracted and executed the exact Python fence. Direct `tools.sf.validate_text` returned errors=[] and warnings=[]; body count 1664 words.

Observed output:

```text
greedy-trap, isolate and shared-neighbor certificates passed
rejected unique disjoint inventories required
rejected unique disjoint inventories required
rejected wrong side or unknown endpoint
rejected duplicate eligibility pair
512 three-by-three graphs matched brute-force optimum and cover certificates
published test, empty sides and invalid input checks passed
```

Additional assertions checked the published P/Q/R-u/v fixture, empty left inventory, empty right inventory, repeated left ID, overlapping side IDs, wrong-side endpoints and repeated eligibility pair.

The independent bounded oracle enumerated all 512 eligibility subsets of a three-by-three bipartite universe. For each graph it brute-forced all candidate pair subsets of sizes up to three and rejected repeated endpoints, obtaining the exact maximum size independently of alternating-path logic. Returned matching sizes equaled that optimum in every case; every edge was covered and cover size equaled the optimum. These checks support the small reference, not arbitrary scale, recursion depth or real assignment completeness.

Independent ordinary/missing/edge procedural review and coordinator registry checks remain required. No live allocations, commitments or source records were changed.
