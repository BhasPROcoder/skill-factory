Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-052
name: authorized-graph-traversal-exposure-check
domain: Graph Engineering Foundations
subdomain: Authorized graph query review
version: 1.0
description: Test whether a directed graph traversal returns only paths supported by a principal's explicit node and edge read grants under a frozen policy snapshot.
triggers: ["check graph traversal access", "filter graph paths by permissions", "audit hidden-node path leakage", "test graph query authorization", "compare visible results after hidden edge change", "verify path witnesses against grants"]
not_for: ["ordinary bounded traversal [GRF-006]", "graph evidence packet selection [GRF-021]", "role permission matrix [TSC-002]", "granting new access", "production side-channel certification"]
requires: []
risk_level: high
---

# Authorized Graph Traversal Exposure Check

## Purpose
Construct a permitted graph view before traversal and replay paths against explicit grants. Compare frozen graphs differing only in denied records to detect fixture-level result leaks. Other production channels remain untested.

## Inputs to collect
1. **Authorized context and jurisdiction** — system, owner, principal, review environment, applicable jurisdiction and policy revision. Why: permissions need current owner evidence. Default: none, required; never assume a rule.
2. **Frozen graph** — complete node IDs and directed edge triples. Why: missing records change paths. Default: none, required.
3. **Node grants** — exact readable node IDs. Why: denied intermediaries must remain hidden. Default: none, required.
4. **Edge grants** — exact readable edge IDs. Why: visible endpoints do not imply a visible edge. Default: none, required.
5. **Query contract** — seed, direction, fields and restrictions. Why: contracts change exposure. Default: outgoing reachability with path IDs, no cutoff for a small fixture.
6. **Comparison fixture** — two snapshots with equal authorized projections but different denied records. Why: tests visible-result stability. Default: no comparison claim without fixtures.

If a required input is missing without a safe default, ask in one message with at most three questions. Verify current policy and grants with the system owner before using the method on real access data: `[VERIFY: current organization authorization policy and target engine access documentation]`.

## Procedure
1. Freeze graph revision, policy revision, principal, granted node IDs, granted edge IDs and query fields together.
2. Validate unique nonempty graph IDs, three-field edge records, known endpoints, grant IDs from the graph inventory and a granted seed. Reject an unknown or invisible seed rather than returning a misleading empty result.
3. Construct the authorized node set from supplied grants only; do not infer access because a node is adjacent to a visible node.
4. Include an edge in the query view only if its ID is granted and both endpoints are granted. An edge grant alone cannot expose a denied endpoint.
5. Build directed adjacency from that view before traversal. ⚠️ Traversing the full graph and redacting hidden nodes afterward can still expose a downstream endpoint through a forbidden path.
6. Traverse from the granted seed under the exact direction and bound contract, storing a permitted edge-ID predecessor path for each returned node. The reference below uses outgoing reachability without a depth cutoff.
7. Independently replay every returned path from the original edge inventory. Check the seed, each edge grant, both endpoint grants, directed continuity and destination. Reject a returned node lacking a fully granted path.
8. Recompute the reachable node set directly from the authorized adjacency and compare it with the returned keys. Equal path counts alone do not prove equal identities.
9. In a second frozen fixture, change only denied records while preserving all granted nodes and granted edge records. Run the same query and compare the complete visible result mapping. Report a difference as a fixture failure; equal outputs support only the tested result fields and cases.
10. Deliver the tested scope, grant projection, path checks, comparison outcome and untested channels. Route any suspected production leak or disputed policy to the responsible security professional; do not probe systems beyond authorization.

This Python 3 reference uses a finite in-memory directed graph with string IDs and one explicit grant set per identity kind. Its result is a node-to-edge-path mapping. It does not implement authentication, tenant policy inheritance, timing/error side channels, caches, pagination or remote enforcement. Run the whole snippet and record the interpreter used. Adapt only after verifying the target's current access behavior in official documentation and owner policy.

