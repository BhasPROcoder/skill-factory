# Batch 7 independent GEO-003 review

Reviewer: finish_schedule; author: finish_geometry. No skill edits.
Source SHA256: 90a69f93cbc1ab376cb13fa2cb68289cf11d7417cf8a067fa994837e99fd5ee0
Interpreter: Python 3.14.6.
Executed embedded assertions and fresh cases below. Arithmetic oracle uses pivot plus independently expected basis displacements. No external application or renderer exercised.

## Normal request: fictional Moss scene
Input: p=(3,1,5), c=(1,2,3), s=(2,3,4), R=((0,-1,0),(1,0,0),(0,0,1)), t=(5,-1,2), A=((1,0,1),(0,2,0),(0,0,1)), b=(0,1,-2). Column-vector chain, scene units, rotation tolerance zero, no observations.

```text
Contract: Object-local to parent by pivot-relative scale, rotation, pivot restoration, translation; then parent affine mapping to world. Column vectors, scene units.
Inputs: Moss P=(3,1,5), c=(1,2,3), s=(2,3,4); R, t, A and b as supplied in the test input.
Trace: P: (2,-1,2) | (4,-3,8) | (3,4,8) | (9,5,13) | (22,11,11).
Checks: Executed Python trace and embedded assertions. Pivot world=(11,3,3); basis offsets x=(0,4,0), y=(-3,0,0), z=(4,0,4). Pivot plus 2x-y+2z independently gives (22,11,11).
Comparison: No observed coordinates; no acceptance verdict.
Next: Obtain the same point's exported world position and comparison tolerance; no application import verified.
```

## Missing-input request: fictional Moss omitted parent
Input: same local point contract, parent transform absent and no explicit no-parent declaration.

```text
Contract: Local chain supplied; parent-to-world mapping unresolved.
Inputs: Moss P and local operations supplied; parent mapping absent.
Trace: World trace withheld pending required parent input.
Checks: Request-level input gate exercised; trace function was not called with an invented identity parent.
Comparison: Unavailable; world-space prediction unresolved.
Next: Supply the parent-to-world matrix and translation, or confirm that no parent applies. No world-coordinate verdict yet.
```

## Edge request: fictional Reed collapsed axis
Input: p=(2,3,4), zero pivot/translation, s=(-1,0,2), identity rotation, parent A=diag(1,0,1), b=0, zero rotation tolerance.

```text
Contract: Pivot-relative scale then identity rotation and zero translation; singular parent forward mapping; column vectors in scene units.
Inputs: Reed P=(2,3,4), scale=(-1,0,2), all other local operations explicit; parent diag(1,0,1).
Trace: P: (2,3,4) | (-2,0,8) | (-2,0,8) | (-2,0,8) | (-2,0,8).
Checks: Executed forward trace gives (-2,0,8). Zero scale loses information; no inverse recovery asserted. A separate reflection passed as rotation raises determinant-check ValueError.
Comparison: No observed output supplied; no acceptance verdict.
Next: Retain this forward result and request separate topology or inverse requirements if needed; collapsed coordinates cannot establish recoverability.
```

## Outcome
PASS: normal numeric trace and three basis controls; missing-input stop; singular/negative scale forward trace; rejection of reflection as rotation. Claims are bounded to the supplied model. No issue requiring a skill change found.
