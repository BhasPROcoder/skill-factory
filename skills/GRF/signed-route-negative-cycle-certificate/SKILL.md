---
id: GRF-041
name: signed-route-negative-cycle-certificate
domain: Graph Engineering Foundations
subdomain: Signed route costs
version: 1.0
description: Certify a minimum directed walk cost with signed integer edges or show a relevant negative cycle when a route may revisit vertices.
triggers: ["shortest route with negative edges", "does a negative cycle affect this target", "verify a signed-cost path", "why is route cost unbounded", "separate irrelevant negative cycles", "signed graph route certificate"]
not_for: ["nonnegative route calculation [GRF-009]", "flow and cut certificates [GRF-010]", "DAG reachability reduction [GRF-035]", "simple-path optimization forbidding revisits"]
requires: []
risk_level: medium
---

# Signed Route Negative-Cycle Certificate

## Purpose
Find a minimum-cost directed walk with signed integer edges. Distinguish finite, unreachable and target-relevant negative-cycle outcomes. Other negative cycles do not affect this target.

## Inputs to collect
1. **Graph** — collect node IDs, edge IDs, directed endpoints and signed integer costs. Why: missing links change routes. Default: no full claim without the inventory.
2. **Terminals and walks** — collect source, target and permission to revisit. Why: cycle repetition differs from simple paths. Default: both terminals required; use this skill only for walks.
3. **Cost contract** — confirm one exact additive unit and filters. Why: mixed units cannot be summed. Default: request clarification.
4. **Coverage** — record revision, omitted links and direction. Why: an unseen cycle exit changes relevance. Default: qualify to the supplied projection.
5. **Execution** — record whether the reference ran. Why: a proposal is not verification. Default: pending.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze inventory, terminals, direction, eligibility and cost units.
2. Validate record shapes, identities, endpoints and exact integer weights.
3. Intersect source-reachable nodes with nodes that reach the target; call this the corridor.
4. Return unreachable if the target is not source-reachable.
5. Relax corridor edges in edge-ID order, retaining predecessors of strict improvements.
6. ⚠️ On a final-pass improvement, extract a closed predecessor cycle; replay its negative cost, source approach and target exit. Report no finite walk minimum.
7. Otherwise build a route on tight edges where `label[b] = label[a] + weight`.
8. Replay route IDs and sum. Check source label zero and every corridor inequality `label[b] <= label[a] + weight`.
9. ⚠️ Exclude a negative cycle without a target exit from this target verdict.
10. Report the certificate and scope; recompute after graph changes.

Python 3 reference for small finite graphs. Edges are tuple/list `(ID, source, target, cost)` records with string IDs and exact integer costs. Run it and record the observed interpreter version. Walks may repeat edges.

