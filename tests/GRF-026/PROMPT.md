Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-026
name: graph-partition-ownership-reconciliation
domain: Graph Engineering Foundations
subdomain: Partition ownership evidence
version: 1.0
description: Reconcile owner and replica records across graph partitions against a frozen placement contract when boundary relationships or repartitioning could omit or duplicate logical graph state.
triggers: ["reconcile graph shard boundaries", "check graph partition ownership", "find missing graph replicas", "audit graph placement epochs", "verify cross-shard edge copies"]
not_for: ["comparing community labels [GRF-013]", "implementing relational storage [GRF-014]", "reconciling restored service views [GRF-024]", "selecting a partition optimization algorithm", "proving distributed atomicity"]
requires: []
risk_level: medium
---

# Graph Partition Ownership Reconciliation

## Purpose
Reconcile each logical node and edge with its declared storage owner and required partition copies. Produce specific placement witnesses so an operator can distinguish a missing replica from conflicting ownership or mixed placement revisions. The result describes the inspected snapshot, without proving distributed consistency during concurrent changes.

## Inputs to collect
1. **Logical graph manifest** — obtain node IDs, edge IDs, endpoints and relevant properties. Why: placement counts alone cannot establish graph completeness. Default: no complete reconciliation without an authoritative inventory.
2. **Placement contract** — obtain the owner partition for every object and the required copy locations. Why: replica copies are legitimate only under an explicit policy. Default: unresolved; do not derive storage ownership from community labels.
3. **Placement epoch** — identify the contract revision and snapshot boundary. Why: old and new ownership records can coexist during migration. Default: unresolved; request the intended epoch.
4. **Partition extracts** — obtain physical copy rows with partition, logical ID, role, epoch and payload evidence. Why: a global merged map can hide duplicate ownership. Default: missing extracts remain unavailable, not empty.
5. **Boundary policy** — specify which endpoint copies a stored edge requires locally. Why: some systems use remote references rather than local replicas. Default: no assumed policy; record unsupported boundary checks.
6. **Repair authority** — name owners of placement changes and required consumer queries. Why: removing a duplicate-looking copy can remove required availability. Default: diagnostic report only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the logical manifest, placement contract and observation boundary under one epoch.
2. Preserve physical rows before grouping them by logical identity, rejecting duplicate physical keys instead of silently overwriting them.
3. Verify that every logical object has exactly one declared owner and that its owner is among its required locations.
4. Validate edge endpoints against the logical node inventory, including isolated nodes that never appear in edge rows.
5. Compare observed owner claims with the declared owner for each object, retaining both absent owners and unexpected owner claims.
6. Compare required and observed copy locations, distinguishing missing, unexpected and unavailable observations.
7. Compare every copy's epoch and payload with the frozen contract before counting it as an acceptable replica.
8. ⚠️ Check the supplied boundary policy for each edge location; report missing endpoint copies or invalid remote references rather than inventing local nodes.
9. Reconstruct one logical graph from the accepted copies, preserving separate parallel edge IDs and rejecting conflicting payloads.
10. Compare selected global query results with the independent logical reference, preserving row multiplicity where the query contract requires it.
11. Propose owner-reviewed repairs and rerun the reconciliation on a separate preview; preserve the original findings and record actual execution boundaries.

The Python 3 reference checks a declared placement manifest against complete physical extracts. Execute it and record the interpreter version. Objects use keys such as `N:A` and `E:e1`; expected entries are `(owner, required_locations, payload)`, and observed rows are `(partition, key, role, epoch, payload)`. Payloads are already normalized comparable values. Prevalidate string identifiers and row shapes. Endpoint policy and live query execution are separate procedure steps; this fixture does not implement a distributed protocol.

```python
def reconcile(expected, rows, epoch):
    if any(owner not in locations for owner, locations, payload in expected.values()):
        raise ValueError("owner outside required placement")
    seen = set()
    findings = []
    grouped = {key: [] for key in expected}
    for partition, key, role, observed_epoch, payload in rows:
        physical = (partition, key)
        if physical in seen:
            raise ValueError("duplicate physical copy")
        seen.add(physical)
        if role not in {"owner", "replica"}:
            raise ValueError("unknown role")
        if key not in expected:
            findings.append((key, "unexpected object", partition))
            continue
        grouped[key].append((partition, role))
        owner, locations, wanted = expected[key]
        if observed_epoch != epoch:
            findings.append((key, "wrong epoch", partition))
        if payload != wanted:
            findings.append((key, "payload mismatch", partition))
    for key, (owner, locations, payload) in expected.items():
        copies = grouped[key]
        actual = {p for p, role in copies}
        claims = {p for p, role in copies if role == "owner"}
        if claims != {owner}:
            findings.append((key, "owner claims", tuple(sorted(claims))))
        for p in sorted(set(locations) - actual):
            findings.append((key, "missing copy", p))
        for p in sorted(actual - set(locations)):
            findings.append((key, "unexpected copy", p))
    return findings

expected = {
    "N:A": ("L", {"L"}, ("A",)),
    "N:B": ("R", {"L", "R"}, ("B",)),
    "N:I": ("R", {"R"}, ("isolated",)),
    "E:e1": ("L", {"L"}, ("A", "B", "link")),
    "E:e2": ("L", {"L"}, ("A", "B", "link"))}
rows = [(p, key, "owner" if p == owner else "replica", "v1", data)
        for key, (owner, places, data) in expected.items() for p in sorted(places)]
assert reconcile(expected, rows, "v1") == []
broken = [r for r in rows if (r[0], r[1]) != ("L", "N:B")]
assert ("N:B", "missing copy", "L") in reconcile(expected, broken, "v1")
assert len(expected) == 5 and len(rows) == 6
print("required boundary copy, parallel identities and isolated node checked")
```

