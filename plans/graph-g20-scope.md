# G20 candidate scope decision

Research checkpoint: 2026-11-14. Candidate only; no registry entry or accepted skill is established by this document.

Proposed task: **knowledge-graph constraint witness review**. Given an explicit constraint contract and a scoped assertion snapshot, produce a violation ledger that identifies the particular constraint and supporting records for each conflict, distinguishes missing evidence from observed violations, and tests proposed repairs without destroying the original evidence.

## Catalog comparison

- GRF-004 was substantively inspected. It validates a parent forest using incoming-edge counts and declared-root reachability. G20 must not reproduce those checks with renamed nodes. Its distinct unit is a semantic constraint and its evidence witness across a typed assertion set.
- GRF-018 was substantively inspected. It defines relation meanings, validates endpoint types, and derives a licensed closure with one witness per triple. G20 must consume a declared semantics and report constraint failures across asserted and derived records; it must not redesign the vocabulary or claim to implement a general reasoner.
- GRF-005 catalog metadata concerns historical graph reconstruction. G20 consumes one explicitly selected context/version; temporal reconstruction is upstream. Mixing time contexts cannot justify a simultaneous contradiction.
- GRF-002 catalog metadata concerns entity merge decisions. G20 must retain separate endpoint identities; a maximum-one constraint violation does not itself authorize merging distinct endpoints.
- G19 is being authored separately. Its planned responsibility is source-span relation candidate extraction. No G19 file was available during this inspection, so comparison with its actual procedure remains an acceptance prerequisite. G20 takes accepted structured assertions rather than extracting or approving natural-language claims.
- `sf.py search 'contradiction'` returned no lexical matches. That is discovery evidence only, not a proof of semantic uniqueness. Broad graph/constraint queries identified the neighbors above.

## Distinct procedure to author

1. Freeze the graph revision, selected context, constraint revision, node inventory, and explicit completeness declarations for each checked relation.
2. Require the owner to choose validation semantics, including whether distinct IDs count as distinct values. Do not import ontology semantics from terminology alone.
3. Keep original assertion IDs and any derived-record support paths in separate ledgers. Reject unsupported derived records before treating their consequences as evidence.
4. Evaluate declared disjoint-type and cardinality constraints. A maximum-value violation can be witnessed by present records; a minimum-value finding needs an explicit closed and complete scope before it can be a confirmed absence violation.
5. If explicit positive/negative assertion conflicts are included, require matching subject, relation, object, time and context. Silence is never an explicit negative assertion.
6. Return one witness per violated constraint/scope with all relevant record IDs. Call it a sufficient witness, not a globally minimal explanation unless minimality was actually established.
7. Propose alternative corrections with source evidence and owners. Never remove the least convenient assertion merely to obtain a passing validator.
8. Rebuild affected derived records and rerun all declared constraints on a separate repaired preview. Distinguish repaired conformance from truth and deployment.

Deliverable fields: scope; semantics; constraint ledger; input exceptions; observed witnesses; unresolved absence findings; proposed alternatives; preview rerun; remaining limits. The runnable reference should demonstrate a bounded, explicitly described constraint subset rather than imply full standard conformance.

## Acceptance scenarios

- Ordinary: a declared maximum-one relation has two distinct values supported by separate source IDs; return the exact witness and retain both sources.
- Missing input: the requested minimum-one relation has no supplied records and no completeness declaration; return unresolved absence, not a confirmed violation or passing result.
- Duplicate evidence: two source records assert the same value; count one distinct value while preserving both evidence records.
- Identity boundary: two different IDs have similar labels; no merge or automatic equality inference is permitted.
- Derived conflict: a licensed derivation produces a value conflicting with a declared constraint; include its rule and source support chain. A proposed repair to a source requires recomputation, not deletion of the visible derived row alone.
- Context mismatch: positive and explicit negative records in different contexts are not reported as a same-context contradiction.
- Repair regression: an alternative resolves one maximum constraint but breaks a required minimum; the full rerun must expose the new failure.

## Remaining authoring gates

Inspect actual G19 and selected identity/storage neighbors before confirming uniqueness; resolve the exact executable subset; independently test ordinary, missing-input and adversarial cases; audit every specific claim; then request coordinated ingestion. No external text or code was copied for this scope research, and no external standard conformance is claimed.
