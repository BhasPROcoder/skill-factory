---
id: SDR-002
name: scan-cleanup-evidence-preservation
domain: Spatial Deformation and Restoration
subdomain: Scan provenance
version: 1.0
description: Plan traceable scan cleanup when removing artifacts or filling gaps could erase observed detail or make reconstructed geometry look captured.
triggers: ["clean a scan without losing evidence", "preserve original scan detail", "document mesh cleanup decisions", "separate captured and repaired geometry", "review scan hole filling", "prepare a scan cleanup handoff"]
not_for: ["forensic evidence certification", "medical scan interpretation", "historical reconstruction labels [VEV-001]", "coordinate transfer contracts [SPD-001]"]
requires: []
risk_level: medium
---

# Scan Cleanup Evidence Preservation

## Purpose
Create a cleanup plan that preserves the distinction between captured surface evidence, uncertain artifacts, and geometry added for presentation or downstream processing. The deliverable makes changes reversible and reviewable without implying that a smoother mesh is a more faithful record of the object.

## Inputs to collect
1. **Source package** — original scan files, capture identifiers, available images, and prior processing history. These establish the baseline. Default: source integrity and prior edits remain unverified.
2. **Intended use** — visual presentation, asset production, measurement, or another stated purpose. This determines which edits are acceptable. Default: preparation only; do not authorize measurement use from an unspecified purpose.
3. **Suspected defects** — named regions and reasons for calling them noise, holes, duplicates, or unwanted background. These focus decisions. Default: ambiguous regions remain unchanged pending evidence.
4. **Protected features** — inscriptions, worn edges, seams, surface marks, or other details the owner needs retained. These define preservation boundaries. Default: ask before removing plausible object features.
5. **Reference evidence** — alternate views, known dimensions, repeat captures, or owner annotations. These support classification. Default: no invented reference geometry or dimensions.
6. **Processing capability** — tools, inspectable files, reversible edit support, and output requirements. These bound execution. Default: plan only; application-specific behavior must be verified before use.
7. **Acceptance criteria** — tolerated change, required detail, and review authority. These establish release conditions. Default: no numerical tolerance or final acceptance is assumed.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Identify a preserved source baseline and record its location or identifier before planning modifications; distinguish it from any already processed derivative.
2. Create a region inventory with stable identifiers that can be followed through topology changes, using view annotations or surface landmarks when vertex identifiers will not remain stable.
3. Classify each proposed edit as removal of evidenced extraneous capture, uncertain cleanup, detail-changing simplification, or reconstruction of missing surface.
4. ⚠️ Compare ambiguous features with supplied references before treating them as defects; a ridge, cavity, or isolated fragment may be part of the object rather than capture noise.
5. Record the purpose and evidence for each proposed operation, including which protected features could be affected.
6. Choose a reversible working copy or staged derivative for each operation; preserve the original and record operation order rather than overwriting the only source.
7. Define before-and-after inspections that target the operation's risk: boundary shape after filling, inscription readability after smoothing, or separation of object and background after removal.
8. Specify how added surfaces will remain identifiable in the edit ledger and deliverable metadata; a closed hole is not evidence of the surface that was originally missing.
9. Execute only the authorized and supported operations, recording actual settings and result references; otherwise leave operations proposed and do not imply a mesh was changed.
10. Compare the derivative against the baseline using the supplied acceptance criteria, noting which regions cannot be assessed from available references.
11. ⚠️ Retain unresolved regions or deliver separate conservative and presentation derivatives when their purposes conflict; do not silently sacrifice evidence to make one attractive file.
12. Deliver the edit ledger, preservation exceptions, and disposition with enough information to reproduce or reject individual changes.

For any tool operation, use `[VERIFY: current cleanup behavior, attribute preservation, and export limitations in the official documentation for the installed scan-processing application]`. Record the actual application version when executing. A generic label such as smoothing does not establish which attributes or boundaries survive the specific implementation.

The following Python 3 check verifies a fictional edit ledger's provenance invariant. It does not inspect scan geometry or authenticate the source. Run it with the available Python 3 interpreter and record the version before adapting it to a real ledger.

```python
edits = [
    {"region": "background", "kind": "removal", "baseline": "raw-A"},
    {"region": "underside", "kind": "reconstruction", "baseline": "raw-A"},
]
assert all(edit["baseline"] for edit in edits)
added_regions = {e["region"] for e in edits if e["kind"] == "reconstruction"}
assert added_regions == {"underside"}
print("Every edit traces to a baseline; reconstructed region remains identified")
```

