# GRF-057 independent review

Reviewer `g32_reviewer`. Read G57 scope, SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-002, GRF-017, GRF-050 and GRF-003. Those review many-to-one merges, bijective migration, node retirement and edge import. GRF-057 instead allocates each occurrence of one conflated node independently to a new identity or holds the entire edge, including two roles of one self-loop. This is scoped comparison evidence, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed full Python 3 reference under Python 3.14.6; its assertions printed `endpoint occurrences, held edge and inverse replay checked`. Exhaustively independently checked all 243 allocations of five incident endpoint occurrences to A, B or unresolved. For each, the candidate node list, accepted/held edge-ID partition, exact rewritten source/target roles, relation, locator, property payload and inverse replay matched a separate occurrence-ledger calculation. Nonincident e5 remained accepted unchanged once. A self-loop X→X could become A→B only when the source and target occurrence dispositions separately said A and B.

The submitted-result verifier rejected duplicate accepted e1 fan-out, forged e4 A→A contrary to its target-role disposition, collateral loss of unrelated e5, and a modified e1 property payload. Stale revision, new-ID collision, string-shaped edge, duplicate edge ID, unknown endpoint, missing occurrence role, unapproved new ID and missing evidence were rejected before preview. Final `sf.validate_text` returned zero errors and warnings. The inverse is a technical reconstruction of old endpoint IDs; it does not prove real-world identity truth or consumer query equivalence.

## Ordinary scenario

```text
Scope: Fictional S1 at v1; old X; approved A and B; offline preview.
Occurrence ledger: e1 source→A s1; e2 source→B s2; e3 target unresolved s3; e4 source→A and target→B s4.
Candidate nodes: Org1,Org2,Y,A,B.
Accepted edges: e1 A worksAt Org1 s1 {role:staff}; e2 B worksAt Org2 s2 {}; e4 A follows B s4 {kind:source}; e5 Y worksAt Org1 s5 {}.
Held edges: e3 Y knows X s3; target referent unresolved.
Verification: Source IDs partition 4 accepted/1 held; relation, properties, locator and inverse endpoints replayed.
Consumer checks: Query comparison pending owner-supplied old/new identity scopes.
Limits: Identity evidence supplied for exercise only; no live write or full cutover.
Next action: Resolve e3 from source evidence and rerun against a frozen revision.
```

## Missing-input scenario

```text
Scope: Old X and proposed new IDs A/B given, but complete incident-edge inventory absent.
Occurrence ledger: Pending all edge IDs and source locators.
Candidate nodes: Not computed.
Accepted edges: None computed.
Held edges: Unresolved inventory; no fabricated edge disposition.
Verification: Partition and inverse replay not executed.
Consumer checks: Pending scoped source graph and affected queries.
Limits: A partial extract cannot establish complete split coverage.
Next action: Request frozen source nodes, identified edges and per-occurrence evidence together.
```

## Edge/Test scenario

```text
Scope: Fictional S1 e4 X→X follows with source/target occurrences independently reviewed.
Occurrence ledger: e4 source→A from s4-source; e4 target→B from s4-target.
Candidate nodes: A,B plus unchanged non-X nodes.
Accepted edges: e4 A follows B s4 {kind:source}.
Held edges: e3 remains unresolved in the complete S1 preview.
Verification: Source e4 maps back to X→X; forged A→A rejects against target-role ledger.
Consumer checks: Old X self-loop versus new A→B query semantics need owner review.
Limits: Technical inverse replay does not prove the real identities.
Next action: Preserve s4 evidence and resolve e3 before cutover.
```

## Verdict

All four Test case assertions pass. The fictional example's five source edges partition into four accepted and one held, with e4's two endpoint roles independently supported. Held e3 prevents a complete cutover claim. No changing current fact, invented source or live write is asserted. Recommend acceptance within the frozen owner-approved split-preview scope. No required repair found.
