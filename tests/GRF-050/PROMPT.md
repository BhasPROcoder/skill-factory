Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-050
name: graph-node-retirement-referential-preview
domain: Graph Engineering Foundations
subdomain: Node retirement previews
version: 1.0
description: Preview a proposed graph node retirement against relation-specific incident-edge policies and verify the exact hypothetical surviving inventory.
triggers: ["preview deletion of a graph node", "which edges would disappear with this node", "check graph cascade policy", "retire a node without dangling edges", "review incident relationships before node removal", "verify a hypothetical graph deletion"]
not_for: ["connectivity loss after a node failure [GRF-029]", "database schema and constraint implementation [GRF-014]", "reversible identity migration [GRF-017]", "restored graph reconciliation [GRF-024]", "executing deletion or deciding retention authority"]
requires: []
risk_level: medium
---

# Graph Node Retirement Referential Preview

## Purpose
Preview the exact node and incident-edge records affected by a proposed node retirement in a directed graph. Apply explicit relation-type policies and return blocked, unresolved, or a copy-on-write cascade preview with independent referential checks. This skill prepares evidence for an owner decision; it does not delete source records.

## Inputs to collect
1. **Frozen snapshot** — complete node IDs and directed edge records `(ID, source, target, relation type)` with a revision marker. Why: unseen incident links can invalidate the preview. Default: none, required.
2. **Target node** — exact ID proposed for retirement. Why: aliases or labels may match multiple nodes. Default: none, required.
3. **Relation policies** — for each incident relation type, explicit `restrict` or `cascade` instruction from the responsible owner. Why: graph structure cannot determine retention authority. Default: unresolved for a missing type; no implicit cascade.
4. **Identity and projection** — rules for parallel edges, loops, edge direction and any excluded relation class. Why: each edge ID needs one disposition. Default: preserve all supplied identified directed edges.
5. **Expected revision** — marker the owner approved for preview. Why: a later graph revision may contain different incident edges. Default: none, required for a definitive preview.
6. **Use boundary** — preview, approval packet or execution handoff. Why: the offline artifact is not a database transaction. Default: preview only.

If a required input is missing without a safe default, ask in one message with at most three questions. Keep every source record unchanged while deciding.

## Procedure
1. Freeze the node and edge inventory, target ID, expected revision and relation-policy map.
2. Validate unique nonempty node and edge IDs, exact row shapes, known endpoints and the target's presence. Reject stale revision markers before computing a definitive preview.
3. Find incident edges by exact edge ID whenever the target is either endpoint. A self-loop belongs in the ledger once, not twice.
4. Record each incident edge's direction, relation type and source locator. Keep separate parallel edges as separate ledger rows.
5. Look up each incident edge's explicit policy. Mark missing policy unresolved and `restrict` blocked. Do not infer policy from a neighboring relation's rule.
6. If any policy is missing, report unresolved with every unknown edge ID and request the owner decision. If none is missing but a restriction exists, report blocked with every restricting edge ID.
7. If every incident relation permits cascade, construct a hypothetical copy: remove the target node and exactly its incident edges. Keep all unrelated nodes and edges, including isolates.
8. ⚠️ Independently compute the expected removed-edge ID set from original endpoints and compare it with the preview's removed set. Reject a missing incident edge or collateral removal of an unrelated edge.
9. Replay every surviving edge against the surviving node IDs and preserve its original ID, direction and relation type. Reject any dangling endpoint or changed payload.
10. Report the disposition ledger, exact before/after identities, referential verification and owner review boundary. Re-freeze and recompute if the source revision moves before an authorized execution.

This Python 3 reference uses finite in-memory string identities and a source revision string. `restrict` and `cascade` are policy labels defined for this fixture, not claims about any database's current behavior. Run the whole snippet and record the interpreter version. An actual store needs a separate transaction and post-write check under its verified documentation.

