---
id: GRF-051
name: bounded-graph-query-cache-invalidation-ledger
domain: Graph Engineering Foundations
subdomain: Versioned traversal caches
version: 1.0
description: Audit versioned bounded traversal cache entries after one graph edge change and distinguish changed answers from unchanged content tied to an old revision.
triggers: ["which graph traversal caches need invalidation", "compare cached paths after an edge update", "audit graph cache revision keys", "find shorter hops after a new edge", "recompute affected bounded graph queries"]
not_for: ["one fresh bounded traversal [GRF-006]", "all-pair unbounded reachability addition [GRF-039]", "adjacency index freshness [GRF-047]", "query-plan tuning [GRF-015]", "live cache deployment"]
requires: []
risk_level: medium
---

# Bounded Graph Query Cache Invalidation Ledger

## Purpose
Audit cached traversals after one edge change. Preserve query contracts and distinguish content changes from stale revisions. Report a plan.

## Inputs to collect
1. **Before graph** — obtain unique node and edge IDs, directed endpoints, relation labels and a frozen revision, including isolates. Why: cached answers need an independent reference. Default: none.
2. **Change** — obtain exactly one add or delete action, edge ID and proposed after revision. Why: an update to endpoints or labels is a delete plus add and needs a separately declared scenario. Default: no assumed change.
3. **Cache manifest** — obtain every inspected key, its old revision, seed, direction, allowed relation labels, nonnegative hop bound and complete minimum-hop answer. Why: a key without its full query contract cannot be safely reused. Default: mark incomplete entries unresolved.
4. **Answer semantics** — confirm that the seed appears at distance zero and each other node has its minimum number of eligible edges within the bound. Why: paths, endpoint sets and counts have different validity. Default: the reference semantics only.
5. **Coverage and use** — identify extract completeness and refresh owner. Why: unseen records limit the claim. Default: supplied scope only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the before graph, proposed after revision and complete cache manifest without changing source records.
2. Validate identities, endpoints, labels and nonblank distinct revisions. Reject reused or unknown edge IDs.
3. Validate each cache key's full query tuple: seed, direction, relation filter and hop bound. Reject missing filter or bound rather than silently using all edges or unlimited traversal.
4. Recompute each old answer from the before graph and compare it with the supplied cached answer. ⚠️ A previously corrupt cache entry cannot serve as evidence of the edge change; label it invalid at baseline.
5. Create the hypothetical after graph by adding or deleting exactly the named edge ID. Preserve all other records, including parallel edges and isolates.
6. Recompute each query from the after graph using its unchanged tuple. Record complete minimum-hop maps, including distance changes when the reached set stays the same.
7. Independently verify old and new maps with a second layer-based traversal. An interrupted or sampled traversal cannot certify unchanged content.
8. Classify each entry as content changed, content equal, or baseline invalid. In every case, mark an old-revision entry stale for the new revision; content equality does not turn its key into a new-revision key.
9. Produce a refresh candidate only from a complete verified after answer; otherwise leave it pending.
10. Deliver revision, query, difference and action ledger.

The Python 3 reference handles finite directed edges `(edge_id, source, target, relation)`. Queries are `(seed, direction, allowed_labels, depth)`, with `out` or `in`, a nonempty label tuple and nonnegative depth. Cache entries map keys to `(revision, query, old_map)`. Run it and record the interpreter version.

