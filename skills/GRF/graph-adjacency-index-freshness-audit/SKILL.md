---
id: GRF-047
name: graph-adjacency-index-freshness-audit
domain: Graph Engineering Foundations
subdomain: Derived adjacency verification
version: 1.0
description: Reconcile materialized outgoing and incoming edge-ID lists against a frozen directed source graph and build epoch when adjacency queries may be stale or misrouted.
triggers: ["audit a graph adjacency index", "why does outgoing lookup miss an edge", "compare incoming and outgoing views with source edges", "find stale edge IDs in a graph index", "check graph index build epoch"]
not_for: ["initial edge-list import [GRF-003]", "relational storage implementation [GRF-014]", "query-plan tuning [GRF-015]", "partition copy ownership [GRF-026]", "whole-service restore readiness [GRF-024]"]
requires: []
risk_level: medium
---

# Graph Adjacency Index Freshness Audit

## Purpose
Compare materialized outgoing and incoming edge-ID lists with one frozen directed primary graph. Return per-node, per-edge witnesses for missing, extra, duplicate or misrouted list entries, and check that both views name the source epoch. This is a derived-view audit for an observed index, not a restore procedure, index rebuild command or performance measurement.

## Inputs to collect
1. **Primary graph** — obtain a frozen node inventory and unique edge IDs with source and target endpoints. Why: the expected lists must come from independent authoritative records. Default: none; do not derive expectations from the index under test.
2. **Source epoch** — obtain the version or build boundary represented by the primary extract. Why: equality between mixed revisions can be misleading. Default: unresolved; withhold a freshness pass.
3. **Index extracts** — obtain complete outgoing and incoming edge-ID lists for every node, including isolates, with their own build epoch. Why: a missing bucket differs from an explicitly empty bucket. Default: unavailable buckets remain unverified.
4. **View contract** — confirm that every source edge ID appears once in its source's outgoing list and once in its target's incoming list; loops appear once in both lists at the same node. Why: systems with filters or other multiplicity rules need their own expectations. Default: no silent filtering; request the actual contract.
5. **Use and repair authority** — identify affected consumer queries, rebuild owner and change boundary. Why: a discrepancy identifies evidence, not permission to rebuild a live index. Default: diagnostic report only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the primary node/edge extract, source epoch, both index extracts and their build epoch together.
2. Validate unique nonempty node and edge IDs, known endpoints and complete node-bucket coverage before comparing lists.
3. Derive expected outgoing and incoming edge-ID lists from the primary edge records, preserving parallel edge IDs separately.
4. Check epoch equality before interpreting a clean comparison as fresh. ⚠️ Do not call an index current merely because one sampled lookup matches when its build marker differs from the source marker.
5. Compare each observed bucket with its expected bucket as a multiset so duplicate IDs cannot disappear under set conversion.
6. Classify missing expected IDs, duplicate IDs and unexpected IDs per node and direction. If an unexpected ID exists in source at another endpoint, call it misrouted; if absent from source, call it stale or foreign under the supplied extract.
7. Check every edge ID has exactly one correct outgoing appearance and one correct incoming appearance. A self-loop appears in two direction-specific lists at its one node; that is not a duplicate within either list.
8. Replay a small affected outgoing and incoming lookup directly from primary records to establish the consumer-visible difference. Retain full index extracts for the audit boundary, not only a favorable sample.
9. Report a pass only when epochs agree, bucket coverage is complete and every list matches primary. Otherwise deliver exact witnesses and a proposed isolated rebuild/recheck sequence for owner review.
10. After an authorized rebuild, capture a new source/index boundary and repeat the full comparison; do not overwrite the initial failure evidence or infer crash durability from an offline fixture.

The Python 3 reference below accepts node IDs and edge triples `(edge_id, source, target)`. Index extracts map each node to a list of edge IDs. It requires complete maps, not sampled buckets. Run the entire snippet on the available Python 3 interpreter and record the observed version. This fixture is read-only and does not implement an index engine or live rebuild.

```python
from collections import Counter

def audit(nodes, edges, source_epoch, index_epoch, outgoing, incoming):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    if any(type(e) not in (tuple, list) or len(e) != 3 or
           any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    known = set(nodes)
    if any(a not in known or b not in known for _, a, b in edges):
        raise ValueError("unknown endpoint")
    if set(outgoing) != known or set(incoming) != known:
        raise ValueError("incomplete node buckets")
    for view in (outgoing, incoming):
        if any(type(bucket) is not list or
               any(type(eid) is not str or not eid for eid in bucket)
               for bucket in view.values()):
            raise ValueError("invalid bucket")
    if (source_epoch is None or index_epoch is None or
        (type(source_epoch) is str and not source_epoch.strip()) or
        (type(index_epoch) is str and not index_epoch.strip())):
        raise ValueError("epoch evidence required")

    expected = {"out": {n: Counter() for n in nodes},
                "in": {n: Counter() for n in nodes}}
    by_id = {}
    for eid, source, target in edges:
        by_id[eid] = (source, target)
        expected["out"][source][eid] += 1
        expected["in"][target][eid] += 1
    observed = {"out": outgoing, "in": incoming}
    issues = []
    if source_epoch != index_epoch:
        issues.append(("epoch", source_epoch, index_epoch))
    for direction in ("out", "in"):
        for node in sorted(nodes):
            want = expected[direction][node]
            got = Counter(observed[direction][node])
            for eid in sorted(set(want) | set(got)):
                if got[eid] < want[eid]:
                    issues.append((direction, node, eid, "missing",
                                   want[eid] - got[eid]))
                if got[eid] > want[eid]:
                    if eid not in by_id:
                        kind = "stale-or-foreign"
                    elif want[eid]:
                        kind = "duplicate"
                    else:
                        kind = "misrouted"
                    issues.append((direction, node, eid, kind,
                                   got[eid] - want[eid]))
    return issues

nodes = ["A", "B", "I"]
edges = [("p1", "A", "B"), ("p2", "A", "B"),
         ("loop", "B", "B")]
good_out = {"A": ["p1", "p2"], "B": ["loop"], "I": []}
good_in = {"A": [], "B": ["p1", "p2", "loop"], "I": []}
assert audit(nodes, edges, 7, 7, good_out, good_in) == []
bad_out = {"A": ["p1", "p1"], "B": ["loop", "p2"], "I": []}
issues = audit(nodes, edges, 7, 6, bad_out, good_in)
assert ("out", "A", "p2", "missing", 1) in issues
assert ("out", "A", "p1", "duplicate", 1) in issues
assert ("out", "B", "p2", "misrouted", 1) in issues
assert ("epoch", 7, 6) in issues
for blank in ("", "   "):
    try:
        audit(["A"], [], blank, blank, {"A": []}, {"A": []})
    except ValueError:
        pass
    else:
        raise AssertionError("blank epoch accepted")
print("adjacency epoch, direction and edge-ID witnesses checked")
```

