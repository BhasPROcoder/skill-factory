# Candidate G57: conflated-entity split edge reassignment

## Decision

Pursue a bounded graph-identity repair preview for one source node known, by supplied identity evidence, to conflate two or more distinct entities. Allocate new node IDs under an owner-approved split decision; reassign each **incident edge endpoint occurrence** through an explicit evidence-backed disposition; hold ambiguous occurrences rather than copying them to every new node. Preserve edge IDs, direction, relation and source locators, and verify the preview can be mapped back to the frozen source records. This is a candidate scope, not a registered skill or authorization to change a live graph.

## Distinctness and nearest procedures

- GRF-002's actual procedure reviews **many-to-one merges**, builds groups of same-entity nodes, rewrites their incident endpoints and checks newly coincident relationships. G57 is a **one-to-many split** of one conflated node: each old endpoint occurrence may map to a different new identity or remain unresolved. A global node-ID replacement cannot perform this decision. Do not reuse G02's merge-group method with labels reversed.
- GRF-017's actual migration procedure requires complete target uniqueness across source nodes and stops many-to-one identity adjudication. Its transform applies a supplied identity mapping, checks inverse reconstruction and consumer aliases. G57 must first decide the one-to-many allocation of incident endpoints from source-specific evidence, including two occurrences of the old node within one self-loop. It must not claim semantic reversibility merely because a technical inverse can recover the old conflated ID.
- GRF-050 previews node retirement with restrict/cascade incident-edge policies; it removes the node or edges and checks referential integrity. G57 preserves accepted edge IDs while changing individually justified endpoints, and holds unresolved edges rather than cascading them.
- GRF-003 reconciles an incoming edge list and quarantines malformed rows; it does not adjudicate a previously conflated node's incident-edge identities.

`sf.py` searches for `entity split`, `node split` and `incident edge reassignment` surfaced those neighbors but no matching split-specific method. This is scoped discovery evidence, not whole-library uniqueness proof. Before authoring, inspect final neighboring procedures again and reject a draft that merely renames migration or node retirement.

## Contract and method

Inputs: a frozen graph revision with unique node and edge IDs; target conflated node `X`; owner-approved new IDs `A` and `B` with identity evidence and no collisions; all node/edge source locators; and a disposition for each **source or target endpoint occurrence** of `X` in every incident edge. A disposition is one approved new ID with evidence, or `unresolved` with reason. Nonincident endpoints are immutable. For a self-loop `X→X`, source and target dispositions are independent. Preserve the original `X` and every held edge in an exception ledger; the candidate graph contains A/B, nonincident nodes and only edges whose X occurrences have approved assignments. Do not clone one source edge into multiple edges, silently choose by label similarity, or erase an unresolved source record.

For each accepted edge, compare ID, relation, properties, direction and source locator with the original. Replay its endpoint assignments against the occurrence ledger. Verify that accepted and held incident edge IDs partition the original incident inventory exactly once; nonincident edges remain byte-for-byte or field-for-field equivalent. Apply a technical inverse `A→X`, `B→X` only to check that approved preview records reconstruct their original endpoint IDs; this does not prove the real-world identities were correctly adjudicated. Compare representative affected queries before/after with their identity scopes declared. Mark the split preview incomplete while any occurrence remains unresolved; no production cutover or alias promise follows from the offline exercise.

## Executable fictional fixture

Fictional source nodes `X, Org1, Org2, Y`, where owner evidence says X conflates two people represented by new IDs `A` and `B`. Source edge records:

- `e1: X→Org1 worksAt`, source locator `s1`; approved source occurrence X→A.
- `e2: X→Org2 worksAt`, locator `s2`; approved source occurrence X→B.
- `e3: Y→X knows`, locator `s3`; target occurrence X is **unresolved**, so e3 is held with its original evidence and no candidate edge is invented.
- `e4: X→X follows`, locator `s4`; separate source occurrence X→A and target occurrence X→B are approved, so the candidate edge is `A→B` with the same e4 identity and direction.
- `e5: Y→Org1 worksAt`, locator `s5`; nonincident edge is unchanged.

Expected accepted candidate edges are e1 `A→Org1`, e2 `B→Org2`, e4 `A→B`, and e5 `Y→Org1`; held set is exactly `{e3}`. An inverse endpoint replay maps A/B back to X and reproduces e1/e2/e4's source endpoints. The candidate is **not ready for complete split cutover** because e3 has no approved target identity. Inject a forged allocation of e3 to both A and B: reject duplicate source edge identity/fan-out. Inject e4 source and target both A: reject against the approved per-occurrence ledger. Inject unknown new ID, missing incident edge, changed relation/locator and a new-ID collision: reject each. Resolving e3 later requires new evidence and a new preview, not a default.

All people, organizations and locators are fictional. No source truth, legal identity status, live database edit or current platform behavior is claimed. A full skill needs SPEC structure, runnable Python 3 reference, independent review and `sf.py` acceptance checks before counting.