```python
from collections import deque

def validate(nodes, edges):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    if any(type(e) not in (tuple, list) or len(e) != 4 or
           any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    if any(a not in nodes or b not in nodes for _, a, b, _ in edges):
        raise ValueError("unknown endpoint")

def query(nodes, edges, spec):
    if type(spec) is not tuple or len(spec) != 4:
        raise ValueError("complete query tuple required")
    seed, direction, labels, depth = spec
    if (seed not in nodes or direction not in ("out", "in") or
        type(labels) is not tuple or not labels or
        any(type(x) is not str or not x for x in labels) or
        type(depth) is not int or depth < 0):
        raise ValueError("invalid query contract")
    adj = {n: [] for n in nodes}
    for _, a, b, label in edges:
        if label in labels:
            adj[a if direction == "out" else b].append(
                b if direction == "out" else a)
    dist, todo = {seed: 0}, deque([seed])
    while todo:
        node = todo.popleft()
        if dist[node] == depth:
            continue
        for nxt in adj[node]:
            if nxt not in dist:
                dist[nxt] = dist[node] + 1
                todo.append(nxt)
    return dist

def verify_layers(nodes, edges, spec, answer):
    seed, direction, labels, depth = spec
    reached, frontier = {seed: 0}, {seed}
    for hop in range(1, depth + 1):
        nxt = set()
        for _, a, b, label in edges:
            source, target = (a, b) if direction == "out" else (b, a)
            if label in labels and source in frontier and target not in reached:
                nxt.add(target)
        for node in nxt:
            reached[node] = hop
        frontier = nxt
    return reached == answer

def audit(nodes, edges, before_rev, after_rev, action, edge, cache):
    validate(nodes, edges)
    valid_rev = lambda v: type(v) is int or (type(v) is str and bool(v.strip()))
    if not valid_rev(before_rev) or not valid_rev(after_rev) or before_rev == after_rev or action not in ("add", "delete"):
        raise ValueError("distinct revisions and action required")
    if type(edge) not in (tuple, list) or len(edge) != 4:
        raise ValueError("identified edge required")
    ids = {e[0] for e in edges}
    if action == "add":
        if edge[0] in ids:
            raise ValueError("edge ID already exists")
        changed = list(edges) + [edge]
    else:
        if edge not in edges:
            raise ValueError("exact deletion record not found")
        changed = [e for e in edges if e[0] != edge[0]]
    validate(nodes, changed)
    ledger = {}
    for key, (cached_rev, spec, cached) in cache.items():
        if not valid_rev(cached_rev) or cached_rev != before_rev:
            raise ValueError("cache entry revision mismatch")
        old = query(nodes, edges, spec)
        new = query(nodes, changed, spec)
        assert verify_layers(nodes, edges, spec, old)
        assert verify_layers(nodes, changed, spec, new)
        baseline_ok = cached == old
        ledger[key] = {
            "old": old, "new": new,
            "content": ("changed" if old != new else "equal")
                       if baseline_ok else "baseline invalid",
            "old_revision_stale": True,
            "refresh_ready": baseline_ok,
        }
    return ledger

nodes = ["A", "B", "C", "D", "I"]
edges = [("ab", "A", "B", "link"),
         ("bc", "B", "C", "link"),
         ("cd", "C", "D", "link")]
q1 = ("A", "out", ("link",), 2)
q2 = ("D", "out", ("link",), 2)
q3 = ("C", "in", ("link",), 1)
cache = {"Q1": ("r1", q1, {"A": 0, "B": 1, "C": 2}),
         "Q2": ("r1", q2, {"D": 0}),
         "Q3": ("r1", q3, {"C": 0, "B": 1})}
report = audit(nodes, edges, "r1", "r2", "add",
               ("ad", "A", "D", "link"), cache)
assert report["Q1"]["new"] == {"A": 0, "B": 1, "C": 2, "D": 1}
assert [report[k]["content"] for k in cache] == [
    "changed", "equal", "equal"]
assert all(row["old_revision_stale"] for row in report.values())
print("bounded cache contents, versions and layer checks passed")
```

The reference recomputes every key. An excluded edge can leave content equal, while the old key still names the old graph. Backend concurrency remains untested.