```python
from collections import deque

def inventory(nodes, edges, source, target):
    if any(type(n) is not str or not n for n in nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("invalid or duplicate node ID")
    if source not in nodes or target not in nodes:
        raise ValueError("unknown terminal")
    known, ids = set(nodes), set()
    for e in edges:
        if type(e) not in (tuple, list) or len(e) != 4:
            raise ValueError("invalid edge record")
        eid, a, b, w = e
        if (any(type(x) is not str or not x for x in (eid, a, b)) or
                type(w) is not int or eid in ids or a not in known or b not in known):
            raise ValueError("invalid edge fields")
        ids.add(eid)
    return {eid: (a, b, w) for eid, a, b, w in edges}

def reach(start, edges, reverse=False):
    adj = {}
    for eid, a, b, w in edges:
        x, y = (b, a) if reverse else (a, b)
        adj.setdefault(x, []).append(y)
    seen, queue = {start}, deque([start])
    while queue:
        for v in adj.get(queue.popleft(), ()):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen

def path(start, goal, edges):
    if start == goal:
        return ()
    adj = {}
    for eid, a, b, w in sorted(edges):
        adj.setdefault(a, []).append((b, eid))
    queue, routes = deque([start]), {start: ()}
    while queue:
        u = queue.popleft()
        for v, eid in adj.get(u, ()):
            if v not in routes:
                routes[v] = routes[u] + (eid,)
                if v == goal:
                    return routes[v]
                queue.append(v)
    return None

def solve(nodes, edges, source, target):
    by_id = inventory(nodes, edges, source, target)
    if target not in reach(source, edges):
        return {"state": "unreachable"}
    corridor = reach(source, edges) & reach(target, edges, True)
    selected = sorted((e for e in edges if e[1] in corridor and e[2] in corridor))
    dist = {v: None for v in corridor}
    dist[source] = 0
    parent, changed = {}, None
    for _ in range(len(corridor)):
        changed = None
        for eid, a, b, w in selected:
            if dist[a] is not None and (dist[b] is None or dist[a]+w < dist[b]):
                dist[b], parent[b], changed = dist[a]+w, (a, eid), b
        if changed is None:
            break
    if changed is not None:
        cursor = changed
        for _ in range(len(corridor)):
            cursor = parent[cursor][0]
        start, backward = cursor, []
        while True:
            previous, eid = parent[cursor]
            backward.append((previous, cursor, eid))
            cursor = previous
            if cursor == start:
                break
        cycle = tuple(eid for _, _, eid in reversed(backward))
        begin = backward[-1][0]
        approach = path(source, begin, edges)
        exit_route = path(begin, target, edges)
        assert approach is not None and exit_route is not None
        assert sum(by_id[eid][2] for eid in cycle) < 0
        return {"state": "no_finite_minimum", "corridor": sorted(corridor),
                "approach": approach, "cycle": cycle, "exit": exit_route}
    tight = [e for e in selected if dist[e[1]] is not None
             and dist[e[2]] == dist[e[1]] + e[3]]
    route = path(source, target, tight)
    assert route is not None
    return {"state": "finite", "corridor": sorted(corridor),
            "cost": dist[target], "route": route, "labels": dist}

def verify(nodes, edges, source, target, result):
    by_id = inventory(nodes, edges, source, target)
    state = result.get("state")
    reachable = reach(source, edges)
    if state == "unreachable":
        return target not in reachable
    if target not in reachable:
        return False
    corridor = reachable & reach(target, edges, True)
    if result.get("corridor") != sorted(corridor):
        return False
    def replay(start, route):
        cursor, total = start, 0
        for eid in route:
            if eid not in by_id or by_id[eid][0] != cursor:
                return None
            cursor, total = by_id[eid][1], total + by_id[eid][2]
        return cursor, total
    if state == "no_finite_minimum":
        approach = replay(source, result.get("approach", ()))
        if approach is None or not result.get("cycle"):
            return False
        cycle = replay(approach[0], result["cycle"])
        ending = replay(approach[0], result.get("exit", ()))
        return (cycle is not None and cycle[0] == approach[0] and cycle[1] < 0
                and ending is not None and ending[0] == target)
    if state != "finite":
        return False
    labels = result.get("labels", {})
    route = replay(source, result.get("route", ()))
    return (set(labels) == corridor and all(type(x) is int for x in labels.values())
            and labels[source] == 0 and route == (target, result.get("cost"))
            and labels[target] == result.get("cost")
            and all(labels[b] <= labels[a] + w for _, a, b, w in edges
                    if a in corridor and b in corridor))

n = ["S", "A", "B", "T", "X", "Y", "I"]
e = [("sa", "S", "A", 4), ("ab", "A", "B", -3),
     ("bt", "B", "T", 2), ("st", "S", "T", 6),
     ("sx", "S", "X", 0), ("xy", "X", "Y", -2),
     ("yx", "Y", "X", 1)]
finite = solve(n, e, "S", "T")
assert finite["state"] == "finite" and finite["cost"] == 3
assert finite["route"] == ("sa", "ab", "bt")
assert verify(n, e, "S", "T", finite)
bad = solve(n, e + [("ba", "B", "A", 1)], "S", "T")
assert bad["state"] == "no_finite_minimum"
assert verify(n, e + [("ba", "B", "A", 1)], "S", "T", bad)
assert verify(n, e, "S", "I", solve(n, e, "S", "I"))
print("finite route, irrelevant cycle and relevant cycle checked")
```

