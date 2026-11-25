---
id: GRF-032
name: minimum-spanning-forest-certificate
domain: Graph Engineering Foundations
subdomain: Weighted spanning structures
version: 1.0
description: Construct and independently check a minimum-total-weight spanning forest when an undirected graph must connect each original component with selected edges.
triggers: ["find a minimum spanning forest", "certify a spanning tree cost", "check an expensive spanning tree", "preserve disconnected graph components", "explain tied spanning alternatives"]
not_for: ["minimum source-to-target routes [GRF-009]", "parent forest validation [GRF-004]", "flow capacity certification [GRF-010]", "directed branching optimization", "physical network engineering approval"]
requires: []
risk_level: medium
---

# Minimum Spanning Forest Certificate

## Purpose
Select an acyclic set of undirected edges that connects every original component with minimum total supplied weight. Return selected edge identities and exchange checks that can expose a cheaper alternative. This solves a declared additive graph objective, without establishing service redundancy or physical suitability.

## Inputs to collect
1. **Graph inventory** — collect all node IDs and identified edges, including isolated nodes. Why: component coverage depends on the complete inventory. Default: required; no invented endpoints.
2. **Direction contract** — confirm undirected semantics. Why: directed reachability does not use the same spanning criterion. Default: unresolved; request interpretation rather than discarding arrows.
3. **Weight meaning** — obtain exact additive values in one common unit. Why: summing incomparable quantities gives an unsupported objective. Default: required; missing values never become zero.
4. **Eligibility rules** — identify permitted edges and any mandatory choices. Why: eligibility changes the optimization problem. Default: all supplied edges eligible; mandatory-edge constraints require a separately verified extension.
5. **Component expectation** — state whether separate original components are acceptable. Why: a forest cannot connect components lacking an eligible connecting edge. Default: preserve each component and explicitly report disconnectedness.
6. **Tie and execution policy** — obtain deterministic tie ordering and practical resource bounds. Why: equal weights may admit multiple solutions. Default: sort by weight then edge ID; bounded local fixture execution, no scalable runtime claim.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the graph revision, eligible edges, undirected interpretation and common weight unit.
2. Validate identities, endpoints and all weights before constructing a candidate.
3. Identify original connected components while retaining isolated nodes.
4. Sort eligible non-loop edges by weight and the declared tie rule.
5. Add an edge only when its endpoints currently belong to different selected components.
6. Recompute the selected-edge total from the original weight records.
7. Independently check that selected IDs exist, are unique and form no cycle.
8. Check that every original non-loop edge has its endpoints connected in the selected forest; this establishes spanning of each original component.
9. For every unselected non-loop edge, find its unique selected-tree endpoint path and record the maximum path weight.
10. ⚠️ Reject optimality when an unselected edge is cheaper than that maximum; retain the edge and replaceable path edge as an improvement witness rather than trusting the construction label.
11. Deliver component coverage, selected identities, cost and all exchange results, distinguishing ties from proven uniqueness.

Use this Python 3 reference for finite in-memory graphs with string IDs and integer weights in a declared exact unit. Signed integers are supported; no floating comparison tolerance is implied. Prevalidate tuple shapes and string fields. Edges are `(ID, endpoint, endpoint, weight)`. Run the complete snippet and record the interpreter version. The verifier inspects a supplied selection without replaying the greedy construction.

```python
def validate(nodes, edges):
    if len(set(nodes)) != len(nodes) or len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate identity")
    if any(a not in nodes or b not in nodes or type(w) is not int
           for eid, a, b, w in edges):
        raise ValueError("invalid endpoint or exact weight")

def construct(nodes, edges):
    validate(nodes, edges)
    parent = {n: n for n in nodes}
    def root(n):
        while parent[n] != n:
            n = parent[n]
        return n
    chosen = []
    for eid, a, b, w in sorted(edges, key=lambda e: (e[3], e[0])):
        x, y = root(a), root(b)
        if x != y:
            chosen.append(eid)
            parent[x] = y
    return chosen

def certify(nodes, edges, chosen):
    validate(nodes, edges)
    table = {e[0]: e for e in edges}
    if len(set(chosen)) != len(chosen) or not set(chosen) <= set(table):
        raise ValueError("invalid selected IDs")
    adj = {n: [] for n in nodes}
    def path(a, b):
        todo, seen = [(a, [])], {a}
        while todo:
            u, steps = todo.pop()
            if u == b:
                return steps
            for v, eid, w in adj[u]:
                if v not in seen:
                    seen.add(v)
                    todo.append((v, steps + [(eid, w)]))
        return None
    for eid in chosen:
        _, a, b, w = table[eid]
        if path(a, b) is not None:
            raise ValueError("selected cycle or loop")
        adj[a].append((b, eid, w))
        adj[b].append((a, eid, w))
    checks = []
    for eid, a, b, w in edges:
        if a == b or eid in chosen:
            continue
        route = path(a, b)
        if route is None:
            raise ValueError("not spanning original component")
        peak_id, peak = max(route, key=lambda x: x[1])
        checks.append((eid, w, peak_id, peak, w >= peak))
    return sum(table[e][3] for e in chosen), checks

nodes = ["A", "B", "C", "I"]
edges = [("ab", "A", "B", -2), ("ac", "A", "C", 4),
         ("bc", "B", "C", 1), ("bc2", "B", "C", 1),
         ("loop", "A", "A", -10)]
chosen = construct(nodes, edges)
total, checks = certify(nodes, edges, chosen)
assert chosen == ["ab", "bc"] and total == -1
assert all(row[-1] for row in checks)
assert not all(row[-1] for row in certify(nodes, edges, ["ab", "ac"])[1])
print("spanning forest and exchange certificate checked")
```