```python
from collections import deque

def visible_paths(nodes, edges, seed, node_grants, edge_grants):
    if type(nodes) not in (list, tuple) or any(
            type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node inventory")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    if type(edges) not in (list, tuple) or any(
            type(e) not in (tuple, list) or len(e) != 3 or
            any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge record")
    edge_ids = {eid for eid, _, _ in edges}
    if len(edge_ids) != len(edges):
        raise ValueError("duplicate edge ID")
    node_ids = set(nodes)
    if any(a not in node_ids or b not in node_ids for _, a, b in edges):
        raise ValueError("unknown endpoint")
    if type(node_grants) not in (set, frozenset) or type(edge_grants) not in (set, frozenset):
        raise ValueError("grant sets required")
    if not node_grants <= node_ids or not edge_grants <= edge_ids:
        raise ValueError("unknown grant ID")
    if seed not in node_grants:
        raise ValueError("invisible seed")
    adjacency = {n: [] for n in node_grants}
    for eid, a, b in edges:
        if eid in edge_grants and a in node_grants and b in node_grants:
            adjacency[a].append((eid, b))
    paths, todo = {seed: ()}, deque([seed])
    while todo:
        node = todo.popleft()
        for eid, other in sorted(adjacency[node]):
            if other not in paths:
                paths[other] = paths[node] + (eid,)
                todo.append(other)
    by_id = {eid: (a, b) for eid, a, b in edges}
    for target, route in paths.items():
        cursor = seed
        for eid in route:
            a, b = by_id[eid]
            assert eid in edge_grants and a in node_grants and b in node_grants
            assert a == cursor
            cursor = b
        assert cursor == target
    reached, pending = {seed}, [seed]
    while pending:
        for _, other in adjacency[pending.pop()]:
            if other not in reached:
                reached.add(other)
                pending.append(other)
    assert set(paths) == reached
    return paths

nodes = ["A", "B", "C", "H"]
edges = [("ab", "A", "B"), ("ah", "A", "H"),
         ("hc", "H", "C"), ("bc", "B", "C")]
granted_nodes, granted_edges = {"A", "B", "C"}, {"ab"}
first = visible_paths(nodes, edges, "A", granted_nodes, granted_edges)
assert first == {"A": (), "B": ("ab",)}
assert visible_paths(nodes, edges + [("bh", "B", "H")], "A",
                     granted_nodes, granted_edges) == first
assert visible_paths(nodes, edges, "A", granted_nodes,
                     {"ab", "bc"})["C"] == ("ab", "bc")
assert "C" in visible_paths(nodes, edges, "A", set(nodes),
                            {e[0] for e in edges})
print("granted paths, denied edge and hidden-record comparison checked")
```

## Decision rules
- IF current owner-approved grants or policy context are missing THEN stop the access verdict BECAUSE graph topology cannot confer permission.
- IF the seed is invisible or a grant ID is unknown THEN reject the request BECAUSE an empty path answer could hide an invalid access contract.
- IF a path uses a denied node or edge THEN reject the returned result BECAUSE every hop must be authorized under the supplied policy.
- IF visible endpoints are connected only through denied records THEN omit that endpoint from this query's reachable result BECAUSE the path cannot be disclosed.
- IF two fixtures have identical authorized projections but different outputs THEN flag a tested output leak BECAUSE denied records altered a visible answer.
- IF outputs match THEN report only fixture-level result parity BECAUSE timing, errors, caches and other channels remain untested.

## Output template
```text
Scope: <system, principal, graph/policy revisions, authorized review boundary>
Query: <seed, direction, bound and visible result fields>
Projection: <granted node/edge counts and exact IDs or protected ledger reference>
Visible result: <node ID -> permitted edge-ID path, or no result>
Verification: <grant replay and reached-set equality; pass/fail/pending>
Hidden-change comparison: <fixture pair and exact visible-map equality or difference>
Decision: <fixture passed | failure | unresolved>
Limits: <untested channels and current-policy verification; max 2 lines>
Next action: <one owner or security-review step>
```