## Decision rules
- IF the target is unreachable THEN report unreachable BECAUSE no requested walk exists.
- IF a negative cycle lies in the corridor THEN report no finite walk minimum BECAUSE repetition lowers cost without bound.
- IF a negative cycle cannot reach the target THEN exclude it BECAUSE no finishing walk can use it.
- IF finite labels satisfy all inequalities and a route attains the target label THEN certify minimum BECAUSE the bound is attained.
- IF revisits are prohibited THEN use a simple-path method BECAUSE repetition is disallowed.

## Output template
```text
Scope: <revision, directed projection, units and completeness; maximum 70 words>
Terminals and walk policy: <source, target, revisits allowed>
Corridor: <nodes reachable from source that can reach target; or pending>
Verdict: <finite minimum / unreachable / no finite minimum / unresolved>
Certificate: <cost and route IDs OR negative closed cycle plus approach/exit IDs OR none>
Verification: <replayed costs, label inequalities or cycle relevance; executed/pending>
Limits: <excluded records, tie ambiguity and semantic limits; maximum 80 words>
Next action: <owner and bounded follow-up; maximum 40 words>
```

## Quality checklist
- [ ] Source, target and walk policy are explicit.
- [ ] Every scoped node and edge identity is validated.
- [ ] Costs use one exact additive unit and allow signed integers.
- [ ] Target reachability is checked before cycle relevance.
- [ ] Any negative-cycle witness is closed, negative and linked to both terminals.
- [ ] Finite route IDs replay in direction and sum to the reported cost.
- [ ] Every corridor edge satisfies the finite-label inequality.
- [ ] No negative cycle outside the corridor is called relevant to this target.

## Anti-patterns
- **Ignore sign**: run a nonnegative method. Fix: use signed relaxation.
- **Any cycle rejects**: blame an irrelevant cycle. Fix: check approach and exit.
- **Number alone**: omit route and label checks. Fix: replay IDs and inequalities.
- **Simple-path confusion**: repeat cycles when revisits are banned. Fix: confirm walk policy.
- **Rounded sum**: mix units. Fix: require exact additive values.

## Worked example
**Input:** Fictional Cedar exercise C1 has nodes S,A,B,T,X,Y,I. Directed edges sa:S→A cost 4, ab:A→B cost -3, bt:B→T cost 2, st:S→T cost 6, sx:S→X cost 0, xy:X→Y cost -2 and yx:Y→X cost 1. I is isolated. Walks may revisit edges. The snapshot and integer cost unit are complete for this exercise.

**Output:**
```text
Scope: Fictional Cedar C1; complete exercise inventory; directed edges and one integer cost unit.
Terminals and walk policy: S to T; revisits allowed.
Corridor: S,A,B,T.
Verdict: Finite minimum.
Certificate: Cost 3; route sa,ab,bt.
Verification: 4+(-3)+2=3; directed replay and corridor label inequalities executed.
Limits: X/Y form a reachable negative cycle but cannot reach T; I is isolated. Ties, if any, may yield another route.
Next action: Graph owner checks omitted exits from X/Y before using the result outside C1.
```

**Bad output:** “The S-to-T cost is unbounded because X/Y has a negative cycle.”
The cycle has no route to T in the supplied snapshot, so it cannot participate in an S-to-T walk.

## Edge cases
- **Source equals target**: the empty walk costs zero unless a reachable negative cycle can return to that node.
- **Irrelevant negative cycle**: retain it as context, but solve on the source-to-target corridor.
- **Relevant negative cycle**: include an approach, a closed negative cycle and an exit route.
- **Unreachable target**: return no route and no target-relevant cycle verdict.
- **Parallel and tied edges**: preserve edge IDs; one deterministic witness suffices, not all optimal walks.

## Test case
**Input:**
> Fictional C1 has S→A=4, A→B=-3, B→T=2, S→T=6, S→X=0, X→Y=-2, Y→X=1 and isolated I. First assess S to T; then add B→A=1 and reassess. Walk revisits are allowed.

**Assertions:**
1. Before the added edge, reports finite cost 3 via sa,ab,bt.
2. Explains that the reachable X/Y negative cycle is irrelevant because it has no exit to T.
3. After B→A is added, gives a negative A/B cycle witness and a source approach and target exit.
4. Reports no finite S-to-T minimum after the addition, with cycle total -2.
5. Preserves edge direction and IDs without inferring a real-world route policy.
