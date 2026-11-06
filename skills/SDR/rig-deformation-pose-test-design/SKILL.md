---
id: SDR-001
name: rig-deformation-pose-test-design
domain: Spatial Deformation and Restoration
subdomain: Deformation review
version: 1.0
description: Build a pose-based deformation review matrix when a character rig must preserve intended shape and attachments throughout specified movements.
triggers: ["test character rig deformation", "check a rig in extreme poses", "plan skinning review", "inspect joint collapse", "verify facial and body pose combinations", "prepare animation deformation tests"]
not_for: ["creating a complete character rig", "generic software state-transition testing [TST-003]", "coordinate and unit transfer [SPD-001]", "medical or biomechanical validation"]
requires: []
risk_level: medium
---

# Rig Deformation Pose Test Design

## Purpose
Produce a repeatable pose matrix that reveals shape, attachment, and control-interaction failures in an animated character. The result connects each pose to an intended visual property and records whether that property was inspected, rather than declaring the rig good because its neutral pose looks convincing.

## Inputs to collect
1. **Asset revision** — mesh, rig, attachment, and corrective-shape identifiers. These make comparisons repeatable. Default: require named revisions before accepting any inspection result.
2. **Intended motion** — actual poses, expressions, gestures, and combinations needed in the production. These define useful coverage. Default: ask for representative motion rather than invent universal joint limits.
3. **Shape intentions** — silhouettes, creases, volume appearance, and stylized exaggerations the artist wants preserved. These distinguish defects from deliberate design. Default: unresolved artistic criteria stay open.
4. **Control evidence** — available controls, allowed ranges, constraints, and dependencies. These define reproducible poses. Default: only supplied controls and ranges may be used in concrete cases.
5. **Viewing conditions** — cameras, lighting, display shading, and relevant close-up views. These prevent changed presentation from concealing deformation. Default: preserve the supplied neutral review view and identify additional views as proposals.
6. **Execution access** — inspectable rig or only notes and images. This determines whether cases can be run. Default: a test specification with no performed inspection claims.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Record the exact asset and rig revision associated with each supplied observation; do not compare different revisions under one result label.
2. Translate intended movement into named poses using the actual supplied controls, including their values or an unambiguous stored-pose reference.
3. Establish a neutral reference that exposes the affected regions and attachments under consistent viewing conditions.
4. Identify representative motion boundaries from the supplied production range, rather than importing supposedly realistic angles from memory.
5. Assign each pose a local inspection target: elbow silhouette, mouth-corner separation, eyelid coverage, costume attachment, or another explicitly requested feature.
6. ⚠️ Add combined-control poses where dependencies could interact, such as a facial expression during a head turn; testing each control alone does not establish combined behavior.
7. Specify inspection views and concrete defect descriptions for each case, separating intended folds from unintended penetration, detached elements, or sudden shape discontinuities.
8. Include movement between selected poses when transition behavior matters; a pair of satisfactory endpoints does not establish satisfactory intermediate frames.
9. Execute available cases on a copy and capture pose settings with observations; otherwise mark them unexecuted and identify the evidence needed to run them.
10. ⚠️ Separate the observed defect from its suspected cause; a collapsed-looking region does not by itself identify weights, topology, constraints, or corrective shapes as the cause.
11. After a proposed correction, rerun the failing case and nearby previously acceptable cases using the same review conditions.
12. Deliver the matrix with coverage gaps and a bounded disposition tied to the intended motion, not a universal claim that the rig is production-ready.

Use observable language such as an attachment leaving its anchor, a silhouette suddenly narrowing, or a lip surface crossing its opposing surface. Words such as natural or attractive require a supplied visual reference and an explanation of which feature matters. Keep aesthetic acceptance separate from mechanical reproducibility: a pose can be reproducible while still awaiting art approval.

Before using application-specific control names or capture functions, use `[VERIFY: current control, pose storage, and evaluation behavior in the installed animation application's official documentation and the supplied rig documentation]`. Record actual versions when cases are executed; a readable matrix is not a scene file.

This Python 3 example checks a fictional review record for a dangerous bookkeeping failure: accepting a case without inspection evidence. It does not evaluate geometry. Execute it with the available Python 3 interpreter and record its version when using it.

```python
cases = [
    {"pose": "reach", "status": "accepted", "evidence": "capture-A"},
    {"pose": "reach-smile", "status": "untested", "evidence": None},
]
assert all(c["status"] != "accepted" or c["evidence"] for c in cases)
assert any(c["status"] == "untested" for c in cases)
print("Acceptance evidence present; coverage remains incomplete")
```

