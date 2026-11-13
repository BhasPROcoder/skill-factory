Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-007
name: weak-component-scope-diagnosis
domain: Graph Engineering Foundations
subdomain: Connectivity partitions
version: 1.0
description: Partition a scoped graph into undirected or weakly connected components with membership evidence and filter-boundary explanations when disconnected regions need diagnosis.
triggers: ["find all disconnected graph regions", "include isolated nodes in component analysis", "explain why this filtered graph splits", "partition weakly connected components", "check whether direction changes connectivity claims"]
not_for: ["checking a rooted forest contract [GRF-004]", "bounded traversal from a selected seed", "strongly connected components or directed reachability", "detecting statistical communities or recommending new relationships"]
requires: []
risk_level: medium
---

# Weak Component Scope Diagnosis

## Purpose
Produce a complete component membership table for an explicit graph projection, including inventory-only nodes. Explain which observed separations depend on filtering and preserve evidence that weak connectivity does not imply directed reachability or a meaningful community.

## Inputs to collect
1. **Node inventory and revision** — obtain every scoped node ID, including nodes without edges. Why: edge-derived inventories hide isolates. Default: no complete partition claim without the inventory.
2. **Edge records** — collect stable edge IDs, original source/target, relation type and source locator. Why: membership and filter explanations need traceable relationships. Default: supplied records only; missing coverage remains explicit.
3. **Connectivity question** — establish undirected connectivity or weak connectivity of a directed graph. Why: ignoring direction answers a different question from following arrows. Default: ask; do not reinterpret a directed routing question.
4. **Projection rules** — obtain included nodes, relation types, time/version and any other filters. Why: components belong to a particular projection. Default: retain all supplied nodes and edges unless the question specifies a filter.
5. **Coverage and comparison evidence** — obtain whether the source is complete and whether excluded edges/nodes remain available. Why: a cut in the projection may not exist in the wider graph. Default: no wider-world separation claim.
6. **Use and authority** — obtain the decision that requires this partition and who can correct source records. Why: disconnected regions are not automatically errors. Default: descriptive diagnosis only, with no fabricated connecting edge.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the source revision and write the connectivity definition and exact projection predicate.
2. Validate unique node and edge identities and known endpoints; retain ambiguous or malformed records as exceptions before accepting a partition.
3. Materialize the included node set and included edges separately, preserving excluded records and their exclusion reasons when available.
4. Build an undirected adjacency view for the selected edges; retain original arrow direction and edge IDs in the evidence ledger rather than altering the source.
5. Start an exhaustive traversal at every still-unassigned included node, assigning its entire reachable set to one component without a depth cap.
6. Record discovery edges as a spanning witness for each component; a singleton needs no discovery edge, even if it has self-loops.
7. Verify that membership covers every included node exactly once and every included edge stays within one component. Verify each witness connects its stated members using included source edges.
8. ⚠️ Inspect excluded edges whose endpoints lie in different projected components. Report them as observed links omitted by the projection, not as newly discovered missing links or permission to relax the filter.
9. Distinguish inventory-only isolates from nodes isolated by filtering; if excluded records are unavailable, mark the cause unresolved rather than guessing.
10. Deliver the partition, witness and scope comparison; label wider-graph connectivity unknown when omitted nodes or edges could provide paths.

The following Python 3 reference accepts complete lists of string node IDs and four-field edge tuples `(edge ID, source, target, relation)`. It preserves all supplied nodes and filters only relation types, using an undirected projection regardless of original direction. Validate tuple shape before calling it. Run the snippet with the available interpreter and record its version; this is an in-memory partition, not a database or full-world coverage test.

```python
def partition(nodes, edges, allowed):
    if any(not isinstance(n, str) or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(nodes) != len(set(nodes)):
        raise ValueError("duplicate node ID")
    known, ids = set(nodes), set()
    adjacent = {n: [] for n in nodes}
    kept, excluded = [], []
    for edge in edges:
        eid, src, dst, relation = edge
        if any(not isinstance(x, str) or not x for x in edge):
            raise ValueError("invalid edge field")
        if eid in ids or src not in known or dst not in known:
            raise ValueError("duplicate edge or unknown endpoint")
        ids.add(eid)
        if relation in allowed:
            kept.append(edge)
            adjacent[src].append((dst, eid))
            adjacent[dst].append((src, eid))
        else:
            excluded.append(edge)
    membership, witnesses = {}, {}
    for start in sorted(nodes):
        if start in membership:
            continue
        membership[start] = start
        witnesses[start] = []
        pending = [start]
        while pending:
            node = pending.pop()
            for neighbor, eid in sorted(adjacent[node]):
                if neighbor not in membership:
                    membership[neighbor] = start
                    witnesses[start].append((node, neighbor, eid))
                    pending.append(neighbor)
    crossing = [edge for edge in excluded
                if membership[edge[1]] != membership[edge[2]]]
    assert set(membership) == known
    assert all(membership[s] == membership[t] for _, s, t, _ in kept)
    return membership, witnesses, crossing

nodes = ["A", "B", "C", "D", "E"]
edges = [("p", "A", "B", "work"),
         ("q", "C", "B", "archive"),
         ("r", "C", "D", "work")]
members, witness, omitted = partition(nodes, edges, {"work"})
assert members == {"A": "A", "B": "A", "C": "C", "D": "C", "E": "E"}
assert omitted == [edges[1]]
assert sum(len(v) for v in witness.values()) == 2
assert len(set(partition(nodes, edges, {"work", "archive"})[0].values())) == 2
print("filtered partition, isolates and excluded-link comparison passed")
```