## Quality checklist
- [ ] Principal, system, graph revision and policy revision are named.
- [ ] Grant sets came from owner-approved current evidence.
- [ ] Node/edge identities and endpoints are validated.
- [ ] The seed is granted and every returned node has a granted path.
- [ ] Every path edge ID is granted and directionally continuous.
- [ ] The authorized view was built before traversal.
- [ ] Returned node keys equal independently reached authorized nodes.
- [ ] Hidden-change fixtures preserve the authorized projection.
- [ ] Comparison claims cover only tested result fields and fixtures.
- [ ] Suspected real leaks are routed to the responsible professional.

## Anti-patterns
- **Traverse then redact**: a hidden intermediary can still expose a downstream node. Fix: filter graph records before traversal.
- **Endpoint-only permission**: visible endpoints do not make their edge visible. Fix: require the edge ID grant too.
- **Implicit neighbor grant**: adjacency does not confer access. Fix: use only supplied policy grants.
- **Empty answer for bad seed**: this masks a contract error. Fix: reject invisible or unknown seeds.
- **Broad security claim**: matching fixture outputs does not test timing or caches. Fix: name the tested channel and limits.
- **Unapproved probing**: running tests against an unauthorized system is outside scope. Fix: use an owner-approved isolated fixture.

## Worked example
**Input:**
> Fictional Harbor system S1 has A→B (`ab`), A→H (`ah`), H→C (`hc`), and B→C (`bc`). Owner-approved P1 grants principal P nodes A,B,C and edge ab only. Query outgoing reachability from A. In S2 add denied edge B→H (`bh`) without changing grants.

**Output:**
```text
Scope: Fictional Harbor; principal P; graph S1/S2 and policy P1; isolated authorized fixture.
Query: Seed A; outgoing; no depth cutoff; node IDs and edge-ID paths.
Projection: Granted nodes A,B,C; granted edge ab.
Visible result: A -> empty path; B -> ab. C absent.
Verification: Both paths replay against grants; authorized reached set is {A,B}.
Hidden-change comparison: S1 and S2 visible maps equal, {A:(), B:(ab)}.
Decision: Fixture passed.
Limits: No timing, error, cache or production enforcement tested; verify current owner policy.
Next action: Ask the security owner to review this fixture before target-engine adaptation.
```

**Bad output:** "C is reachable because A→H→C exists; hide H in the display." This fails because H and its edges are denied, so the path itself is unauthorized.

## Edge cases
- **Invisible seed**: reject instead of returning an empty map.
- **Visible endpoints, denied edge**: omit the path until that edge ID is granted.
- **Hidden intermediary**: do not reach a visible downstream node through it.
- **Parallel edges**: keep IDs separate; only granted identities enter adjacency.
- **Unknown grant ID or malformed record**: reject before traversal.
- **Changed permitted projection**: do not call it a hidden-only comparison; record a different test.

## Test case
**Input:**
> Fictional Harbor P1 grants A,B,C and edge ab. S1 contains ab A→B, ah A→H, hc H→C, and denied bc B→C; S2 adds denied bh B→H. Query from A, then test an invisible H seed and an unknown edge grant.

**Assertions:**
1. Both S1 and S2 return exactly A and B with the permitted path ab to B; C is absent.
2. Every returned path edge and endpoint is replayed against P1 grants.
3. The hidden-edge change leaves the complete visible result map equal in this fixture.
4. Invisible H seed and unknown edge grant are rejected, not reported as ordinary empty results.
5. The result does not claim production-wide noninterference or current policy without owner verification.
</skill>

<user_request>
Fictional Harbor P1 grants A,B,C and edge ab. S1 contains ab A→B, ah A→H, hc H→C, and denied bc B→C; S2 adds denied bh B→H. Query from A, then test an invisible H seed and an unknown edge grant.
</user_request>
