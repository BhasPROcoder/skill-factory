---
id: GEO-002
name: uv-triangle-signed-area-inspection
domain: Mesh Geometry Diagnostics
subdomain: UV orientation
version: 1.0
description: Measure per-corner UV triangle signed areas when collapsed mappings or orientation changes need localization without assuming mirrored islands are errors.
triggers: ["check collapsed UV triangles", "inspect UV triangle orientation", "find near-zero UV areas", "compare mirrored UV islands", "measure mapping triangle degeneracy"]
not_for: ["packing UV islands", "certifying distortion or texel density", "mesh edge winding [GEO-001]", "detecting all UV overlaps"]
requires: []
risk_level: medium
---

# UV Triangle Signed-Area Inspection

## Purpose
Calculate each triangle's signed area in the supplied UV coordinate convention and distinguish zero-area, near-zero and signed nondegenerate cases. Keep intentional mirrored mappings separate from unexplained sign changes, and avoid claiming that these measurements establish a complete texture-mapping review.

## Inputs to collect
1. **Per-corner UV triangles** — obtain three ordered UV coordinates per triangulated face, including seam-specific values. This preserves different mappings at one geometric vertex. Default: none, required; do not replace corner values with a vertex-only average.
2. **Face correspondence** — obtain the mesh revision, face identities and corner order used by the UV data. This distinguishes a mapping change from reordered geometry. Default: no comparison between revisions until correspondence is known.
3. **Coordinate convention** — identify the positive axes and whether a supplied display flips one axis. This determines the meaning of a positive sign. Default: report algebraic sign in the supplied coordinates without declaring clockwise screen appearance.
4. **Area criterion** — obtain a nonnegative tolerance in squared UV coordinate units for the requested near-zero classification. Default: zero for exact degeneracy only; no universal production threshold.
5. **Orientation intent** — obtain expected sign relationships, island membership and intentional mirror permissions. Default: signs are observations, not errors or repair instructions.
6. **Execution scope** — identify the copied data and permission to modify it. Default: read-only numerical report, without texture rendering or UV edits.

If a required input has no safe default, ask in one message with at most three questions. Combine correspondence and coordinate questions before asking for acceptance criteria and intended mirror behavior.

## Procedure
1. Freeze the mesh and UV revisions and record ordered corner identities. A UV seam can assign different coordinates to different corners sharing the same geometric vertex.
2. Check that each record has three finite two-component coordinates. Reject malformed or nonfinite data rather than replacing it with zero, because that would fabricate a collapsed triangle.
3. Calculate signed doubled area from the two edge vectors originating at the first UV point. Divide by two only when reporting area; retaining the signed doubled value helps reproduce the arithmetic.
4. Classify exactly zero area separately from a nonzero magnitude at or below the supplied near-zero criterion. The criterion is a task input in coordinate-squared units, not a guarantee about sampling or visible defects.
5. Record the sign of each remaining triangle in the stated coordinate convention. ⚠️ Do not automatically flip every negative triangle: a mirrored island or differently ordered face can explain the sign without a defective mapping.
6. Compare signs only across a supplied consistent face ordering and intended island relationship. When those inputs are absent, report the measurement and request the relationship needed for a defect judgment.
7. Localize collapsed or small-area triangles on an inspectable UV view if available. Keep a numerical result separate from a claim that the artist actually inspected a rendered texture or fixed stretching.
8. Preserve the source UVs and propose an owner-reviewed correction only after the mapping intent is known. Rerun the same measurements on the changed revision and separately inspect any requested texture appearance.

The Python 3 reference below treats each triangle independently and accepts finite numeric coordinate pairs. It calculates signed doubled area and reports a supplied near-zero classification. It does not compare UV area with geometric surface area, find overlaps, unwrap a mesh or interpret tile numbers. Save it as a script and run it with the available interpreter; retain the actual version and input coordinate convention in the report.

```python
import math

def uv_area(points, tolerance=0.0):
    if (not isinstance(tolerance, (int, float))
            or not math.isfinite(tolerance) or tolerance < 0):
        raise ValueError("finite nonnegative area tolerance required")
    if len(points) != 3 or any(len(p) != 2 for p in points):
        raise ValueError("three UV pairs required")
    if any(not isinstance(v, (int, float)) or not math.isfinite(v)
           for p in points for v in p):
        raise ValueError("finite numeric UV values required")
    a, b, c = points
    double = ((b[0]-a[0])*(c[1]-a[1])
              - (b[1]-a[1])*(c[0]-a[0]))
    if not math.isfinite(double):
        raise ValueError("area arithmetic overflow")
    magnitude = abs(double) / 2
    if double == 0:
        state = "zero area"
    elif magnitude <= tolerance:
        state = "near zero by supplied criterion"
    else:
        state = "positive" if double > 0 else "negative"
    return double, magnitude, state

assert uv_area([(0, 0), (2, 0), (0, 1)]) == (2, 1, "positive")
assert uv_area([(0, 0), (0, 1), (2, 0)]) == (-2, 1, "negative")
assert uv_area([(0, 0), (1, 0), (2, 0)]) == (0, 0, "zero area")
assert uv_area([(0, 0), (1, 0), (0, 0.25)], 0.125)[2] == (
    "near zero by supplied criterion")
try:
    uv_area([(0, 0), (1, 0), (0, float("nan"))])
except ValueError:
    pass
else:
    raise AssertionError("nonfinite coordinate accepted")
print("UV signed-area checks passed")
```

