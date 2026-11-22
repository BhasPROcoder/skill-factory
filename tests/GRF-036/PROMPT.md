Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-036
name: bounded-graph-coloring-feasibility
domain: Graph Engineering Foundations
subdomain: Constrained coloring certificates
version: 1.0
description: Decide finite undirected graph coloring feasibility under an explicit palette and per-node restrictions, reporting a checked coloring, exhaustive infeasibility, or cutoff uncertainty.
triggers: ["color this conflict graph", "assign limited colors to adjacent nodes", "check three-color feasibility", "respect fixed node colors", "show why the palette is insufficient", "bound a graph coloring search"]
not_for: ["two-color bipartition or odd-cycle witness [GRF-031]", "maximum one-to-one matching [GRF-011]", "resource booking policy [SVC-001]", "choosing an optimal number of colors", "authorizing real-world schedule changes"]
requires: []
risk_level: medium
---

# Bounded Graph Coloring Feasibility

## Purpose
Decide whether nodes can receive permitted palette colors while adjacent nodes differ. Return a checked assignment, exhaustive infeasibility, or unknown at the declared search limit. Color labels are structural categories; operational assignments need separate rules.

## Inputs to collect
1. **Inventory** — complete node IDs and uniquely identified undirected edge endpoints for one snapshot. Why: omitted edges can turn a false positive into an apparent valid coloring. Default: none, required.
2. **Palette** — exact finite color labels available to this instance. Why: feasibility depends on the offered labels and their identity. Default: none, required.
3. **Per-node allowed sets** — permitted palette labels for each node, including any fixed color as a one-element set. Why: a valid abstract coloring may violate an external restriction. Default: every palette color for a node whose restrictions are explicitly absent.
4. **Projection rule** — which source relationships become undirected conflicts and whether parallel IDs remain distinct records. Why: direction or relation filtering must not be guessed. Default: none when the source is ambiguous.
5. **Search budget** — maximum recursive states and whether proof is required. Why: stopped search cannot prove infeasibility. Default: an explicitly stated finite budget; report its value.
6. **Use boundary** — whether the result is a structural analysis or a proposed operational assignment. Why: domain constraints may be missing. Default: structural analysis only.

If a required input is missing without a safe default, ask in one message with at most three questions. Preserve the supplied inventory and color restrictions as the evidence boundary.

## Procedure
1. Freeze the node, edge, palette and restriction snapshot before computation.
2. Validate nonempty unique node IDs, unique edge IDs, known endpoints, distinct palette labels, and allowed sets contained in the palette. Reject malformed records rather than repairing them silently.
3. Interpret every selected edge as an undirected inequality constraint, including parallel records. A self-loop is immediately infeasible because its endpoint cannot differ from itself.
4. Represent a fixed node color as an allowed set containing only that color. If an allowed set is empty, return infeasible with the node as a direct witness.
5. Choose a deterministic node order and a deterministic order of allowed colors. State the order so another implementation can replay the search.
6. Search assignments depth first. Reject a color whenever it equals the already assigned color of an adjacent node; count each visited search state against the declared budget.
7. On a complete assignment, independently verify that every node has exactly one allowed palette color and every edge crosses different colors. A successful search without this replay is not the final certificate.
8. If the search exhausts all branches within the budget, report infeasible and give the visited-state count and exact inventory. For a small fixture, independently enumerate all assignments as an additional check.
9. ⚠️ If the budget is reached before exploration completes, report unknown and the explored count, not infeasible. Increasing the budget is a new run with a new evidence record.
10. Deliver the scope, result, certificate or exhaustive-search evidence, limits, and next action. Keep operational decisions with the relevant owner.

This Python 3 reference uses finite in-memory string identities, integer palette labels and edge triples `(ID, A, B)`. It makes no production runtime claim. Run the full snippet and record the interpreter used. `limit` counts entered search states, including the root, so a too-small limit can return unknown even when a coloring exists.

