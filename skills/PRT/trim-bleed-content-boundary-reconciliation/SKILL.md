---
id: PRT-004
name: trim-bleed-content-boundary-reconciliation
domain: Print Production Handoffs
subdomain: Page boundary review
version: 1.0
description: Reconcile trim, bleed and protected-content boundaries against a supplier's job specification when artwork dimensions or edge placement are uncertain.
triggers: ["check artwork trim and bleed", "review content near a cut edge", "reconcile page boundary dimensions", "check supplied print margins", "prepare an edge placement exception list"]
not_for: ["choosing universal print margins", "operating cutting equipment", "approving a production file from an unscaled preview"]
requires: []
risk_level: medium
---

# Trim, bleed and content boundary reconciliation

## Purpose
Compare an artwork revision with the job's declared page boundaries and protected-content requirements. Distinguish an incorrect boundary definition from artwork that fails to reach or stay inside the intended boundary, so changing a page box does not falsely resolve an object-placement problem.

## Inputs to collect
1. **Finished dimensions:** Collect the intended finished shape, dimensions, orientation and units. Required; no default paper size or trim is assumed.
2. **Supplier requirements:** Obtain job-specific bleed extent, protected-content inset and the reference boundary for each. Required for compliance findings; leave unknown values unresolved.
3. **Artwork revision:** Identify the exact file or evidence under review. Required; previews from another revision cannot establish current placement.
4. **Boundary evidence:** Request the declared trim and bleed boundaries or a dimensioned layout. Default: visual-only review with no claim of measured compliance.
5. **Critical objects:** Identify text, marks, images and edge-to-edge backgrounds whose placement matters. Default: inspect supplied objects only, identifying uninspected pages separately.
6. **Finishing context:** Collect folds, binding edges, shaped cuts or other job features that alter the relevant boundary. Default: no assumptions about hidden finishing allowances.

If required inputs have no safe default, ask in one message with at most three questions.

## Procedure
1. Establish a common unit and orientation for the supplied dimensions. Preserve the original values next to conversions so a rotated page or unit mismatch is visible before layout judgments.
2. Draw or describe the finished boundary using the supplied job specification. For shaped work, use its actual approved outline instead of replacing it with a surrounding rectangle.
3. Map each additional requirement to its stated reference: outward bleed from the finished edge, inward protected region, fold exclusion or another supplied condition. Do not substitute one boundary for another.
4. Compare the file's declared boundaries with this map. Label a missing or conflicting boundary as a file-definition issue even when the visible artwork seems large enough.
5. ⚠️ Inspect actual edge artwork separately from boundary metadata. A large bleed boundary containing empty space does not establish that an intended background extends through the required region.
6. Compare critical content with its relevant protected region. Record the object, edge, measured or supplied distance and requirement, keeping a visual estimate distinct from a measurement.
7. Check each page or face under its own orientation and finishing context. An inside fold, binding edge or reverse face may have a different supplied condition; copying one page's disposition needs supporting evidence.
8. Separate proposed geometry corrections from content movement or image extension. Identify dependencies such as a moved caption colliding with another object rather than presenting every fix as an isolated coordinate edit.
9. Request a revised artifact or a named exception decision for unresolved items. Recheck changed objects and boundaries in the replacement evidence; do not claim that describing a correction implemented it.
10. Deliver a boundary ledger that identifies confirmed matches, exceptions and measurement limits. Reserve release decisions for the required owner and evidence under the actual job process.

Use [VERIFY: current job-specific artwork and finishing requirements from the receiving supplier] for all production values. Do not invent a standard bleed, minimum text inset, cutting tolerance or binding allowance; a value from another job is not evidence for this one.

## Decision rules
- IF the units or orientation differ THEN normalize them before comparison BECAUSE a numerical mismatch may come from incompatible reference frames.
- IF boundary metadata passes but edge artwork stops early THEN retain an artwork exception BECAUSE declared space does not fill that space.
- IF evidence is an unscaled screenshot THEN limit findings to visible relationships BECAUSE it cannot establish exact physical distances.
- IF a finishing feature changes the protected region THEN use its supplied requirement BECAUSE the outer trim alone may not describe content placement needs.
- IF a proposed fix affects neighboring objects THEN include them in the recheck BECAUSE resolving one edge conflict can create another layout conflict.

