---
id: GRF-009
name: weighted-route-cost-verification
domain: Graph Engineering Foundations
subdomain: Weighted route computation
version: 1.0
description: Compute and verify a minimum additive-cost route under an explicit weight contract, separating solver eligibility, path evidence and unreachable results.
triggers: ["find the lowest cost graph route", "verify a weighted shortest path", "check whether this route solver applies", "explain equal cost graph routes", "audit route cost and edge evidence"]
not_for: ["bounded minimum-hop traversal [GRF-006]", "dependency critical-path slack [SEQ-003]", "safety-critical navigation or emergency routing", "time-dependent, multiobjective or capacity-constrained routing"]
requires: []
risk_level: medium
---

# Weighted Route Cost Verification

## Purpose
Produce a checkable minimum additive-cost route for a supplied graph and weight definition. Establish solver preconditions before computation, retain edge identities in the route, and distinguish one optimal witness from all optimal routes. A mathematically optimal result does not establish physical route availability or operational safety.

## Inputs to collect
1. **Snapshot and direction** — obtain unique node IDs, edge IDs, endpoints and revision. Why: parallel edges can have different costs and reversing an edge changes the problem. Default: no inferred direction; require explicit directed representation or an approved undirected expansion.
2. **Source and destination** — obtain exact inventory IDs. Why: matching labels is not identity resolution. Default: required; do not select similarly named nodes automatically.
3. **Weight meaning and units** — obtain each edge's cost and whether costs add along a route. Why: probabilities, capacities and durations under congestion cannot automatically be summed. Default: missing weights remain unresolved, never zero.
4. **Numeric contract** — obtain exact units, allowed signs and treatment of missing or nonfinite values. Why: rounding can change ties or the best route. Default: reference requires nonnegative integer units; obtain an exact scaling rule rather than silently rounding fractions.
5. **Eligibility and coverage** — obtain excluded edges/nodes and evidence that the snapshot contains the relevant alternatives. Why: a shortest route in a filtered extract may differ from a complete graph. Default: supplied snapshot only, no complete-world claim.
6. **Tie and execution needs** — identify whether one minimum-cost witness suffices and whether results guide any real action. Why: one witness does not enumerate alternatives or authorize travel. Default: one deterministic witness, analysis only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the graph, eligibility filters, endpoints and cost definition as one named scenario.
2. Verify that every allowed route cost is the sum of supplied edge costs in a common exact unit. Route nonadditive or state-dependent objectives to a separately specified model.
3. Select a solver class from the validated weights: equal nonnegative edge costs permit minimum-hop reasoning; varying nonnegative costs permit the reference below; negative edges require a separately verified method and applicable negative-cycle handling. Do not run this reference by removing signs.
4. Validate the entire scoped inventory and weight table before solving. Reject unknown endpoints, repeated edge identities and missing values rather than changing the problem to obtain an answer.
5. Execute the chosen method while retaining one predecessor edge for each improved distance. For the reference, settle the smallest tentative distance before relaxing its outgoing edges.
6. ⚠️ Replace a predecessor only on a strictly smaller cost. Equal-cost rewrites around zero-cost cycles can create circular predecessor records; retain the declared tie policy instead.
7. Reconstruct the source-to-target witness from predecessor edges. Verify every edge's identity, direction and endpoint continuity against the frozen input.
8. Recompute the witness sum independently from the input weights and compare it with the reported target distance. Retain the all-reachable distance labels for the optimality checks below.
9. Check that every reachable edge satisfies the distance inequality and every predecessor edge is tight. Together with a zero source label and witnessed label costs, these checks support the minimum-cost claim within the supplied graph.
10. Deliver the route or scoped unreachable result, solver assumptions and tie limits. Mark unavailable execution as pending; do not turn a proposed run into a verified answer.

This Python 3 reference uses finite string-ID nodes and directed tuples `(edge_id, source, target, cost)`. It uses exact nonnegative integer costs and a simple full scan suitable for small fixtures; use a separately tested implementation for larger graphs. Run the entire snippet with the available interpreter and record its version. Tuple shape and string fields require prevalidation. It returns all reachable labels and one target route, not every optimal route.

```python
def cheapest(nodes, edges, source, target):
    known = set(nodes)
    if len(known) != len(nodes) or source not in known or target not in known:
        raise ValueError("unique inventory and known endpoints required")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("unique edge IDs required")
    adj = {n: [] for n in nodes}
    by_id = {}
    for eid, a, b, w in sorted(edges):
        if a not in known or b not in known:
            raise ValueError("unknown edge endpoint")
        if type(w) is not int or w < 0:
            raise ValueError("nonnegative integer cost required")
        adj[a].append((eid, b, w))
        by_id[eid] = (a, b, w)
    dist, parent, settled = {source: 0}, {}, set()
    while True:
        choices = [n for n in dist if n not in settled]
        if not choices:
            break
        a = min(choices, key=lambda n: (dist[n], n))
        settled.add(a)
        for eid, b, w in adj[a]:
            candidate = dist[a] + w
            if b not in dist or candidate < dist[b]:
                dist[b], parent[b] = candidate, (a, eid)
    assert all(b in dist and dist[b] <= dist[a] + w
               for eid, a, b, w in edges if a in dist)
    assert all(dist[b] == dist[a] + by_id[eid][2]
               for b, (a, eid) in parent.items())
    if target not in dist:
        return None, [], dist
    path, cursor, seen = [], target, set()
    while cursor != source:
        assert cursor not in seen
        seen.add(cursor)
        previous, eid = parent[cursor]
        assert by_id[eid][:2] == (previous, cursor)
        path.append(eid)
        cursor = previous
    path.reverse()
    assert sum(by_id[eid][2] for eid in path) == dist[target]
    return dist[target], path, dist

nodes = ["A", "B", "C", "D", "X"]
edges = [("ab", "A", "B", 2), ("bd", "B", "D", 3),
         ("ac", "A", "C", 1), ("cd", "C", "D", 4),
         ("ad", "A", "D", 8), ("loop", "B", "B", 0)]
cost, path, labels = cheapest(nodes, edges, "A", "D")
assert (cost, path) == (5, ["ac", "cd"])
assert labels == {"A": 0, "B": 2, "C": 1, "D": 5}
assert cheapest(nodes, edges, "A", "X")[:2] == (None, [])
assert cheapest(nodes, edges, "A", "A")[:2] == (0, [])
print("cost, tie witness, zero-loop, unreachable and source-equals-target passed")
```

