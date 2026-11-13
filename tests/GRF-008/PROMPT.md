Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-008
name: strong-component-condensation-analysis
domain: Graph Engineering Foundations
subdomain: Strong connectivity and condensation
version: 1.0
description: Partition a directed graph into maximal mutually reachable regions and construct an acyclic inter-region view with original edge evidence when feedback groups obscure dependency structure.
triggers: ["find all strongly connected regions", "condense this directed graph", "separate feedback groups from downstream dependencies", "retain edge evidence after graph contraction", "check singleton cycles in a component graph"]
not_for: ["returning one prerequisite cycle witness [SEQ-001]", "weak connectivity ignoring direction [GRF-007]", "bounded traversal from one seed [GRF-006]", "deciding which dependency to remove or scheduling a cyclic group"]
requires: []
risk_level: medium
---

# Strong Component Condensation Analysis

## Purpose
Expose every maximal region whose nodes can reach one another by directed paths, then summarize the relationships between those regions. Preserve internal relationships and source edges so contraction remains an explanatory view rather than an apparent repair. An acyclic component view does not make the original feedback groups executable.

## Inputs to collect
1. **Node inventory and snapshot** — obtain unique IDs including isolated nodes and the source revision. Why: an edge-only inventory omits singleton components. Default: no complete partition claim without the inventory.
2. **Directed edge evidence** — obtain unique edge IDs, endpoints, relation meaning and source locators. Why: reachability depends on arrow interpretation. Default: unresolved direction requires clarification, not an undirected approximation.
3. **Projection contract** — obtain selected relation types, node exclusions and time/version boundary. Why: mixing relations or historical states can create unsupported feedback. Default: use the supplied graph as a labeled scope; do not silently filter it.
4. **Coverage and scale** — obtain whether the scoped records are complete and available execution limits. Why: missing paths can split a true component. Default: claims apply only to supplied records; use the small reference only for manageable in-memory inputs.
5. **Downstream use** — identify whether the view supports debugging, dependency review or another decision, including the direction required for any ordering. Why: topological order does not supply domain scheduling authority. Default: structural analysis only, no repair or execution commitment.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the inventory and directed projection, retaining the original snapshot and any excluded-record ledger.
2. Validate unique node and edge identities and declared endpoints before computing reachability; reject ambiguous inputs without inventing nodes or removing repeated relationships.
3. Compute directed reachability across the entire scoped graph without a depth cutoff. For large inputs, use a suitable tested strong-component implementation and verify its current interface in official documentation.
4. Group nodes by mutual reachability: each pair in a group must reach each other, and no outside node may satisfy that condition with the group. Include every inventory node exactly once.
5. Assign snapshot-local component labels and retain the complete node-to-component mapping. Do not treat labels as durable identities across revisions.
6. Classify a region as cyclic when it contains several nodes or a singleton with a self-loop. Preserve singleton regions without self-loops as noncyclic.
7. Classify every original edge as internal or crossing. Aggregate crossing edges by ordered component pair while retaining every original edge ID and source locator.
8. ⚠️ Remove internal edges only from the inter-region view, never from source evidence. Contraction hides internal cycles visually; it does not resolve their domain meaning.
9. Verify partition coverage, mutual reachability, maximality, edge provenance coverage and acyclicity of the condensed view. A condensed cycle indicates a partition or construction error under the same scoped graph.
10. Deliver the component ledger and condensed edges with internal-cycle evidence and limits. If an ordering is requested, state its arrow convention and keep cyclic-group execution unresolved until domain policy supplies a valid interpretation.

This Python 3 reference computes reachability separately from every node, so it prioritizes inspectability over large-graph efficiency. It accepts finite lists of nonempty string node IDs and edge triples `(edge ID, source, target)`; validate tuple shape before calling. Run the complete snippet and record the installed interpreter version. Original edge IDs act as source locators in this fixture; production records need their own locator mapping.

```python
def condense(nodes, edges):
    if any(not isinstance(n, str) or not n for n in nodes):
        raise ValueError("invalid node ID")
    known = set(nodes)
    if len(known) != len(nodes):
        raise ValueError("duplicate node ID")
    adjacency = {n: set() for n in nodes}
    ids = set()
    for eid, source, target in edges:
        if any(not isinstance(x, str) or not x
               for x in (eid, source, target)):
            raise ValueError("invalid edge field")
        if eid in ids or source not in known or target not in known:
            raise ValueError("duplicate edge or unknown endpoint")
        ids.add(eid)
        adjacency[source].add(target)
    reach = {}
    for start in nodes:
        seen, pending = {start}, [start]
        while pending:
            for target in adjacency[pending.pop()]:
                if target not in seen:
                    seen.add(target)
                    pending.append(target)
        reach[start] = seen
    groups, membership = {}, {}
    for start in sorted(nodes):
        if start not in membership:
            group = sorted(n for n in nodes
                           if n in reach[start] and start in reach[n])
            groups[start] = group
            membership.update((n, start) for n in group)
    internal = {c: [] for c in groups}
    crossing = {}
    for eid, source, target in edges:
        a, b = membership[source], membership[target]
        if a == b:
            internal[a].append(eid)
        else:
            crossing.setdefault((a, b), []).append(eid)
    cyclic = {c: len(group) > 1 or bool(internal[c])
              for c, group in groups.items()}
    remaining, order = set(groups), []
    while remaining:
        ready = sorted(c for c in remaining
                       if not any(a in remaining and b == c
                                  for a, b in crossing))
        if not ready:
            raise AssertionError("condensed cycle")
        order.extend(ready)
        remaining.difference_update(ready)
    return groups, internal, crossing, cyclic, order

nodes = ["A", "B", "C", "D", "E"]
edges = [("p", "A", "B"), ("q", "B", "A"),
         ("r", "B", "C"), ("s", "A", "C"),
         ("t", "C", "D"), ("u", "D", "C")]
g, inside, between, cycles, order = condense(nodes, edges)
assert g == {"A": ["A", "B"], "C": ["C", "D"], "E": ["E"]}
assert between == {("A", "C"): ["r", "s"]}
assert inside == {"A": ["p", "q"], "C": ["t", "u"], "E": []}
assert cycles == {"A": True, "C": True, "E": False}
assert order.index("A") < order.index("C")
assert condense(["X"], [("loop", "X", "X")])[3] == {"X": True}
print("partition, provenance, condensed order and singleton checks passed")
```