The comparison treats edge identity, not endpoint pair, as the indexing unit. Distinct parallel A→B edges must each appear; a B→B loop appears once in B's outgoing and once in B's incoming bucket. An epoch mismatch blocks freshness even if all supplied list rows happen to match.

## Decision rules
- IF either epoch marker is missing or unequal THEN withhold a freshness pass BECAUSE the extracts may represent different graph states.
- IF a required node bucket is missing THEN reject complete coverage BECAUSE absence of a bucket is not evidence of an empty list.
- IF an edge ID appears in the wrong node bucket THEN report its expected endpoint and observed bucket BECAUSE a global count can still match.
- IF an edge ID repeats in one bucket THEN report multiplicity BECAUSE set equality would hide the duplicate.
- IF all buckets and epochs pass THEN limit the conclusion to this source/index boundary BECAUSE later mutations require a new audit.

## Output template
```text
Boundary: <source epoch, index epoch, extraction scope; maximum 70 words>
View contract: <outgoing/incoming, loop and parallel handling>
Coverage: <all node buckets present, or exact gaps>
Findings: <direction | node | edge ID | missing/duplicate/misrouted/stale | count; full ledger>
Checks: <source-derived expected lists and observed lookup comparison executed/pending>
Verdict: <fresh for boundary / mismatch / unresolved>
Limits: <scope, currentness and live-system limits; maximum 80 words>
Next action: <owner and bounded recheck; maximum 40 words>
```

## Quality checklist
- [ ] Primary records are independent of index extracts.
- [ ] Source and index epochs are present and compared.
- [ ] Every node has outgoing and incoming buckets.
- [ ] Parallel edge IDs remain separate.
- [ ] Loops appear once in each direction-specific bucket.
- [ ] Multiset comparison catches duplicate list entries.
- [ ] Misrouted and absent-source IDs receive distinct witnesses.
- [ ] The result does not claim performance or live rebuild completion.

## Anti-patterns
- **Self-certified index**: build expected lists from the same observed buckets. Fix: derive them from frozen primary edges.
- **Count-only pass**: equal total entries hide a misrouted ID. Fix: compare each node and direction by edge ID.
- **Set collapse**: duplicate IDs disappear. Fix: compare multisets.
- **Missing means empty**: omit an isolate bucket without notice. Fix: require explicit empty lists.
- **Stale epoch pass**: matching rows override different markers. Fix: keep boundary mismatch as a blocker.

## Worked example
**Input:** Fictional graph service Finch supplies the snippet source and index extracts. Source epoch is 7; index epoch is 6. The outgoing A bucket lacks p2, repeats p1 and the outgoing B bucket wrongly includes p2.

**Output:**
```text
Boundary: Finch exercise F1; source epoch 7, index epoch 6; supplied A/B/I graph and complete buckets.
View contract: Directed outgoing/incoming lists; each edge ID once at its endpoint; parallel p1/p2 separate; loop in B's two direction-specific lists.
Coverage: A/B/I outgoing and incoming buckets present, including explicit empty I buckets.
Findings: out | A | p1 | duplicate | 1; out | A | p2 | missing | 1; out | B | p2 | misrouted | 1; epoch | 7 versus 6.
Checks: Source-derived lists compared with all supplied buckets; incoming view matched, outgoing did not.
Verdict: Mismatch.
Limits: Exercise extract only; no live index rebuild or performance observation.
Next action: Index owner checks build boundary and proposes an isolated rebuild, then repeats the full audit.
```

**Bad output:** “Three outgoing records exist, so the index is current; rebuild the live index now.”
The entries include a duplicate and wrong bucket, one expected ID is absent from A, and epochs differ.

## Edge cases
- **Isolated node**: require explicit empty outgoing and incoming buckets.
- **Parallel edges**: compare both distinct IDs rather than a single endpoint pair.
- **Self-loop**: expect one appearance in each direction-specific list at its node.
- **Unknown index ID**: classify it as stale or foreign under the supplied primary extract.
- **Missing or mixed epoch**: withhold a freshness verdict even when row comparison passes.

## Test case
**Input:**
> Fictional source has two A→B edge IDs, a B self-loop and isolated I. The outgoing index repeats one A edge, omits the other from A, places it in B, and reports an older build epoch. Audit both directions.

**Assertions:**
1. Reports the epoch mismatch and withholds a freshness pass.
2. Gives separate missing, duplicate and misrouted edge-ID witnesses.
3. Preserves both parallel identities and explicit empty I buckets.
4. Verifies incoming and outgoing views separately.
5. Does not claim a live rebuild was performed.
