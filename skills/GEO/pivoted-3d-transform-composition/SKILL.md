---
id: GEO-003
name: pivoted-3d-transform-composition
domain: Mesh Geometry Diagnostics
subdomain: Transform composition
version: 1.0
description: Trace pivoted three-dimensional scale and rotation through a parent affine transform when operation order or coordinate space may explain misplaced geometry.
triggers: ["trace a 3D pivot transform", "check scale rotation order", "compute a vertex through its parent", "diagnose misplaced mesh points", "compare local and world coordinates"]
not_for: ["coordinate exchange policy [SPD-001]", "recovering transforms from a screenshot", "normal vector transformation", "projective camera transforms"]
requires: []
risk_level: medium
---

# Pivoted 3D Transform Composition

## Purpose
Compute a reproducible point trace for a declared three-dimensional transform chain, retaining intermediate coordinates that expose order and space mistakes. This skill evaluates supplied numerical transforms; it does not infer an application's hidden conventions or certify the whole mesh from a few points.

## Inputs to collect
1. **Point identities and coordinates:** obtain finite local-space triples, preserving vertex identifiers so results remain traceable; no default coordinates.
2. **Local operation contract:** collect a pivot triple, axis scale triple, supplied rotation matrix, translation triple, and operation order; no silent identity defaults for omitted operations.
3. **Parent transform:** collect its linear three-by-three matrix and translation triple, both in the declared parent-to-world mapping; explicit no-parent means identity and zero translation.
4. **Space conventions:** collect axis order, coordinate units, column-vector versus row-vector meaning, and whether matrices are local-to-parent or inverses; no default for ambiguous source conventions.
5. **Comparison evidence:** obtain observed point coordinates, approved absolute tolerance, and the same vertex identities if diagnosing a discrepancy; without observations produce only predicted traces, and without tolerance report differences without pass/fail.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Normalize the supplied contract into column-vector notation with explicit source and destination spaces. Record any documented conversion; do not transpose an unexplained matrix until the numbers look plausible. The supported local order is subtract pivot, axis scale, supplied rotation, restore pivot, then translation. A different approved order requires a separately written expression and separately checked implementation.
2. Validate every input shape and numeric value before computing points. Require a genuine rotation matrix within a declared dimensionless checking tolerance; a reflection or shear belongs in an explicitly named linear transform, not an undocumented rotation. Check the current source application's transform convention in its documentation when adapting exported data.
3. Write the chain as `local = c + R * (s componentwise (p - c)) + t`, followed by `world = A * local + b`. Here `p` and `c` share the object's local coordinate space; `t` is the post-rotation translation in parent coordinates; `A,b` describe the already composed parent-to-world affine map. Do not apply a parent twice to coordinates already in world space.
4. ⚠️ Calculate one point stage by stage before processing the full selection. Preserve pivot-relative, scaled, rotated, local-result, and world-result triples. Multiplication order matters with unequal axis scales; swapping rotation and scale is a different expression even when some control points happen to agree.
5. Run the following dependency-free Python 3 reference calculation on supplied finite inputs. Its rotation tolerance is an input, not a universal accuracy threshold. It accepts an arbitrary finite parent linear map, including shear or singular scale, because forward point mapping does not require inversion. The code transforms positions only.

```python
import math

def vector(v):
    if len(v) != 3 or any(type(x) not in (int, float) for x in v):
        raise ValueError("finite numeric triple required")
    q = tuple(float(x) for x in v)
    if not all(math.isfinite(x) for x in q):
        raise ValueError("nonfinite input")
    return q

def matrix(m):
    if len(m) != 3:
        raise ValueError("three matrix rows required")
    return tuple(vector(row) for row in m)

def mul(m, v):
    return vector(tuple(sum(m[i][j] * v[j] for j in range(3))
                        for i in range(3)))

def add(a, b):
    return vector(tuple(x + y for x, y in zip(a, b)))

def trace(p, c, s, r, t, a, b, rotation_tolerance):
    p, c, s, t, b = map(vector, (p, c, s, t, b))
    r, a = matrix(r), matrix(a)
    e = rotation_tolerance
    if type(e) not in (int, float) or not math.isfinite(e) or e < 0:
        raise ValueError("nonnegative finite rotation tolerance required")
    det = (r[0][0] * (r[1][1]*r[2][2] - r[1][2]*r[2][1])
           - r[0][1] * (r[1][0]*r[2][2] - r[1][2]*r[2][0])
           + r[0][2] * (r[1][0]*r[2][1] - r[1][1]*r[2][0]))
    if not math.isfinite(det) or abs(det - 1) > e:
        raise ValueError("rotation determinant check failed")
    for i in range(3):
        for j in range(3):
            dot = sum(r[i][k] * r[j][k] for k in range(3))
            if not math.isfinite(dot) or abs(dot - (i == j)) > e:
                raise ValueError("rotation orthogonality check failed")
    relative = vector(tuple(p[i] - c[i] for i in range(3)))
    scaled = vector(tuple(relative[i] * s[i] for i in range(3)))
    rotated = mul(r, scaled)
    local = add(add(c, rotated), t)
    world = add(mul(a, local), b)
    return dict(relative=relative, scaled=scaled, rotated=rotated,
                local=local, world=world)

R = ((1,0,0), (0,0,-1), (0,1,0))
A = ((1,1,0), (0,1,0), (0,0,2))
args = ((1,1,1), (2,3,4), R, (0,2,1), A, (10,0,-1), 0)
assert trace((2,1,3), *args)["world"] == (8,-5,3)
assert trace((1,1,1), *args)["world"] == (14,3,3)
```

