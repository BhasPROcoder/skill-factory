"""Independent coordinator fixtures for the two recovered geometry skills."""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
report = ['# Independent recovered GEO review', '',
          'Reviewer: coordinator, separate from geometry7 author. Six fresh fictional cases run against the actual saved snippets. No renderer or modeling application exercised.', '',
          'Observed Python: ' + sys.version.split()[0], '']

def load(name):
    p = ROOT / 'skills' / 'GEO' / name / 'SKILL.md'
    data = p.read_bytes()
    ns = {}
    with contextlib.redirect_stdout(io.StringIO()) as output:
        for block in re.findall(r'```python\s*\n(.*?)```', data.decode('utf-8'), re.S):
            exec(compile(block, str(p), 'exec'), ns)
    report.extend([name + ': ' + hashlib.sha256(data).hexdigest(),
                   'Embedded assertions: ' + output.getvalue().strip(), ''])
    return ns

def case(title, request, result, response):
    report.extend(['## ' + title, '', 'Request: ' + request, '',
                   'Executed result:', '```text', repr(result), '```', '',
                   'Reviewer output:', '```text', response, '```', '', 'Assertions PASS.', ''])

edge = load('triangle-shared-edge-winding-check')['edge_report']
faces = [(0,1,2),(2,1,3)]
r = edge(4, faces)
assert r[(1,2)][0] == 'opposite traversal'
assert sum(v[0]=='boundary' for v in r.values()) == 4
case('GEO-001 ordinary', 'Fictional Birch open sheet has four vertices and faces (0,1,2),(2,1,3). Diagnose only.', r,
'''Mesh scope: Birch supplied snapshot, four vertices and two ordered faces.
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
1,2 | F0 1->2; F1 2->1 | opposite traversal | no local conflict
0,1;0,2;1,3;2,3 | one each | boundary | retain intended open sheet
Repair proposal: None justified in supplied scope.
Executed checks: Python returned four boundaries and opposite shared traversal.
Unresolved: No coordinates or exterior reference supplied.
Limits: Connectivity only; no geometry or outward orientation verdict.''')
try:
    edge(3, [(0,1,3)])
except ValueError as exc:
    r = str(exc)
else:
    raise AssertionError('Undeclared vertex accepted')
case('GEO-001 missing identity', 'Fictional Birch declares vertices 0 through 2 but references vertex 3.', r,
'''Mesh scope: Birch inconsistent vertex extent.
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
unresolved | face includes undeclared 3 | invalid triangle | obtain correct vertex extent or face record
Repair proposal: None; no invented vertex or welding.
Executed checks: ValueError invalid triangle.
Unresolved: Owner must reconcile the identity universe.
Limits: No adjacency verdict from invalid input; no edit performed.''')
r = edge(3, [(0,1,2),(2,1,0)])
assert all(v[0]=='opposite traversal' for v in r.values())
case('GEO-001 reverse duplicate edge', 'Fictional Birch provides one triangle and its reversed duplicate; asks if opposite edges prove valid geometry.', r,
'''Mesh scope: Birch two faces sharing all three vertex identities.
Edge findings:
Endpoint pair | Incident faces/directions | Classification | Next check
0,1;1,2;0,2 | two opposite uses each | opposite traversal | inspect duplicate faces separately
Repair proposal: No automatic removal; ask owner whether duplicate face identities are intended.
Executed checks: All shared edges report opposite traversal even for this duplicate pair.
Unresolved: Duplicate-face disposition and coordinate evidence.
Limits: Passing local edge directions do not establish a valid surface. No geometry certification.''')

area = load('uv-triangle-signed-area-inspection')['uv_area']
r = area([(1,1),(4,1),(1,3)])
assert r == (6,3,'positive')
case('GEO-002 ordinary', 'Fictional Elm supplies UV corners (1,1),(4,1),(1,3), fixed axes and zero tolerance.', r,
'''Mapping scope: Elm supplied UV snapshot and ordered corners, fixed algebraic axes.
Criterion: Zero tolerance; squared UV coordinate units.
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
F | 6 | 3 | positive | no collapse in this calculation
Executed checks: Python result (6,3,positive); edges (3,0),(0,2).
Unresolved: Texture appearance uninspected.
Limits: No distortion or overlap result. No rendering performed.''')
try:
    area([(0,0),(1,0)])
except ValueError as exc:
    r = str(exc)
else:
    raise AssertionError('Missing UV corner accepted')
case('GEO-002 missing corner', 'Fictional Elm supplies only two UV corners and asks to assume the last.', r,
'''Mapping scope: Elm incomplete corner record.
Criterion: Exact calculation pending complete input.
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
F | unavailable | unavailable | invalid input | request actual third corner
Executed checks: ValueError three UV pairs required.
Unresolved: Third corner and its face correspondence.
Limits: No fabricated zero-area triangle. No texture quality finding.''')
r = area([(0,0),(0,0.5),(1,0)],0.25)
assert r == (-0.5,0.25,'near zero by supplied criterion')
above = area([(0,0),(0,0.5),(1,0)],0.125)
assert above[2] == 'negative'
case('GEO-002 tolerance and mirrored intent', 'Fictional Elm permits a mirrored island; UVs (0,0),(0,0.5),(1,0). Compare supplied trial criteria 0.25 and 0.125 without selecting one for convenience.', (r,above),
'''Mapping scope: Elm same ordered UV corners and axes, intentional mirrored island.
Criterion: Two supplied scenarios, 0.25 and 0.125 squared UV units; neither inferred as a production requirement.
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
F at 0.25 | -0.5 | 0.25 | near zero by supplied criterion | owner decides area acceptance
F at 0.125 | -0.5 | 0.25 | negative | retain authorized mirror
Executed checks: Equality falls inside inclusive criterion; lower criterion changes classification, not the measured area.
Unresolved: Governing acceptance criterion if a release decision is requested.
Limits: Negative sign is not an unauthorized-mirror finding. No rendering, overlap or distortion assessment.''')
report.extend(['## Claim and uniqueness review', '',
    'GEO-001 concerns directed edge incidence, unlike SPD coordinate handoff and SDR scan evidence preservation. GEO-002 measures per-corner signed area rather than mesh connectivity or texture packing. Specific claims are stable topology/coordinate arithmetic or explicit fixture choices. All numerical expectations above are asserted against actual execution; fictional assets are named as such. Both instructions bound complete-mesh and rendered-quality claims.', '',
    'Only GEO-001 and GEO-002 are reviewed here. The planned third transform workflow is not created, reviewed or counted by this report.'])
(ROOT/'logs'/'b7-geo-tests.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('PASS six fresh GEO cases plus embedded assertions; saved logs/b7-geo-tests.md')
