---
id: GRF-042
name: bounded-steiner-connector-certificate
domain: Graph Engineering Foundations
subdomain: Terminal connector optimization
version: 1.0
description: Find and verify a minimum-cost undirected tree connecting selected terminals by exhaustive bounded search over eligible nonnegative weighted edges.
triggers: ["connect selected graph terminals cheaply", "find a small Steiner tree", "compare terminal connector cost", "include intermediate nodes in a connector", "certify optimal terminal network on a tiny graph", "report connector search cutoff"]
not_for: ["spanning every component [GRF-032]", "minimum source-to-target route [GRF-009]", "directed network design", "negative or nonadditive edge costs", "physical construction authorization"]
requires: []
risk_level: medium
---

# Bounded Steiner Connector Certificate

## Purpose
Choose a minimum-cost tree connecting specified terminals in a finite undirected graph. Nonterminals may serve as connectors; unrelated nodes need not be spanned. Report a checked tree, exhaustive optimum or infeasibility, or unknown at cutoff.

## Inputs to collect
1. **Snapshot** — unique node IDs and edge records `(ID, endpoint, endpoint, cost)` from one version. Why: missing alternatives change optimality. Default: none, required.
2. **Terminals** — nonempty set of required node IDs. Why: the tree need only connect these nodes. Default: none, required.
3. **Weight contract** — exact nonnegative integer costs in one additive unit. Why: the reference's tree objective and comparisons depend on that contract. Default: none, required.
4. **Eligibility** — undirected edge projection and excluded links. Why: eligibility changes feasibility. Default: all supplied edges eligible; mandatory links require an extension.
5. **Search cap** — maximum edge subsets to inspect. Why: completed and stopped searches support different conclusions. Default: state a finite cap before running.
6. **Use boundary** — analysis, proposal or operational plan. Why: a structural cost optimum is not a safety or construction approval. Default: analysis only.

If a required input is missing without a safe default, ask in one message with at most three questions. Preserve every original edge ID, including parallel links and loops.

## Procedure
1. Freeze snapshot, undirected interpretation, terminal IDs, eligible edges and exact cost unit.
2. Validate unique nonempty node and edge IDs, known endpoints, nonempty terminals and nonnegative integer weights. Reject missing or mixed units rather than assigning defaults.
3. Identify eligible non-loop edges for subset search. Keep loop IDs in an exclusion ledger; a loop cannot connect different terminals in a tree.
4. Enumerate candidate edge subsets in a deterministic order under the declared cap. Check each candidate for unique identities, no cycle, one connected selected component, and inclusion of every terminal.
5. For the one-terminal case, include the empty tree with cost zero. For several terminals, reject an empty candidate as disconnected.
6. Recompute each feasible candidate's cost from original edge records. Break equal-cost ties by fewer edges, then sorted edge IDs; do not call one tie unique without comparing alternatives.
7. Independently replay the chosen tree's edges and terminal reachability from the original inventory, and recompute its sum.
8. ⚠️ Claim exact optimality or infeasibility only after every candidate subset was inspected. If the cap stops enumeration, report the best feasible incumbent, if any, with optimum unknown.
9. Deliver selected IDs, connector nodes, cost, search coverage, any tied alternatives observed, and scope limits. An infeasible result refers only to the complete eligible snapshot.

This Python 3 reference exhaustively searches subsets of non-loop edges for a small finite graph. Costs are nonnegative integers. Its cap counts visited subsets, including the empty subset. It does not scale to large inputs and does not handle directed, negative-cost, capacity or reliability constraints. Run the entire snippet and record the interpreter version.

