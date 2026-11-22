Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-029
name: graph-single-failure-connectivity-witnesses
domain: Graph Engineering Foundations
subdomain: Removal sensitivity
version: 1.0
description: Identify newly disconnected surviving node pairs after one declared vertex or edge removal when reviewing structural single-failure consequences in an undirected multigraph.
triggers: ["find single failure graph connectors", "test edge removal connectivity", "test node removal connectivity", "check parallel edge resilience", "explain articulation consequences"]
not_for: ["partitioning an unchanged graph [GRF-007]", "directed strong components [GRF-008]", "flow capacity certification [GRF-010]", "estimating physical failure probability", "simulating simultaneous failures"]
requires: []
risk_level: medium
---

# Graph Single Failure Connectivity Witnesses

## Purpose
Produce a removal ledger showing which surviving node pairs lose connectivity after each specified single failure. Preserve the unchanged baseline and identify witnesses for the new separation. This evaluates a supplied topology, not physical reliability, service capacity or failure likelihood.

## Inputs to collect
1. **Graph snapshot** — collect complete node IDs and separately identified edges with endpoints. Why: parallel edges and isolated nodes affect removal consequences. Default: none; require the scoped inventory.
2. **Connectivity semantics** — confirm undirected connectivity and any relation filters. Why: directional reachability answers a different question. Default: unresolved; never silently discard arrows.
3. **Failure inventory** — list exact node IDs or edge IDs to remove one at a time. Why: removing one edge differs from removing all relationships between its endpoints. Default: propose all supplied nodes and edges, pending scope agreement.
4. **Population rule** — state which surviving pairs matter and any service priorities. Why: counting the removed node as disconnected inflates vertex impact. Default: all unordered pairs of surviving nodes that were connected before removal.
5. **Evidence coverage** — identify snapshot revision and omitted material. Why: unseen alternative routes can invalidate global conclusions. Default: conclusions apply only to the supplied graph.
6. **Execution bounds** — obtain available runtime and practical input limit. Why: repeated exhaustive traversal is intended for small fixtures. Default: explain the reference approach; do not claim execution or full completion without observed results.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the graph revision, undirected interpretation, relation filter and failure inventory.
2. Validate unique node and edge IDs and known endpoints before assessing consequences.
3. Compute baseline reachability over every supplied node, including isolated nodes.
4. For each requested failure, create a separate hypothetical graph from the unchanged baseline.
5. Remove exactly the named edge, or remove the named vertex together with all its incident edges.
6. ⚠️ Restrict the comparison population to surviving nodes; compare their original connectivity instead of charging the failed vertex itself as a newly separated pair.
7. Compute exhaustive reachability in the hypothetical graph without a depth cutoff.
8. Enumerate previously connected surviving pairs that are now disconnected, retaining pair identities and the failure responsible.
9. Record one separated pair and the two resulting reachable sets as an inspectable witness for every failure with impact.
10. Verify each witness against the same removed-object snapshot and retain all unaffected or originally disconnected pairs outside the new-loss count.
11. Deliver the removal ledger with coverage limits and proposed follow-up; do not alter the real graph or infer failure probabilities from topology alone.

This Python 3 reference accepts finite lists of string node IDs and edge tuples `(edge_ID, endpoint_A, endpoint_B)`. Prevalidate tuple shapes and string identifiers. Every edge is undirected; multiplicity is represented by distinct edge IDs. Execute the snippet and record the installed interpreter version. It computes all newly lost pairs for one failure at a time; it is an inspectable small-graph method rather than a scalable production solver.

```python
def reach(nodes, edges):
    adj = {n: set() for n in nodes}
    for eid, a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    out = {}
    for root in nodes:
        seen, todo = {root}, [root]
        while todo:
            for nxt in adj[todo.pop()]:
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
        out[root] = seen
    return out

def removal(nodes, edges, kind, identity):
    if len(set(nodes)) != len(nodes) or len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate identity")
    if any(a not in nodes or b not in nodes for _, a, b in edges):
        raise ValueError("unknown endpoint")
    if kind not in {"node", "edge"}:
        raise ValueError("unknown failure kind")
    ids = set(nodes) if kind == "node" else {e[0] for e in edges}
    if identity not in ids:
        raise ValueError("unknown failed object")
    baseline = reach(nodes, edges)
    survivors = [n for n in nodes if not (kind == "node" and n == identity)]
    kept = [e for e in edges if not
            ((kind == "edge" and e[0] == identity) or
             (kind == "node" and identity in e[1:]))]
    after = reach(survivors, kept)
    pairs = [(a, b) for i, a in enumerate(sorted(survivors))
             for b in sorted(survivors)[i+1:]
             if b in baseline[a] and b not in after[a]]
    witness = None if not pairs else (pairs[0], sorted(after[pairs[0][0]]),
                                     sorted(after[pairs[0][1]]))
    return pairs, witness

nodes = ["A", "B", "C", "I"]
edges = [("e1", "A", "B"), ("e2", "A", "B"),
         ("e3", "B", "C"), ("loop", "B", "B")]
assert removal(nodes, edges, "edge", "e1")[0] == []
assert removal(nodes, edges, "edge", "e3")[0] == [("A", "C"), ("B", "C")]
assert removal(nodes, edges, "node", "B")[0] == [("A", "C")]
assert removal(nodes, edges, "edge", "loop")[0] == []
print("parallel edge, node population and disconnected baseline checked")
```