```python
def preview(nodes, edges, target, policies, observed, expected):
    if type(observed) is not str or not observed or observed != expected:
        raise ValueError("snapshot changed or missing")
    if any(type(n) is not str or not n for n in nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("invalid node inventory")
    if target not in nodes:
        raise ValueError("unknown target")
    if any(type(e) not in (tuple, list) or len(e) != 4 or
           any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    if any(a not in nodes or b not in nodes for _, a, b, _ in edges):
        raise ValueError("unknown endpoint")
    if type(policies) is not dict or any(
            type(k) is not str or not k or v not in {"cascade", "restrict"}
            for k, v in policies.items()):
        raise ValueError("invalid policy")
    incident = {eid: (a, b, kind) for eid, a, b, kind in edges
                if target in (a, b)}
    missing = sorted(eid for eid, (_, _, kind) in incident.items()
                     if kind not in policies)
    blocked = sorted(eid for eid, (_, _, kind) in incident.items()
                     if policies.get(kind) == "restrict")
    if missing:
        return {"status": "unresolved", "witnesses": missing,
                "preview": None}
    if blocked:
        return {"status": "blocked", "witnesses": blocked,
                "preview": None}
    survivors = [n for n in nodes if n != target]
    kept = [e for e in edges if e[0] not in incident]
    removed = sorted(incident)
    # Independent replay from original endpoint records.
    expected_removed = {eid for eid, a, b, _ in edges
                        if a == target or b == target}
    assert set(removed) == expected_removed
    assert {e[0] for e in kept} == {e[0] for e in edges} - expected_removed
    assert all(a in survivors and b in survivors for _, a, b, _ in kept)
    assert kept == [e for e in edges if e[0] not in expected_removed]
    return {"status": "preview", "witnesses": removed,
            "preview": (survivors, kept)}

nodes = ["A", "B", "C", "I"]
edges = [("e1", "A", "B", "link"), ("e2", "A", "B", "link"),
         ("e3", "B", "C", "owned"), ("e4", "B", "B", "link"),
         ("e5", "C", "A", "link")]
assert preview(nodes, edges, "B", {"link": "cascade", "owned": "restrict"},
               "S", "S")["witnesses"] == ["e3"]
assert preview(nodes, edges, "B", {"link": "cascade"},
               "S", "S")["status"] == "unresolved"
result = preview(nodes, edges, "B",
                 {"link": "cascade", "owned": "cascade"}, "S", "S")
assert result == {"status": "preview",
                  "witnesses": ["e1", "e2", "e3", "e4"],
                  "preview": (["A", "C", "I"], [("e5", "C", "A", "link")])}
print("blocked, unresolved, parallel, loop and referential preview checked")
```

## Decision rules
- IF the revision differs from the expected marker THEN stop and re-freeze BECAUSE incident membership may have changed.
- IF any incident type lacks an owner policy THEN return unresolved BECAUSE a cascade cannot be assumed.
- IF any incident edge has `restrict` policy and none is unresolved THEN return blocked with its IDs BECAUSE the proposed retirement conflicts with the supplied policy.
- IF all incident policies are `cascade` THEN build a hypothetical preview BECAUSE the policy map permits that structural disposition, subject to owner review.
- IF the preview loses an unrelated edge or leaves a dangling endpoint THEN reject it BECAUSE the referential result is incorrect.
- IF the graph extract is incomplete THEN label known incident edges as partial evidence BECAUSE no exact closure can be certified.

## Output template
```text
Scope: <snapshot and completeness; target ID; node/edge inventory size>
Policy: <relation type -> restrict/cascade or unresolved>
Incident ledger: <edge ID, source, target, type, disposition; one line each>
Decision: <blocked | unresolved | verified hypothetical preview>
Survivors: <node IDs and edge IDs, or pending>
Verification: <removed-ID parity, unaffected-edge parity, endpoint replay, or pending>
Limits: <source records unchanged; owner/transaction checks outstanding; max 2 lines>
Next action: <one concrete owner or analyst step>
```

