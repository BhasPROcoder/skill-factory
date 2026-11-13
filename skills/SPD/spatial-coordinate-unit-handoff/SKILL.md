---
id: SPD-001
name: spatial-coordinate-unit-handoff
domain: Spatial Asset Preparation
subdomain: Coordinate handoffs
version: 1.0
description: Prepare a coordinate and unit contract for transferring a spatial asset between tools when scale, orientation, origin, or transform handling may change.
triggers: ["model imports at the wrong size", "asset faces the wrong direction", "prepare a 3D handoff", "coordinate system transfer", "verify imported model scale", "document scene units"]
not_for: ["designing the asset geometry", "general reproduction handoff [TRP-010]", "diagnosing procedural material parameters [SPD-002]"]
requires: []
risk_level: medium
---

# Spatial coordinate and unit handoff

## Purpose
Produce a transfer contract that makes scale, orientation, pivot placement, and transform ownership testable at the receiving end. Use it before exporting an asset or when an imported object looks plausible but its measurements or placement disagree with the source.

## Inputs to collect
1. **Source evidence** — asset identifier, dimensions, local axes, world placement, and relevant transform hierarchy. These distinguish authored geometry from display settings. Default: unknown values remain unresolved.
2. **Destination contract** — required units, axis convention, pivot use, and intended assembly placement. These define success. Default: none for a transfer intended for production.
3. **Transfer path** — exporter, intermediate format, importer, and actual installed versions. These identify conversion owners. Default: name the missing stage without assuming its behavior.
4. **Reference measurements** — a known length, an asymmetric orientation marker, and a named origin landmark. These provide independent checks. Default: request author-confirmed references.
5. **Execution access** — permission to inspect a copy, import a sample, and measure results. This controls whether findings are observed or proposed. Default: preparation only.
6. **Acceptance limits** — tolerances and preservation requirements supplied by the asset owner. These determine acceptance. Default: report comparisons without inventing a passing tolerance.

If a required input is missing and has no safe default, ask in one message with at most three questions.

## Procedure
1. Identify the exact source revision and proposed destination revision so later checks cannot accidentally compare different assets.
2. Separate geometry dimensions, object transforms, parent transforms, scene-unit display, and export settings into distinct evidence fields.
3. Write the destination's coordinate contract in words using explicit axis directions and physical units; label every unconfirmed convention.
4. ⚠️ Assign each required conversion to exactly one stage in the transfer path; do not scale both the object and importer merely because either control appears available.
5. Define a measurement witness whose physical size is supplied independently of how the viewport labels units.
6. Define an asymmetric orientation witness using named features, such as a left-mounted handle and front-facing opening, so a symmetric box cannot conceal reversal.
7. Record how the pivot and parent hierarchy should behave after import, distinguishing intentional placement from geometry recentering.
8. Prepare a sample transfer on a separate copy using the proposed conversion ownership; preserve the original asset and note all actual settings used.
9. Compare imported length, feature orientation, pivot location, and parent behavior against the contract; record observed values only when the import was actually inspected.
10. ⚠️ Classify each discrepancy before proposing repair: size, orientation, pivot, inherited transform, or unsupported transfer behavior; an arbitrary rotation is not evidence that all problems are solved.
11. Produce the handoff record with a release disposition and explicit unresolved checks. When tools are unavailable, deliver the contract and inspection procedure with status untested.

Before relying on exporter or importer options, use `[VERIFY: coordinate, unit, and hierarchy behavior in the documentation for the installed exporter and importer versions]`. Interface labels and defaults are not evidence that the whole path applies exactly one conversion.

For a supplied conversion factor, this standalone Python 3 arithmetic check can verify the expected lengths. Record the actual interpreter version when executing it; it does not inspect a mesh or prove a coordinate transformation.

```python
source_lengths = [120, 35]
target_units_per_source_unit = 0.01  # fictional contract input
expected = [x * target_units_per_source_unit for x in source_lengths]
assert abs(expected[0] - 1.2) < 1e-9
assert abs(expected[1] - 0.35) < 1e-9
print(expected)
```

