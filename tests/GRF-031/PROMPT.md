Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-031
name: graph-bipartition-or-odd-cycle-certificate
domain: Graph Engineering Foundations
subdomain: Bipartition certificates
version: 1.0
description: Produce a complete two-color partition or an explicit odd-cycle witness when deciding whether a supplied undirected graph supports bipartite reasoning.
triggers: ["check whether graph is bipartite", "show an odd cycle witness", "validate a two-color graph partition", "prepare graph sides for matching", "explain why graph cannot have two sides"]
not_for: ["optimizing a supplied bipartite matching [GRF-011]", "finding unchanged connected components [GRF-007]", "validating declared parent forests [GRF-004]", "directed cycle detection", "choosing a minimum edge deletion repair"]
requires: []
risk_level: medium
---

# Graph Bipartition or Odd Cycle Certificate

## Purpose
Decide whether every selected undirected edge can connect opposite sides of a two-color partition. Return either a coloring covering the complete supplied inventory or a closed odd-cycle witness explaining the obstruction. Structural sides do not establish business roles or authorize changing relationships.

## Inputs to collect
1. **Graph inventory** — obtain node IDs and separately identified edge endpoints. Why: isolates, loops and parallel records must survive interpretation. Default: none; required before a complete verdict.
2. **Undirected interpretation** — confirm whether edges are already undirected or which explicit projection is intended. Why: silently ignoring direction changes the question. Default: unresolved; ask for the interpretation.
3. **Snapshot and selection** — obtain revision, included relation types and completeness evidence. Why: excluding a conflicting edge can change the verdict. Default: supplied extract only, wider graph unknown.
4. **Identity policy** — obtain scoped node identities and unresolved aliases. Why: merging distinct nodes can create or remove an obstruction. Default: preserve exact supplied IDs, no inferred merges.
5. **Execution boundary** — identify the available interpreter and permitted workload. Why: a partial coloring cannot prove the remaining graph is bipartite. Default: a small offline fixture with real execution reported separately.
6. **Consumer purpose** — identify the downstream use and any externally fixed side assignments. Why: a mathematical coloring may disagree with required business sides. Default: structural decision only; fixed-side feasibility is a separate additional constraint.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the inventory, projection and snapshot boundary before testing.
2. Validate unique node and edge identities and known endpoints.
3. Build undirected adjacency while retaining each original edge ID.
4. Start a new traversal at every uncolored node, including isolates, and assign its root color zero.
5. Assign each newly reached neighbor the opposite color and retain its discovery parent and edge.
6. When an edge joins equal colors, reconstruct the tree route between its endpoints and close it with that conflicting edge.
7. Verify the resulting cycle closes, has odd edge count, contains no repeated internal vertex and uses the listed actual edges.
8. If every component completes without conflict, verify every inventory node has a color and every selected edge crosses colors.
9. ⚠️ Distinguish an early negative witness from incomplete positive exploration; a valid odd cycle suffices for rejection, but a partial coloring never certifies the entire graph.
10. Report the certificate and coverage together, preserving excluded-edge and unresolved-identity limitations.
11. Route any suggested edge removal or reassignment to separate owner review instead of deleting an arbitrary witness edge.

The Python 3 reference handles finite lists of string nodes and `(edge_ID, endpoint_A, endpoint_B)` tuples. Prevalidate tuple shapes and string fields. Run the snippet and record the actual interpreter version. It uses deterministic ordering for the supplied identifiers and returns either a complete color map or one cycle as ordered vertices and edge IDs. It is an offline certificate builder, not a scale or deployment claim.

```python
from collections import deque

def certify(nodes, edges):
    if len(set(nodes)) != len(nodes) or len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate identity")
    adj = {n: [] for n in nodes}
    for eid, a, b in sorted(edges):
        if a not in adj or b not in adj:
            raise ValueError("unknown endpoint")
        adj[a].append((b, eid))
        adj[b].append((a, eid))
    color, parent = {}, {}
    def ancestry(v):
        vertices, links = [v], []
        while parent[v] is not None:
            v, eid = parent[v]
            vertices.append(v)
            links.append(eid)
        return vertices[::-1], links[::-1]
    for root in sorted(nodes):
        if root in color:
            continue
        color[root], parent[root] = 0, None
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v, eid in adj[u]:
                if v not in color:
                    color[v], parent[v] = 1-color[u], (u, eid)
                    queue.append(v)
                elif color[v] == color[u]:
                    pu, eu = ancestry(u)
                    pv, ev = ancestry(v)
                    i = 0
                    while i < min(len(pu), len(pv)) and pu[i] == pv[i]:
                        i += 1
                    vertices = pu[i-1:][::-1] + pv[i:] + [u]
                    links = eu[i-1:][::-1] + ev[i-1:] + [eid]
                    return None, (vertices, links)
    return color, None

def verify(nodes, edges, result):
    color, cycle = result
    if cycle is None:
        return (color is not None and set(color) == set(nodes)
                and all(type(c) is int and c in (0, 1) for c in color.values())
                and all(color[a] != color[b] for _, a, b in edges))
    vertices, links = cycle
    lookup = {eid: {a, b} for eid, a, b in edges}
    return (color is None and len(links) % 2 == 1
            and len(vertices) == len(links)+1 and vertices[0] == vertices[-1]
            and len(set(vertices[:-1])) == len(vertices)-1
            and all(v in nodes for v in vertices)
            and all(eid in lookup and lookup[eid] == {a, b}
                    for eid, a, b in zip(links, vertices, vertices[1:])))

nodes = ["A", "B", "C", "I"]
edges = [("ab", "A", "B"), ("bc", "B", "C"), ("ca", "C", "A")]
result = certify(nodes, edges)
assert result[0] is None and verify(nodes, edges, result)
assert len(result[1][1]) == 3
parallel = [("p1", "A", "B"), ("p2", "A", "B")]
assert verify(nodes, parallel, certify(nodes, parallel))
assert verify(["A"], [("loop", "A", "A")], certify(["A"], [("loop", "A", "A")]))
print("odd-cycle, parallel-edge and self-loop certificates checked")
```

