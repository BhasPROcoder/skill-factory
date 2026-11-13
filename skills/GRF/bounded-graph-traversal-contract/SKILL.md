---
id: GRF-006
name: bounded-graph-traversal-contract
domain: Graph Engineering Foundations
subdomain: Traversal boundaries
version: 1.0
description: Execute a reproducible bounded graph traversal with explicit direction, relation filters and minimum-hop semantics while distinguishing depth-limited results from exhausted reachability.
triggers: ["define graph traversal boundaries", "find nodes within this many hops", "explain truncated graph traversal", "traverse incoming versus outgoing relationships", "check graph traversal termination"]
not_for: ["finding prerequisite cycles [SEQ-001]", "validating rooted forests [GRF-004]", "planning dataset withdrawal actions [TDS-012]", "weighted shortest paths or all-path enumeration"]
requires: []
risk_level: medium
---

# Bounded Graph Traversal Contract

## Purpose
Return the nodes reachable within a declared hop limit, with minimum-hop distances and one reproducible witness per reached node. Separate a complete bounded result from an exhausted reachable region, and distinguish both from an interrupted or incompletely observed search. The method answers graph reachability, not whether an indirect relationship is a valid domain inference.

## Inputs to collect
1. **Snapshot and coverage** — collect node inventory, edge IDs, endpoints, relation labels and revision. Why: missing edges can hide reachable nodes. Default: supplied snapshot only; external completeness unknown.
2. **Seed identity** — obtain exact node ID or an evidenced resolution from a label. Why: a name may identify several nodes. Default: ask; never choose the first text match.
3. **Traversal meaning** — specify outgoing, incoming or either-direction steps, allowed relation labels and any node exclusions. Why: direction and filters change the reachable region. Default: no inferred direction or relation set.
4. **Distance and limit** — obtain a nonnegative maximum number of edges traversed; distinguish this from weighted cost or path count. Why: depth means different things in different tasks. Default: ask rather than invent a cutoff.
5. **Operational budget** — obtain time, fetched-page or memory limits if applicable. Why: an interrupted search cannot claim completion at the requested depth. Default: offline reference has no separate resource cap; stop safely and report interruption if execution cannot finish.
6. **Requested evidence** — clarify whether one witness per node suffices. Why: a visited-node traversal does not enumerate every route. Default: reached-node table, minimum-hop distances, one witness and frontier evidence only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the snapshot and resolve the seed to a unique inventory ID, retaining any identity ambiguity as an intake blocker.
2. Write the traversal contract: direction, allowed relations, node exclusions, hop definition and requested bound.
3. Validate identities and endpoints, then construct traversal adjacency from the approved filters without altering the source graph.
4. Initialize the seed at distance zero with no predecessor and place it in a first-in, first-out queue.
5. Expand queued nodes in distance order until the queue empties, recording each newly discovered node once with its distance and predecessor edge.
6. ⚠️ Do not expand nodes at the maximum depth. Retain them as the boundary layer; expanding them would silently exceed the contract.
7. Check eligible neighbors of the boundary layer against the final reached set to identify concrete exits to unreached nodes, when complete adjacency is available.
8. Distinguish bounded completion, exhausted reachability and operational interruption. A nonempty boundary layer alone does not prove omitted nodes: its edges may return only to already reached nodes.
9. Reconstruct each witness using predecessor records and check that direction, relation eligibility and path length agree with the contract.
10. Deliver the reached table and stopping evidence with snapshot limitations. Do not describe excluded or unobserved nodes as globally unreachable.

This Python 3 reference uses a finite in-memory graph with string IDs and edges `(edge_id, source, target, relation)`. Run the full snippet and record the installed interpreter version. It permits loops and parallel edges, has no resource cap, and requires prevalidated tuple shapes and string fields. It does not implement node exclusions, remote pagination, weighted costs or path-dependent permissions; apply those requirements explicitly before adapting it.

```python
from collections import deque

def traverse(nodes, edges, seed, labels, direction, depth):
    if type(depth) is not int or depth < 0:
        raise ValueError("nonnegative integer depth required")
    if direction not in ("out", "in", "both"):
        raise ValueError("explicit direction required")
    known = set(nodes)
    if len(known) != len(nodes) or seed not in known:
        raise ValueError("unique inventory and known seed required")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("unique edge identities required")
    adj = {n: [] for n in nodes}
    for eid, source, target, label in sorted(edges):
        if source not in known or target not in known:
            raise ValueError("unknown endpoint")
        if label in labels:
            if direction in ("out", "both"):
                adj[source].append((target, eid))
            if direction in ("in", "both"):
                adj[target].append((source, eid))
    distance, parent = {seed: 0}, {seed: None}
    queue = deque([seed])
    while queue:
        node = queue.popleft()
        if distance[node] == depth:
            continue
        for neighbor, eid in adj[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                parent[neighbor] = (node, eid)
                queue.append(neighbor)
    exits = sorted({(node, eid, neighbor)
                    for node in distance if distance[node] == depth
                    for neighbor, eid in adj[node]
                    if neighbor not in distance})
    return distance, parent, exits

nodes = ["A", "B", "C", "D", "X"]
edges = [("e1", "A", "B", "link"),
         ("e2", "B", "A", "link"),
         ("e3", "B", "C", "link"),
         ("e4", "C", "D", "link"),
         ("e5", "A", "X", "note")]
d, p, exits = traverse(nodes, edges, "A", {"link"}, "out", 2)
assert d == {"A": 0, "B": 1, "C": 2}
assert p["C"] == ("B", "e3")
assert exits == [("C", "e4", "D")]
assert traverse(nodes, edges, "A", {"link"}, "out", 3)[2] == []
assert traverse(nodes, edges, "A", {"link"}, "out", 0)[0] == {"A": 0}
print("bounded, exhausted and zero-depth checks passed")
```

