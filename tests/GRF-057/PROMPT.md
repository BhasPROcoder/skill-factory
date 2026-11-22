Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-057
name: conflated-entity-split-edge-reassignment
domain: Graph Engineering Foundations
subdomain: Entity split previews
version: 1.0
description: Preview an evidence-backed split of one conflated graph node by assigning each incident edge endpoint occurrence to a new identity or holding it unresolved.
triggers: ["split a conflated graph entity", "reassign edges after identity separation", "hold ambiguous incident edges", "check a self-loop during entity split", "audit one-to-many node identity repair"]
not_for: ["reviewing many-to-one entity merges [GRF-002]", "bijective identity migration [GRF-017]", "retiring a graph node [GRF-050]", "importing a new edge list [GRF-003]"]
requires: []
risk_level: medium
---

# Conflated Entity Split Edge Reassignment

## Purpose
Preview one node's split into approved identities. Assign each incident endpoint occurrence from evidence or hold its edge. Verify accepted edge IDs, payloads and directions; no live graph changes.

## Inputs to collect
1. **Frozen source** — obtain revision, nodes and identified edges with relation, properties and locator. Why: every incident edge needs reconciliation. Default: no complete claim without inventory.
2. **Identity decision** — obtain the conflated node and approved distinct new IDs with identity evidence. Why: labels alone do not justify a person/entity split. Default: no split without owner decision.
3. **Endpoint dispositions** — obtain one assignment or unresolved reason for each occurrence of the old node in every incident edge. Why: a self-loop has two independent occurrences. Default: unresolved, never automatic fan-out.
4. **Consumer checks** — obtain affected queries and any alias/cutover constraints. Why: preserved edge counts do not prove equivalent query meaning. Default: query and cutover approval pending.
5. **Execution boundary** — obtain whether this is offline preview or a separately authorized write. Why: source records and reader state may change. Default: offline preview only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the source revision and retain node/edge records with locators.
2. Validate unique nonempty IDs, record shapes, known endpoints and new-ID noncollision.
3. List every incident edge ID and each role in which the conflated node occurs.
4. Check an evidence-backed disposition for each occurrence; reject missing or extra ledger keys.
5. Put edges with any unresolved occurrence in a held ledger. ⚠️ Do not clone an edge to all candidate identities.
6. Rewrite only approved occurrences in a candidate; copy edge ID, relation, properties, direction and locator.
7. Keep every nonincident edge unchanged and exclude the original conflated node from candidate nodes.
8. Verify accepted and held edge IDs partition the frozen inventory, with every held edge incident and every fully assigned edge accepted.
9. Replay each accepted endpoint against its occurrence disposition, then map new IDs back to the old ID to confirm source-record reconstruction. This technical inverse does not adjudicate identity.
10. Compare affected queries under explicit old/new identity scopes and report pending checks; require a new preview if source revision or dispositions change.

This Python 3 reference uses `(edge_ID, source, relation, target, locator, properties)` with plain dictionaries. A disposition maps `(edge_ID, role)` to `(new_ID_or_None, evidence)`. It compares copied properties exactly. Run it and record the interpreter version; live transactions are outside it.

