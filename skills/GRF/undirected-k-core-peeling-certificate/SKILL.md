---
id: GRF-037
name: undirected-k-core-peeling-certificate
domain: Graph Engineering Foundations
subdomain: Degree-constrained subgraphs
version: 1.0
description: Derive and verify the maximal vertex-induced subgraph with minimum degree at least a supplied threshold when an undirected graph needs a reproducible k-core certificate.
triggers: ["find the k-core of this graph", "peel low-degree vertices", "show why nodes left the core", "verify a degree-threshold subgraph", "compare core membership after an edge change"]
not_for: ["weak component membership [GRF-007]", "comparing supplied community labels [GRF-013]", "single-failure connectivity [GRF-029]", "inferring the importance or identity of a person from degree"]
requires: []
risk_level: medium
---

# Undirected K-Core Peeling Certificate

## Purpose
Compute a vertex-induced subgraph in which every retained vertex has at least k distinct retained neighbors. Provide a replayable removal ledger so the maximal result can be checked from the original inventory. This structural filter is not a community detector or a judgment about the value of any entity.

## Inputs to collect
1. **Graph snapshot** — obtain unique node IDs, edge IDs, endpoints and source revision, including isolates. Why: an edge-only inventory omits vertices that may be removed immediately. Default: no complete claim without the node inventory.
2. **Undirected projection** — confirm that selected edges should be interpreted without direction and state any relation or time filters. Why: an unapproved projection changes degrees. Default: ask rather than silently discard arrows.
3. **Degree policy** — specify how parallel edges and loops count. Why: a multigraph degree convention may differ from distinct-neighbor degree. Default for this reference: collapse parallel edges to one neighbor and ignore self-loops for degree; show both in the source ledger.
4. **Threshold k** — obtain a nonnegative integer. Why: an arbitrary threshold changes the returned set. Default: none; do not choose one for the user.
5. **Coverage and use** — identify missing records, expected scale and the decision to be informed. Why: an unseen edge can change survival. Default: conclusions apply to the supplied projection only; no semantic rank or real-world action.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the node inventory, edge list, projection and k as a named snapshot.
2. Validate unique nonempty node and edge IDs, known endpoints and a nonnegative integer k before building adjacency.
3. Materialize one undirected adjacency set per node from nonloop edges, retaining the original parallel and loop records in an evidence ledger.
4. Initialize the retained set to all inventory nodes, including isolates.
5. Calculate each retained vertex's number of distinct neighbors still retained.
6. Remove every vertex with degree below k in a simultaneous round; record the round and each pre-removal degree.
7. Repeat degree calculation and removal until a round removes no vertices. ⚠️ Do not stop after one round: deleting leaves can make their former neighbors fall below k.
8. Verify that every survivor has degree at least k within the final induced subgraph.
9. Replay each removal round from the full starting set, checking each listed vertex's degree is below k immediately before its round. Recompute the complete low-degree set for each simultaneous round; reject omitted or extra removals.
10. Check that no unremoved low-degree vertex remains. A complete valid peeling ledger and final degree check certify the maximal fixed point under this graph and counting policy.
11. Report the survivor set, removal ledger, normalized degree policy, source-record treatment and coverage limits. Recompute from a new snapshot after any accepted edge change.

The following Python 3 reference accepts node IDs as nonempty strings and edge triples `(edge_id, endpoint_a, endpoint_b)`. It operates on small finite lists. Run the whole snippet in an available Python 3 interpreter and record its observed version. Its verifier independently reconstructs adjacency from source records and replays the supplied rounds; it does not trust the builder's adjacency.

```python
def adjacency(nodes, edges):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    known, ids = set(nodes), set()
    adj = {n: set() for n in nodes}
    for e in edges:
        if type(e) not in (tuple, list) or len(e) != 3 or any(
                type(x) is not str or not x for x in e):
            raise ValueError("invalid edge record")
        eid, a, b = e
        if eid in ids or a not in known or b not in known:
            raise ValueError("duplicate edge or unknown endpoint")
        ids.add(eid)
        if a != b:
            adj[a].add(b)
            adj[b].add(a)
    return adj

def peel(nodes, edges, k):
    if type(k) is not int or k < 0:
        raise ValueError("nonnegative integer k required")
    adj = adjacency(nodes, edges)
    remaining, rounds = set(nodes), []
    while True:
        low = sorted(v for v in remaining if len(adj[v] & remaining) < k)
        if not low:
            break
        rounds.append([(v, len(adj[v] & remaining)) for v in low])
        remaining.difference_update(low)
    return sorted(remaining), rounds

def verify(nodes, edges, k, survivors, rounds):
    if type(k) is not int or k < 0:
        raise ValueError("nonnegative integer k required")
    adj = adjacency(nodes, edges)
    remaining = set(nodes)
    for row in rounds:
        expected = {v: len(adj[v] & remaining) for v in remaining
                    if len(adj[v] & remaining) < k}
        if not expected or dict(row) != expected or len(row) != len(expected):
            return False
        remaining.difference_update(expected)
    return (survivors == sorted(remaining)
            and all(len(adj[v] & remaining) >= k for v in remaining))

nodes = ["A", "B", "C", "D", "E", "I"]
edges = [("ab", "A", "B"), ("bc", "B", "C"),
         ("ca", "C", "A"), ("cd", "C", "D"),
         ("de", "D", "E"), ("ab2", "A", "B"),
         ("loop", "E", "E")]
survivors, rounds = peel(nodes, edges, 2)
assert survivors == ["A", "B", "C"]
assert rounds == [[("E", 1), ("I", 0)], [("D", 1)]]
assert verify(nodes, edges, 2, survivors, rounds)
assert not verify(nodes, edges, 2, ["A", "B", "C", "D"], rounds)
assert peel(nodes, edges, 0)[0] == sorted(nodes)
try:
    peel(["a", "b"], ["xab"], 1)
except ValueError:
    pass
else:
    raise AssertionError("string edge record accepted")
print("k-core, cascaded peeling and ledger checks passed")
```