6. Verify the pivot and three independent local basis offsets through the chain. The pivot's pre-parent result must be `c+t`; basis offsets reveal axis mixing that a pivot alone cannot expose. Recompute selected points with direct matrix arithmetic independent of the trace function. If execution is unavailable, label calculations manual rather than claiming an executed test.
7. Compare predictions with observations only after matching point identities, spaces, and units. Report component differences and the supplied acceptance rule; do not hide a mismatch through rounding. If testing an alternative order, retain both labeled expressions and identify which evidence discriminates between them.
8. Return the bounded trace and a proposed next check. Apply no geometry edit unless requested. A successful point calculation establishes that calculation under its contract, not the correctness of an application import, normal directions, or animation evaluation.

## Decision rules
- IF the matrix convention is unknown THEN request its documented meaning BECAUSE transposing and reversing order can produce different coordinates.
- IF unequal scale and rotation are present THEN test a non-axis-aligned point BECAUSE coincident control results can conceal an order error.
- IF a scale component is zero THEN allow the forward trace but flag information loss BECAUSE an inverse recovery may be impossible.
- IF parent data are absent without an explicit no-parent declaration THEN stop world-coordinate calculation BECAUSE local coordinates cannot establish world position alone.

## Output template
```text
Contract: <spaces, units, order; maximum 80 words>
Inputs: <point IDs and transform references; maximum 80 words>
Trace: <at most 5 points; relative | scaled | rotated | local | world>
Checks: <pivot, basis, independent calculation, execution status; maximum 100 words>
Comparison: <observations and differences, or unavailable; maximum 60 words>
Next: <one bounded action and remaining limitation; maximum 50 words>
```

## Quality checklist
- [ ] Every reported point retains its input identity.
- [ ] Pivot and point coordinates use the same local space.
- [ ] Rotation and parent matrices have separate documented meanings.
- [ ] Translation is applied at its declared stage.
- [ ] Every intermediate value is finite.
- [ ] Pivot and independent basis controls are evaluated.
- [ ] Observed comparisons identify their tolerance or withhold pass/fail.
- [ ] Execution claims correspond to actual runs.

## Anti-patterns
- **Visual guessing**: choose a sign from a screenshot. Fix: request coordinate conventions and a numeric control point.
- **Parent duplication**: transform an already world-space point again. Fix: annotate each stage's source and destination.
- **Uniform-scale comfort**: test only equal scales. Fix: add unequal scale and an off-axis control.
- **Normal reuse**: treat normals as points with translation. Fix: route normals to a separately specified vector transformation procedure.

## Worked example
**Input:** Fictional Cedar Mesh supplies point V=(2,1,3), pivot=(1,1,1), scale=(2,3,4), and the exact R and A matrices from the snippet. Translation=(0,2,1), parent translation=(10,0,-1), column-vector order as specified, all positions in fictional scene units, and rotation tolerance=0 for these integer matrices. No observed result is available.

**Output:**
```text
Contract: Local point to parent by pivot-relative scale, R rotation, pivot restoration and translation; parent to world by A and b. Column vectors; scene units.
Inputs: V=(2,1,3); c=(1,1,1); s=(2,3,4); R and A as supplied; t=(0,2,1); b=(10,0,-1).
Trace: V: (1,0,2) | (2,0,8) | (2,-8,0) | (3,-5,2) | (8,-5,3).
Checks: Manual arithmetic: pivot world=(14,3,3). World offsets for local x,y,z basis steps are (2,0,0), (0,0,6), (-4,-4,0); adding x and twice z to pivot gives (8,-5,3). Code execution not claimed here.
Comparison: Observed coordinates unavailable; no acceptance verdict.
Next: Compare V against an exported world-space control using an agreed tolerance; this does not verify the renderer.
```

**Bad output:** `V is (10,-3,3); the imported mesh is correct.`
This silently scales after rotation and certifies an import without observations.

## Edge cases
- **Negative scale:** retain its sign and flag possible orientation reversal; point correctness alone does not establish triangle winding.
- **Singular parent:** compute forward positions but do not promise recoverable local coordinates.
- **Huge finite inputs:** reject nonfinite intermediate results; rescale units or use an appropriate higher-precision calculation explicitly.
- **Animated hierarchy:** require a specific evaluated time and parent transform; do not mix transforms from different frames.

## Test case
**Input:**
> Use the fictional matrices above with point equal to pivot, then with V. Compare the specified scale-then-rotation order against rotation-then-scale. No observed output or acceptance tolerance is supplied.

**Assertions:**
1. The pivot maps to (14,3,3) under the specified chain.
2. V maps to (8,-5,3) under the specified chain.
3. The reversed local order is separately labeled and yields (10,-3,3) for V.
4. The response withholds an import acceptance verdict because observations and an acceptance rule are absent.
