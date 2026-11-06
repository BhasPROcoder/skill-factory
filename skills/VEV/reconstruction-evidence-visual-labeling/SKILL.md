---
id: VEV-001
name: reconstruction-evidence-visual-labeling
domain: Visual Evidence Interpretation
subdomain: Reconstruction interpretation
version: 1.0
description: Design visible evidence labels for historical or museum reconstructions when documented features, inferred geometry, and illustrative additions share one scene.
triggers: ["label uncertain parts of a reconstruction", "show evidence behind this museum model", "distinguish restored from documented geometry", "annotate a historical scene", "explain conjecture in a virtual exhibit"]
not_for: ["general image and text composition [MVA-007]", "general art-direction production handoff [MVA-009]", "forensic reconstruction or legal testimony", "establishing historical facts without source evidence"]
requires: []
risk_level: medium
---

# Reconstruction Evidence Visual Labeling

## Purpose
Produce a scene annotation specification that lets viewers distinguish what a supplied source supports from what the reconstruction team inferred or invented for illustration. The deliverable is an evidence-linked labeling plan and verification task, not a certification that the reconstruction is historically correct.

## Inputs to collect
1. **Scene inventory** — named objects, surfaces, and views; identifies where claims occur. Default: none; request an inventory or a representative scene description.
2. **Evidence packet** — supplied photographs, measurements, descriptions, and their identifiers; establishes support. Default: no supported claims until relevant evidence is supplied.
3. **Reconstruction rationale** — how missing features were selected; distinguishes inference from decoration. Default: classify unexplained additions as unresolved.
4. **Audience and viewing format** — kiosk, guided display, print, or interactive model; determines persistent versus on-demand explanations. Default: general visitors viewing a static image.
5. **Editorial authority** — person or team allowed to approve interpretation; identifies unresolved decisions. Default: approval pending, without inventing an owner.
6. **Reuse contexts** — screenshots, cropped images, promotional stills, or exports; prevents evidence labels disappearing downstream. Default: assume the main view may be copied separately.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Divide the scene into claims at the level supported by the evidence. An object's location, shape, surface finish, and function can have different support; do not assign one confidence label to the entire object when those differ.
2. Give each claim a stable local identifier and copy its source identifier exactly. Record missing source identifiers as missing; do not create plausible archive citations.
3. Classify each claim as documented, inferred, illustrative, disputed, or unresolved. Documented means the supplied evidence supports that particular claim, not that the source is automatically authentic or complete.
4. ⚠️ Write the inference bridge explicitly: what is observed, what assumption connects it to the depiction, and what remains unknown. Replace unsupported precision with a bounded statement rather than inventing a probability.
5. Assign a visible text cue and an additional observable treatment to each class. For example, use a repeated word label plus a patterned outline; ensure the distinction survives without color. Specify which surfaces or annotations carry the cue.
6. Write concise visitor labels that name the uncertain feature directly. Prefer “Roof profile inferred from the supplied comparison drawing” over a vague global warning that the whole reconstruction is approximate.
7. Define default, evidence-inspection, and export behavior. Essential uncertainty must remain visible in the default view; detailed provenance may appear in a linked panel. A static export needs a retained legend and claim references.
8. Test a representative crop and an isolated object view against the labeling plan. Mark the test proposed if no actual image is available. Check whether either view could make an inferred feature look documented.
9. Assemble the specification with unresolved editorial questions and the exact evidence needed to settle them. Keep alternative interpretations visible when the supplied packet does not justify choosing one.

## Decision rules
- IF a source supports dimensions but not decoration THEN classify those claims separately BECAUSE support for shape does not establish surface appearance.
- IF competing sources support different depictions THEN expose the competing interpretations or leave the feature disputed BECAUSE a polished scene cannot resolve conflicting evidence.
- IF labels are hidden during an immersive view THEN retain an uncertainty cue and an accessible route to the explanation BECAUSE visual realism can otherwise conceal reconstruction choices.
- IF the source packet is incomplete THEN label the relevant claim unresolved BECAUSE absence from the packet does not prove the original feature was absent.
- IF a crop removes the evidence legend THEN add a local caption or prohibit that export state in the handoff BECAUSE the detached image must remain interpretable.