The verifier compares each round with the complete set of vertices below k; it rejects a fabricated deletion even when the final survivors happen to satisfy the degree condition. The explicit policy makes two A/B records one neighbor and makes E's loop contribute no neighbor. The loop and parallel IDs remain in the source inventory for audit.

## Decision rules
- IF k is zero THEN retain every inventoried vertex BECAUSE every induced degree is nonnegative.
- IF a round removes vertices THEN recompute surviving degrees BECAUSE deletion may expose a new low-degree vertex.
- IF a loop or parallel record exists THEN apply the stated neighbor policy BECAUSE raw edge count is not the reference degree.
- IF a supplied removal ledger omits a low-degree vertex THEN reject its certificate BECAUSE that round is incomplete.
- IF the snapshot is partial THEN qualify the core claim BECAUSE unseen neighbors may change membership.

## Output template
```text
Scope: <revision, undirected projection, coverage; maximum 70 words>
Threshold and degree policy: <k, distinct-neighbor, loops and parallel handling>
Survivors: <all retained IDs, or attached complete ledger>
Peeling rounds: <round | removed ID | degree immediately before round; full ledger>
Source exceptions: <excluded records, or None>
Verification: <round replay and final induced-degree checks executed/pending>
Limits: <coverage, semantic and scale limits; maximum 80 words>
Next action: <owner and bounded follow-up; maximum 40 words>
```

## Quality checklist
- [ ] Node and edge identity validation precedes adjacency construction.
- [ ] k is a supplied nonnegative integer.
- [ ] Direction and projection are explicit.
- [ ] Loop and parallel policies are recorded.
- [ ] Isolates appear in the initial inventory and removal ledger where required.
- [ ] Each removal round lists every vertex below k.
- [ ] Final induced degrees meet the threshold.
- [ ] No survival result is described as a semantic community or social ranking.

## Anti-patterns
- **One-pass pruning**: retain a node that falls below k after neighbors leave. Fix: repeat to a fixed point.
- **Raw record degree**: count two parallel edges as two neighbors. Fix: use distinct endpoints under this policy.
- **Loop inflation**: let a self-loop satisfy this reference threshold. Fix: retain its record but exclude it from neighbor count.
- **Arbitrary deletion**: remove a vertex with degree at least k. Fix: replay and reject the round.
- **Meaning from structure**: call retained nodes important people. Fix: report only graph membership under the chosen projection.

## Worked example
**Input:** Fictional graph Team Willow supplies the complete exercise nodes and edges in the snippet. All edges are undirected; use k=2 and the stated distinct-neighbor policy.

**Output:**
```text
Scope: Willow exercise W1; supplied undirected inventory A/B/C/D/E/I complete for this exercise.
Threshold and degree policy: k=2; distinct retained neighbors; parallel A/B IDs collapse for degree; E loop contributes zero neighbors.
Survivors: A, B, C.
Peeling rounds: Round 1 | E | 1; I | 0. Round 2 | D | 1.
Source exceptions: None; ab and ab2, and loop, remain in the source ledger.
Verification: Embedded reference replay and final induced-degree assertions executed for W1.
Limits: Exercise topology only; no domain community, importance or wider graph claim.
Next action: Graph owner checks any omitted links before using the W1 result in a separate analysis.
```

**Bad output:** “D survives because it had both C and E as neighbors originally; E's loop makes it high degree.”
E leaves first, leaving D with one retained neighbor, and the declared policy excludes loop degree.

## Edge cases
- **Empty inventory**: return empty survivors and no rounds when the empty scope is explicit.
- **k=0**: return every node, including isolates, with no rounds.
- **k above possible distinct-neighbor degree**: peel to empty, reporting each round.
- **Self-loop only**: under this policy, the vertex has zero distinct neighbors other than itself.
- **Parallel-only pair**: each endpoint has one distinct neighbor regardless of record count.

## Test case
**Input:**
> Fictional graph has triangle A/B/C, tail C/D/E, isolated I, a second A/B edge ID and an E self-loop. Use undirected distinct-neighbor degree and k=2.

**Assertions:**
1. Reports A/B/C as survivors and no other node.
2. Removes E and I in the first round, then D in the second.
3. States that the second A/B record and E loop do not increase distinct-neighbor degree.
4. Verifies the final induced degrees and the complete removal ledger.
5. Does not infer a social or operational ranking from membership.
