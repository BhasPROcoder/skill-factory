---
id: GRF-033
name: edge-once-graph-trail-construction
domain: Graph Engineering Foundations
subdomain: Edge coverage trails
version: 1.0
description: Construct and verify an undirected trail covering every edge identity exactly once when a task requires complete edge coverage without repeating an edge.
triggers: ["cover every graph edge once", "construct an edge coverage trail", "check Euler trail feasibility", "preserve parallel edges in a trail", "verify a complete edge walk"]
not_for: ["minimum cost source-to-target routes [GRF-009]", "bounded node reachability [GRF-006]", "single-failure connectivity [GRF-029]", "shortest repeated-edge coverage routes", "directed trail construction"]
requires: []
risk_level: medium
---

# Edge Once Graph Trail Construction

## Purpose
Construct an ordered edge witness that uses every supplied edge identity exactly once under an explicit undirected interpretation. Explain infeasibility from parity or disconnected edge support, and verify successful output independently against the original inventory. This is a structural coverage result, not a shortest-route, scheduling or physical-access guarantee.

## Inputs to collect
1. **Graph snapshot** — obtain node IDs and uniquely identified edge endpoint pairs. Why: parallel relationships must remain separate required visits. Default: none; request the scoped inventory.
2. **Direction policy** — confirm that traversing either endpoint direction is allowed. Why: ignoring directed restrictions changes feasibility. Default: unresolved; do not convert a directed task silently.
3. **Start requirement** — obtain a required start node or permission to select one. Why: an open trail must begin at an appropriate odd-degree endpoint. Default: select deterministically after feasibility checks, explicitly disclosed.
4. **Coverage inventory** — confirm that every supplied edge must be traversed and identify any excluded relationships before construction. Why: omitting inconvenient edges changes the task. Default: all supplied edges.
5. **Isolated-node policy** — decide whether visiting isolated vertices is a separate requirement. Why: edge coverage alone does not require visiting them. Default: report isolates separately, with no promise to visit them.
6. **Execution context** — obtain runtime and graph size constraints. Why: the reference materializes the graph and output in memory. Default: portable reference and pending execution until run; no production scale claim.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the node and required edge inventory with the approved undirected interpretation.
2. Validate unique IDs and known endpoints before building adjacency.
3. Count degree by edge incidences, adding two incidences for a self-loop.
4. Identify odd-degree vertices and reject nonempty edge sets with an odd-vertex count other than zero or two.
5. Check connectivity among vertices incident to at least one required edge; retain isolated vertices separately.
6. Select an allowed start: an odd vertex when there are two, otherwise an incident vertex for a nonempty edge set.
7. Traverse unused edge identities while maintaining a vertex stack and the edge used to enter each stacked vertex.
8. When a stack vertex has no unused incident edge, remove it and append its incoming edge to the reversed trail.
9. Reverse the collected edge order and replay it from the selected start against the original endpoint records.
10. ⚠️ Compare the complete used-ID multiset with the required inventory; do not accept a continuous partial walk merely because its endpoints look correct.
11. Deliver start, ordered IDs, vertex sequence, endpoint and excluded isolated-node evidence, or a specific infeasibility witness.

This Python 3 reference accepts finite string node IDs and tuples `(edge_ID, endpoint_A, endpoint_B)`. Prevalidate string fields and tuple shapes. It returns a start and ordered edge IDs, then a separate verifier reconstructs the vertex sequence without using construction adjacency. Record the actual interpreter version when running the full snippet. Each loop contributes two adjacency incidences but its identity is consumed once.

```python
def verify(nodes, edges, start, trail):
    records = {eid: (a, b) for eid, a, b in edges}
    if len(records) != len(edges) or len(trail) != len(edges):
        raise ValueError("inventory mismatch")
    if len(set(trail)) != len(trail) or set(trail) != set(records):
        raise ValueError("missing or repeated edge")
    if start is None:
        if nodes or edges or trail:
            raise ValueError("missing start")
        return []
    if start not in nodes:
        raise ValueError("unknown start")
    walk = [start]
    for eid in trail:
        a, b = records[eid]
        here = walk[-1]
        if here == a:
            walk.append(b)
        elif here == b:
            walk.append(a)
        else:
            raise ValueError("discontinuous trail")
    return walk

def construct(nodes, edges, start=None):
    if len(set(nodes)) != len(nodes) or len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate identity")
    adj = {n: [] for n in nodes}
    for eid, a, b in sorted(edges):
        if a not in adj or b not in adj:
            raise ValueError("unknown endpoint")
        adj[a].append((eid, b))
        adj[b].append((eid, a))
    if start is not None and start not in adj:
        raise ValueError("unknown start")
    if not edges:
        return (start if start is not None else min(nodes, default=None)), []
    support = {n for n in nodes if adj[n]}
    odd = sorted(n for n in support if len(adj[n]) % 2)
    if len(odd) not in (0, 2):
        raise ValueError("infeasible odd vertices: " + repr(odd))
    seen, todo = set(), [min(support)]
    while todo:
        n = todo.pop()
        if n not in seen:
            seen.add(n)
            todo.extend(other for eid, other in adj[n])
    if seen != support:
        raise ValueError("disconnected edge support")
    allowed = set(odd) if odd else support
    if start is None:
        start = min(allowed)
    if start not in allowed:
        raise ValueError("start incompatible with parity/support")
    used, reversed_ids, stack = set(), [], [(start, None)]
    while stack:
        n, incoming = stack[-1]
        while adj[n] and adj[n][-1][0] in used:
            adj[n].pop()
        if adj[n]:
            eid, other = adj[n].pop()
            used.add(eid)
            stack.append((other, eid))
        else:
            stack.pop()
            if incoming is not None:
                reversed_ids.append(incoming)
    trail = list(reversed(reversed_ids))
    verify(nodes, edges, start, trail)
    return start, trail

nodes = ["A", "B", "I"]
edges = [("e1", "A", "B"), ("e2", "A", "B"), ("loop", "A", "A")]
start, trail = construct(nodes, edges)
walk = verify(nodes, edges, start, trail)
assert start == "A" and trail == ["loop", "e2", "e1"]
assert walk == ["A", "A", "B", "A"]
print("loop, parallel identities and complete trail replay checked")
```