```python
from copy import deepcopy

def validate(nodes, edges, old, new_ids, ledger, observed, expected):
    if type(observed) is not str or not observed or observed != expected:
        raise ValueError("stale or missing revision")
    if any(type(x) not in (list, tuple) for x in (nodes, edges, new_ids)):
        raise ValueError("invalid inventory shape")
    if any(type(n) is not str or not n for n in nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("invalid source nodes")
    known = set(nodes)
    if type(old) is not str or old not in known:
        raise ValueError("unknown conflated node")
    if len(new_ids) < 2 or any(type(n) is not str or not n for n in new_ids):
        raise ValueError("invalid new identities")
    if len(set(new_ids)) != len(new_ids) or set(new_ids) & known:
        raise ValueError("new identity collision")
    edge_ids, needed = set(), set()
    for row in edges:
        if type(row) not in (list, tuple) or len(row) != 6:
            raise ValueError("invalid edge record")
        rid, s, rel, o, locator, props = row
        if any(type(x) is not str or not x for x in row[:5]) or type(props) is not dict:
            raise ValueError("invalid edge field")
        if rid in edge_ids or s not in known or o not in known:
            raise ValueError("duplicate edge ID or unknown endpoint")
        edge_ids.add(rid)
        if s == old:
            needed.add((rid, "source"))
        if o == old:
            needed.add((rid, "target"))
    if type(ledger) is not dict or set(ledger) != needed:
        raise ValueError("incomplete occurrence ledger")
    for key, value in ledger.items():
        if type(value) not in (tuple, list) or len(value) != 2:
            raise ValueError("invalid disposition")
        new_id, evidence = value
        if new_id is not None and new_id not in new_ids:
            raise ValueError("unknown new identity")
        if type(evidence) is not str or not evidence:
            raise ValueError("missing disposition evidence")

def preview(nodes, edges, old, new_ids, ledger, observed, expected):
    validate(nodes, edges, old, new_ids, ledger, observed, expected)
    candidate_nodes = [n for n in nodes if n != old] + list(new_ids)
    accepted, held = [], []
    for rid, s, rel, o, locator, props in edges:
        s_to = ledger[(rid, "source")][0] if s == old else s
        o_to = ledger[(rid, "target")][0] if o == old else o
        if s_to is None or o_to is None:
            held.append(rid)
        else:
            accepted.append((rid, s_to, rel, o_to, locator, deepcopy(props)))
    result = (candidate_nodes, accepted, held)
    verify(nodes, edges, old, new_ids, ledger, result)
    return result

def verify(nodes, edges, old, new_ids, ledger, result):
    candidate_nodes, accepted, held = result
    expected_nodes = [n for n in nodes if n != old] + list(new_ids)
    if candidate_nodes != expected_nodes:
        raise ValueError("candidate node mismatch")
    by_id = {r[0]: r for r in edges}
    accepted_ids = [r[0] for r in accepted]
    if len(set(accepted_ids)) != len(accepted_ids) or len(set(held)) != len(held):
        raise ValueError("edge fan-out or duplicate hold")
    if set(accepted_ids) & set(held) or set(accepted_ids) | set(held) != set(by_id):
        raise ValueError("edge partition mismatch")
    accepted_by_id = {r[0]: r for r in accepted}
    inverse = {n: old for n in new_ids}
    for rid, s, rel, o, locator, props in edges:
        assigned_s = ledger[(rid, "source")][0] if s == old else s
        assigned_o = ledger[(rid, "target")][0] if o == old else o
        unresolved = assigned_s is None or assigned_o is None
        if unresolved:
            if rid not in held or s != old and o != old:
                raise ValueError("held edge mismatch")
            continue
        expected = (rid, assigned_s, rel, assigned_o, locator, props)
        if accepted_by_id.get(rid) != expected:
            raise ValueError("edge reassignment or payload mismatch")
        out = accepted_by_id[rid]
        if (inverse.get(out[1], out[1]), inverse.get(out[3], out[3])) != (s, o):
            raise ValueError("inverse endpoint replay mismatch")
    return True

nodes = ["X", "Org1", "Org2", "Y"]
edges = [("e1", "X", "worksAt", "Org1", "s1", {"role": "staff"}),
         ("e2", "X", "worksAt", "Org2", "s2", {}),
         ("e3", "Y", "knows", "X", "s3", {}),
         ("e4", "X", "follows", "X", "s4", {"kind": "source"}),
         ("e5", "Y", "worksAt", "Org1", "s5", {})]
ledger = {("e1", "source"): ("A", "owner evidence s1"),
          ("e2", "source"): ("B", "owner evidence s2"),
          ("e3", "target"): (None, "referent unresolved s3"),
          ("e4", "source"): ("A", "owner evidence s4-source"),
          ("e4", "target"): ("B", "owner evidence s4-target")}
candidate, accepted, held = preview(nodes, edges, "X", ["A", "B"], ledger, "v1", "v1")
assert held == ["e3"] and {r[0] for r in accepted} == {"e1", "e2", "e4", "e5"}
assert ("e4", "A", "follows", "B", "s4", {"kind": "source"}) in accepted
assert ("e5", "Y", "worksAt", "Org1", "s5", {}) in accepted
print("endpoint occurrences, held edge and inverse replay checked")
```

## Decision rules
- IF an incident occurrence lacks approved identity evidence THEN hold its whole edge BECAUSE guessing a referent changes graph meaning.
- IF a self-loop has two occurrence dispositions THEN apply them separately BECAUSE source and target may represent different entities.
- IF a proposed edge appears twice THEN reject the preview BECAUSE source edge fan-out was not authorized.
- IF an accepted edge changes relation, ID or locator THEN reject it BECAUSE the split concerns identity endpoints only.
- IF any edge remains held THEN label cutover incomplete BECAUSE the original node still carries unresolved evidence.