Adjacency sets collapse parallel neighbors only after the selected edge has been removed by ID, so a surviving parallel edge still preserves adjacency. Isolated I was already disconnected and never enters the new-loss ledger. The witness sets establish separation inside the supplied hypothetical graph; they do not prove that a real service has no alternative network, cache or recovery mechanism.

## Decision rules
- IF removing an edge leaves a parallel connection THEN retain that surviving connection BECAUSE one failed edge does not erase another identified edge.
- IF a pair was already disconnected THEN exclude it from new loss BECAUSE the specified failure did not cause that separation.
- IF a vertex is removed THEN exclude that vertex from pair comparisons BECAUSE the target measure concerns surviving nodes.
- IF connectivity semantics are directed THEN stop this reference computation BECAUSE undirected projection would change the question.
- IF execution stops before all requested failures finish THEN report completed failures and remaining work BECAUSE a partial scan cannot establish absence of critical connectors.

## Output template
```text
Scope: <snapshot, connectivity semantics, coverage; maximum 60 words>
Failures: <object kind/ID | completed/pending>
Loss ledger: <failure | newly lost surviving pairs | count>
Witnesses: <failure | separated pair | reachable sets or none>
Checks: <executed fixture/input checks and pending real checks; maximum 70 words>
Decision: <bounded consequences and next action; maximum 80 words>
```

## Quality checklist
- [ ] Node and edge identities are validated separately.
- [ ] Undirected semantics and graph scope are explicit.
- [ ] Each failure starts from the unchanged baseline.
- [ ] Parallel edges retain distinct failure identities.
- [ ] Removed vertices do not enter surviving-pair counts.
- [ ] Previously disconnected pairs are excluded from new losses.
- [ ] Each reported impact includes a reproducible separation witness.
- [ ] Physical reliability and incomplete execution remain outside conclusions.

## Anti-patterns
- **Endpoint deletion**: remove every parallel edge after one edge fails. Fix: delete the exact edge ID.
- **Failed-node inflation**: count every pair containing a removed vertex. Fix: compare surviving nodes only.
- **Baseline blindness**: blame all disconnected pairs on the new failure. Fix: retain original reachability.
- **Capacity substitution**: interpret connectivity as throughput adequacy. Fix: assess capacity separately.
- **Probability invention**: assign failure risk from connector status. Fix: require an appropriate empirical model for probabilistic claims.

## Worked example
**Input:** Fictional fixture above requests separate removals of e1, e3 and B. All edges are undirected and the supplied inventory is complete for this exercise.

**Output:**
```text
Scope: Fictional fixture; undirected connectivity; supplied A/B/C/I inventory only.
Failures: edge e1 | pending; edge e3 | pending; node B | pending; expected outcomes below.
Loss ledger: e1 | none | 0; e3 | A-C,B-C | 2; B | A-C | 1.
Witnesses: e1 none; e3 | A-C | {A,B} and {C}; B | A-C | {A} and {C}.
Checks: Execute the reference to confirm these expected results; actual service and physical reliability checks remain pending.
Decision: e3 and B cause new separation in their separate hypothetical removals. e1 retains e2. I remains outside new-loss pairs because it was already isolated.
```

**Bad output:** “Deleting e1 disconnects A from B and deleting B loses its connections to every node, including I.”
This erases a surviving parallel edge and mixes failed-node pairs with baseline disconnection.

## Edge cases
- **Self-loop removal**: evaluate it normally; it does not connect distinct nodes in this model.
- **No edges**: report no newly lost surviving connectivity for node removals; preserve the scoped inventory.
- **Simultaneous failure request**: require a separate joint-failure contract; single-failure results cannot simply be added.
- **Incomplete inventory**: label every separation as scoped; do not claim a global connector.
- **Unknown object requested**: reject that case explicitly rather than silently evaluating no removal.

## Test case
**Input:**
> Fictional A/B have two parallel undirected edges. B/C have one edge. I is isolated. Compare removal of one A/B edge with removal of B, counting only new separation among survivors.

**Assertions:**
1. Reports no lost pair from removing one parallel A/B edge.
2. Reports A-C as the lost surviving pair after removing B.
3. Does not count pairs involving removed B or previously isolated I as new losses.
4. Makes no physical failure probability or throughput claim.
</skill>

<user_request>
Fictional A/B have two parallel undirected edges. B/C have one edge. I is isolated. Compare removal of one A/B edge with removal of B, counting only new separation among survivors.
</user_request>
