---
id: RNT-003
name: rental-return-condition-evidence-comparison
domain: Rental Asset Operations
subdomain: Return observations
version: 1.0
description: Compare checkout and return condition evidence for the same rental asset while separating visible changes from unsupported cause or liability conclusions.
triggers: ["compare rental return photos", "was this mark present at checkout", "reconcile return condition notes", "build a before and after asset record", "review a disputed return observation"]
not_for: ["damage liability or compensation advice", "equipment safety certification", "missing checkout accessories [RNT-002]"]
requires: []
risk_level: medium
---

# Rental return condition evidence comparison

## Purpose
Produce a region-by-region comparison of supplied checkout and return observations for an identified rental asset. Preserve what the evidence can establish without treating a newly noticed mark as proof of when, how or by whom it was caused.

## Inputs to collect
1. **Asset and rental identity:** Obtain the unique unit and relevant rental transaction. This prevents comparing similar units. Default: no identity match assumed; required for a same-asset conclusion.
2. **Checkout evidence:** Collect original photos, inspection notes, region labels and observation times. These define the baseline actually documented. Default: missing regions remain undocumented rather than undamaged.
3. **Return evidence:** Obtain equivalent observations and the receiving record. This establishes the current visible state. Default: reported condition only if originals cannot be inspected.
4. **Intervening events:** Collect swaps, servicing, transport or custody transfers relevant to the comparison. This identifies breaks in continuity. Default: intervening history unknown.
5. **Observation conditions:** Collect orientation, lighting, scale and whether coverings or dirt obscure the surface. These affect comparability. Default: limitations stated explicitly.
6. **Requested output and reviewer:** Establish who needs the evidence record and whether a follow-up inspection is possible. Default: comparison dossier only, without fee, blame or safety determination.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Identify the physical unit in each source using supplied labels or distinguishing features. Stop the same-asset comparison where identity cannot be established; retain those sources as unmatched observations.
2. Create a source inventory with observation time, receipt time if different, original file or note reference and observer. Keep an upload timestamp separate from the time an image was captured.
3. Divide the asset into observable regions that can be located consistently, such as the labeled front panel or a particular hinge. Avoid vague references such as left side when camera orientation differs.
4. Pair each return observation with the closest comparable checkout view or note. Mark unmatched regions instead of stretching a distant or obscured view into evidence of absence.
5. ⚠️ Describe visible differences using neutral observable features: position, apparent shape and supplied measurements. Do not infer a crack's depth, mechanical effect or cause from a surface photo alone.
6. Classify each finding as documented at both stages, difference visible in comparable evidence, return observation with inadequate baseline, contradictory evidence or not assessable. Preserve the source references supporting the classification.
7. Record alternative explanations for a perceived difference where the evidence itself supports them, such as a cover removed between photographs. Do not invent a likely accident or customer behavior to complete the narrative.
8. ⚠️ Separate the observation conclusion from responsibility and remedy. A visible change can justify a follow-up inspection without establishing liability, repair necessity or a charge.
9. Specify the smallest additional observation that could resolve each uncertainty. Request a matching angle, original image, asset-label check or qualified assessment according to the gap; avoid asking for an entire rental history when one missing view is sufficient.
10. Deliver the comparison with its scope and unresolved continuity limits. Preserve originals and annotate copies when annotations are needed; never silently edit a source to improve the apparent comparison.

## Decision rules
- IF the checkout view does not show the relevant region THEN label the baseline inadequate BECAUSE absence from the image is not evidence that the mark was absent.
- IF the sources identify different units THEN stop direct before-and-after inference BECAUSE visual similarity does not establish the same asset.
- IF comparable views show a difference THEN report that difference without assigning cause BECAUSE the evidence may not establish the intervening mechanism or custodian.
- IF a condition could affect safe use THEN route assessment to the responsible qualified person BECAUSE this observational record does not certify usability.

## Output template
```text
Comparison scope: <unit, rental and evidence boundary; up to three lines>
Source register: <reference, observation time and identity basis; up to eight entries>
Findings:
Region | Checkout evidence | Return evidence | Comparability | Observation classification
<up to ten rows; attach additional findings separately>
Unresolved history: <continuity gaps or none evidenced; up to four lines>
Follow-up: <gap, requested observation and responsible reviewer; up to five lines>
Conclusion boundary: <supported visible findings and excluded determinations; up to four lines>
```

## Quality checklist
- [ ] Every compared source has an asset-identity basis.
- [ ] Observation time is distinguished from later receipt or upload time.
- [ ] Region descriptions remain meaningful across camera orientations.
- [ ] Missing baseline views are explicitly marked.
- [ ] Each finding cites the supporting supplied sources.
- [ ] Observable changes are separate from cause and responsibility.
- [ ] Follow-up requests target an actual evidence gap.
- [ ] The conclusion does not certify safety or impose charges.

## Anti-patterns
- **Undocumented means pristine:** an unseen surface is assumed undamaged. Fix: classify the baseline as inadequate.
- **Photo proves cause:** a mark is assigned to misuse from appearance alone. Fix: describe the observation and retain causal uncertainty.
- **Timestamp collapse:** upload time is called capture time. Fix: label each timestamp by its actual meaning.
- **Mirror confusion:** left and right are compared from opposing views. Fix: anchor regions to physical labels.
- **Edited original:** contrast or annotation changes replace source evidence. Fix: preserve originals and identify derived copies.

## Worked example
**Input:** Fictional rental studio Reed has unit C8. Checkout photo A shows its labeled front panel with a short white mark beside the handle. Return photo B shows the same panel and mark under comparable lighting. Return photo C shows a dent on the back, but no checkout back view exists. All photos identify C8; intervening custody history is not supplied.

**Output:**
```text
Comparison scope: Reed unit C8; supplied checkout A and return B/C only.
Source register: A—checkout observation, C8 label; B/C—return observations, C8 label. Exact observation times not supplied.
Findings:
Region | Checkout evidence | Return evidence | Comparability | Observation classification
Front beside handle | A: white mark | B: same visible mark | comparable supplied views | documented at both stages
Back panel | no view | C: dent visible | baseline inadequate | return observation; timing of change unestablished
Unresolved history: Intervening custody and exact observation times unknown.
Follow-up: Records owner seeks any original checkout back view; receiving reviewer confirms the back-panel observation if needed.
Conclusion boundary: Front mark is documented at checkout and return. Back dent is visible at return with no comparable baseline; no cause, liability, fee or safety conclusion.
```

**Bad output:** “Charge the renter for the new back dent.”
It invents newness and responsibility from an undocumented baseline.

## Edge cases
- A repair occurred during the rental: establish a new post-repair baseline for affected regions and preserve the earlier comparison separately.
- Only low-resolution copies exist: state the visible limit and request originals before describing details that cannot be resolved.
- Dirt obscures a suspected mark: request an appropriate observation by the responsible handler; do not prescribe a cleaning method that might alter evidence or damage the object.
- Notes and photographs conflict: retain both with their dates and observers, then route the specific contradiction for review.

## Test case
**Input:**
> Fictional hire shop Birch supplies checkout images of unit A and return images of unit B, which look identical. It asks which scratches appeared during A's rental.

**Assertions:**
1. Identifies the unit-identity mismatch.
2. Refuses a same-asset change conclusion from these images.
3. Requests matching evidence for the relevant unit.
4. Does not assign damage responsibility.
