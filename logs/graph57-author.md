# GRF-057 author evidence

## Distinctness

Read AGENTS.md, SPEC.md, GOLD example and plans/graph-g57-scope.md. Used `sf.py` searches for entity split, node split and incident edge reassignment. Inspected actual Procedure sections of GRF-002, GRF-017, GRF-050 and GRF-003. G02 handles many-to-one merge groups, G17 applies complete bijective identity mapping, G50 retires a node with restrict/cascade policies, and G03 reconciles edge import. G57 instead allocates each occurrence of a conflated old node to one of several approved new identities or holds its edge; a self-loop may map its source and target separately. This is a scoped distinction, not whole-catalog proof.

## Execution

Final direct `sf.validate_text(text,path)` returned `errors [] warnings []`; body word count by whitespace split was 1,791. The full embedded Python 3 snippet printed:

```text
endpoint occurrences, held edge and inverse replay checked
```

Additional executed tests printed:

```text
extra fixtures PASS; occurrence maps 243
```

Tests rejected stale revisions, new-ID collisions, string-shaped edges, duplicate edge IDs, unknown endpoints, missing occurrence role, unapproved new ID, missing held e3, duplicate e3 fan-out, e4 A→A contrary to the approved A→B role mapping, altered relation and altered property payload. Every mapping of the five incident endpoint occurrences to A, B or unresolved (3^5 = 243) passed the exact partition and independent source-record inverse replay checks; unrelated e5 remained accepted exactly once. The fixture is finite and does not establish production performance or real-world identity truth.

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

## Claim audit

Specific claims are exact edge-ID partitioning, per-occurrence endpoint assignment, unchanged relation/locator/property payload and technical inverse endpoint replay; all were exercised. Example count is four accepted and one held from five source edge IDs. The self-loop X→X maps to A→B only because the two endpoint roles have separate evidence. No source truth, live write, current platform API, invented source or universal identity rule is claimed. Registry untouched; independent review required before acceptance.