## Decision rules
- IF source units are unknown THEN withhold a conversion factor and request an author-confirmed measurement BECAUSE viewport appearance cannot establish physical scale.
- IF multiple stages apply the same conversion THEN choose one owner and neutralize the redundant conversion in a test copy BECAUSE repeated conversion changes the intended result.
- IF dimensions match but named features reverse THEN investigate axis mapping and reflection separately BECAUSE matching size does not establish orientation.
- IF the pivot has a downstream assembly role THEN preserve or explicitly remap that role BECAUSE recentering can break otherwise correct placement.
- IF no actual import has been inspected THEN label the transfer untested BECAUSE a proposed contract is not execution evidence.

## Output template
```text
Asset: <revision and destination; one line>
Contract: <units, axes, pivot, hierarchy; maximum six lines>
Conversion ownership: <stage and operation, or unresolved; maximum four lines>
Witnesses: <length, orientation, origin; maximum four lines>
Results: <expected versus observed, with evidence or untested; maximum six lines>
Disposition: <accepted against supplied limits / revise / blocked / untested>
Next check: <specific action and responsible role; maximum three lines>
```

## Quality checklist
- [ ] Source and target revisions are named or explicitly unresolved.
- [ ] Geometry dimensions and display units are separate evidence fields.
- [ ] Each proposed conversion has exactly one owner.
- [ ] A measurement witness has an author-confirmed physical interpretation.
- [ ] Orientation checking uses an asymmetric feature.
- [ ] Pivot and hierarchy preservation are addressed explicitly.
- [ ] Results distinguish proposed values from inspected observations.
- [ ] Acceptance uses supplied limits rather than invented tolerances.

## Anti-patterns
- **Viewport reassurance**: the asset looks about right. Fix: compare named witnesses and dimensions.
- **Stacked conversion**: object and importer both rescale the asset. Fix: assign one conversion owner and inspect a sample.
- **Symmetry trap**: a cube is the sole orientation reference. Fix: use an asymmetric feature with an explicit direction.
- **Destructive normalization**: transforms are applied to the original without checking dependencies. Fix: test a copy and preserve the intended hierarchy contract.
- **Unobserved acceptance**: a written export plan is called verified. Fix: label it untested until receiving-side evidence exists.

## Worked example
**Input:**
> Fictional artist Nera is handing asset Lamp-A revision 2 to a scene team. The author confirms its height is 120 source units and width 35, with each source unit representing a centimeter. The destination uses meters. Its handle must remain on the left when looking at the front opening, and its base-center pivot must remain the placement anchor. The proposed exporter converts lengths; the importer must not convert them again. No import has been performed and no tolerance is supplied.

**Output:**
```text
Asset: Lamp-A revision 2 to scene-team staging scene; destination revision pending.
Contract: Source centimeters to destination meters; source axis labels unresolved. Preserve left handle relative to front opening. Preserve base-center placement pivot; parent hierarchy still to inspect.
Conversion ownership: Exporter applies factor 0.01 to lengths. Importer must apply no additional length conversion; verify its actual settings.
Witnesses: Height 120 centimeters becomes 1.2 meters. Width 35 centimeters becomes 0.35 meters. Left handle, front opening, and base-center landmark anchor orientation and placement checks.
Results: Expected height 1.2 meters and width 0.35 meters; observed values unavailable. Orientation, pivot, and hierarchy untested.
Disposition: untested
Next check: Scene team confirms destination axes and acceptance limits, then imports a copy and records witness measurements and placement behavior.
```

**Bad output:**
> Scale the object and importer by 0.01; the model is now verified for production.

This applies the proposed conversion twice and claims verification without an inspected import.

## Edge cases
- **Mixed-unit collection** — obtain a reference and conversion owner for each differently authored asset; do not infer the whole collection from one object.
- **Animated or constrained hierarchy** — test the relevant poses and dependencies on a copy before changing transform handling.
- **Only screenshots available** — record visible orientation clues but withhold physical dimensions and transform claims not evidenced by the images.
- **Mirrored source geometry** — ask whether the mirror is intentional and preserve that distinction when checking named features.

## Test case
**Input:**
> A fictional stage prop has a known 200-centimeter height. Its exporter converts centimeters to meters, and its importer also applies factor 0.01. The user wants a handoff checklist but has no imported measurements or agreed tolerance.

**Assertions:**
1. Identifies duplicate length conversion and assigns a single conversion owner for the proposed test.
2. States the expected physical height as 2 meters without claiming an observed result.
3. Requires asymmetric orientation and pivot checks beyond the length comparison.
4. Leaves acceptance untested and requests the missing acceptance limits.