## Decision rules
- IF cached baseline differs from recomputed baseline THEN mark baseline invalid BECAUSE change attribution would be unreliable.
- IF a minimum hop changes while node membership stays fixed THEN mark content changed BECAUSE the answer contract includes distance.
- IF content is equal but revisions differ THEN keep the old key stale BECAUSE its provenance names the old source.
- IF an entry lacks direction, filter or bound THEN mark it unresolved BECAUSE its answer cannot be independently recomputed.
- IF traversal is incomplete THEN withhold a refresh candidate BECAUSE an unchecked frontier may change the answer.

## Output template
```text
Boundary: <before/after revisions, graph scope and change; maximum 70 words>
Cache contract: <seed, direction, labels, bound and minimum-hop semantics per key>
Ledger: <key | baseline valid? | content changed/equal | old key stale? | new answer and difference>
Verification: <complete before/after recomputation and independent layers executed/pending>
Refresh plan: <keys with verified new entries and keys unresolved>
Limits: <coverage, cache backend and concurrency; maximum 80 words>
Next action: <owner and bounded follow-up; maximum 40 words>
```

## Quality checklist
- [ ] Before and after revisions are distinct and explicit.
- [ ] Each cache key has a complete query contract.
- [ ] Baseline cached answers are checked before change attribution.
- [ ] Exactly one identified edge changes in the scenario.
- [ ] Parallel edges remain separate source records.
- [ ] Both traversal methods agree on old and new answers.
- [ ] Distance changes are treated as content changes.
- [ ] Equal content is not called a current old-revision key.

## Anti-patterns
- **Cache self-certification**: trust old answers without source recomputation. Fix: compare with the frozen baseline graph.
- **Membership-only check**: ignore changed shortest hop. Fix: compare full minimum-hop maps.
- **Version laundering**: rename an old key as current because contents match. Fix: bind refresh to a newly verified revision.
- **Filter omission**: treat every edge as eligible. Fix: require labels in each query key.
- **Live-action fiction**: say caches were invalidated from an offline model. Fix: report a plan and execution boundary.

## Worked example
**Input:** Fictional Team Maple supplies the snippet's revision r1 graph, three cache entries and proposed ad:A→D at r2. Query contracts are complete; no cache backend action is authorized.

**Output:**
```text
Boundary: Maple exercise; r1 to hypothetical r2; add ad:A→D with label link; A/B/C/D/I in scope.
Cache contract: Q1 A/out/link/depth2; Q2 D/out/link/depth2; Q3 C/in/link/depth1; minimum-hop maps include seed at zero.
Ledger: Q1 | valid | changed, adds D1 | stale | r2 A0,B1,C2,D1. Q2 | valid | equal | stale | r2 D0. Q3 | valid | equal | stale | r2 C0,B1.
Verification: Complete before/after query recomputation and independent layer checks executed for all three keys.
Refresh plan: Q1/Q2/Q3 have verified r2 answer candidates; no live invalidation executed.
Limits: Exercise extracts only; no backend atomicity, concurrent change or wider graph claim.
Next action: Cache owner reviews the r2 candidates and executes a separately controlled refresh.
```

**Bad output:** “Q2 and Q3 did not change, so their r1 keys are current at r2.”
Their contents match, but their keys still identify r1.

## Edge cases
- **Deletion**: recompute from the graph with exactly that edge ID removed; a parallel edge may preserve a route.
- **Shorter path**: treat changed minimum distance as changed content even if the reached set is unchanged.
- **Excluded relation**: record equal content under that query filter, while retaining revision staleness.
- **Missing bound or filter**: return unresolved, not a guessed query.
- **Isolate**: keep it in the source universe even if no cached answer mentions it.

## Test case
**Input:**
> Fictional cache stores A/out/link/depth2, D/out/link/depth2 and C/in/link/depth1 results for r1 graph A→B→C→D. Add A→D at r2; explain content and revision dispositions.

**Assertions:**
1. Q1 adds D at distance one; Q2 and Q3 content remains equal.
2. Every r1 key is marked stale for r2 despite equal content for two queries.
3. Each new answer is checked against the same query direction, filter and bound.
4. No live cache refresh or graph mutation is claimed.
