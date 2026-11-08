---
id: EXP-003
name: exhibit-object-label-placement-reconciliation
domain: Exhibition Interpretation Operations
subdomain: Placement correspondence
version: 1.0
description: Reconcile exhibit objects, label identities and installed positions when a display move or rehang could attach accurate text to the wrong object.
triggers: ["check labels after a rehang", "match objects to installed labels", "reconcile an exhibit case map", "check a group label key", "resolve swapped display captions"]
not_for: ["changing interpretive claims [EXP-001]", "collection accession completeness [ARC-001]", "authorizing object handling or conservation treatment"]
requires: []
risk_level: medium
---

# Exhibit object label placement reconciliation

## Purpose
Create a correspondence record between object identity, approved label content and the positions visitors encounter. Separate a correct label proof from correct installation so a display can be reviewed without guessing identities from appearance or authorizing object movement.

## Inputs to collect
1. **Object identity list:** Obtain the display identifiers and their authoritative collection references. Required; a short title or resemblance is not a substitute for an identifier.
2. **Label inventory:** Obtain each label's identity, approved revision and intended object or group. Required for matching; mark unknown revisions instead of inventing approval.
3. **Placement evidence:** Obtain an annotated case plan, installation photographs or an observer's position record. Default: a proposed placement check, with actual installation unverified.
4. **Position convention:** Establish viewing direction, case name and row or position references. Default: request a labeled sketch rather than interpreting an ambiguous “left.”
5. **Group conventions:** Obtain the intended numbering, arrows, brackets or shared captions for grouped objects. Default: one explicit correspondence per object, with group design unresolved.
6. **Change and handling authority:** Identify the owner of the label schedule and the staff responsible for physical installation. Default: recommendations only; no handling or relocation.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Fix the reconciliation boundary: named display, plan revision and evidence date or observation session. Avoid merging photographs from before and after a rehang into a single apparent installation.
2. Build the intended map using collection identity, label identity and planned position as separate fields. A label title can repeat across objects; retain distinct record keys even when visible wording matches.
3. Build an observed map from the available evidence. Distinguish a legible identifier from an observer's inferred identity, and record obscured positions without filling them from the intended plan.
4. ⚠️ Normalize orientation before comparing positions. If the plan is viewed from behind the case and the photograph from the visitor side, obtain an annotated correspondence rather than swapping left and right by intuition.
5. Compare the intended and observed maps for missing labels, unused labels, duplicate assignments and object-label mismatches. Keep absence of photographic evidence separate from evidence that an item is absent.
6. Trace each group label's number, arrow or bracket to the actual object position. Check whether the visitor can resolve the correspondence from the public side without access to internal accession records.
7. Assess uncertain matches by requesting the smallest additional evidence: a readable label crop, a position annotation or confirmation by the responsible collection staff. Do not request physical handling merely to improve a photograph.
8. Propose corrections to label identity, directional references or installation schedule. If the intended object itself changed, obtain a revised interpretive assignment instead of moving a label solely because the titles look similar.
9. Define post-correction evidence that would resolve each mismatch. Recheck the affected group after a swap because correcting one label can create another unresolved position.
10. Deliver a reconciliation ledger with confirmed, conflicting and unknown correspondences. State whether any changes were proposed, carried out or independently observed; these are separate completion states.

## Decision rules
- IF visible titles repeat THEN match by the supplied identity records BECAUSE title equality does not establish object identity.
- IF orientation is ambiguous THEN hold position conclusions BECAUSE a mirrored view can make a correct installation appear swapped.
- IF a group key is correct internally but unclear from the visitor position THEN request a labeling revision BECAUSE an internal map alone does not convey the association.
- IF only an old photograph is available THEN limit findings to that observation BECAUSE it cannot establish the current display.
- IF correction requires moving an object THEN route the proposal to the authorized installation staff BECAUSE label reconciliation does not establish handling permission.

## Output template
```text
Scope: <display, plan revision and observation boundary; up to three lines>
Orientation: <agreed position convention or unresolved ambiguity; up to two lines>
Correspondence ledger: <up to ten rows; attach additional rows>
Position | Intended object and label | Observed evidence | Finding | Required resolution
Visitor mapping: <group key, arrow or adjacency issues; up to four lines>
Correction plan: <owner role and proposed change for each conflict; up to six actions>
Verification boundary: <confirmed positions, unknowns and evidence needed after correction; up to five lines>
```

## Quality checklist
- [ ] Object, label and physical position have separate identifiers.
- [ ] The comparison uses a stated plan revision and observation boundary.
- [ ] Viewing direction is resolved before left/right conclusions.
- [ ] Inferred identity is distinguishable from observed identity.
- [ ] Missing evidence is not described as a missing object.
- [ ] Group numbering and arrows are checked from the visitor side.
- [ ] Each proposed correction has a post-change observation requirement.
- [ ] No handling or completed installation is inferred from a recommendation.

## Anti-patterns
- **Title matching:** two similar bowls are assigned by their titles. Fix: use collection identity and a verified position reference.
- **Plan as observation:** intended positions are reported as installed. Fix: maintain intended and observed maps separately.
- **Mirror correction:** labels are swapped because an unexplained photograph seems reversed. Fix: resolve the viewing convention first.
- **Single-label tunnel:** one moved label is checked in isolation. Fix: inspect the other assignments affected by the move.
- **Hidden key:** group numbers exist only on a staff plan. Fix: verify the public correspondence mechanism.

## Worked example
**Input:** Fictional gallery Moss shows objects Cup-A and Cup-B in Case-C. Approved plan P assigns Cup-A with label L-A to visitor-left, Cup-B with L-B to visitor-right. A supplied staff observation confirms object identities in those positions but records L-B left and L-A right. No installation changes have been performed.

**Output:**
```text
Scope: Case-C, approved plan P, supplied staff observation only.
Orientation: Left and right are defined from the visitor side in both records.
Correspondence ledger:
Position | Intended object and label | Observed evidence | Finding | Required resolution
visitor-left | Cup-A and L-A | Cup-A with L-B, staff identity confirmation | label mismatch | installer to place approved L-A and verify association
visitor-right | Cup-B and L-B | Cup-B with L-A, staff identity confirmation | label mismatch | installer to place approved L-B and verify association
Visitor mapping: The present adjacency associates each cup with the other label; no group-key ambiguity was reported.
Correction plan: Label installation owner to correct both label assignments against P without a proposed object move.
Verification boundary: Object positions confirmed by supplied observation; both label corrections pending. Obtain a post-change position record covering both assignments.
```

**Bad output:** “The cups look similar, so swap the objects and reopen the case.”
This substitutes visual inference and an unauthorized handling action for the evidenced label mismatch.

## Edge cases
- A label describes several objects: retain its group identity and check the public key for every member instead of forcing a one-to-one match.
- A loan substitute shares the same title: require the revised object assignment and appropriate label revision before treating the old caption as applicable.
- Reflection obscures the label in a photograph: mark the observed label unknown and request an appropriate view or staff confirmation.
- A deliberately empty position is part of interpretation: record the approved empty position so it is not classified as a missing object.

## Test case
**Input:**
> Fictional display Fern has a rear-view plan and a front-view photograph. Both labels say “Vessel,” but the photograph does not show object identifiers. A colleague says they must be swapped.

**Assertions:**
1. Leaves the swap conclusion unresolved until orientation and identity evidence are available.
2. Does not use matching titles as identity proof.
3. Requests a position annotation or responsible staff identity confirmation.
4. Does not instruct physical object movement.
