---
id: GEO-001
name: triangle-shared-edge-winding-check
domain: Mesh Geometry Diagnostics
subdomain: Edge orientation
version: 1.0
description: Inspect indexed triangle winding across shared edges when adjacent faces may traverse their common edge in the same direction.
triggers: ["check triangle winding", "find inconsistent shared edges", "inspect mesh edge orientation", "diagnose reversed adjacent faces", "separate boundaries from winding defects"]
not_for: ["coordinate transfer contracts [SPD-001]", "scan cleanup provenance [SDR-002]", "proving watertightness or printable geometry", "automatic surface reconstruction"]
requires: []
risk_level: medium
---

# Triangle Shared-Edge Winding Check

## Purpose
Build an edge-incidence report that distinguishes boundary edges, consistently traversed shared edges, same-direction conflicts and edges with more than two incident triangles. Use the report to localize orientation questions without calling the whole mesh valid or choosing an outward direction from connectivity alone.

## Inputs to collect
1. **Indexed triangles** — obtain a frozen face list with three vertex identifiers per face; this establishes adjacency without guessing from nearby coordinates. Default: none, required.
2. **Vertex identity scope** — obtain the vertex count and any intended seam duplication; this establishes valid indices and whether coincident positions are intentionally separate. Default: no welding or coordinate-based merging.
3. **Surface intent** — identify expected openings, sheets and disconnected components because boundary edges can be deliberate. Default: classify boundaries without calling them defects.
4. **Orientation evidence** — obtain a trusted face orientation or exterior reference if repair is requested. Default: diagnostic report only; no outward-normal claim.
5. **Execution boundary** — identify a copied mesh representation and permission to modify it. Default: read-only Python 3 fixture check, no application edits.

If a required input is missing and has no safe default, ask in one message with at most three questions. Group topology identity, surface intent and permitted repair evidence.

## Procedure
1. Freeze the mesh revision and retain face indices so each reported edge can be found in the source. A reordered export needs its own mapping rather than reusing old face numbers.
2. Validate that each face contains three distinct integer indices within the declared vertex extent. Reject malformed topology before building an adjacency conclusion; geometric zero-area faces with distinct indices require a separate coordinate check.
3. Enumerate each face's directed edges in its stored vertex order. Keep both the unordered endpoint pair for grouping and the original direction for comparison.
4. Group all edge uses by the unordered pair. Do not weld nearby vertices: a seam with duplicate identities remains disconnected under this topology, even if the positions look identical.
5. Classify each group by incident-use count and direction. One use is a boundary, two opposite traversals are locally consistent, two identical traversals conflict, and more than two uses require a separate incidence review.
6. Inspect conflicting faces together with trusted orientation evidence. ⚠️ Reversing the first reported face can move a conflict to another neighbor; propose a component-level orientation plan before authorizing a repair.
7. Report disconnected or uninspected regions explicitly. An all-consistent edge report does not prove absence of self-intersection, duplicate faces, degenerate coordinates, holes or unintended disconnected shells.
8. Execute the reference and map its findings back to the actual face identifiers. If a repair is approved, rerun the report on the repaired revision and preserve a record of changed face order.

This Python 3 reference accepts a nonnegative vertex count and triangles of integer indices. It reports topology only; no coordinates, normal vectors or application-specific mesh API are used. Save the code as a script, run it, and record the installed interpreter version. The face-order convention is authored for this fixture, not a claim about an importer's behavior.

```python
def edge_report(vertex_count, faces):
    if type(vertex_count) is not int or vertex_count < 0:
        raise ValueError("invalid vertex count")
    uses = {}
    for fid, face in enumerate(faces):
        if (len(face) != 3 or any(type(v) is not int for v in face)
                or len(set(face)) != 3
                or any(v < 0 or v >= vertex_count for v in face)):
            raise ValueError("invalid triangle")
        a, b, c = face
        for u, v in ((a, b), (b, c), (c, a)):
            edge = tuple(sorted((u, v)))
            uses.setdefault(edge, []).append((fid, u, v))
    result = {}
    for edge, entries in uses.items():
        if len(entries) == 1:
            state = "boundary"
        elif len(entries) > 2:
            state = "multiple incidence"
        elif entries[0][1:] == entries[1][1:]:
            state = "direction conflict"
        else:
            state = "opposite traversal"
        result[edge] = (state, entries)
    return result

bad = edge_report(4, [(0, 1, 2), (1, 2, 3)])
assert bad[(1, 2)][0] == "direction conflict"
good = edge_report(4, [(0, 1, 2), (2, 1, 3)])
assert good[(1, 2)][0] == "opposite traversal"
assert sum(v[0] == "boundary" for v in good.values()) == 4
multi = edge_report(5, [(0, 1, 2), (1, 0, 3), (0, 1, 4)])
assert multi[(0, 1)][0] == "multiple incidence"
try:
    edge_report(3, [(0, 0, 2)])
except ValueError:
    pass
else:
    raise AssertionError("repeated vertex accepted")
print("shared-edge checks passed")
```