## Output template
```text
Scope: <source revision, old ID, approved new IDs; max 60 words>
Occurrence ledger: <edge ID and role | new ID or unresolved | evidence>
Candidate nodes: <complete IDs or attached ledger>
Accepted edges: <ID | source | relation | target | locator | properties>
Held edges: <ID | unresolved occurrence and reason>
Verification: <partition, payload and inverse endpoint replay result>
Consumer checks: <query comparison or pending>
Limits: <identity and execution limits; max 60 words>
Next action: <owner review or evidence request>
```

## Quality checklist
- [ ] Frozen revision and owner-approved split decision are identified.
- [ ] Every old-node endpoint occurrence has one disposition.
- [ ] Original edge IDs partition exactly into accepted and held sets.
- [ ] Nonincident edges remain unchanged.
- [ ] Accepted IDs, relations, direction and locators replay exactly.
- [ ] Self-loop roles are assigned independently.
- [ ] Held edges remain in the source evidence ledger.
- [ ] No unresolved result is described as a completed live split.

## Anti-patterns
- **Global replacement**: sending every X edge to A. Fix: decide each endpoint occurrence.
- **Fan-out**: copying e3 to both A and B. Fix: hold e3 until evidence resolves it.
- **Self-loop shortcut**: mapping both e4 endpoints together. Fix: use separate role dispositions.
- **Silent loss**: omitting e3 from both candidate and held ledger. Fix: reconcile all source IDs.
- **False reversibility**: claiming technical X reconstruction proves identity truth. Fix: keep semantic approval separate.

## Worked example
**Input:** Fictional graph S1 has source nodes X, Org1, Org2, Y and edges e1–e5 shown in the reference. The owner has approved new identities A/B and the occurrence dispositions in the ledger; e3's referent remains unknown.

**Output:**
```text
Scope: Fictional S1 at v1; old X; approved A and B; offline preview.
Occurrence ledger: e1 source→A s1; e2 source→B s2; e3 target unresolved s3; e4 source→A and target→B s4.
Candidate nodes: Org1,Org2,Y,A,B.
Accepted edges: e1 A worksAt Org1 s1 {role:staff}; e2 B worksAt Org2 s2 {}; e4 A follows B s4 {kind:source}; e5 Y worksAt Org1 s5 {}.
Held edges: e3 Y knows X s3; target referent unresolved.
Verification: Source IDs partition 4 accepted/1 held; payload and inverse endpoints replayed.
Consumer checks: Query comparison pending owner-supplied old/new identity scopes.
Limits: Identity evidence supplied for exercise only; no live write or full cutover.
Next action: Resolve e3 from source evidence and rerun against a frozen revision.
```

**Bad output:** “Duplicate e3 as Y→A and Y→B so no edge is lost.” This invents two relationships from one unresolved source edge and violates unique edge identity.

## Edge cases
- **Two-role self-loop**: X→X may become A→B only when each occurrence is separately supported.
- **Unresolved incident edge**: hold its source record once; do not leave a dangling X endpoint in the candidate.
- **New-ID collision**: reject a proposed A/B ID already present in the source node inventory.
- **Stale revision**: reject mismatched observed and expected source revisions before preview.
- **Malformed input**: reject duplicate edge IDs, unknown endpoints, missing ledger roles or string-shaped rows.

## Test case
**Input:**
> Preview the fictional X split with e1–e5 and the supplied occurrence ledger. Then forge a candidate with e3 duplicated to A and B, and another with e4 mapped A→A despite approved A→B roles.

**Assertions:**
1. The candidate contains e1 A→Org1, e2 B→Org2, e4 A→B and unchanged e5, all with original IDs and locators.
2. e3 is held exactly once and full cutover remains incomplete.
3. The duplicate-e3 candidate is rejected as fan-out or invalid partition.
4. The A→A e4 candidate is rejected by occurrence-ledger replay.
</skill>

<user_request>
Preview the fictional X split with e1–e5 and the supplied occurrence ledger. Then forge a candidate with e3 duplicated to A and B, and another with e4 mapped A→A despite approved A→B roles.
</user_request>
