# Mesh Geometry Diagnostics (GEO)

Diagnose indexed triangle edge orientation, per-corner UV signed area, and explicitly ordered three-dimensional point transforms.

Macro-area: Visual Arts, Photo & Video

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| GEO-001 | [triangle-shared-edge-winding-check](triangle-shared-edge-winding-check/SKILL.md) | Inspect indexed triangle winding across shared edges when adjacent faces may traverse their common edge in the same direction. | check triangle winding; find inconsistent shared edges; inspect mesh edge orientation | validated |
| GEO-002 | [uv-triangle-signed-area-inspection](uv-triangle-signed-area-inspection/SKILL.md) | Measure per-corner UV triangle signed areas when collapsed mappings or orientation changes need localization without assuming mirrored islands are errors. | check collapsed UV triangles; inspect UV triangle orientation; find near-zero UV areas | validated |
| GEO-003 | [pivoted-3d-transform-composition](pivoted-3d-transform-composition/SKILL.md) | Trace pivoted three-dimensional scale and rotation through a parent affine transform when operation order or coordinate space may explain misplaced geometry. | trace a 3D pivot transform; check scale rotation order; compute a vertex through its parent | validated |