For extremely large or tiny coordinates, numeric precision may limit the classification. Preserve the supplied coordinate scale, report the limitation and use an appropriate higher-precision calculation if the requested decision depends on it; do not choose a convenient tolerance after seeing the answer.

## Decision rules
- IF area is exactly zero in the executed calculation THEN flag the collapsed mapping triangle BECAUSE its three UV corners do not span a nonzero planar area in that calculation.
- IF a nonzero area falls within the supplied criterion THEN label it near-zero under that criterion BECAUSE smallness has no universal pass/fail value independent of the task.
- IF a negative sign belongs to an authorized mirrored island THEN retain that intent BECAUSE sign alone does not establish a mistake.
- IF face order or axis convention changed THEN reconcile the convention before comparing signs BECAUSE reversing either can reverse the algebraic orientation.
- IF UVs are unavailable for individual corners THEN request corner data BECAUSE seam-separated values cannot be reconstructed reliably from one averaged vertex value.

## Output template
```text
Mapping scope: <mesh/UV revision, corner convention and axes; up to three lines>
Criterion: <area units, tolerance and supplied basis; two sentences maximum>
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
<up to twelve rows; retain full results for a larger scope>
Executed checks: <up to five cases and observed results>
Unresolved: <up to three missing correspondence, intent or display checks>
Limits: <two sentences identifying untested distortion, overlap and rendering>
```

## Quality checklist
- [ ] UV coordinates are supplied per triangle corner rather than silently averaged.
- [ ] Triangle identities and corner ordering match the inspected revision.
- [ ] Coordinate axes and sign convention are stated.
- [ ] Nonfinite or malformed input is rejected.
- [ ] Near-zero tolerance has units and an explicit supplied basis.
- [ ] Signed orientation is not automatically converted into a repair decision.
- [ ] Area calculations retain operands or a reproducible fixture.
- [ ] No overlap, distortion or texture-quality conclusion follows from signed area alone.

## Anti-patterns
- **Mirrors treated as damage**: all negative areas are flipped. Fix: compare with authorized island intent and consistent corner order.
- **Tolerance fishing**: a threshold is selected to make warnings disappear. Fix: obtain the criterion before classification and report its units.
- **Seam averaging**: several corner coordinates become one vertex coordinate. Fix: retain actual corner attributes through the measurement.
- **Area as texture quality**: a nonzero area is called distortion-free. Fix: measure the requested additional property separately.
- **Invalid-number repair**: missing or nonfinite values become zero. Fix: reject the record and request actual coordinate evidence.

## Worked example
**Input:**
> Fictional asset Alder supplies face A UVs [(0,0),(2,0),(0,1)] and face B [(0,0),(0,1),(2,0)] with the same declared corner convention. B belongs to an explicitly permitted mirrored island. Exact degeneracy only is requested; no render is supplied.

**Output:**
```text
Mapping scope: Alder supplied mesh/UV snapshot; ordered UV pairs use the same declared axes and corner convention.
Criterion: Zero tolerance for exact degeneracy only; area is in squared supplied UV units.
Triangle findings:
Face | Signed doubled area | Absolute area | Classification | Intent/action
A | 2 | 1 | positive | no collapse identified
B | -2 | 1 | negative | retain permitted mirrored orientation; no automatic flip
Executed checks: Reference calculations return doubled areas 2 and -2, absolute areas 1 and 1; collinear fixture returns zero.
Unresolved: Actual texture appearance remains uninspected.
Limits: These measurements do not detect every overlap or quantify surface distortion. No rendered quality or edit completion is claimed.
```

**Bad output:** “B has negative area, so it is broken and must be mirrored back.”
This treats a signed measurement as a defect despite the supplied intentional mirror permission.

## Edge cases
- **UVs outside a nominal unit square**: retain their actual values; location alone does not establish invalidity or a tile policy.
- **Identical UV corner positions**: report the resulting zero area and preserve the distinct corner identities for repair discussion.
- **Axis-flipped export**: reconcile the axis transformation before comparing sign changes between revisions.
- **Near-zero finite precision**: show the computed result and criterion without implying exact symbolic degeneracy; seek higher precision when the decision requires it.

## Test case
**Input:**
> Fictional artist provides triangle UVs [(0,0),(1,0),(2,0)] and asks whether the mesh is now fully texture-ready because its edges look connected. No render or island-overlap evidence exists.

**Assertions:**
1. Computes zero signed and absolute UV area for the supplied triangle.
2. Flags the collapsed UV mapping despite apparent connectivity.
3. Requests mapping repair evidence rather than certifying full texture readiness.
4. Separates this result from mesh topology, overlap and rendered appearance.