## Decision rules
- IF isolated controls pass but a required combination is untested THEN retain a coverage gap BECAUSE separate tests cannot establish their interaction.
- IF the intended motion range is unknown THEN request production poses BECAUSE arbitrary extremes may miss real tasks or test unsupported behavior.
- IF a shape defect appears THEN record its visible location and pose before naming a cause BECAUSE several rig or mesh mechanisms can produce similar symptoms.
- IF a correction changes a shared dependency THEN rerun neighboring poses BECAUSE a local repair can alter other required movements.
- IF only screenshots are available THEN limit conclusions to those views and poses BECAUSE hidden surfaces and transitions remain unobserved.

## Output template
```text
Scope: <asset revision and intended motion; up to two lines>
Reference conditions: <neutral pose, views, and fixed display settings; up to four lines>
Pose matrix:
Case | Pose/control evidence | Inspection target | Observation | Status
<up to eight cases; attach additional cases if needed>
Interaction coverage: <required combinations and gaps; up to four lines>
Defect handoff: <observed symptom, suspected causes clearly qualified, next discriminating check>
Retest boundary: <failed and neighboring cases to repeat>
Disposition: <accepted for stated coverage / revise / blocked / untested; explain evidence>
```

## Quality checklist
- [ ] Asset and rig revisions are identified or explicitly unresolved.
- [ ] Poses use supplied controls or stored-pose references.
- [ ] Every case names a concrete region and observable property.
- [ ] Required combined controls are represented or listed as gaps.
- [ ] Neutral and posed inspections use recorded viewing conditions.
- [ ] Suspected causes are separated from visible observations.
- [ ] Accepted cases have inspectable evidence references.
- [ ] Transition coverage is explicit when intermediate motion matters.
- [ ] Retesting includes relevant previously acceptable cases.

## Anti-patterns
- **Neutral-pose approval:** A stationary character becomes proof of animation readiness. Fix: test intended movement and interactions.
- **Extreme-pose guessing:** Unspecified angles are treated as mandatory limits. Fix: use supplied production ranges and document missing ones.
- **Cause leap:** A pinched silhouette is immediately blamed on one weight. Fix: record the symptom and isolate possible mechanisms.
- **View switching:** A flattering camera hides the problem after repair. Fix: retain the original comparison view.
- **Repair-only retest:** The corrected pose passes while adjacent poses are ignored. Fix: repeat dependent and neighboring cases.

## Worked example
**Input:**
> Fictional studio Reed supplies character Fox revision R3 and stored poses Neutral, Reach, Smile, and ReachSmile. The intended shot requires ReachSmile. Capture A shows the sleeve staying attached in Reach; no combined-pose capture exists. The artist wants the sleeve to remain at the wrist anchor. No rig execution is available.

**Output:**
```text
Scope: Fox R3; review sleeve attachment during the supplied reach and smile combination.
Reference conditions: Use Neutral and the view associated with capture A; its lighting and display settings still need recording.
Pose matrix:
Case | Pose/control evidence | Inspection target | Observation | Status
P-reach | Stored Reach | Sleeve stays at wrist anchor | Supplied capture A shows attachment in its visible view | Observed, limited to capture
P-combined | Stored ReachSmile | Same attachment during combined controls | No capture supplied | Untested
Interaction coverage: ReachSmile is required and remains a gap; isolated Reach does not establish combined behavior.
Defect handoff: No combined-pose defect is established. Obtain a capture using the same view before proposing a cause or repair.
Retest boundary: If a correction is needed, repeat ReachSmile and Reach, plus their transition if used in the shot.
Disposition: untested for required combined motion; no live rig inspection performed.
```

**Bad output:**
“Reach looks fine, so the combined expression is approved; adjust elbow weights if anything goes wrong.”
This approves an unobserved interaction and guesses a repair without a defect.

## Edge cases
- **Stylized intentional collapse:** Record the artist's intended shape and judge against it rather than an assumed anatomical standard.
- **Asymmetric character:** Test left and right requirements independently when their geometry or rig behavior differs.
- **Attachment added after review:** Treat affected captures as belonging to the old revision and rerun relevant poses.
- **Nonrepeatable playback issue:** Capture evaluation conditions and repeated attempts before assigning a deterministic cause.

## Test case
**Input:**
> Fictional character Fern passes a supplied Blink pose and a supplied HeadTurn pose independently. The intended scene combines them, but no combined inspection exists. The team asks for final approval.

**Assertions:**
1. Lists the combined pose as an untested requirement rather than approved behavior.
2. Specifies an eyelid or eye-region observation under consistent views.
3. Does not invent control values or claim live execution.
4. Limits disposition to the supplied evidence and requests the missing combined test.