The verifier assumes the same validated inventory used by the builder. A self-loop gives a closed one-edge odd cycle. Parallel undirected edges do not alone prevent opposite endpoint colors. Disconnected components may independently swap colors; the returned orientation is not unique and is not an inferred semantic classification.

## Decision rules
- IF a verified odd cycle is present THEN reject bipartiteness within that scope BECAUSE alternating two colors cannot close an odd cycle consistently.
- IF all nodes and edges pass a completed coloring check THEN accept the structural partition BECAUSE every selected edge connects opposite colors.
- IF execution stops without a verified obstruction THEN leave the whole-graph verdict unresolved BECAUSE unchecked edges may conflict.
- IF external side assignments matter THEN check them separately BECAUSE structural color names are arbitrary.
- IF the graph is a partial extract THEN limit a positive verdict to it BECAUSE omitted edges may introduce an odd cycle.

## Output template
```text
Scope: <revision, projection and coverage; maximum 60 words>
Verdict: <bipartite / not bipartite / unresolved>
Certificate: <complete color map OR closed vertex sequence and matching edge sequence OR pending>
Verification: <node coverage, crossing-edge or odd-cycle checks; executed/pending>
Limits: <excluded records, orientation ambiguity and semantic limits; maximum 80 words>
Next action: <owner and startable step; maximum 40 words>
```

## Quality checklist
- [ ] Undirected interpretation is explicitly approved.
- [ ] Node and edge IDs were validated before dictionary construction.
- [ ] A positive certificate covers isolated and disconnected nodes.
- [ ] Every selected edge crosses colors in a positive certificate.
- [ ] A negative certificate closes with odd edge count.
- [ ] Cycle vertices and edge IDs replay against the same snapshot.
- [ ] Incomplete exploration is never reported as complete positive evidence.
- [ ] No structural color is silently treated as a business role.

## Anti-patterns
- **Any cycle rejects**: reject an even cycle. Fix: verify odd length and the actual edges.
- **Parallel collapse confusion**: mistake two edge IDs for an odd cycle. Fix: inspect endpoint colors and closed witness length.
- **First component only**: approve after checking one region. Fix: visit every uncolored inventory node.
- **Arbitrary repair**: delete a witness edge without source review. Fix: return the obstruction for owner adjudication.

## Worked example
**Input:** Fictional triangle A/B/C has edges ab,bc,ca; I is isolated. Use undirected semantics and inspect the supplied complete exercise inventory.

**Output:**
```text
Scope: Fictional T1; undirected triangle and isolated I; supplied exercise only.
Verdict: Not bipartite.
Certificate: Vertices B,A,C,B; edges ab,ca,bc.
Verification: Expected closed three-edge witness with distinct B/A/C internal vertices; execute reference and verifier to record confirmation.
Limits: One obstruction suffices; no complete coloring exists for this graph. No identity or business-role conclusion and no authorized deletion.
Next action: Graph owner verifies the three source relationships before considering a separate correction.
```

**Bad output:** “Delete bc and assign the remaining colors as mandatory business roles.”
This invents repair authority and semantic meaning absent from the inputs.

## Edge cases
- **Empty graph**: return an empty complete coloring if the intended inventory is explicitly empty.
- **Self-loop**: return its node twice and its single edge ID as the obstruction.
- **Disconnected inventory**: inspect all components for a positive verdict; retain isolates.
- **Fixed side constraints**: report structural coloring separately from compatibility with fixed assignments.
- **Directed input without projection policy**: ask for the intended semantics before treating arrows as undirected edges.

## Test case
**Input:**
> Fictional graph has parallel A/B edges, an isolated I, and a separate triangle X/Y/Z. Can the whole undirected graph be split into two sides?

**Assertions:**
1. Rejects the whole graph using a verified triangle witness.
2. Does not blame the parallel A/B edges or isolated I.
3. Gives the closed vertex and corresponding edge sequences.
4. Makes no automatic deletion or semantic-role assignment.
</skill>

<user_request>
Fictional graph has parallel A/B edges, an isolated I, and a separate triangle X/Y/Z. Can the whole undirected graph be split into two sides?
</user_request>
