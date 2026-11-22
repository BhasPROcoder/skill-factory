Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-034
name: directed-root-dominator-certificate
domain: Graph Engineering Foundations
subdomain: Directed reachability bottlenecks
version: 1.0
description: Compute and verify which reachable vertices occur on every directed path from a declared root when a graph owner needs an inspectable dominator tree.
triggers: ["find directed dominators", "which vertex gates every path from this entry", "build an immediate dominator tree", "verify a directed reachability bottleneck", "check alternate paths around a vertex"]
not_for: ["undirected single-removal connectivity [GRF-029]", "strong component grouping [GRF-008]", "bounded hop traversal [GRF-006]", "physical failure likelihood or service availability"]
requires: []
risk_level: medium
---

# Directed Root Dominator Certificate

## Purpose
Identify vertices that every directed path from one declared entry to a reachable target must pass. Return the immediate-dominator parent of each reachable nonroot vertex, plus a separate verification based on removing candidate vertices. This is structural evidence for the supplied snapshot, not a claim that removing a machine or person would interrupt a real service.

## Inputs to collect
1. **Root and interpretation** — obtain one exact root ID and confirm that an edge permits travel from source to target. Why: changing the entry or reversing arrows changes the answer. Default: none; ask for the root and direction.
2. **Inventory** — obtain unique vertex IDs, including isolates and explicitly unreachable vertices, with snapshot revision. Why: edge-only records cannot show excluded or unreachable inventory. Default: none.
3. **Edges** — obtain unique edge IDs with source and target IDs, selected relation types and source locators. Why: parallel edges and alternate routes must remain distinguishable. Default: no silent deduplication or invented endpoints.
4. **Coverage** — establish whether the supplied snapshot is complete for the intended conclusion. Why: an omitted alternate path can make a false bottleneck. Default: report results only for the supplied scope.
5. **Use and scale** — identify the decision supported and feasible execution limit. Why: this small reference repeatedly scans a finite graph. Default: structural report only; larger graphs require an implementation whose current interface is checked from its official documentation.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the root, directed projection, inventory and revision before computing.
2. Validate nonempty string IDs, unique vertex IDs, unique edge IDs and known endpoints; reject ambiguous records rather than merging them.
3. Traverse outgoing edges from the root to obtain the reachable set. Keep unreachable vertices in a separate ledger; do not assign them a root-relative dominator parent.
4. Initialize the root's dominator set to itself and every other reachable vertex's candidate set to all reachable vertices.
5. Repeatedly replace each nonroot candidate set with that vertex plus the intersection of its reachable predecessors' sets until no set changes.
6. ⚠️ Interpret a set member as a dominator only within this root and snapshot. Do not treat mutual reachability, an incoming edge or a high degree as proof of domination.
7. For each reachable nonroot vertex, select its strict dominator that is itself dominated by every other strict dominator. This is its immediate parent; reject a missing or ambiguous parent as an implementation defect.
8. Independently verify each claimed dominator by deleting that vertex and checking whether the target remains reachable from the root. For the target itself, deletion makes the target absent by definition.
9. Check that each proposed parent is a verified strict dominator and every other verified strict dominator of its child also dominates that parent; then follow each parent chain to the root without repetition. Reject a parent that is too high in the tree.
10. Deliver the root-relative tree, complete dominator sets, unreachable ledger, executed checks and coverage limits. Ask an owner to investigate alternate paths before any graph or operational change.

The Python 3 reference below is for small finite directed graphs. Its tuple contract is `(edge_id, source, target)`; all IDs are nonempty strings. It uses no external package. Run the full snippet in the available Python 3 interpreter and record its actual version. The verifier's removal scan is deliberately separate from the fixed-point calculation.

```python
def analyze(nodes, edges, root, proposed_parent=None):
    if any(type(x) is not str or not x for x in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes) or root not in nodes:
        raise ValueError("duplicate node or unknown root")
    if any(len(e) != 3 or any(type(x) is not str or not x for x in e)
           for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    known = set(nodes)
    if any(a not in known or b not in known for _, a, b in edges):
        raise ValueError("unknown endpoint")
    adj = {n: set() for n in nodes}
    pred = {n: set() for n in nodes}
    for _, a, b in edges:
        adj[a].add(b)
        pred[b].add(a)

    def reached(block=None):
        if root == block:
            return set()
        seen, todo = {root}, [root]
        while todo:
            for nxt in adj[todo.pop()]:
                if nxt != block and nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
        return seen

    reachable = reached()
    dom = {v: ({root} if v == root else set(reachable))
           for v in reachable}
    changed = True
    while changed:
        changed = False
        for v in sorted(reachable - {root}):
            parents = pred[v] & reachable
            new = {v} | set.intersection(*(dom[p] for p in parents))
            if new != dom[v]:
                dom[v], changed = new, True
    parent = {}
    for v in sorted(reachable - {root}):
        strict = dom[v] - {v}
        candidates = [d for d in strict
                      if all(d == other or other in dom[d]
                             for other in strict)]
        if len(candidates) != 1:
            raise AssertionError("immediate parent not unique")
        parent[v] = candidates[0]

    checked = {}
    for v in reachable:
        by_removal = {d for d in reachable
                      if d == v or v not in reached(d)}
        assert dom[v] == by_removal
        checked[v] = by_removal
    candidate = parent if proposed_parent is None else proposed_parent
    assert set(candidate) == reachable - {root}
    for v in candidate:
        cursor, seen = v, set()
        while cursor != root:
            assert cursor not in seen and cursor in candidate
            seen.add(cursor)
            cursor = candidate[cursor]
        d = candidate[v]
        strict = checked[v] - {v}
        assert d in strict
        assert all(other == d or other in checked[d]
                   for other in strict)
    return {v: sorted(dom[v]) for v in sorted(reachable)}, parent, sorted(known-reachable)

nodes = ["R", "A", "B", "C", "D", "I"]
edges = [("ra", "R", "A"), ("ab", "A", "B"),
         ("ac", "A", "C"), ("bd", "B", "D"),
         ("cd", "C", "D")]
dom, parent, absent = analyze(nodes, edges, "R")
assert parent == {"A": "R", "B": "A", "C": "A", "D": "A"}
assert dom["D"] == ["A", "D", "R"] and absent == ["I"]
assert analyze(["R"], [("loop", "R", "R")], "R")[1] == {}
try:
    analyze(nodes, edges, "R",
            {"A": "R", "B": "A", "C": "A", "D": "R"})
except AssertionError:
    pass
else:
    raise AssertionError("non-immediate parent accepted")
print("root-relative dominators and removal checks passed")
```