## Decision rules
- IF a suspected artifact could be a real feature and references do not resolve it THEN preserve it or isolate an optional edit BECAUSE removal would erase an unresolved observation.
- IF a hole is filled without source evidence for its shape THEN classify the result as reconstructed BECAUSE geometric closure does not establish captured surface detail.
- IF simplification removes protected detail THEN reject that derivative for the protected use BECAUSE a smaller file is not sufficient acceptance evidence.
- IF original and derivative identifiers cannot be distinguished THEN stop acceptance and establish provenance BECAUSE later reviewers cannot attribute the changes reliably.
- IF presentation and measurement needs conflict THEN propose separate derivatives with explicit purposes BECAUSE one cleanup policy may not satisfy both uses.

## Output template
```text
Scope: <source identifier, intended use, and execution boundary; up to three lines>
Preservation baseline: <original, protected features, and unresolved provenance; up to four lines>
Edit ledger:
Region | Proposed operation | Evidence | Risk to retained detail | Status
<up to eight regions; attach more if necessary>
Reconstructed content: <added regions and labeling method; up to four lines>
Comparison checks: <before/after evidence needed; up to five checks>
Disposition: <proposed / revise / accepted for stated use / blocked; evidence basis>
Handoff: <source, derivative, edit history, unresolved decisions; up to four lines>
```

## Quality checklist
- [ ] Original and processed derivatives have distinct identifiers.
- [ ] Proposed edits are separated from executed changes.
- [ ] Ambiguous object features are not silently classified as noise.
- [ ] Protected details are named before smoothing or simplification.
- [ ] Added surfaces remain identifiable as reconstructed content.
- [ ] Each operation has a source reference and an inspection target.
- [ ] Numerical acceptance limits come from supplied requirements.
- [ ] Region references remain usable after any topology changes.
- [ ] The disposition names the intended use and remaining evidence gaps.

## Anti-patterns
- **Smooth means true:** A polished derivative is called more accurate without reference evidence. Fix: compare retained features and qualify the intended use.
- **Hole-fill laundering:** Reconstructed surface is presented as captured geometry. Fix: retain its region identifier and reconstruction label.
- **Original overwrite:** Cleanup destroys the only baseline. Fix: work on an identified copy and preserve the source.
- **Noise by appearance:** Unusual surface marks are removed because they look irregular. Fix: inspect references and protect ambiguous features.
- **Untraceable edits:** A final mesh is delivered without operation history. Fix: include region-level changes and derivative provenance.

## Worked example
**Input:**
> Fictional studio Ash supplies scan Raw-A of a decorative vessel for a presentation asset. Photo P shows a real chipped rim. A disconnected patch behind the vessel is identified by the owner as background. The underside was not captured. No processing tools are available; the owner asks for a cleanup plan with an optional closed underside.

**Output:**
```text
Scope: Raw-A decorative vessel; presentation preparation only, no mesh processing performed.
Preservation baseline: Preserve Raw-A unchanged. Protect the chipped rim supported by photo P. Prior processing history is not supplied.
Edit ledger:
Region | Proposed operation | Evidence | Risk to retained detail | Status
Background patch | Remove on derivative | Owner identifies background | Confirm region does not include vessel surface | Proposed
Chipped rim | Preserve | Photo P | Smoothing could erase real chip | Protected
Underside gap | Optional closure on presentation derivative | No captured underside | Added shape may be mistaken for observation | Proposed reconstruction
Reconstructed content: Identify underside closure in the edit ledger and derivative metadata; retain a conservative version without the closure.
Comparison checks: Confirm background removal boundary. Compare rim shape with Raw-A and photo P. Verify closure region remains labeled. Check derivative identifiers and operation history.
Disposition: proposed; no cleanup or fidelity inspection has been executed.
Handoff: Raw-A plus proposed derivative names, region annotations, and operation ledger. Owner must approve optional closure and define presentation acceptance criteria.
```

**Bad output:**
“Smooth the chipped rim and fill the underside; the cleaned scan is now a faithful complete capture.”
This removes an evidenced feature and misrepresents an invented surface as captured data.

## Edge cases
- **Only a processed mesh exists:** Mark the missing raw baseline and avoid claims about original capture fidelity.
- **Texture conceals geometric change:** Inspect geometry and appearance separately so a convincing texture cannot hide a removed feature.
- **Several capture passes disagree:** Preserve pass identifiers and unresolved alignment or surface conflicts instead of silently choosing one as true.
- **Sensitive or regulated intended use:** Request the applicable context and appropriate expert review before accepting cleanup for consequential measurement or evidentiary use.

## Test case
**Input:**
> Fictional artist Elm wants to smooth an engraved plate scan and close an unobserved back surface. The engraving must remain legible, but no acceptance tolerance or back reference exists. Only planning is possible.

**Assertions:**
1. Protects the engraving and specifies before-and-after inspection before accepting smoothing.
2. Labels the back closure reconstructed rather than captured.
3. Preserves an identified baseline and distinguishes proposed edits from execution.
4. Does not invent a numerical tolerance or claim processing occurred.
