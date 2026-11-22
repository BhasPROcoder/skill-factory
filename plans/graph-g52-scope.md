# GRF-052 candidate: authorization-filtered graph reachability review

Status: discovery card only. No skill, manifest or registry entry. Security-sensitive scope; an author must review current organization policy and any target engine documentation before adapting the offline method.

## Distinct deliverable

Given a principal, a frozen directed graph, explicit node and edge read grants, and a seed visible to that principal, construct the principal's **authorized subgraph before traversal**. Return reachable visible node IDs and permitted edge-ID path witnesses. Compare a hidden-edge mutation fixture to check that the visible answer is unchanged when only denied records differ. A path that passes through a denied node or denied edge must not make its downstream endpoint appear reachable merely because that endpoint itself is visible.

This is a bounded, offline output-equivalence check over the supplied fixture. It does not certify timing, error-message, cache, count, or other production side-channel behavior. No permission is inferred from topology; explicit grants and the organization’s current policy are inputs.

## Overlap check

- GRF-006's actual Procedure provides directed, relation-filtered bounded traversal and says node exclusions need separate adaptation. It does not define per-principal grants, filter edges and nodes before path search, or test hidden-record noninterference.
- GRF-021's actual Procedure builds evidence packets from paths and passages; it does not enforce read grants at every intermediate node/edge.
- TSC-002's actual Procedure compares role actions with effective grants. It does not calculate graph path exposure under node/edge grants.
- `sf.py search 'authorization traversal'` returned GRF-006 and unrelated security charter/matrix entries; `permission path` returned GRF-021/030 and TSC-002, none with the specified authorized-subgraph result.

If deeper comparison finds an existing skill already computes this principal-specific subgraph and hidden-edge output comparison, reject the candidate. The distinct decision is whether a graph query's *returned path and endpoint set* is supported entirely by granted graph records, not whether a user should be granted access.

## Executable acceptance fixture

Fictional snapshot S: nodes A,B,C,H, directed edges `ab: A→B`, `ah: A→H`, `hc: H→C`. Principal P can read A,B,C and edge ab, but cannot read H, ah or hc. From A, the authorized result must include A,B and path ab; C is absent even though C itself is visible, because its only path passes through denied records. A naive full-graph traversal followed by redacting H would incorrectly reveal C.

Add a second hidden edge `bh: B→H` in a separate hypothetical snapshot while leaving the permitted projection unchanged. P's returned node IDs and paths must remain identical. A privileged principal allowed all nodes and edges can reach C. Reject an invisible seed and unknown grant IDs rather than producing a misleading empty answer.

```python
from collections import deque

def visible_paths(nodes, edges, seed, node_grants, edge_grants):
    node_ids = set(nodes)
    edge_ids = {eid for eid, _, _ in edges}
    if len(node_ids) != len(nodes) or len(edge_ids) != len(edges):
        raise ValueError("duplicate graph identity")
    if any(a not in node_ids or b not in node_ids for _, a, b in edges):
        raise ValueError("unknown endpoint")
    if not node_grants <= node_ids or not edge_grants <= edge_ids:
        raise ValueError("unknown grant identity")
    if seed not in node_grants:
        raise ValueError("seed not visible")
    adjacency = {n: [] for n in node_grants}
    for eid, a, b in edges:
        if eid in edge_grants and a in node_grants and b in node_grants:
            adjacency[a].append((eid, b))
    result = {seed: ()}
    todo = deque([seed])
    while todo:
        node = todo.popleft()
        for eid, other in sorted(adjacency[node]):
            if other not in result:
                result[other] = result[node] + (eid,)
                todo.append(other)
    by_id = {eid: (a, b) for eid, a, b in edges}
    for destination, route in result.items():
        cursor = seed
        for eid in route:
            a, b = by_id[eid]
            assert eid in edge_grants and a in node_grants and b in node_grants
            assert a == cursor
            cursor = b
        assert cursor == destination
    return result

nodes = ["A", "B", "C", "H"]
edges = [("ab", "A", "B"), ("ah", "A", "H"), ("hc", "H", "C")]
allowed_nodes, allowed_edges = {"A", "B", "C"}, {"ab"}
first = visible_paths(nodes, edges, "A", allowed_nodes, allowed_edges)
assert first == {"A": (), "B": ("ab",)}
changed_hidden = edges + [("bh", "B", "H")]
assert visible_paths(nodes, changed_hidden, "A", allowed_nodes,
                     allowed_edges) == first
assert "C" in visible_paths(nodes, edges, "A", set(nodes),
                            {e[0] for e in edges})
try:
    visible_paths(nodes, edges, "H", allowed_nodes, allowed_edges)
except ValueError:
    pass
else:
    raise AssertionError("invisible seed accepted")
print("authorized path and hidden-edge fixture checks passed")
```

Before authoring, add a case where both endpoints are visible but the edge ID is denied, plus malformed record and boundary tests. The code is a candidate fixture, not an accepted implementation or production authorization mechanism.

## Accuracy boundary

All entities and grants above are fictional. No current platform access rule, law, API or performance claim is asserted. For an actual product, `[VERIFY: current organization authorization policy, graph query engine behavior, cache scope and official engine documentation]`. A fixture result cannot prove full noninterference across production responses or channels.
