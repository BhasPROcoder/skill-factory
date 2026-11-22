Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-056
name: bounded-graph-walk-cardinality-preflight
domain: Graph Engineering Foundations
subdomain: Walk result sizing
version: 1.0
description: Count exact edge-ID walks by length and endpoint before a bounded graph query when result multiplicity may exceed a supplied output budget.
triggers: ["count graph walks before querying", "estimate exact path rows by hop", "check parallel edge walk explosion", "find first over-budget traversal layer", "preflight a bounded graph walk query"]
not_for: ["minimum-hop endpoint reachability [GRF-006]", "one relation-pattern witness [GRF-030]", "query-plan equivalence [GRF-015]", "simple paths or unrestricted walk enumeration", "promising runtime or memory use"]
requires: []
risk_level: medium
---

# Bounded Graph Walk Cardinality Preflight

## Purpose
Count distinct edge-ID walks from one seed at every exact hop length up to a supplied bound. Report per-endpoint totals and the first layer where a supplied result-row budget is exceeded. The count can inform query scoping, but does not predict execution time, memory or business importance.

## Inputs to collect
1. **Graph snapshot** — obtain unique node and edge IDs, directed endpoints, relation labels and revision, including isolates. Why: parallel records and loops change walk counts. Default: none.
2. **Query contract** — obtain exact seed, outgoing or incoming direction, allowed relation labels, and nonnegative maximum hop count. Why: each choice changes the counted walk population. Default: none; do not infer direction or bound.
3. **Walk semantics** — confirm repeated nodes and edges are allowed, each edge ID is a separate transition, and whether the zero-hop seed walk counts in the total. Why: simple paths and endpoint DISTINCT are different tasks. Default: reference semantics with repeats allowed; request zero-hop choice.
4. **Result budget** — obtain a nonnegative integer row limit chosen by the owner. Why: no universal safe output size exists. Default: report counts without a pass/fail threshold if absent.
5. **Execution and use** — obtain whether the snapshot and calculation are complete and who decides query changes. Why: partial counts cannot certify a bound. Default: supplied graph only and no live query execution.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the node/edge inventory, revision, seed, direction, allowed labels, bound and zero-hop policy.
2. Validate unique nonempty IDs, exact edge-record shapes, known endpoints, a nonnegative integer bound and nonnegative integer budget if supplied.
3. Initialize the exact-length-zero count to one at the seed and zero elsewhere.
4. For each next length, propagate the previous layer's count across every eligible directed edge ID. Reverse endpoint roles for an incoming query; do not change the source records.
5. Sum contributions arriving at the same endpoint, including separate parallel edge IDs and loop traversals. ⚠️ Do not mark a vertex visited and suppress revisits: a walk count includes them.
6. Store every layer's complete endpoint-count table, including explicit zero-count nodes where useful for the audit.
7. Sum only the layers requested by the zero-hop policy. Compare each cumulative total with the owner budget and record the first length at which it is **greater** than the budget; equality alone does not cross it.
8. Independently enumerate edge-ID sequences for a small fixture and compare its per-length/per-endpoint counts with dynamic propagation. For larger data, use a separately verified implementation; do not claim the small fixture proves performance.
9. Stop with an incomplete marker if calculation or graph extraction ends early. A partial lower bound cannot prove that the final result stays within budget.
10. Deliver the table, cumulative totals, budget decision, executed verification and limits. Ask the owner to choose a smaller bound, a changed result contract or pagination when the count exceeds the supplied limit; do not silently replace walks with distinct endpoints.

This Python 3 reference accepts `(edge_id, source, target, relation)` records. It uses exact integers and counts walks with repeated nodes and edges. The independent enumerator materializes edge-ID sequences only for small verification fixtures. Run the snippet and record the observed interpreter version.

```python
from collections import Counter

def check(nodes, edges, seed, labels, direction, depth, budget):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes) or seed not in nodes:
        raise ValueError("duplicate node or unknown seed")
    if any(type(e) not in (tuple, list) or len(e) != 4 or
           any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    if any(a not in nodes or b not in nodes for _, a, b, _ in edges):
        raise ValueError("unknown endpoint")
    if type(labels) not in (tuple, list, set) or not labels or any(
            type(x) is not str or not x for x in labels):
        raise ValueError("explicit relation labels required")
    if direction not in ("out", "in") or type(depth) is not int or depth < 0:
        raise ValueError("invalid direction or depth")
    if budget is not None and (type(budget) is not int or budget < 0):
        raise ValueError("nonnegative budget required")

def count_walks(nodes, edges, seed, labels, direction, depth,
                include_zero, budget=None):
    check(nodes, edges, seed, labels, direction, depth, budget)
    if type(include_zero) is not bool:
        raise ValueError("zero-hop policy required")
    selected = [(eid, a, b) if direction == "out" else (eid, b, a)
                for eid, a, b, label in edges if label in labels]
    layers = [{n: int(n == seed) for n in nodes}]
    cumulative = int(include_zero)
    crossing = 0 if budget is not None and cumulative > budget else None
    totals = [cumulative]
    for length in range(1, depth + 1):
        prior = layers[-1]
        next_layer = {n: 0 for n in nodes}
        for _, a, b in selected:
            next_layer[b] += prior[a]
        layers.append(next_layer)
        cumulative += sum(next_layer.values())
        totals.append(cumulative)
        if budget is not None and crossing is None and cumulative > budget:
            crossing = length
    return layers, totals, crossing

def enumerate_small(nodes, edges, seed, labels, direction, depth):
    selected = [(eid, a, b) if direction == "out" else (eid, b, a)
                for eid, a, b, label in edges if label in labels]
    frontier = [(seed, ())]
    layers = []
    for length in range(depth + 1):
        counts = Counter(node for node, _ in frontier)
        layers.append({n: counts[n] for n in nodes})
        frontier = [(b, route + (eid,))
                    for node, route in frontier
                    for eid, a, b in selected if a == node]
    return layers

nodes = ["A", "B", "C", "I"]
edges = [("p1", "A", "B", "link"), ("p2", "A", "B", "link"),
         ("q1", "B", "C", "link"), ("q2", "B", "C", "link"),
         ("l", "B", "B", "link")]
layers, totals, crossing = count_walks(
    nodes, edges, "A", ("link",), "out", 3, False, 5)
assert layers == enumerate_small(nodes, edges, "A", ("link",), "out", 3)
assert [sum(row.values()) for row in layers] == [1, 2, 6, 6]
assert totals == [0, 2, 8, 14] and crossing == 2
assert count_walks(nodes, edges, "A", ("link",), "out", 0,
                   True, 0)[2] == 0
print("edge-ID walk layers and budget boundary checked")
```

