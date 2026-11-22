---
id: GRF-039
name: directed-edge-addition-reachability-delta
domain: Graph Engineering Foundations
subdomain: Directed reachability changes
version: 1.0
description: Compare all directed reachable node pairs before and after one identified edge addition when an owner needs exact gain evidence and witness paths.
triggers: ["what reachability changes if I add this edge", "show new directed paths after a link", "verify edge addition reachability", "find newly reachable ordered pairs", "check whether a new edge changes graph access"]
not_for: ["bounded traversal from one seed [GRF-006]", "undirected removal losses [GRF-029]", "removing redundant DAG edges [GRF-035]", "authorization to add a real relationship or access"]
requires: []
risk_level: medium
---

# Directed Edge Addition Reachability Delta

## Purpose
Compare the complete ordered-pair reachability relation of a supplied directed graph before and after one proposed edge is added. Return every newly reachable pair with an edge-ID path witness, and verify that no old pair disappeared. This is a hypothetical structural analysis, not approval to create the relationship in a source system.

## Inputs to collect
1. **Baseline inventory** — obtain unique node IDs and edge records with stable IDs, endpoints and revision, including isolates. Why: pair comparison needs the same node universe before and after. Default: none; request complete scoped inventory.
2. **Proposed edge** — obtain one new edge ID, existing source and existing target. Why: adding a node or replacing an edge is a different change. Default: none.
3. **Direction and projection** — confirm arrow meaning and selected relation types. Why: reversal or implicit filtering changes paths. Default: no silent undirected interpretation.
4. **Reachability convention** — decide whether a zero-edge self-pair counts. Why: self-pairs are ambiguous otherwise. Default for this reference: require one or more directed edges; a self-loop or directed cycle can make a self-pair reachable.
5. **Coverage and decision** — obtain excluded records, source completeness and what will use the result. Why: unseen alternate paths can reduce the reported gain. Default: supplied snapshot only, structural proposal only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze one baseline revision, the selected directed projection, proposed edge identity and reachability convention.
2. Validate unique nonempty string IDs, three-field edge records, known endpoints and a proposed ID absent from the baseline.
3. Retain the full unchanged node universe and original edge inventory for before-state calculation.
4. Compute every ordered pair connected by at least one directed edge path in the baseline; include cyclic self-pairs under the declared convention.
5. Create a hypothetical after-state by appending exactly the proposed edge, preserving parallel source records and all old edges.
6. Compute the complete after-state pair relation under the same convention.
7. Calculate gained pairs as after minus before and lost pairs as before minus after. ⚠️ Reject any lost pair as a computation or snapshot inconsistency: adding an edge cannot erase an existing path under an unchanged universe.
8. For each gained pair, recover a directed path of original/proposed edge IDs in the after-state; verify continuity, endpoints and at least one occurrence of the proposed edge. A gain cannot be witnessed solely by old edges.
9. Independently recompute before and after pair relations using a different closure method and compare exact sets, not just counts or a few examples.
10. Deliver the full gain ledger, zero-loss check, witness paths and limitations. If the graph is too large for complete execution, report the calculation as pending or partial rather than a global delta.

The Python 3 reference below accepts finite node lists and edge tuples `(edge_id, source, target)`. It uses exhaustive in-memory searches for an inspectable small graph. Run the complete snippet and record the actual interpreter version. The verifier independently recomputes reachability by repeated Boolean relation expansion; neither routine implements a remote graph query or an operational permission check.

```python
def check(nodes, edges, proposed):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    records = list(edges) + [proposed]
    if any(type(e) not in (tuple, list) or len(e) != 3
           or any(type(x) is not str or not x for x in e)
           for e in records):
        raise ValueError("invalid edge record")
    if len({e[0] for e in records}) != len(records):
        raise ValueError("duplicate edge ID")
    if any(a not in nodes or b not in nodes for _, a, b in records):
        raise ValueError("unknown endpoint")

def paths(nodes, edges):
    adj = {n: [] for n in nodes}
    for eid, a, b in sorted(edges):
        adj[a].append((b, eid))
    result = {}
    for start in nodes:
        queue = [(start, ())]
        seen = {start}
        for node, route in queue:
            for nxt, eid in adj[node]:
                candidate = route + (eid,)
                if (start, nxt) not in result:
                    result[start, nxt] = candidate
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, candidate))
    return result

def closure(nodes, edges):
    relation = {(a, b) for _, a, b in edges}
    while True:
        expanded = relation | {(a, c) for a, b in relation
                               for x, c in relation if b == x}
        if expanded == relation:
            return relation
        relation = expanded

def addition_delta(nodes, edges, proposed):
    check(nodes, edges, proposed)
    after_edges = list(edges) + [proposed]
    before, after = paths(nodes, edges), paths(nodes, after_edges)
    gained = {pair: after[pair] for pair in sorted(after.keys() - before.keys())}
    lost = before.keys() - after.keys()
    assert not lost
    assert set(before) == closure(nodes, edges)
    assert set(after) == closure(nodes, after_edges)
    by_id = {eid: (a, b) for eid, a, b in after_edges}
    for (source, target), route in gained.items():
        cursor = source
        assert proposed[0] in route
        for eid in route:
            a, b = by_id[eid]
            assert a == cursor
            cursor = b
        assert cursor == target
    return gained, sorted(lost)

nodes = ["A", "B", "C", "D", "I"]
edges = [("ab", "A", "B"), ("cd", "C", "D")]
gained, lost = addition_delta(nodes, edges, ("bc", "B", "C"))
assert set(gained) == {("A", "C"), ("A", "D"),
                       ("B", "C"), ("B", "D")}
assert lost == [] and gained["A", "D"] == ("ab", "bc", "cd")
assert addition_delta(["X"], [], ("loop", "X", "X"))[0] == {
    ("X", "X"): ("loop",)}
print("directed addition delta, witnesses and closure checks passed")
```

