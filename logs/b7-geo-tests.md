# Independent recovered GEO review

Reviewer: coordinator, separate from geometry7 author. Six fresh fictional cases run against the actual saved snippets. No renderer or modeling application exercised.

Observed Python: 3.14.6

triangle-shared-edge-winding-check: ed24d14790603ad168982c55a853004b585088c864dd5e8ef975fc7e46908a51
Embedded assertions: shared-edge checks passed

## GEO-001 ordinary

Request: Fictional Birch open sheet has four vertices and faces (0,1,2),(2,1,3). Diagnose only.

Executed result:
```text
{(0, 1): ('boundary', [(0, 0, 1)]), (1, 2): ('opposite traversal', [(0, 1, 2), (1, 2, 1)]), (0, 2): ('boundary', [(0, 2, 0)]), (1, 3): ('boundary', [(1, 1, 3)]), (2, 3): ('boundary', [(1, 3, 2)])}
```

Reviewer output:
```text
Mesh scope: Birch supplied snapshot, four vertices and two ordered faces.
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
1,2 | F0 1->2; F1 2->1 | opposite traversal | no local conflict
0,1;0,2;1,3;2,3 | one each | boundary | retain intended open sheet
Repair proposal: None justified in supplied scope.
Executed checks: Python returned four boundaries and opposite shared traversal.
Unresolved: No coordinates or exterior reference supplied.
Limits: Connectivity only; no geometry or outward orientation verdict.
```

Assertions PASS.

## GEO-001 missing identity

Request: Fictional Birch declares vertices 0 through 2 but references vertex 3.

Executed result:
```text
'invalid triangle'
```

Reviewer output:
```text
Mesh scope: Birch inconsistent vertex extent.
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
unresolved | face includes undeclared 3 | invalid triangle | obtain correct vertex extent or face record
Repair proposal: None; no invented vertex or welding.
Executed checks: ValueError invalid triangle.
Unresolved: Owner must reconcile the identity universe.
Limits: No adjacency verdict from invalid input; no edit performed.
```

Assertions PASS.

## GEO-001 reverse duplicate edge

Request: Fictional Birch provides one triangle and its reversed duplicate; asks if opposite edges prove valid geometry.

Executed result:
```text
{(0, 1): ('opposite traversal', [(0, 0, 1), (1, 1, 0)]), (1, 2): ('opposite traversal', [(0, 1, 2), (1, 2, 1)]), (0, 2): ('opposite traversal', [(0, 2, 0), (1, 0, 2)])}
```

Reviewer output:
```text
Mesh scope: Birch two faces sharing all three vertex identities.
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
0,1;1,2;0,2 | two opposite uses each | opposite traversal | inspect duplicate faces separately
Repair proposal: No automatic removal; ask owner whether duplicate face identities are intended.
Executed checks: All shared edges report opposite traversal even for this duplicate pair.
Unresolved: Duplicate-face disposition and coordinate evidence.
Limits: Passing local edge directions do not establish a valid surface. No geometry certification.
```

Assertions PASS.

uv-triangle-signed-area-inspection: 9d7144913c9f05ca948f6fef13dfab9989211cca3bd758c3fde5f5c976f46a86
Embedded assertions: UV signed-area checks passed

## GEO-002 ordinary

Request: Fictional Elm supplies UV corners (1,1),(4,1),(1,3), fixed axes and zero tolerance.

Executed result:
```text
(6, 3.0, 'positive')
```

Reviewer output:
```text
Mapping scope: Elm supplied UV snapshot and ordered corners, fixed algebraic axes.
Criterion: Zero tolerance; squared UV coordinate units.
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
F | 6 | 3 | positive | no collapse in this calculation
Executed checks: Python result (6,3,positive); edges (3,0),(0,2).
Unresolved: Texture appearance uninspected.
Limits: No distortion or overlap result. No rendering performed.
```

Assertions PASS.

## GEO-002 missing corner

Request: Fictional Elm supplies only two UV corners and asks to assume the last.

Executed result:
```text
'three UV pairs required'
```

Reviewer output:
```text
Mapping scope: Elm incomplete corner record.
Criterion: Exact calculation pending complete input.
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
F | unavailable | unavailable | invalid input | request actual third corner
Executed checks: ValueError three UV pairs required.
Unresolved: Third corner and its face correspondence.
Limits: No fabricated zero-area triangle. No texture quality finding.
```

Assertions PASS.

## GEO-002 tolerance and mirrored intent

Request: Fictional Elm permits a mirrored island; UVs (0,0),(0,0.5),(1,0). Compare supplied trial criteria 0.25 and 0.125 without selecting one for convenience.

Executed result:
```text
((-0.5, 0.25, 'near zero by supplied criterion'), (-0.5, 0.25, 'negative'))
```

Reviewer output:
```text
Mapping scope: Elm same ordered UV corners and axes, intentional mirrored island.
Criterion: Two supplied scenarios, 0.25 and 0.125 squared UV units; neither inferred as a production requirement.
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
F at 0.25 | -0.5 | 0.25 | near zero by supplied criterion | owner decides area acceptance
F at 0.125 | -0.5 | 0.25 | negative | retain authorized mirror
Executed checks: Equality falls inside inclusive criterion; lower criterion changes classification, not the measured area.
Unresolved: Governing acceptance criterion if a release decision is requested.
Limits: Negative sign is not an unauthorized-mirror finding. No rendering, overlap or distortion assessment.
```

Assertions PASS.

## Claim and uniqueness review

GEO-001 concerns directed edge incidence, unlike SPD coordinate handoff and SDR scan evidence preservation. GEO-002 measures per-corner signed area rather than mesh connectivity or texture packing. Specific claims are stable topology/coordinate arithmetic or explicit fixture choices. All numerical expectations above are asserted against actual execution; fictional assets are named as such. Both instructions bound complete-mesh and rendered-quality claims.

Only GEO-001 and GEO-002 are reviewed here. The planned third transform workflow is not created, reviewed or counted by this report.