Here the contract requires B on L so that both local edge copies have local endpoints. An adapter must independently derive that requirement from the supplied boundary policy; the checker cannot discover an omitted placement requirement. A stale owner can still occupy its expected location, so an empty missing-copy list is not a pass when epoch or payload findings remain. Use all findings together, and do not call an incomplete extract complete merely to run the fixture.

## Decision rules
- IF owner claims disagree with the contract THEN preserve every claim for adjudication BECAUSE choosing one silently hides split ownership.
- IF several physical copies share one logical ID THEN apply the placement policy BECAUSE required replicas are not duplicate logical entities.
- IF epochs differ THEN report a mixed observation BECAUSE apparent missing ownership may reflect an unfinished migration.
- IF a partition extract is unavailable THEN keep its completeness unresolved BECAUSE unavailable evidence is not an empty partition.
- IF a repair removes a boundary copy THEN rerun endpoint and global query checks BECAUSE local placement changes can break cross-partition access.

## Output template
```text
Boundary: <logical revision, placement epoch, extract completeness; maximum 60 words>
Contract: <object owner/copy policy and boundary rule; maximum 80 words>
Witnesses: <object | finding | physical locations | expected evidence>
Logical reconstruction: <identity/payload/parallel-edge checks or pending>
Query comparison: <query | expected/observed | executed or pending>
Repair preview: <proposal | owner | recheck result or pending>
Decision: <conforms to inspected contract / violates / unresolved; maximum 80 words>
```

## Quality checklist
- [ ] Logical manifest includes isolated nodes and parallel edge IDs.
- [ ] Owners and required replicas come from a declared contract.
- [ ] Physical duplicate rows cannot disappear during map construction.
- [ ] Epoch and payload disagreements appear beside placement findings.
- [ ] Missing observations are distinguished from complete empty extracts.
- [ ] Boundary requirements reflect the supplied local/remote policy.
- [ ] Reconstructed queries retain the declared multiplicity.
- [ ] Repair execution and distributed consistency remain separately evidenced.

## Anti-patterns
- **Community becomes owner**: reuse analysis labels as storage authority. Fix: obtain the placement contract.
- **Replica deletion**: deduplicate physical copies indiscriminately. Fix: reconcile required locations first.
- **Count-only parity**: accept matching totals after replacing an edge ID. Fix: compare complete logical records.
- **Epoch blending**: combine old owners with new replicas. Fix: freeze the intended epoch and expose mixed observations.
- **Offline certainty**: claim atomic migration from extracts. Fix: limit findings to the observed boundary.

## Worked example
**Input:** Fictional fixture above supplies v1 and complete extracts, but omits B's replica on L. Its boundary policy requires local endpoint copies. No service queries or repair have run.

**Output:**
```text
Boundary: Fictional logical manifest; v1 placement; supplied extracts declared complete.
Contract: A/e1/e2 owned on L; B/I owned on R; B replica required on L; local endpoints required.
Witnesses: N:B | missing copy | L absent, R owner present | contract requires L and R.
Logical reconstruction: Five logical IDs retain separate e1/e2 and isolated I; local endpoint availability fails on L.
Query comparison: Global consumer query execution pending; offline identity inspection does not establish service availability.
Repair preview: Restore authorized B replica on L | placement owner | pending; rerun epoch, payload and endpoint checks.
Decision: Violates inspected placement contract; no live repair or atomicity established.
```

**Bad output:** “Remove B from R because it already belongs to the L community.”
This substitutes an analytical label for ownership and deletes the authoritative copy without evidence.

## Edge cases
- **Migration in progress**: request an epoch-specific acceptance rule; retain both observed states without silently selecting a winner.
- **Remote endpoints permitted**: verify remote reference resolution under the supplied policy; do not demand unnecessary local replicas.
- **Identical parallel edges**: preserve distinct edge IDs even when payloads match.
- **No edges**: reconcile every node and its copies; isolation does not exclude storage ownership.
- **Conflicting replica payloads**: report each physical location and expected payload; do not select the newest timestamp without an approved conflict rule.

## Test case
**Input:**
> Fictional N:B is owned by R with a required replica on L. Both extracts claim owner, and L reports an old epoch. Diagnose this without changing storage.

**Assertions:**
1. Reports conflicting owner claims against R's declared ownership.
2. Reports L's epoch mismatch even though both locations exist.
3. Does not delete or promote either copy automatically.
4. Keeps live consistency and repaired-state verification unresolved.
</skill>

<user_request>
Fictional N:B is owned by R with a required replica on L. Both extracts claim owner, and L reports an old epoch. Diagnose this without changing storage.
</user_request>