The verifier assumes the constructor's validated endpoint inventory; when checking an externally supplied trail, validate nodes and endpoints first too. Deterministic ordering is an implementation tie policy, not a canonical or optimal route. Operational interruption must preserve an incomplete status rather than converting an unfinished construction into infeasibility.

## Decision rules
- IF exactly two vertices have odd degree THEN require the start to be one of them BECAUSE an edge-once open trail has odd-degree endpoints.
- IF nonisolated support is disconnected THEN report infeasibility BECAUSE one continuous trail cannot cross between those components without an additional edge.
- IF parallel edges share endpoints THEN retain separate IDs BECAUSE each is a separate coverage obligation.
- IF isolates must also be visited THEN flag the additional requirement BECAUSE a complete edge trail does not satisfy disconnected vertex visitation.
- IF a proposed route repeats edges THEN route it to a different objective BECAUSE this contract permits each required identity once.

## Output template
```text
Scope: <revision, undirected policy, edge inventory; maximum 60 words>
Feasibility: <odd vertices, edge-support connectivity, required/selected start>
Trail: <ordered edge IDs and reconstructed vertex sequence, or none>
Coverage: <required/used IDs and isolate treatment>
Verification: <executed checks and pending checks; maximum 70 words>
Decision: <feasible witness / infeasible / unresolved; reason and next action, maximum 80 words>
```

## Quality checklist
- [ ] Unique edge IDs preserve parallel coverage obligations.
- [ ] Loop degree includes both incidences.
- [ ] Connectivity checks use nonisolated support.
- [ ] Selected start satisfies the approved requirement and parity.
- [ ] Replayed edges are continuous from the selected start.
- [ ] Every required edge appears exactly once.
- [ ] Isolated-node visitation limits are explicit.
- [ ] Execution and structural feasibility are separate from real route access.

## Anti-patterns
- **Neighbor deduplication**: collapse parallel edges. Fix: consume edge IDs rather than neighbor pairs.
- **Loop miscount**: count one loop incidence. Fix: add both endpoint incidences.
- **Partial walk approval**: accept continuity without coverage. Fix: compare complete ID inventories.
- **Isolate rejection**: reject edge coverage because an unused isolated node exists. Fix: distinguish vertex-visitation requirements.
- **Route optimality inflation**: call the constructed trail cheapest. Fix: state only verified edge-once coverage.

## Worked example
**Input:** Fictional fixture A/B/I has e1 and e2 between A/B and a loop at A. Undirected edge coverage is required; isolated I need not be visited; start selection is permitted.

**Output:**
```text
Scope: Fictional fixture; undirected; required e1,e2,loop.
Feasibility: No odd vertices; incident support A/B connected; selected start A.
Trail: loop,e2,e1; vertices A,A,B,A.
Coverage: All three required IDs once; I isolated and not visited.
Verification: Reference assertions specify expected replay; record execution separately before claiming a run.
Decision: Feasible structural witness; no shortest-route or physical-access claim. Owner checks operational restrictions before use.
```

**Bad output:** “Use e1 from A to B and stop; the graph has been covered.”
This omits the parallel edge and self-loop despite a continuous partial walk.

## Edge cases
- **No edges**: return an empty trail at the supplied or selected node; with no nodes return no start and an empty vertex sequence.
- **Invalid required start**: reject that start explicitly; do not silently substitute a permitted endpoint.
- **More than two odd vertices**: list them as the parity obstruction; do not add edges without a changed task.
- **Disconnected edge support**: identify the separation and request whether independent trails are acceptable.
- **Directed inputs**: obtain a directed method or explicit approved projection before running this reference.

## Test case
**Input:**
> Fictional A/B have two parallel undirected edges, A has a self-loop, and I is isolated. Cover every edge once from A and explain whether I prevents success.

**Assertions:**
1. Retains both parallel edge identities and the loop exactly once.
2. Replays a continuous closed trail from A.
3. Explains that I does not obstruct edge-only coverage but is not visited.
4. Claims neither cheapest routing nor physical accessibility.