## Decision rules
- IF two nodes are linked only in one direction THEN do not merge them BECAUSE strong connectivity requires return reachability too.
- IF a singleton has a self-loop THEN retain its cyclic classification BECAUSE component size alone does not detect that cycle.
- IF crossing edges share a component pair THEN aggregate their display while retaining all edge evidence BECAUSE a single summary arrow does not mean one source relationship.
- IF a condensed cycle remains THEN reject the result and inspect the partition BECAUSE mutually reachable components should have formed one maximal group.
- IF coverage is incomplete THEN qualify the partition BECAUSE omitted return paths can join apparently separate regions.

## Output template
```text
Scope: <revision, arrow meaning, projection and coverage; maximum 80 words>
Components: <label | all member IDs | cyclic/noncyclic; full table>
Internal evidence: <component | original edge IDs and source locators; full ledger>
Condensed edges: <source component | target component | original edge evidence>
Checks: <partition, mutual reachability/maximality, edge coverage, DAG; executed or pending>
Interpretation: <structural order if requested, direction and unresolved group behavior; maximum 100 words>
Limits: <coverage, scale, semantic and execution limits; maximum 70 words>
```

## Quality checklist
- [ ] Original direction and selected relation scope are explicit.
- [ ] Every inventory node appears in exactly one component.
- [ ] Group membership requires reachability in both directions.
- [ ] Singleton self-loops remain classified as cyclic.
- [ ] Every original edge remains in internal or crossing evidence.
- [ ] Condensed arrows retain their original ordered direction.
- [ ] The condensed view passes acyclicity checks or is rejected.
- [ ] Structural grouping is separated from domain repair and execution.

## Anti-patterns
- **Weak becomes strong**: merge nodes because an undirected path exists. Fix: require both directed paths.
- **One cycle defines all groups**: stop after the first witness. Fix: partition the entire inventory.
- **Cycles cured by drawing**: call a contracted group repaired. Fix: retain its internal-cycle evidence.
- **Parallel evidence loss**: keep only one edge per component pair. Fix: attach all original edge identities.
- **Stable label fiction**: reuse a component label as a permanent entity ID. Fix: bind labels to snapshot membership.

## Worked example
**Input:** Fictional team Hazel supplies the snippet graph H1. Arrows indicate directed dependency links, without a confirmed scheduling convention. All listed records are complete for H1; no changes are authorized.

**Output:**
```text
Scope: H1 supplied directed links, no filters; complete fictional inventory A/B/C/D/E.
Components: A | A,B | cyclic; C | C,D | cyclic; E | E | noncyclic.
Internal evidence: A | p:A→B,q:B→A; C | t:C→D,u:D→C; E | none. Edge IDs locate H1 records.
Condensed edges: A | C | r:B→C,s:A→C; both source records retained.
Checks: Reference assertions check partition, source-edge classification and acyclic component order when executed. Mutual reachability gives A/B and C/D; no return path joins the groups.
Interpretation: A precedes C in an arrow-respecting structural order. No operational scheduling order asserted; internal feedback remains unresolved.
Limits: H1 only; no production-scale test, dependency repair or live execution.
```

**Bad output:** “The new graph has no cycles, so run A/B together, then C/D; discard their internal edges.”
This invents an execution policy and destroys the evidence of unresolved original cycles.

## Edge cases
- **Empty graph**: return empty membership and edge ledgers; do not imply evidence completeness.
- **Isolated node**: retain a singleton noncyclic component with no internal edges.
- **Parallel crossing relationships**: show one ordered summary pair and all original edge IDs.
- **Partial extract**: report scoped components and missing coverage; do not claim maximality in the unseen graph.
- **Resource exhaustion**: mark analysis incomplete; a partial traversal cannot establish a complete partition.

## Test case
**Input:**
> Fictional directed graph has a:X→Y, b:Y→X, c:Y→Z, d:Z→Z and isolated W. Produce all strong components and the condensed edge evidence; no execution policy is supplied.

**Assertions:**
1. Groups X/Y together and retains Z and W as separate singleton components.
2. Marks X/Y and self-loop singleton Z cyclic, but W noncyclic.
3. Retains c as crossing evidence and a/b/d as internal evidence.
4. Does not claim contraction resolves cycles or authorizes an execution schedule.
</skill>

<user_request>
Fictional directed graph has a:X→Y, b:Y→X, c:Y→Z, d:Z→Z and isolated W. Produce all strong components and the condensed edge evidence; no execution policy is supplied.
</user_request>