## Decision rules
- IF the request means minimum edge count THEN use distance-ordered discovery BECAUSE a depth-first first visit may follow a longer route.
- IF an eligible boundary exit reaches an undiscovered node THEN report depth truncation BECAUSE at least one additional reachable node lies beyond the bound.
- IF execution finishes and no eligible exit exists under complete adjacency THEN report exhausted reachability within the filtered snapshot BECAUSE no reached node can lead to an unreached node.
- IF a fetch fails or a resource budget interrupts expansion THEN report incomplete execution BECAUSE requested depth is not proof that all nodes within it were examined.
- IF eligibility depends on path history THEN redesign the visited-state key before execution BECAUSE marking only the node visited can discard a distinct permitted state.

## Output template
```text
Scope: <snapshot, coverage and seed; maximum 70 words>
Contract: <direction, relations, exclusions, hop bound and evidence type>
Reached: <node | minimum hops | predecessor node/edge; complete table>
Boundary: <nodes at bound and eligible exits, or unavailable>
Stopping: <bounded complete / interrupted; exhausted / depth-truncated / unknown>
Witness checks: <executed checks and results or pending; maximum 80 words>
Limits: <excluded meanings, coverage gaps and unperformed checks; maximum 80 words>
```

## Quality checklist
- [ ] Seed identity and snapshot are explicit.
- [ ] Direction and relation filters are declared before execution.
- [ ] Seed distance is zero and distances count edges.
- [ ] Each reached non-seed node has a valid predecessor witness.
- [ ] Loops terminate without discarding legitimate reachable nodes.
- [ ] Boundary membership is separate from evidence of omitted nodes.
- [ ] Execution interruption cannot be mistaken for bounded completion.
- [ ] Exhaustion claims are limited to the filtered observed graph.

## Anti-patterns
- **Arrow guessing**: reverse relations to match an expected answer. Fix: obtain the required direction first.
- **Depth-first distance**: treat first discovery along any route as shortest. Fix: process by increasing hop count.
- **Boundary means truncation**: infer omission from a node at the limit. Fix: check exits to unreached nodes.
- **Visited means all paths**: present one witness as every route. Fix: state the node-reachability evidence scope.
- **Filter disappears**: call an excluded node globally unreachable. Fix: include the filter in the conclusion.

## Worked example
**Input:** Fictional team Finch supplies the snippet snapshot F1, complete for its fixture. Start at A, follow outgoing link edges up to two hops; note edges are excluded. One witness per node suffices.

**Output:**
```text
Scope: Finch F1 complete fictional fixture; seed A.
Contract: Outgoing link only; no node exclusions; two-edge bound; one witness per reached node.
Reached: A | 0 | none; B | 1 | A/e1; C | 2 | B/e3.
Boundary: C; eligible exit C/e4/D reaches an unreached node.
Stopping: Bounded complete; depth-truncated within filtered F1.
Witness checks: Reference assertions check A/B/C distances and C's predecessor when executed; A-e1-B-e3-C is a two-edge witness.
Limits: D lies beyond this bound. X is excluded by the relation filter, not proved globally unreachable. No remote service or all-path enumeration tested.
```

**Bad output:** “A, B and C are the whole connected graph; X and D cannot be reached.”
This conceals a known boundary exit and turns a relation filter into a global absence claim.

## Edge cases
- **Zero depth**: return the seed alone; inspect its eligible exits only to explain the stopping boundary.
- **Boundary with only return edges**: report no unseen-node exit, not truncation merely because the boundary is nonempty.
- **Parallel edges**: retain source identities; one deterministic witness is sufficient for node reachability, not an edge inventory.
- **Partial remote page**: preserve observed nodes but mark execution incomplete until all required adjacency pages are resolved.
- **Stateful traversal**: include relevant permission or path state in visited keys and revalidate termination; the reference is insufficient.

## Test case
**Input:**
> Fictional complete graph has link edges a:P→Q, b:Q→P and c:Q→R. Traverse outgoing link from P with depth one, then compare depth two. No weighted costs or all-path output requested.

**Assertions:**
1. Depth one returns P at zero and Q at one, with Q/c/R as an unseen-node exit.
2. Depth two also returns R at two and reports exhaustion within the filtered snapshot.
3. The cycle P→Q→P does not cause repeated expansion or infinite execution.
4. The result distinguishes a node witness from all possible paths and makes no live-service claim.