## Output template
```text
Scene scope: <one sentence>
Claim ledger: <up to 8 representative claims; continue in an attachment if needed>
Claim | Depiction | Status | Supplied support | Remaining uncertainty
Visual encoding: <one short line per used status>
Visitor labels: <one short sentence per claim needing explanation>
View and export rules: <up to 4 rules>
Verification: <proposed or performed check, evidence, result>
Open decisions: <up to 4 questions and the evidence needed>
```

## Quality checklist
- [ ] Shape, position, finish, and function are separated where their support differs.
- [ ] Every documented claim points to supplied evidence.
- [ ] Every inference states its bridge and remaining uncertainty.
- [ ] Status meanings appear in text rather than color alone.
- [ ] Default and exported views preserve essential uncertainty cues.
- [ ] Visitor labels name the relevant feature rather than making a blanket disclaimer.
- [ ] Disputed evidence is not silently reduced to one authoritative depiction.
- [ ] Verification states whether an actual view was inspected.

## Anti-patterns
- **Confidence paint:** A colored overlay supplies unexplained certainty. Fix: define the categories and attach feature-level evidence.
- **Whole-object certainty:** A measured foundation makes an imagined roof look documented. Fix: separate the foundation and roof claims.
- **Legend exile:** The explanation exists only in a different document. Fix: retain a concise legend or caption in each standalone view.
- **Aesthetic certainty:** Detailed texture is treated as historical support. Fix: classify decorative choices as illustrative unless the packet supports them.
- **False absence:** An incomplete image becomes proof that a feature never existed. Fix: describe the visibility limit and leave the claim unresolved.

## Worked example
**Input:**
> Fictional exhibit team Larch supplies scene Court-A, photo P showing a low surviving wall, sketch S proposing a roof profile, and no evidence about wall color. The planned scene adds a red surface for readability. Visitors see a static image that may be cropped. No rendering is supplied.

**Output:**
```text
Scene scope: Label supported remains and reconstruction choices in Court-A.
Claim ledger:
Claim | Depiction | Status | Supplied support | Remaining uncertainty
C-wall | Surviving low wall | Documented | Photo P | Hidden surfaces not established
C-roof | Proposed roof profile | Inferred | Sketch S | Sketch rationale not supplied
C-color | Red wall surface | Illustrative | Team readability choice | Historical color unknown
Visual encoding: Documented = text label with solid boundary; inferred = text label with dashed boundary; illustrative = text label with patterned swatch.
Visitor labels: C-roof: Proposed roof profile follows sketch S; historical support remains unresolved. C-color: Red is an illustrative display choice, not a documented historical color.
View and export rules: Keep the status legend with the full image. Keep local roof and color captions in crops. Omit claims about hidden wall surfaces.
Verification: Proposed crop review only; no rendering was supplied, so visual legibility has not been tested.
Open decisions: What evidence supports sketch S? Request its source rationale before approving the roof interpretation.
```

**Bad output:**
“This accurately recreates the red-walled roofed courtyard; the photograph confirms the reconstruction.”
This transfers support for one visible feature to an unsupported roof and color.

## Edge cases
- **Evidence arrives after publication:** Identify affected claim identifiers, revise labels, and record which exports need replacement; do not silently change the scene's interpretation history.
- **No interactive annotation capability:** Use numbered callouts with a nearby ledger and retained export caption rather than promising an unavailable inspection mode.
- **Several plausible reconstructions:** Present separate labeled alternatives or a clearly marked switch; do not blend alternatives into a scene that no source supports.
- **Sensitive cultural interpretation:** Identify whose interpretation is represented and request appropriate editorial consultation; do not invent community endorsement.

## Test case
**Input:**
> Fictional museum Pine supplies a measured doorway outline, a conjectural arch drawn by its designer, and an old image that does not show the roof. Prepare labels for a cropped promotional still. No finished still is available.

**Assertions:**
1. The doorway outline and conjectural arch receive separate evidence statuses.
2. The unseen roof is not declared historically absent.
3. The cropped still retains a local uncertainty label or caption.
4. Verification is proposed rather than claimed performed.