## Quality checklist
- [ ] Revision, target ID and inventory completeness are explicit.
- [ ] Node and edge IDs are unique; every endpoint exists.
- [ ] Every incident edge has one ledger row, including loops and parallels.
- [ ] Every incident relation type has an explicit policy or unresolved finding.
- [ ] A restricting policy blocks the preview when no policy is missing.
- [ ] Removed IDs equal the original incident-edge ID set exactly.
- [ ] Unrelated edge identities and payloads survive unchanged.
- [ ] Every surviving edge references surviving nodes.
- [ ] No source deletion is claimed from the offline preview.

## Anti-patterns
- **Blanket cascade**: applying one type's policy to another. Fix: require a rule for every incident relation type.
- **Loop double count**: treating a B→B edge as two records. Fix: group by edge ID.
- **Parallel collapse**: keeping one A→B ID while losing another. Fix: reconcile identities, not endpoint pairs.
- **Silent collateral loss**: deleting edges unrelated to the target. Fix: compare complete surviving ID and payload sets.
- **Stale snapshot**: approving a preview built before new edges arrived. Fix: re-freeze and rerun against the expected revision.
- **Execution claim**: describing a hypothetical result as a completed database operation. Fix: label it preview until the owner performs and verifies execution.

## Worked example
**Input:**
> Fictional Vale snapshot S has nodes A,B,C,I. Directed edges e1/e2 A→B are parallel `link` records, e3 B→C is `owned`, e4 B→B is a `link` loop, and e5 C→A is unrelated. Retire B under explicit `link=cascade`, `owned=cascade` policies.

**Output:**
```text
Scope: Fictional Vale S complete exercise; target B; 4 nodes and 5 edge IDs.
Policy: link -> cascade; owned -> cascade.
Incident ledger: e1 A→B link remove; e2 A→B link remove; e3 B→C owned remove; e4 B→B link remove once.
Decision: Verified hypothetical preview.
Survivors: Nodes A,C,I; edge e5 C→A.
Verification: Removed IDs equal {e1,e2,e3,e4}; e5 unchanged; both endpoints of e5 survive.
Limits: Source records unchanged; owner approval and real transaction checks outstanding.
Next action: Send the exact ledger and preview to the relation owners for approval.
```

**Bad output:** "B is gone, and all A→B links were merged into one deletion." This fails because B has four distinct incident edge IDs, including two parallel records and a loop.

## Edge cases
- **Missing policy**: return unresolved with affected IDs; do not construct a definitive cascade preview.
- **Restriction**: report every restricting edge ID and leave the source graph untouched.
- **Isolated target**: preview removes only the target node; no edge ID is removed.
- **Self-loop**: list and remove its ID once if its relation policy permits cascade.
- **Duplicate edge ID or unknown endpoint**: reject the inventory before policy evaluation.
- **Stale revision**: reject and request a new frozen snapshot.

## Test case
**Input:**
> Fictional Vale S has A,B,C,I and e1/e2 A→B (`link`), e3 B→C (`owned`), e4 B→B (`link`), e5 C→A (`link`). Preview B retirement first with `owned=restrict`, then with `owned=cascade`, while `link=cascade` throughout.

**Assertions:**
1. Restrict scenario is blocked with e3 as its witness, with no definitive survivor preview.
2. Cascade scenario removes B and exactly e1,e2,e3,e4, listing e4 once.
3. A,C,I and e5 C→A remain unchanged, with no dangling endpoint.
4. The result labels the cascade as hypothetical and does not claim source deletion.
</skill>

<user_request>
Fictional Vale S has A,B,C,I and e1/e2 A→B (`link`), e3 B→C (`owned`), e4 B→B (`link`), e5 C→A (`link`). Preview B retirement first with `owned=restrict`, then with `owned=cascade`, while `link=cascade` throughout.
</user_request>