The layer table is exact for the supplied finite graph and bound. Parallel IDs create separate walks even when the endpoints coincide. A cycle can produce further walks at later lengths, but this result makes no unrestricted-count claim. The enumerator is a fixture verifier, not the proposed production counting strategy.

## Decision rules
- IF a parallel edge ID exists THEN propagate a separate contribution BECAUSE distinct edge sequences are distinct walks.
- IF a walk revisits a node or edge THEN keep it BECAUSE the declared contract allows repetition.
- IF cumulative count exceeds the supplied budget THEN identify the first crossing layer BECAUSE the owner needs a concrete scope decision.
- IF cumulative count equals the budget THEN do not flag an exceedance BECAUSE crossing means strictly greater.
- IF execution is incomplete THEN withhold a within-budget conclusion BECAUSE unchecked layers may add rows.

## Output template
```text
Scope: <revision, seed, direction, relation filter, bound; maximum 70 words>
Walk policy: <edge IDs distinct, revisits, zero-hop inclusion>
Layers: <length | endpoint | exact count; complete table or attached ledger>
Cumulative: <length | total through length; complete table>
Budget: <owner limit | first crossing length or None>
Verification: <independent enumeration executed/pending and input checks>
Limits: <coverage, scale and runtime uncertainty; maximum 80 words>
Next action: <owner and concrete query-scope choice; maximum 40 words>
```

## Quality checklist
- [ ] Seed, direction, labels, bound and zero-hop policy are explicit.
- [ ] Unique edge IDs and known endpoints are checked.
- [ ] Every parallel ID contributes independently.
- [ ] Repeated nodes and loops follow walk semantics.
- [ ] Every layer's endpoint counts sum to its layer total.
- [ ] Cumulative totals use the declared zero-hop policy.
- [ ] First budget crossing uses strict greater-than.
- [ ] Count evidence is not described as runtime prediction.

## Anti-patterns
- **Visited-node pruning**: suppress later walks to a reached node. Fix: propagate counts at every length.
- **Endpoint deduplication**: count one result for all edge-ID sequences. Fix: count each transition.
- **Loop deletion**: remove self-loops as inconvenient. Fix: retain eligible loop walks.
- **Silent zero-hop**: include or exclude the seed without stating it. Fix: declare the policy.
- **Count as performance**: promise the query will be fast because row count is low. Fix: measure separately.

## Worked example
**Input:** Fictional Team Fern supplies the snippet graph. Count outgoing link walks from A through length three, exclude zero hop from total, and use an owner budget of five rows.

**Output:**
```text
Scope: Fern exercise F1; A/B/C/I and identified directed link edges; seed A, outgoing, bound 3.
Walk policy: Edge IDs distinct, repeats allowed, zero hop excluded from cumulative total.
Layers: 0 | A | 1; 1 | B | 2; 2 | B | 2, C | 4; 3 | B | 2, C | 4; all other endpoint counts zero.
Cumulative: Length 0 | 0; length 1 | 2; length 2 | 8; length 3 | 14.
Budget: Five rows; first exceeded at length 2.
Verification: Dynamic propagation matched independent edge-ID sequence enumeration for all four layers.
Limits: Exercise graph and bound only; no runtime or memory estimate.
Next action: Query owner chooses a shorter bound or changes the output contract before execution.
```

**Bad output:** “A reaches B and C, so there are only two rows and the query is safe.”
That counts endpoints rather than distinct edge-ID walks and ignores loops.

## Edge cases
- **Depth zero**: report one zero-hop seed walk; include it in cumulative total only if chosen.
- **No eligible edges**: positive-length layers have zero counts.
- **Parallel edges**: retain separate ID contributions.
- **Loop or cycle**: count bounded revisits; do not infer an unrestricted finite total.
- **Missing budget**: report counts without a crossing verdict.

## Test case
**Input:**
> Fictional A has two parallel A→B links; B has two B→C links and one B loop; I is isolated. Count outgoing link walks through length three, excluding zero hop, with budget five.

**Assertions:**
1. Reports positive-length layer totals two, six and six.
2. Reports cumulative totals two, eight and fourteen.
3. Identifies length two as the first strictly over-budget layer.
4. Keeps parallel and loop edge-ID walks distinct and I at zero positive-length count.
5. Does not claim measured query runtime.
</skill>

<user_request>
Fictional A has two parallel A→B links; B has two B→C links and one B loop; I is isolated. Count outgoing link walks through length three, excluding zero hop, with budget five.
</user_request>
