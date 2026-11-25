Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-038
name: undirected-motif-witness-census
domain: Graph Engineering Foundations
subdomain: Small motif census
version: 1.0
description: Count triangles and open wedges in a finite undirected multigraph while retaining distinct-vertex and edge-identity witnesses under an explicit parallel-edge policy.
triggers: ["count triangles in a graph", "enumerate open wedges", "audit motif counts", "handle parallel edges in triangle counts", "show edge witnesses for graph motifs", "compare motif counts across snapshots"]
not_for: ["graph import reconciliation [GRF-003]", "bounded seed traversal [GRF-006]", "community partition sensitivity [GRF-013]", "clustering interpretation without a declared denominator", "directed motifs or weighted motif scoring"]
requires: []
risk_level: medium
---

# Undirected Motif Witness Census

## Purpose
Count three-distinct-vertex triangles and open wedges in a declared undirected multigraph snapshot. Return structural triple counts separately from edge-identity instance counts, with witnesses a reviewer can replay. This method describes graph structure; it does not explain why links exist or assign significance to a motif without domain evidence.

## Inputs to collect
1. **Complete inventory** — node IDs and edge records `(edge ID, endpoint A, endpoint B)` from one version. Why: missing links can turn a triangle into a wedge. Default: none, required.
2. **Projection** — which relation records become undirected links. Why: silently dropping direction or relation types changes the census. Default: none when source semantics are ambiguous.
3. **Multiplicity policy** — whether to report unique vertex triples, edge-identity combinations, or both. Why: parallel records change instance counts. Default: report both, keeping IDs separate.
4. **Loop policy** — handling for self-loops. Why: three-distinct-vertex motifs cannot use a loop. Default: exclude loops from motif construction and list their IDs separately.
5. **Completeness and budget** — whether all eligible edges were supplied and whether exhaustive enumeration can finish. Why: an interrupted census is not an exact count. Default: state completeness unknown and report only a supplied-extract count if confirmation is absent.
6. **Purpose** — structural audit, comparison or another decision. Why: a count alone does not establish a causal or quality conclusion. Default: structural audit only.

If a required input is missing without a safe default, ask in one message with at most three questions. Freeze the snapshot before counting.

## Procedure
1. Record snapshot ID, node universe, undirected projection, relation filters and evidence of completeness.
2. Validate unique nonempty node IDs, unique nonempty edge IDs and known endpoints. Do not merge parallel edge IDs.
3. Separate self-loops into an exclusion ledger. Keep isolated nodes in the inventory, although no three-vertex motif can include one.
4. For each unordered distinct endpoint pair, collect all eligible edge IDs in a sorted bucket. An endpoint pair is present when its bucket is nonempty.
5. Visit each unordered triple of distinct nodes exactly once. Classify it as triangle when all three pair buckets are present, open wedge when exactly two are present, and neither otherwise.
6. For a triangle, enumerate one ID from each of its three pair buckets. For an open wedge, enumerate one ID from each of its two present buckets and name the unique vertex incident to both selected links as center.
7. ⚠️ Keep structural triple counts separate from identity-instance counts. Parallel edges can increase the latter without adding another vertex triple.
8. Independently replay each witness against original endpoint records: three distinct vertices, correct pair coverage, no repeated edge ID, and a missing closing pair for an open wedge.
9. Recompute expected instance totals from products of bucket sizes for each classified triple. Compare these totals with enumerated witness counts and reject mismatches or duplicate witness keys.
10. Deliver counts, witness ledger, exclusions, and scope limits. If enumeration was interrupted, report partial evidence and an unfinished census rather than an exact result.

This Python 3 reference accepts finite lists of string nodes and undirected edge triples. It retains parallel identities, excludes loops and enumerates every witness, so its memory and time costs grow with the input. Execute the full snippet and record the interpreter version. Choose a bounded input suitable for the available environment before adapting it to large graphs.