```python
from itertools import combinations

def solve(nodes, edges, terminals, cap):
    if type(cap) is not int or cap < 1:
        raise ValueError("positive subset cap required")
    if any(type(n) is not str or not n for n in nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("invalid or duplicate node")
    if any(type(e) not in (tuple, list) or len(e) != 4 or
           any(type(x) is not str or not x for x in e[:3]) or
           type(e[3]) is not int or e[3] < 0 for e in edges):
        raise ValueError("invalid edge or weight")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    known = set(nodes)
    if any(a not in known or b not in known for _, a, b, _ in edges):
        raise ValueError("unknown endpoint")
    if type(terminals) not in (set, frozenset) or not terminals or not terminals <= known:
        raise ValueError("nonempty known terminal set required")
    eligible = sorted((e for e in edges if e[1] != e[2]), key=lambda e: e[0])
    loops = sorted(e[0] for e in edges if e[1] == e[2])
    def inspect(selection):
        parent = {n: n for n in nodes}
        def root(n):
            while parent[n] != n:
                n = parent[n]
            return n
        used = set()
        for eid, a, b, _ in selection:
            ra, rb = root(a), root(b)
            if ra == rb:
                return None
            parent[ra] = rb
            used.update((a, b))
        if len(terminals) == 1 and not selection:
            return 0, set(terminals)
        if not selection or len({root(n) for n in used}) != 1:
            return None
        if any(root(t) != root(next(iter(used))) for t in terminals):
            return None
        return sum(e[3] for e in selection), used
    seen, best, ties = 0, None, []
    for size in range(len(eligible) + 1):
        for subset in combinations(eligible, size):
            if seen == cap:
                return {"status": "unknown", "visited": seen,
                        "best": best, "ties": ties, "loops": loops}
            seen += 1
            checked = inspect(subset)
            if checked is None:
                continue
            cost, used = checked
            ids = tuple(e[0] for e in subset)
            record = {"ids": ids, "cost": cost,
                      "connectors": tuple(sorted(used - terminals))}
            if best is None or (cost, len(ids), ids) < (
                    best["cost"], len(best["ids"]), best["ids"]):
                best = record
            if not ties or cost < ties[0]["cost"]:
                ties = [record]
            elif cost == ties[0]["cost"]:
                ties.append(record)
    if best is not None:
        selected = [e for e in eligible if e[0] in best["ids"]]
        adjacency = {n: set() for n in nodes}
        for _, a, b, _ in selected:
            adjacency[a].add(b)
            adjacency[b].add(a)
        start = min(terminals)
        reached, pending = {start}, [start]
        while pending:
            for other in adjacency[pending.pop()]:
                if other not in reached:
                    reached.add(other)
                    pending.append(other)
        used = set(terminals) if not selected else {
            n for _, a, b, _ in selected for n in (a, b)}
        assert terminals <= reached and reached == used
        assert len(selected) == len(used) - 1
        assert sum(e[3] for e in selected) == best["cost"]
    return {"status": "optimal" if best else "infeasible",
            "visited": seen, "best": best, "ties": ties, "loops": loops}

nodes = ["A", "B", "C", "D", "X"]
edges = [("ab", "A", "B", 2), ("bc", "B", "C", 2),
         ("bd", "B", "D", 2), ("ac", "A", "C", 5),
         ("cd", "C", "D", 5), ("ad", "A", "D", 5),
         ("bx", "B", "X", 1), ("loop", "A", "A", 0)]
result = solve(nodes, edges, {"A", "C", "D"}, 1000)
assert result["status"] == "optimal"
assert result["best"] == {"ids": ("ab", "bc", "bd"),
                          "cost": 6, "connectors": ("B",)}
assert result["loops"] == ["loop"]
assert solve(["A"], [], {"A"}, 1)["best"]["cost"] == 0
assert solve(nodes, edges, {"A", "C", "D"}, 1)["status"] == "unknown"
print("terminal tree, irrelevant node, loop, singleton and cutoff checked")
```

## Decision rules
- IF the terminal set is missing or contains an unknown ID THEN stop intake BECAUSE the target connectivity cannot be defined.
- IF weights are negative, missing or incomparable THEN reject this reference BECAUSE its nonnegative additive tree contract is not met.
- IF only one terminal exists THEN the empty tree is a valid zero-cost connector BECAUSE it is already connected to itself.
- IF all subsets are inspected and none connects the terminals THEN report infeasible for the scoped graph BECAUSE no eligible tree exists there.
- IF the cap stops search THEN report optimum unknown even with a feasible incumbent BECAUSE a cheaper unvisited subset may exist.
- IF a selected tree fails independent edge replay or cost summation THEN reject it BECAUSE the reported certificate does not match the source inventory.

