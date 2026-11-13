# GRF-017 independent review

Reviewer: rank_review, 2026-11-14. Decision: qualified acceptance for coordinator ingestion and checks; no blocking finding. The author had not completed execution evidence, so this review extracted and tested the actual draft from scratch. Only this log was changed; no registry, skill, commit or push operation was performed.

## Completeness and selected-neighbor comparison

Read the full draft and SPEC. Direct tools.sf.validate_text returned empty errors and warnings. Read actual GRF-002 and TDE-004 procedures after sf.py lookup; GRF-014 inputs/procedure were read during the immediately preceding comparison work. GRF-002 adjudicates whether nodes represent one entity and previews a potentially many-to-one merge. TDE-004 plans producer/consumer compatibility and tests required-field presence. GRF-014 implements initial relational storage and persistence checks. GRF-017 instead constructs an injective, complete identity translation into a different field representation, verifies an inverse and preserves version-scoped consumer meaning through swaps. Its executable artifact and rejection decisions are substantively distinct from those selected neighbors. This is not an exhaustive catalog uniqueness proof.

## Actual executed evidence

Extracted the exact Python code fence and ran it on Python 3.14.6. Observed output:

```text
swap, parallel edges, loop, inverse and copy isolation passed
all 6 identity permutations: inverse, translated outgoing query and nested copy isolation passed
7 malformed/collision inputs and incomplete inverse rejected; empty and disjoint rename passed
runtime 3.14.6
validation ([], [])
```

The six independent permutation cases used nodes A/B/I, nested node properties and provenance, distinct parallel A-to-B edges p/q and a B self-loop. For every permutation of the target IDs, the inverse restored the complete original records, a translated outgoing query for original A returned exactly p/q, and a mutation of a nested target property did not alter the original. A separate rename into X/Y/Z also round-tripped. Empty inventory and mapping returned empty target artifacts.

Seven rejected inputs covered collision with an unchanged identity, missing mapping entry, extraneous mapping entry, repeated edge ID, dangling source endpoint, empty target ID and a non-dictionary property value. An incomplete inverse was rejected separately. Source inputs remained unchanged throughout failure tests. The reference intentionally assumes validated tuple shapes/plain copied data, and the inverse assumes its generated target shape; the prose requires validation of extra/missing fields for externally edited targets. No generic serialization, arbitrary-object copying, production database or crash-recovery claim was tested.

## Specific-claim and correctness review

Complete mapping coverage and uniqueness of target values establish a one-to-one correspondence between the supplied source IDs and generated target IDs. The inverse dictionary is therefore unambiguous on that target inventory. Simultaneously applying the frozen map to both edge endpoints preserves direction and the equality relationships needed for loops; retaining separate edge IDs preserves parallel relationship evidence. A many-to-one mapping is rejected before transformation, including a renamed node colliding with an unchanged node. Copying properties avoids preview aliasing of the tested nested mutable values. Source/target namespace qualification is necessary during A/B swaps because an unqualified string can denote different source identities across revisions.

All numerical claims are fixture counts or internally tested arithmetic. No current law, release, storage capability or fabricated source is asserted. Round-trip success covers the frozen source representation; it cannot prove compatibility with absent consumers or preserve post-cutover writes without a separate recovery mechanism. The draft states those limits consistently.

## Ordinary procedural application

Input: fictional V1 contains A/B/I with p/q A-to-B and loop B-to-B, supplied properties/provenance. Mapping A-to-B, B-to-A, I-to-I; target uses vertices/links fields. No live cutover requested.

```text
Scope: V1 frozen fictional snapshot to V2 named-field representation; offline preview only.
Mapping: V1/A -> V2/B, inverse B->A; V1/B -> V2/A, inverse A->B; V1/I -> V2/I, inverse I->I.
Artifacts: Generated target and inverse map; complete frozen V1 records retained.
Parity: p/q become B->A; loop becomes A->A; I retained. Executed inverse equality includes properties and provenance. Translated outgoing query for V1/A returns p/q in V2.
Recovery: Offline inverse and nested copy-isolation checks passed. Post-cutover write handling not supplied or tested.
Consumers: Pending; a V1/B reference resolves to V2/A, not V2/B. No unqualified alias accepted.
Decision: Preview verified for the tested frozen artifact; cutover incomplete pending consumer, source-consistency and live-recovery evidence.
```

This distinguishes actual fixture execution from operational readiness and retains isolated nodes, multiplicity and self-loops.

## Missing-input application

Input: “Rename our graph IDs and deploy it,” without a complete snapshot, map or consumer information.

Response: “Can you provide the frozen node/edge snapshot with properties and source revision? What complete old-to-new identity and field mapping should apply, including unchanged nodes? Which readers/writers reference those IDs, and what authorized cutover and post-cutover-write recovery mechanism is available?”

Three grouped questions in one message. No source identity is inferred, partial map transformed, database changed or rollback success claimed. The default remains a preview until required evidence exists.

## Collision edge application

Input: fictional P/Q/R with separate u/v P-to-Q, map P-to-Q, Q-to-Q, R-to-R, no merge evidence.

```text
Scope: Supplied frozen P/Q/R artifact; proposed rename only.
Mapping: P->Q and Q->Q collide; R->R unchanged. No unambiguous inverse exists for Q.
Artifacts: Original nodes and u/v retained; no accepted migrated target or inverse produced.
Parity: Transformation rejected before copying; original edge identities/endpoints remain unchanged.
Recovery: No inverse run claimed for the rejected mapping; source preserved.
Consumers: Unassessed; no alias or cutover accepted.
Decision: Blocked; supply an injective complete mapping or route the many-to-one request to a separately evidenced entity-merge decision.
```

The collision rejection was independently executed using the equivalent A/B/I fixture above. All published test assertions hold. A later source-version change would similarly invalidate a current-parity claim until captured writes are reconciled or the preview is rebuilt; offline success does not remove that gate.