```python
from itertools import combinations, product

def census(nodes, edges):
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
    by_id = {eid: frozenset((a, b)) for eid, a, b in edges}
    buckets, loops = {}, []
    for eid, a, b in edges:
        if a == b:
            loops.append(eid)
        else:
            buckets.setdefault(tuple(sorted((a, b))), []).append(eid)
    for ids in buckets.values():
        ids.sort()
    structural = {"triangle": 0, "open_wedge": 0}
    witnesses = {"triangle": [], "open_wedge": []}
    expected = {"triangle": 0, "open_wedge": 0}
    for triple in combinations(sorted(nodes), 3):
        keys = list(combinations(triple, 2))
        present = [key for key in keys if key in buckets]
        if len(present) not in (2, 3):
            continue
        kind = "triangle" if len(present) == 3 else "open_wedge"
        structural[kind] += 1
        amount = 1
        for key in present:
            amount *= len(buckets[key])
        expected[kind] += amount
        center = None
        if kind == "open_wedge":
            center = next(n for n in triple if all(n in key for key in present))
        for choice in product(*(buckets[key] for key in present)):
            witnesses[kind].append((triple, center, tuple(choice)))
    for kind, records in witnesses.items():
        if len(records) != expected[kind] or len(set(records)) != len(records):
            raise AssertionError("instance census mismatch")
        for triple, center, ids in records:
            assert len(set(triple)) == 3
            pairs = {tuple(sorted(by_id[eid])) for eid in ids}
            assert all(len(by_id[eid]) == 2 for eid in ids)
            assert len(set(ids)) == len(ids) and len(pairs) == len(ids)
            if kind == "triangle":
                assert center is None and pairs == set(combinations(triple, 2))
            else:
                assert len(pairs) == 2 and all(center in p for p in pairs)
                assert len(set(combinations(triple, 2)) - pairs) == 1
    return structural, {k: len(v) for k, v in witnesses.items()}, witnesses, sorted(loops)

nodes = ["A", "B", "C", "D", "I"]
edges = [("ab1", "A", "B"), ("ab2", "A", "B"),
         ("bc", "B", "C"), ("ac", "A", "C"),
         ("cd", "C", "D"), ("loop", "A", "A")]
structural, instances, witness, loops = census(nodes, edges)
assert structural == {"triangle": 1, "open_wedge": 2}
assert instances == {"triangle": 2, "open_wedge": 2}
assert loops == ["loop"]
assert {w[2] for w in witness["triangle"]} == {
    ("ab1", "ac", "bc"), ("ab2", "ac", "bc")}
assert census(["I"], [])[0] == {"triangle": 0, "open_wedge": 0}
print("distinct triples, parallel witnesses, loop exclusion and isolates checked")
```

## Decision rules
- IF the projection or inventory is incomplete THEN label the count as supplied-extract only BECAUSE unseen edges can change wedge and triangle classification.
- IF an edge is a self-loop THEN exclude it from these three-distinct-vertex motifs and list its ID BECAUSE it cannot connect two distinct vertices.
- IF parallel edges share endpoints THEN keep one structural pair but separate identity combinations BECAUSE multiplicity affects instances, not the vertex triple.
- IF exactly two of three endpoint pairs are present THEN classify one open wedge with the shared center BECAUSE the closing pair is absent within the scoped snapshot.
- IF a witness fails endpoint replay or count products differ THEN reject the census BECAUSE the reported exact total lacks supporting records.
- IF execution stops early THEN report partial enumeration and no exact total BECAUSE unvisited triples may contain motifs.

## Output template
```text
Scope: <snapshot, undirected projection, nodes/edges and completeness; max 3 lines>
Policy: <distinct vertices; parallel identities; loop handling>
Structural: <triangle triple count; open-wedge triple count>
Instances: <triangle edge-combination count; open-wedge edge-combination count>
Witnesses: <triple, center if wedge, ordered edge IDs; one line each or attached ledger>
Exclusions: <loop IDs and other excluded records, or none>
Verification: <endpoint replay and product totals, or unresolved reason>
Limits: <unseen records, semantics or incomplete run; max 2 lines>
Next action: <one concrete step>
```