For an acyclic spanning selection, each non-tree edge closes one cycle with its endpoint path. If it is cheaper than a maximum-weight path edge, exchanging those edges decreases total weight. Conversely, when all such inequalities hold, the selection is minimum under this unconstrained undirected contract. Equality permits a tied exchange; deterministic tie handling does not prove unique optimality. Loops never help connect distinct nodes and cannot belong to a forest even if their weights are negative.

## Decision rules
- IF the original graph is disconnected THEN return a forest and identify its components BECAUSE no eligible edge connects those components.
- IF a selected cycle or uncovered component exists THEN reject feasibility before optimality BECAUSE exchange checks require an acyclic spanning selection.
- IF an exchange inequality fails THEN report the cheaper entering edge and replaceable edge BECAUSE they witness a strict improvement.
- IF an inequality is equal THEN report a tied alternative BECAUSE the selected edge set need not be unique.
- IF weights represent distances from one source THEN clarify the objective BECAUSE minimum total connection cost does not minimize every route length.

## Output template
```text
Contract: <revision, direction, eligibility, unit; maximum 70 words>
Components: <original node groups including isolates>
Selection: <edge IDs and independently recomputed total>
Feasibility: <identity, acyclicity and spanning checks; executed/pending>
Exchange ledger: <unselected edge | weight | maximum path edge/weight | pass/fail/tie>
Decision: <minimum certified / infeasible / improvable / unresolved>
Limits: <ties, omitted constraints and operational limits; maximum 70 words>
```

## Quality checklist
- [ ] All scoped nodes, including isolates, appear in component coverage.
- [ ] Direction and additive weight meaning are explicit.
- [ ] Parallel edges retain independent IDs.
- [ ] Selected IDs, cycles and component spanning were checked.
- [ ] Total is recomputed from source weights.
- [ ] Every unselected non-loop edge has an exchange check.
- [ ] Tied alternatives are not described as unique.
- [ ] Physical suitability and route optimality are outside the conclusion.

## Anti-patterns
- **Cheap routes substitute**: deliver shortest-source routes as a minimum forest. Fix: minimize selected total and certify exchanges.
- **Negative-loop bargain**: include a negative loop to lower cost. Fix: enforce acyclic forest feasibility.
- **Counts prove coverage**: accept an edge count without checking endpoints. Fix: verify original component spanning.
- **Greedy trust**: label a result optimal solely because code sorted weights. Fix: inspect the independent exchange ledger.
- **Tie certainty**: treat deterministic ordering as unique optimality. Fix: expose equal exchange alternatives.

## Worked example
**Input:** Fictional fixture above uses exact cost units, undirected edges and unconstrained eligibility. I is isolated; tied parallel edges bc and bc2 are permitted.

**Output:**
```text
Contract: Fictional F; undirected; all supplied edges eligible; integer cost units.
Components: {A,B,C}; {I}.
Selection: ab,bc; total -1 from -2+1.
Feasibility: Expected unique IDs, acyclic selection and original-component spanning; execute reference to confirm.
Exchange ledger: ac | 4 | bc/1 | pass; bc2 | 1 | bc/1 | tie; loop excluded from forest.
Decision: Minimum certified when the listed feasibility and exchange checks execute successfully.
Limits: bc2 can replace bc at equal total; no unique edge-set, route-optimality or physical readiness claim.
```

**Bad output:** “Select the negative loop too; its lower total proves a better spanning tree.”
This violates acyclicity and changes the admissible solution class.

## Edge cases
- **Empty or isolated inventory**: return the empty selection with zero total and explicit components; do not invent links.
- **Unknown selected edge**: reject the selection before cost calculation.
- **Required edge constraints**: stop this unconstrained certificate and specify a verified constrained method.
- **Equal-weight parallel edges**: retain IDs and show a tied exchange without selecting both into a cycle.
- **Incomplete graph**: certify only the supplied eligible snapshot; unseen cheaper connections remain outside evidence.

## Test case
**Input:**
> Fictional undirected A-B costs 1, B-C costs 2, A-C costs 8, and I is isolated. Review the proposed selection A-B plus A-C.

**Assertions:**
1. Preserves isolated I and recognizes a forest across original components.
2. Recomputes proposed total as 9.
3. Identifies B-C replacing A-C as a cheaper exchange, producing total 3.
4. Does not call the proposed selection minimum or infer source-route optimality.