The fixed point uses vertex sets; parallel edge IDs do not change vertex domination, but they remain separate source records. A self-loop cannot create an alternate entry path. The root dominates every reachable vertex by definition; unreachable vertices have no root-relative dominator claim.

## Decision rules
- IF an alternate root-to-target path avoids a candidate THEN reject its dominator claim BECAUSE domination requires presence on every such path.
- IF a vertex is unreachable from the root THEN leave its parent undefined BECAUSE no root-to-vertex path exists in the supplied graph.
- IF the snapshot is partial THEN qualify every positive result BECAUSE an unseen bypass can invalidate it.
- IF edge direction or root is unresolved THEN withhold the calculation BECAUSE both define the path population.
- IF a parent chain does not reach the root exactly once THEN reject the certificate BECAUSE it cannot be an immediate-dominator tree.

## Output template
```text
Scope: <revision, root, directed relation and coverage; maximum 70 words>
Reachable: <complete IDs, or attached complete ledger>
Unreachable: <complete IDs, or None>
Dominator sets: <reachable vertex | all dominators; full ledger>
Immediate parents: <nonroot reachable vertex | parent; full ledger>
Verification: <fixed-point and independent removal checks actually executed/pending>
Limits: <coverage, scale and operational meaning; maximum 80 words>
Next action: <owner and bounded follow-up; maximum 40 words>
```

## Quality checklist
- [ ] Root and arrow semantics are explicit.
- [ ] Input vertex and edge identities are checked before set construction.
- [ ] Reachable and unreachable vertices are separated.
- [ ] Each reported dominator survives the independent removal test.
- [ ] Every immediate parent is a strict dominator of its child.
- [ ] Parent chains terminate at the declared root without a cycle.
- [ ] Parallel records are retained by ID even though vertex reachability uses sets.
- [ ] Coverage and real-world inference limits appear in the result.

## Anti-patterns
- **Degree as gate**: call a busy vertex mandatory. Fix: search for a root-to-target bypass.
- **Undirected shortcut**: walk backward along directed edges. Fix: retain the supplied arrow orientation.
- **Unreachable parent**: assign a tree parent to an unreachable inventory vertex. Fix: list it separately.
- **One path is enough**: infer a dominator from one observed route. Fix: run the all-path condition by deletion.
- **Operational guarantee**: claim service outage after removing a graph vertex. Fix: limit conclusions to the supplied topology.

## Worked example
**Input:** Fictional graph Team Cedar supplies the complete exercise inventory and edges in the snippet. R is the entry and I is isolated. Determine the root-relative dominators; no real system change is authorized.

**Output:**
```text
Scope: Cedar exercise C1; root R; directed source-to-target links; supplied inventory complete for this exercise.
Reachable: R, A, B, C, D.
Unreachable: I.
Dominator sets: R | R; A | R,A; B | R,A,B; C | R,A,C; D | R,A,D.
Immediate parents: A | R; B | A; C | A; D | A.
Verification: Reference fixed-point and independent vertex-removal assertions executed for C1; parent chains reach R.
Limits: Exercise topology only; B and C each have a bypass to D, while A does not. No physical availability claim.
Next action: Graph owner reviews source links and any omitted bypasses before using A as a structural gate.
```

**Bad output:** “B dominates D because B lies on the first route R,A,B,D; shut B down to test it.”
The supplied R,A,C,D route bypasses B, and the instruction invents operational authority.

## Edge cases
- **Only the root**: return its one-member set and no parent links.
- **Disconnected inventory**: list unreachable vertices without assigning them parent links.
- **Self-loop**: retain its ID; it does not by itself change paths to other vertices.
- **Parallel directed edges**: retain both IDs; neither changes the vertex-domination test when endpoints match.
- **Root removed in independent check**: treat the reachable set as empty; this verifies root domination.

## Test case
**Input:**
> Fictional directed graph has R→A, A→B, A→C, B→D, C→D, parallel R→A records and isolated I. Give root-relative dominators and immediate parents without claiming an outage.

**Assertions:**
1. Lists I as unreachable with no immediate parent.
2. Shows A, but neither B nor C, dominating D.
3. Assigns D's immediate parent to A.
4. Retains both R→A source edge IDs without treating them as distinct vertices.
5. Qualifies the conclusion to the supplied directed snapshot.
</skill>

<user_request>
Fictional directed graph has R→A, A→B, A→C, B→D, C→D, parallel R→A records and isolated I. Give root-relative dominators and immediate parents without claiming an outage.
</user_request>