## Output template
```text
Job frame: <revision, dimensions, units and orientation; up to three lines>
Boundary basis: <supplier requirement and its reference for each boundary>
Exception ledger: <up to ten rows; attach the full list if larger>
Page/object | Relevant boundary | Evidence/distance | Required relationship | Disposition
Corrections: <up to five grouped proposals with recheck scope>
Questions: <up to three consolidated requirements or evidence questions>
Next gate: <named review or blocked condition>
Verification limits: <measurements performed and unavailable evidence>
```

## Quality checklist
- [ ] Finished dimensions have units and orientation.
- [ ] Every production limit has a supplied source or a verify placeholder.
- [ ] Bleed and protected-content references are distinguished.
- [ ] File boundaries and actual artwork extent are checked separately.
- [ ] Each exception identifies an object and relevant edge.
- [ ] Visual estimates are not reported as exact measurements.
- [ ] Finishing-specific requirements remain visible.
- [ ] Corrections include the affected neighboring content in their recheck.

## Anti-patterns
- **Borrowed default:** a familiar inset is imposed without a job instruction. Fix: obtain the receiving supplier's requirement.
- **Box equals artwork:** metadata is treated as filled bleed. Fix: inspect the object's extent within the declared region.
- **Screenshot ruler:** an unscaled preview is assigned exact physical distances. Fix: request dimensioned evidence or retain visual-only findings.
- **Trim-only thinking:** all content is judged against the outer edge. Fix: include supplied fold, binding or shaped-cut boundaries.
- **Fix without recheck:** a requested move is called complete. Fix: inspect the resulting revision and neighboring layout.

## Worked example
**Input:** Fictional printer Wren specifies a 100 by 150 mm finished card, background extension of 3 mm beyond each finished edge and title placement at least 5 mm inside it. Dimensioned evidence for revision C shows the declared bleed boundary reaches 3 mm outward, but the background stops at trim. The title is 4 mm inside the top edge. These are job-specific fictional values.

**Output:**
```text
Job frame: Revision C; 100 by 150 mm finished card, portrait orientation.
Boundary basis: Wren's supplied requirement: background 3 mm beyond trim; title at least 5 mm inside trim.
Exception ledger:
Page/object | Relevant boundary | Evidence/distance | Required relationship | Disposition
Front/background | trim outward | artwork stops at trim | extends 3 mm beyond | artwork exception despite correct declared boundary
Front/title | top trim inward | 4 mm | at least 5 mm | one mm short of required inset
Corrections: Extend background under designer review; move title to satisfy supplied inset and recheck neighboring content in revised evidence.
Questions: Please supply revision C's replacement with dimensioned evidence for both corrections.
Next gate: Blocked for corrected-artwork review.
Verification limits: Supplied dimensions compared; no physical output or cutting operation observed.
```

**Bad output:** “The bleed boundary is correct, so the card is ready.”
It ignores both the missing background extension and the title's failure to meet the supplied requirement.

## Edge cases
- Artwork intentionally ends at the edge: ask whether edge-to-edge coverage is actually intended before declaring missing bleed content.
- A shaped cut passes near text: use the approved cut outline and supplied protected region rather than the page rectangle.
- Only one face has dimensions: keep the other face unverified instead of copying a passing result.
- A supplier grants an exception: retain the exact accepted object, revision and condition rather than rewriting the requirement for all pages.

## Test case
**Input:**
> Fictional job D provides a screenshot showing text near a fold but no dimensions, fold allowance or supplier requirement. The client asks if the margin is sufficient.

**Assertions:**
1. Identifies the fold as a relevant boundary.
2. Requests its job-specific requirement and dimensioned evidence.
3. Does not invent a minimum margin or exact measured distance.
4. Limits the disposition to the available visual evidence.