Component labels here use the smallest string ID within the supplied snapshot only. They are reproducible presentation labels, not stable identifiers across changed membership. The witness traversal may oppose an original arrow; it demonstrates weak connectivity only.

## Decision rules
- IF the question requires following directed paths THEN route it to directed traversal BECAUSE weak connectivity deliberately ignores arrow direction.
- IF an excluded edge joins two projected components THEN identify filter-dependent separation BECAUSE the supplied wider graph already contains that link.
- IF an isolated node has no supplied incident records THEN label it inventory-only within supplied coverage BECAUSE absence in an incomplete source cannot prove real isolation.
- IF traversal is capped or interrupted THEN withhold a complete component partition BECAUSE an unexplored path could join apparent regions.
- IF several components remain THEN describe their membership without inventing repairs BECAUSE separation may be intentional and structurally valid.

## Output template
```text
Scope: <revision, node/edge coverage; maximum 70 words>
Projection: <connectivity definition and exact filters; maximum 70 words>
Membership: <node | snapshot-local component label; complete table or attachment>
Witnesses: <component | discovery edge IDs | singleton state; complete table>
Isolation: <node | inventory-only/filter-induced/unresolved | supporting records>
Excluded links: <edge ID | original endpoints | projected components | exclusion reason>
Checks: <coverage, disjointness, internal edges, witness checks; executed/pending>
Interpretation: <supported separation and wider-graph limits; maximum 100 words>
Next action: <source question or no correction needed; maximum 60 words>
```

## Quality checklist
- [ ] Connectivity definition differs explicitly from directed reachability.
- [ ] Every included node appears once, including isolates.
- [ ] Every included edge has endpoints in the same component.
- [ ] Witness edge IDs resolve to included source records.
- [ ] Projection exclusions remain distinguishable from absent evidence.
- [ ] Original edge directions and identities remain recoverable.
- [ ] Component labels are not promised stable across snapshots.
- [ ] Execution and source-completeness limits are stated separately.

## Anti-patterns
- **Edge-only inventory**: omit nodes without selected edges. Fix: seed traversal from the explicit inventory.
- **Arrow overclaim**: equate weak membership with two-way reachability. Fix: preserve the declared projection meaning.
- **Filtered gap becomes defect**: blame the source for a removed relationship. Fix: inspect exclusion evidence first.
- **Artificial bridge**: add a convenient link to make one component. Fix: require domain evidence and separate authorization.
- **Premature partition**: use bounded search fragments as final components. Fix: finish exhaustive traversal or mark incomplete.

## Worked example
**Input:** Fictional studio Hazel supplies complete snapshot H1 from the snippet. Analyze weak components using only work relations while retaining all five nodes. The archive relation q remains available for comparison.

**Output:**
```text
Scope: H1; supplied complete five-node, three-edge fixture.
Projection: Weak connectivity, work relations only; all supplied nodes retained.
Membership: A|A; B|A; C|C; D|C; E|E.
Witnesses: A|p; C|r; E|none, singleton.
Isolation: E|inventory-only|no incident source record in H1.
Excluded links: q|C→B|C and A|archive relation excluded.
Checks: Reference assertions verify coverage and internal edges when executed; witnesses p/r connect their pairs, E needs no edge.
Interpretation: Three projected components. Including q joins A/B/C/D, leaving E separate: two weak components in the supplied wider graph. No claim that B can follow directed edges to C.
Next action: Confirm work-only scope meets the decision; no source correction established.
```

**Bad output:** “Three broken communities; add B→C and delete E.”
This confuses connectivity with community meaning and invents graph changes despite the documented filter and node inventory.

## Edge cases
- **Self-loop or parallel edges**: retain edge identities; these do not connect previously separate endpoint sets by themselves.
- **Empty inventory**: report zero components for the empty supplied graph, not one empty component; any edge then has an invalid endpoint.
- **Node filtering**: record removed nodes and incident edges; paths through them cannot support connectivity in the induced projection.
- **Excluded records unavailable**: report partition only for the observed projection and mark the reason for separation unresolved.
- **Changing snapshot**: freeze one revision or rerun; do not combine membership assignments computed from different edge states.

## Test case
**Input:**
> Fictional nodes P/Q/R/S have directed edges x:P→Q of type live and y:Q→R of type archived. Retain all nodes, select live edges and report weak components; the complete source records are supplied.

**Assertions:**
1. Assigns P/Q together and R and S to separate singleton components.
2. Identifies R as isolated by filtering y and S as inventory-only.
3. Reports y as an excluded link between projected components without adding it automatically.
4. Does not infer a directed path from Q to P or call separation a source defect.
5. States complete membership coverage within the supplied projection.
</skill>

<user_request>
Fictional nodes P/Q/R/S have directed edges x:P→Q of type live and y:Q→R of type archived. Retain all nodes, select live edges and report weak components; the complete source records are supplied.
</user_request>