```python
def solve(nodes, edges, palette, allowed, limit):
    if type(limit) is not int or limit < 1:
        raise ValueError("positive integer state limit required")
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    if any(type(c) is not int for c in palette) or len(set(palette)) != len(palette):
        raise ValueError("distinct integer palette required")
    if any(type(e) not in (tuple, list) or len(e) != 3 or
           any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    node_set = set(nodes)
    if any(a not in node_set or b not in node_set for _, a, b in edges):
        raise ValueError("unknown endpoint")
    if set(allowed) != node_set:
        raise ValueError("allowed sets must cover every node")
    choices = {}
    for n in nodes:
        v = allowed[n]
        if type(v) not in (set, frozenset) or any(type(c) is not int for c in v):
            raise ValueError("invalid allowed set")
        if not v <= set(palette):
            raise ValueError("color outside palette")
        choices[n] = sorted(v)
    if any(a == b for _, a, b in edges) or any(not choices[n] for n in nodes):
        return {"status": "infeasible", "states": 0, "coloring": None}
    order = sorted(nodes)
    neighbors = {n: set() for n in nodes}
    for _, a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    states, stopped = 0, False
    assignment = {}
    def search(i):
        nonlocal states, stopped
        if states == limit:
            stopped = True
            return None
        states += 1
        if i == len(order):
            return dict(assignment)
        n = order[i]
        for c in choices[n]:
            if all(assignment.get(other) != c for other in neighbors[n]
                   if other in assignment):
                assignment[n] = c
                found = search(i + 1)
                if found is not None:
                    return found
                del assignment[n]
                if stopped:
                    return None
        return None
    coloring = search(0)
    if coloring is not None:
        assert set(coloring) == node_set
        assert all(coloring[n] in choices[n] for n in nodes)
        assert all(coloring[a] != coloring[b] for _, a, b in edges)
        return {"status": "feasible", "states": states, "coloring": coloring}
    return {"status": "unknown" if stopped else "infeasible",
            "states": states, "coloring": None}

triangle = [("ab", "A", "B"), ("bc", "B", "C"), ("ca", "C", "A")]
nodes = ["A", "B", "C", "I"]
three = {n: {0, 1, 2} for n in nodes}
three["A"] = {0}
yes = solve(nodes, triangle, [0, 1, 2], three, 100)
assert yes["status"] == "feasible" and yes["coloring"]["A"] == 0
two = {n: {0, 1} for n in nodes}
assert solve(nodes, triangle, [0, 1], two, 100)["status"] == "infeasible"
assert solve(nodes, triangle, [0, 1, 2], three, 1)["status"] == "unknown"
assert solve(["A"], [("loop", "A", "A")], [0], {"A": {0}}, 10)["status"] == "infeasible"
print("coloring, exhaustive failure, cutoff and loop checked")
```

## Decision rules
- IF the graph inventory or projection is incomplete THEN return unresolved BECAUSE a missing conflict edge can invalidate a coloring.
- IF a self-loop or empty allowed set exists THEN return infeasible with that direct witness BECAUSE no color assignment can satisfy it.
- IF a complete coloring passes all node and edge checks THEN report feasible within the supplied scope BECAUSE every declared constraint has been replayed.
- IF every search branch is exhausted within the limit THEN report infeasible for this exact finite instance BECAUSE no permitted complete assignment remains.
- IF the state limit interrupts search THEN report unknown BECAUSE explored failures do not cover unexplored branches.
- IF external labels impose additional business rules THEN seek their explicit allowed sets before operational use BECAUSE structural colors have no inherent meaning.

## Output template
```text
Scope: <snapshot, nodes, undirected edge IDs, palette and allowed-set policy; max 3 lines>
Search: <node/color order, state limit, visited states, completed or cut off>
Verdict: <feasible | infeasible | unknown | unresolved>
Certificate: <complete node=color map | direct obstruction | exhaustive search completed | none>
Verification: <node coverage, allowed-color membership, edge inequality checks, or why unavailable>
Limits: <unexamined records and operational restrictions; max 2 lines>
Next action: <one concrete step>
```