The two methods compare complete pair sets for the supplied node universe. The proposed edge may be parallel to an old edge, in which case the gain can be empty. A cycle-closing insertion can produce new self-pairs under the one-or-more-edge convention. The script's exhaustive closure is deliberately unsuitable for large graphs; use a verified scalable method there and preserve the same pair contract.

## Decision rules
- IF the proposed edge ID already exists THEN reject the input BECAUSE two source records cannot share one identity.
- IF a gained pair's path omits the proposed edge THEN reject the gain BECAUSE an old path would have made the pair reachable before.
- IF any old pair is absent afterward THEN reject the comparison BECAUSE an append-only edge change preserves old paths.
- IF the new edge is parallel to an existing one THEN allow an empty gain BECAUSE new identity need not create new reachability.
- IF coverage is partial THEN qualify the result BECAUSE missing baseline edges may make an apparent gain already reachable.

## Output template
```text
Scope: <revision, directed projection, node universe and coverage; maximum 70 words>
Proposed edge: <ID, source, target; hypothetical only>
Gained pairs: <ordered source,target | witness edge-ID sequence; complete ledger>
Lost pairs: <None or computation conflict>
Checks: <exact before/after pair-set comparison and witness replay executed/pending>
Limits: <coverage, scale and authorization limits; maximum 80 words>
Next action: <owner and bounded follow-up; maximum 40 words>
```

## Quality checklist
- [ ] Before and after use the same nodes and projection.
- [ ] Proposed edge has a new ID and known endpoints.
- [ ] Directed paths use one or more edges under the declared convention.
- [ ] Every gained pair has a continuous edge-ID witness.
- [ ] Each gain witness contains the proposed edge.
- [ ] Independent pair recomputation matches both exact sets.
- [ ] Lost-pair set is empty or identified as an error.
- [ ] No structural result is called approval to add the source relationship.

## Anti-patterns
- **Count-only parity**: equal totals hide different pairs. Fix: compare exact ordered-pair sets.
- **Undirected shortcut**: infer reverse paths from one arrow. Fix: preserve source-to-target direction.
- **Witness without new edge**: claim gain from an old route. Fix: require the proposed edge ID in every gain witness.
- **Replaced baseline**: silently drop an old record. Fix: append exactly one edge to the frozen inventory.
- **Permission laundering**: equate a hypothetical path with allowed access. Fix: keep graph structure separate from authorization.

## Worked example
**Input:** Fictional Team Maple supplies the complete exercise graph in the snippet. It proposes bc:B→C without changing nodes or old edges; show all new directed reachable pairs.

**Output:**
```text
Scope: Maple exercise M1; A/B/C/D/I, directed links, supplied inventory complete for this exercise.
Proposed edge: bc, B→C; hypothetical only.
Gained pairs: A,C | ab,bc; A,D | ab,bc,cd; B,C | bc; B,D | bc,cd.
Lost pairs: None.
Checks: Embedded reference exact pair-set comparison and witness replay executed for M1.
Limits: Exercise graph only; I remains isolated. No relationship creation or access permission approved.
Next action: Graph owner verifies the proposed bc source meaning before any separate change request.
```

**Bad output:** “Only B reaches C now; go ahead and grant access.”
It omits the transitive A/D gains and invents permission.

## Edge cases
- **Empty baseline edges**: a proposed nonloop edge yields its ordered endpoint pair.
- **Self-loop insertion**: gains a self-pair if no prior nonempty return path exists.
- **Parallel insertion**: may gain no pairs; keep the new ID as separate source evidence.
- **Cycle closure**: check newly reachable self-pairs as well as cross-node pairs.
- **Isolated node**: retain it in the universe even when no pair involving it changes.

## Test case
**Input:**
> Fictional directed graph has A→B and C→D, plus isolated I. Add proposed B→C with a new edge ID. State the exact reachability delta.

**Assertions:**
1. Lists exactly A→C, A→D, B→C and B→D as gained pairs.
2. Gives a directed edge-ID path for each gain containing the proposed edge.
3. Reports no lost pairs and retains I in scope.
4. Qualifies the result as hypothetical structure rather than permission to add a real edge.