## Decision rules
- IF costs are not additive THEN stop this computation BECAUSE summing them optimizes an invented objective.
- IF any scoped weight is negative THEN reject the reference and obtain a verified alternate BECAUSE its nonnegative settlement argument no longer applies.
- IF several routes tie THEN report one witnessed optimum without claiming uniqueness BECAUSE a deterministic tie choice is not proof that alternatives are absent.
- IF the destination lacks a label after completed exploration THEN report unreachable in the scoped snapshot BECAUSE missing real-world coverage prevents a global conclusion.
- IF fractional units cannot be represented exactly by the agreed conversion THEN preserve them for a tested exact implementation BECAUSE rounding may change the selected route.

## Output template
```text
Scenario: <snapshot, source, target, direction and filters; maximum 70 words>
Cost contract: <meaning, unit, additivity, numeric/sign checks; maximum 70 words>
Method: <selected solver and eligibility evidence; maximum 60 words>
Result: <minimum cost / unreachable / unresolved; scoped interpretation>
Witness: <ordered edge IDs with endpoints and costs; full table or attachment>
Verification: <recomputed sum, distance/predecessor checks, execution evidence>
Alternatives: <one witness only; observed ties or untested uniqueness>
Limits: <coverage, unsupported constraints and operational claims; maximum 80 words>
```

## Quality checklist
- [ ] Direction, source, target and snapshot are explicit.
- [ ] Every scoped edge has an evidenced cost in the same unit.
- [ ] Additivity and sign assumptions match the selected solver.
- [ ] Every witness edge retains its original identity and direction.
- [ ] The independently summed witness cost equals the target label.
- [ ] Distance inequalities and tight predecessors pass or remain pending.
- [ ] Ties and unreachable states are described without unsupported uniqueness.
- [ ] Computed optimality is separated from real-world route authorization.

## Anti-patterns
- **Fewest hops shortcut**: choose a direct costly edge. Fix: optimize the declared additive weights.
- **Negative-value cleanup**: take absolute values to fit the solver. Fix: select a verified compatible method or stop.
- **Equal-cost predecessor churn**: rewrite parents on every tie. Fix: preserve the declared stable witness rule.
- **Endpoint-only path**: omit which parallel edge was chosen. Fix: retain edge IDs and their weights.
- **Optimal means available**: call a computed path physically usable. Fix: separate graph evidence from operational checks.

## Worked example
**Input:** Fictional sandbox Fir supplies the snippet graph. Costs are exact additive effort ticks; all edges are directed and eligible. Find A to D; one witness suffices. No real navigation is requested.

**Output:**
```text
Scenario: Fir fixture; A to D; directed supplied edges; no filters.
Cost contract: Nonnegative integer effort ticks, additive; complete supplied weight table.
Method: Small-graph nonnegative label settlement; all scoped weights checked.
Result: Minimum supplied-graph cost 5 ticks.
Witness: ac | A->C | 1; cd | C->D | 4.
Verification: Recomputed 1+4=5. Reference checks witness continuity, tight predecessors and distance inequalities when executed.
Alternatives: ab then bd also totals 2+3=5; one deterministic witness returned, uniqueness not claimed.
Limits: Snapshot arithmetic only; no physical availability, safety, resource capacity or live system validated.
```

**Bad output:** "Use ad because one hop is shorter than two; cost eight is optimal."
It optimizes hop count while the supplied objective is additive effort cost.

## Edge cases
- **Source equals target**: return the empty route with zero cost under this nonnegative contract; do not invent a required cycle.
- **Zero-cost cycle**: retain strict improvements and one acyclic predecessor witness; do not promise enumeration of infinitely many equal-cost walks.
- **Parallel alternatives**: compare their actual costs and retain the selected edge ID; equal costs do not make source records identical.
- **Unreachable destination**: return no route and no finite cost, distinguishing failure to finish execution from completed unreachability.
- **Negative edges elsewhere in scope**: reference still rejects the graph; narrowing scope requires an explicit justified transformation, not silent omission.

## Test case
**Input:**
> Fictional directed graph has s->t cost 9, s->a cost 2, a->t cost 3 and a->a cost 0, with distinct supplied edge IDs. Costs are exact additive ticks. Compute s to t; one witness only.

**Assertions:**
1. Returns the two-edge route through a with cost five, not the direct route of nine.
2. Includes edge identities and independently sums two plus three.
3. Terminates despite the zero-cost self-loop without adding it to the witness.
4. Limits the minimum-cost claim to the supplied weighted graph and distinguishes actual execution from a proposed run.