## Output template
```text
Scope: <snapshot, undirected eligible graph, terminals, cost unit; max 3 lines>
Search: <subset cap, visited/total subsets, complete or cut off>
Selection: <edge IDs, connector nodes, total cost; or none>
Verification: <acyclic, one component, terminal coverage, recomputed sum>
Optimality: <proved minimum | infeasible | unknown; tie status if known>
Exclusions: <loop IDs and ineligible edges, or none>
Limits: <unexamined source/operational conditions; max 2 lines>
Next action: <one concrete step>
```

## Quality checklist
- [ ] Snapshot, terminal IDs, undirected eligibility and cost unit are fixed.
- [ ] Unique IDs, endpoints and integer weights are validated.
- [ ] Loops are excluded with IDs retained in the ledger.
- [ ] The selected edges form one acyclic terminal-containing component.
- [ ] Nonterminal connectors are named explicitly.
- [ ] Cost is recomputed from original edge records.
- [ ] Visited and total subset counts show whether search finished.
- [ ] A cutoff is labeled unknown rather than optimal.
- [ ] Ties are not described as unique without evidence.
- [ ] The certificate does not authorize physical implementation.

## Anti-patterns
- **Spanning everything**: including an unrelated node raises cost without helping terminals. Fix: optimize only terminal connectivity.
- **Path substitution**: a cheapest A-to-C route need not connect D. Fix: verify every terminal lies in the chosen tree.
- **Greedy optimum claim**: a cheap-looking tree is merely an incumbent after an incomplete search. Fix: complete enumeration or report unknown.
- **Cycle as connector**: positive-cost cycles add no terminal reachability to a tree. Fix: check acyclicity and reject cyclic candidates.
- **Silent loop inclusion**: a self-loop connects no distinct terminal. Fix: list it as excluded.
- **Semantic cost leap**: a numerical edge cost does not prove safe buildability. Fix: seek operational approval separately.

## Worked example
**Input:**
> Fictional Harbor graph S1 has A,B,C,D,X. Terminals are A,C,D. Undirected edges ab=2, bc=2, bd=2, ac=5, cd=5, ad=5, bx=1, and loop at A=0. Costs share one exact unit. Search all non-loop subsets.

**Output:**
```text
Scope: Fictional Harbor S1; undirected eligible inventory; terminals A,C,D; exact cost units.
Search: Cap 1000; visited 128/128 non-loop subsets; complete.
Selection: ab,bc,bd; connector B; total cost 6.
Verification: Three edges, no cycle, A/C/D connected through B; 2+2+2=6.
Optimality: Proved minimum for S1; one cost-6 tree observed.
Exclusions: loop; X and bx remain in inventory but are not selected.
Limits: The cost unit does not establish physical suitability.
Next action: Preserve the witness with S1 for owner review before operational use.
```

**Bad output:** "Use every node because this is a spanning tree." This fails because the task names only A,C,D as terminals and X need not be connected.

## Edge cases
- **Disconnected terminals**: complete search yields infeasible; an early cutoff yields unknown.
- **Equal-cost trees**: report all observed ties and avoid uniqueness claims; complete search establishes the tie set.
- **Parallel edges**: keep IDs distinct and enumerate them as separate subset choices.
- **Zero-cost loop**: exclude by ID because it adds no terminal connection.
- **Singleton terminal**: the empty tree is feasible with cost zero.
- **Invalid endpoint or signed negative weight**: reject input before search.

## Test case
**Input:**
> Fictional Harbor S1 has terminals A,C,D and edges ab=2, bc=2, bd=2, ac=5, cd=5, ad=5, bx=1, plus loop A-A=0; node X attaches by bx. Compare a complete cap of 1000 with cap 1.

**Assertions:**
1. Complete search selects ab,bc,bd for total 6 and names B as a connector.
2. It reports 128 of 128 non-loop subsets visited and independently checks terminal coverage and the sum.
3. It excludes loop by ID and does not require X to be connected.
4. Cap 1 reports optimum unknown, not proved minimum.