## Quality checklist
- [ ] Snapshot, projection and completeness boundary are explicit.
- [ ] Node and edge IDs are unique and endpoints exist.
- [ ] Every triple has three distinct nodes and appears once.
- [ ] Loops are excluded with their IDs listed.
- [ ] Parallel IDs remain separate in instance witnesses.
- [ ] Open wedges have exactly two present pairs and a named center.
- [ ] Every witness replays against original edge endpoint records.
- [ ] Structural and instance counts are separately reported.
- [ ] Instance counts equal per-triple bucket-size products.
- [ ] Exact totals are withheld if enumeration is incomplete.

## Anti-patterns
- **Parallel collapse**: reporting one edge instance for two parallel IDs. Fix: report structural and identity-instance counts separately.
- **Triple duplication**: counting each triangle once from every vertex. Fix: visit sorted unordered triples once.
- **Loop as wedge arm**: treating a self-loop as a distinct endpoint pair. Fix: exclude loops and list their IDs.
- **Closed wedge labeled open**: ignoring the third pair. Fix: test all three pair buckets before classification.
- **Unreplayed witness**: trusting a motif label without endpoints. Fix: verify each selected ID against the source record.
- **Global claim from extract**: calling a sampled subgraph census complete. Fix: state the extract boundary and seek full inventory.

## Worked example
**Input:**
> Fictional Grove snapshot S1 has nodes A,B,C,D,I. Undirected edges ab1 and ab2 both A-B, bc B-C, ac A-C, cd C-D, and loop A-A. Count both structural motifs and identity instances.

**Output:**
```text
Scope: Fictional Grove S1; undirected complete supplied exercise; nodes A,B,C,D,I; six edge IDs.
Policy: Three distinct vertices; parallel IDs separate for instances; loop excluded.
Structural: 1 triangle triple (A,B,C); 2 open-wedge triples (A,C,D),(B,C,D).
Instances: 2 triangle combinations; 2 open-wedge combinations.
Witnesses: (A,B,C), center none, (ab1,ac,bc); (A,B,C), center none, (ab2,ac,bc); (A,C,D), center C, (ac,cd); (B,C,D), center C, (bc,cd).
Exclusions: loop.
Verification: All IDs replayed; products 2×1×1=2 and 1×1+1×1=2.
Limits: I is isolated; motif counts do not explain the relationships.
Next action: Retain this witness ledger with S1 for comparison to a later snapshot.
```

**Bad output:** "Three triangles because A-B has two edges and A has a loop." This fails the distinct-vertex policy: one triangle triple has two identity instances, and the loop is excluded.

## Edge cases
- **No edges or fewer than three nodes**: both counts zero; keep the node inventory and any loop ledger.
- **Parallel closing pair**: one structural triangle can have several identity combinations, equal to the product of three bucket sizes.
- **Parallel wedge arm**: multiply open-wedge instances by the arm bucket sizes while keeping one vertex triple.
- **Self-loop**: exclude by ID; do not count it as a wedge arm or triangle side.
- **Missing closing edge status**: if inventory completeness is unknown, call the wedge open only in the supplied extract.

## Test case
**Input:**
> Fictional Grove S1 contains nodes A,B,C,D,I; ab1 and ab2 join A-B, bc joins B-C, ac joins A-C, cd joins C-D, and loop joins A-A. Give a complete undirected motif census with identity witnesses.

**Assertions:**
1. Structural counts are one triangle triple and two open-wedge triples.
2. Identity-instance counts are two triangles and two open wedges, with ab1 and ab2 kept distinct.
3. The triangle witnesses use A,B,C; wedge witnesses have center C and triples A,C,D and B,C,D.
4. The loop is excluded by ID, I remains in scope, and each witness names source edge IDs.
</skill>

<user_request>
Fictional Grove S1 contains nodes A,B,C,D,I; ab1 and ab2 join A-B, bc joins B-C, ac joins A-C, cd joins C-D, and loop joins A-A. Give a complete undirected motif census with identity witnesses.
</user_request>