## Decision rules
- IF a shared edge has identical directed traversals THEN flag the incident face pair BECAUSE those stored windings disagree locally across that edge.
- IF an edge has one incident face THEN report a boundary without automatic repair BECAUSE an open sheet may be intentional.
- IF more than two faces use an edge THEN separate incidence review from pairwise winding repair BECAUSE flipping one face does not resolve the attachment structure.
- IF outward direction is unspecified THEN leave it undecided BECAUSE reversing every face preserves opposite traversal relationships.
- IF coordinates coincide but indices differ THEN preserve the identity distinction BECAUSE a weld would change topology and needs its own authorization.

## Output template
```text
Mesh scope: <revision, vertex extent, face identities; up to three lines>
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
<up to twelve rows; provide full report separately if longer>
Repair proposal: <up to four actions with required orientation evidence, or None>
Executed checks: <up to five inputs, observed outcomes and environment>
Unresolved: <up to three questions>
Limits: <two sentences distinguishing topology from geometry and outward orientation>
```

## Quality checklist
- [ ] Face identity maps to the inspected revision.
- [ ] Each triangle has valid distinct integer indices.
- [ ] Directed uses are retained beside unordered edge keys.
- [ ] Boundaries, pair conflicts and multiple incidence are separate states.
- [ ] Coincident coordinates are not silently welded.
- [ ] Repair requests identify the evidence for orientation choice.
- [ ] A passing local report is not called watertight or printable.
- [ ] Original face order remains unchanged unless a separate edit was authorized.

## Anti-patterns
- **Boundary panic**: every single-use edge is filled. Fix: compare with intended openings before any geometric edit.
- **Local flip cascade**: individual faces are reversed until the first warning disappears. Fix: examine component relationships and recheck every affected neighbor.
- **Outward by majority**: local agreement is treated as exterior orientation. Fix: obtain an exterior witness or leave direction unresolved.
- **Coordinate welding shortcut**: close vertices are merged to reduce warnings. Fix: retain index topology and review welding separately.
- **Geometry certification**: consistent edge traversal is called a complete mesh validation. Fix: list the untested geometric properties explicitly.

## Worked example
**Input:**
> Fictional asset Cedar has four vertices and faces F0=(0,1,2), F1=(1,2,3). It is an intentionally open sheet. No exterior reference or repair permission is supplied. Inspect shared-edge winding only.

**Output:**
```text
Mesh scope: Cedar supplied revision, four vertices, F0 and F1 as listed.
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
1,2 | F0:1→2; F1:1→2 | direction conflict | inspect component orientation before proposing a flip
0,1; 0,2; 1,3; 2,3 | one use per edge | boundary | preserve intended open-sheet boundary
Repair proposal: No edit performed; obtain a trusted orientation if repair is requested.
Executed checks: Reference fixture identifies same-direction traversal on 1,2; a separately constructed reversed-face fixture changes that relationship to opposite traversal.
Unresolved: Which face or exterior reference should govern an authorized repair?
Limits: Local topology only. No geometric degeneracy, intersection or outward-direction claim.
```

**Bad output:** “Flip F1 and close every boundary; the mesh is now production-ready.”
This invents repair permission and surface intent, then claims geometric validity from an edge check.

## Edge cases
- **Duplicate triangle with reverse order**: opposite traversals can still occur on coincident duplicate faces; review duplicate-face identity separately.
- **Empty face list**: return an empty report and state that no surface was inspected, rather than a meaningful whole-asset pass.
- **Coordinate-degenerate face**: distinct valid indices do not prove nonzero area; request coordinates for a separate geometric check.
- **Disconnected components**: retain separate orientation decisions and do not propagate one exterior witness across unrelated components without evidence.

## Test case
**Input:**
> Fictional mesh has three triangles using edge (0,1), and its owner suggests flipping one triangle to make it manifold. No reconstruction policy is supplied.

**Assertions:**
1. Reports multiple incidence rather than an ordinary two-face winding conflict.
2. Does not claim flipping alone resolves the attachment count.
3. Retains the incident face identities for owner review.
4. Makes no complete geometric-validity claim.