## Quality checklist
- [ ] The inventory and undirected projection are explicit.
- [ ] Each node and edge ID is unique and all endpoints are known.
- [ ] Palette labels and per-node allowed sets are complete.
- [ ] Fixed colors appear as one-element allowed sets.
- [ ] The state limit and actual visited count are reported.
- [ ] A positive assignment covers every node and passes each edge inequality.
- [ ] An infeasible verdict comes from a direct obstruction or completed search.
- [ ] A cutoff is labeled unknown rather than infeasible.
- [ ] Operational restrictions are not inferred from color labels.

## Anti-patterns
- **Greedy failure as impossibility**: one failed choice order does not exhaust alternatives. Fix: complete the bounded backtracking tree or report unknown.
- **Hidden precolor**: an externally fixed color omitted from allowed sets can change the answer. Fix: encode it as a singleton.
- **Ignoring isolates**: a valid color map still must cover every declared node. Fix: verify complete inventory coverage.
- **Silent self-loop drop**: removing a loop can turn an impossible instance into an apparent solution. Fix: return the loop obstruction.
- **Cutoff laundering**: a time or state limit is not a negative proof. Fix: label incomplete exploration unknown.
- **Scheduling assertion**: color labels alone do not prove resources or times are available. Fix: ask the owner for domain constraints.

## Worked example
**Input:**
> Fictional Cedar team supplies undirected snapshot S1 with nodes A,B,C,I and triangle edges ab,bc,ca. Palette is 0,1,2. A must use 0; all other nodes may use any palette color. State limit 100. Show structural feasibility.

**Output:**
```text
Scope: Fictional Cedar S1; A,B,C,I; undirected ab,bc,ca; palette {0,1,2}; A={0}, others={0,1,2}.
Search: Nodes A,B,C,I; ascending allowed colors; limit 100; completed after 5 states.
Verdict: Feasible.
Certificate: A=0, B=1, C=2, I=0.
Verification: All four nodes covered; colors allowed; ab,bc,ca cross different colors.
Limits: I is isolated; color labels have no scheduling meaning.
Next action: Check any real assignment constraints before using these labels operationally.
```

**Bad output:** "Two colors fail, so the triangle cannot be colored." This fails because the declared palette has three colors and a valid complete assignment exists.

## Edge cases
- **Parallel edges**: check each identity; equal endpoints impose the same inequality but remain separate evidence records.
- **Isolated node**: still assign one permitted color; an empty allowed set is infeasible even without edges.
- **Self-loop**: return infeasible immediately and identify the loop; no search is needed.
- **Conflicting fixed colors**: adjacent singleton sets with the same label exhaust all branches and yield infeasible.
- **Tiny limit**: return unknown if the search stops before a solution or exhaustive failure.
- **Empty node set**: an empty assignment is feasible if no edge exists and the root state fits the budget.

## Test case
**Input:**
> Fictional Delta snapshot T1 has nodes P,Q,R,I, triangle edges pq,qr,rp, and palette {0,1,2}; P is fixed to 0. Compare a complete search with the same graph restricted to {0,1}, and a run with state limit 1.

**Assertions:**
1. The three-color run returns a complete allowed map covering P,Q,R,I, with different colors on each triangle edge.
2. The two-color run reports infeasible only after a completed search or direct obstruction, not after one greedy attempt.
3. The state-limit-1 run reports unknown, not infeasible.
4. The output keeps I in the node inventory and states that colors have no automatic scheduling meaning.
</skill>

<user_request>
Fictional Delta snapshot T1 has nodes P,Q,R,I, triangle edges pq,qr,rp, and palette {0,1,2}; P is fixed to 0. Compare a complete search with the same graph restricted to {0,1}, and a run with state limit 1.
</user_request>
