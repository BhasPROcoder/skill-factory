# Spatial deformation and restoration: independent text executions

Reviewer: recover_interfaces (did not write the SDR procedures). Inputs: the six spatial requests in `plans/directory-batch2-requests.md` and the SDR skills. No answer key, mesh, render, screenshot file, production control values, or measurement records were supplied to the reviewer. The artifacts below are actual text responses; all geometry operations are proposed unless explicitly attributed to the input.

## SDR-001 / sleeve collapse

```text
Scope: Character and rig revisions pending. Investigate the reported sleeve collapse during combined arm raise and torso twist.
Reference conditions: Obtain the affected rig and costume revisions, stored neutral and failing poses, and animator-approved sleeve behavior. Fix mesh visibility, lighting and side/front views throughout; retain an unobstructed view of the sleeve.
Pose matrix:
Case | Pose/control evidence | Inspection target | Observation | Status
N | Neutral, actual stored pose needed | Sleeve at arm attachment and inner fold | None supplied | Unexecuted
A | Arm raised to its failing-pose setting, torso neutral | Sleeve silhouette at shoulder | None supplied | Unexecuted
T | Torso twisted to its failing-pose setting, arm neutral | Seam and attachment | None supplied | Unexecuted
AT | Both settings from the reported pose | Point where sleeve narrows or penetrates body | Collapse reported, no capture inspected | Reproduction pending
Path | Replay movement into and out of AT | First onset and recovery of fold | Unknown | Unexecuted
Interaction coverage: Single-control cases distinguish an interaction from a defect already present in a component motion; check transitions as well as endpoints.
Defect handoff: Report describes collapse, not its cause. Ask animator for pose references, contrasting intended folds, and matched captures. Compare the same sleeve region across cases before isolating weights or constraints.
Retest boundary: Rerun AT, neighboring poses on both sides of onset, and A/T/N under matched conditions after any authorized fix.
Disposition: Untested; a test matrix is available, but no rig or observation evidence establishes the failure mechanism.
```

## SDR-001 / neutral screenshot

```text
Scope: Review limited to the team's report of a neutral screenshot. No asset revision, intended range or test rig available.
Reference conditions: Preserve the screenshot as a neutral-view reference when supplied. Request (1) asset/rig revision and controls, (2) intended shot motions and required combinations, (3) target features, acceptance examples and inspection views.
Pose matrix:
Case | Pose/control evidence | Inspection target | Observation | Status
Neutral | Reported screenshot only | Visible silhouette in its view | No image available for inspection here | Reference pending
Production extreme | Required pose/range unknown | Region stressed by intended motion, to be identified | No evidence | Blocked
Combined motion | Production dependency unknown | Shared affected region, to be identified | No evidence | Blocked
Transition | Desired movement between approved poses unknown | Onset of discontinuities across movement | No evidence | Blocked
Interaction coverage: A single static view supplies no evidence for combined motions, unseen surfaces, or transitions.
Defect handoff: No defect established. Agree a bounded motion brief and inspect approved pose references in a copy of the rig.
Retest boundary: Retain the eventual failing and neighboring passing poses as reproducible comparison cases.
Disposition: Blocked for certification. Even passing a selected matrix would establish only that matrix under its specified conditions.
```

## SDR-001 / topology and weights changed

```text
Scope: A posed character reportedly tears after changes to topology and weights. Identify the exact before/after mesh and weight revisions before comparison.
Reference conditions: Freeze shared pose, control values, rig settings, camera and garment visibility. Record the same surface landmark across topology revisions; old vertex indices may no longer identify it.
Pose matrix:
Case | Pose/control evidence | Inspection target | Observation | Status
Old pair | Before mesh and original weights; same suspect pose | Seam at reported tear | Baseline behavior not supplied | Unexecuted
New pair | After mesh and new weights; same pose | Corresponding seam | Tear reported, not independently reproduced | Unexecuted
Weights-only trial | Fixed compatible mesh; approved alternate weight set | Whether separation changes at the matched seam | None | Conditional on valid correspondence
Topology trial | Matched pose and a documented comparable binding across meshes | Connectivity or geometry gap at landmark | None | Conditional; mapping may confound comparison
Control pose | Repeat paired comparison in neutral and neighboring poses | Pose-specific versus static gap | None | Unexecuted
Interaction coverage: The observed change involved two variables. Do not transfer weights by old vertex index across incompatible meshes. If comparable bindings cannot be established, classify the mixed comparison as unresolved.
Defect handoff: Record actual geometry separation independently of the presumed cause. Inspect the neutral seam, connectivity and deformation in matched captures before proposing repair.
Retest boundary: Repeat the suspect pose, transition into it, neutral and adjacent earlier-good poses on a preserved copy.
Disposition: Untested. Existing report cannot isolate topology from weight changes; no repair or weight transfer performed.
```

## SDR-002 / hidden surface behind handle

```text
Scope: Museum scan, source identifier and intended use pending. Plan a derivative only; scanner reportedly lacked a view behind the handle.
Preservation baseline: Keep the original scan and available acquisition evidence unchanged; annotate the handle rim and missing region in named views. Treat the capture boundary as evidence of missing coverage, not of the original hidden shape.
Edit ledger:
Region | Proposed operation | Evidence | Risk to retained detail | Status
Captured handle and rim | Preserve existing surfaces and reference landmarks | Described scan coverage; raw evidence to inspect | Filling could move the measured boundary | Protected
Occluded interior | Leave open in evidence copy; optionally fill on separate presentation copy | No measured surface behind handle | Fabricated contour could be mistaken for measured geometry | Proposed only
Reconstructed content: Identify any filled faces as inferred additions using region annotation plus an accompanying edit record that survives export. Do not label a closure as measured.
Comparison checks: Compare rim landmarks and captured handle detail before/after; inspect patch boundaries. Verify exported patch provenance independently of mesh appearance.
Disposition: Proposed; no change or physical fidelity verified. Confirm intended use and acceptability of a visibly identified reconstruction.
Handoff: Retain source scan, untouched evidence copy, separately named proposed display derivative, region map and unknown hidden shape.
```

## SDR-002 / attractive mesh without history

```text
Scope: Supplied mesh of unknown provenance, described as visually attractive. Original-fidelity certification requested; no raw scans, scale reference or edit history supplied.
Preservation baseline: Preserve the incoming mesh as received; identify it as received mesh, not scan original. Acquisition conditions, units and preexisting edits remain unknown.
Edit ledger:
Region | Proposed operation | Evidence | Risk to retained detail | Status
All surfaces | No cleanup on the received copy | No trusted baseline | Changing it would make even the received state unrecoverable | Hold
Suspected defects | Record candidate areas for review only when inspectable | Appearance alone cannot distinguish source detail and synthesis | Misclassifying undocumented edits as measured | Unresolved
Reconstructed content: Unknown; absence of an edit history does not mean no surfaces were invented.
Comparison checks: Request (1) raw captures and source identifiers, (2) scale evidence and registration references, (3) processing history and acceptance criteria. Compare against supplied originals only if they become available.
Disposition: Blocked for faithful-original certification. A descriptive review of the supplied derivative remains possible within its evidence limits.
Handoff: Return source request, unchanged received-file reference and unresolved provenance/scale/edit status. Do not call the file a certified cleaned original.
```

## SDR-002 / notch removed during smoothing

```text
Scope: Investigate a reportedly removed notch in a smoothed derivative; treat the notch as potentially identifying until reviewed.
Preservation baseline: Preserve the current derivative and any earlier versions separately. Locate a pre-smoothing baseline, raw capture views of the notch, smoothing history and a stable surrounding landmark.
Edit ledger:
Region | Proposed operation | Evidence | Risk to retained detail | Status
Notch landmark | Compare pre/post surfaces and raw views at matching scale | Operator reports smoothing removed it; physical significance unknown | Mistaking an identifying feature for noise | Freeze further smoothing
Notch region on working copy | If baseline exists, rerun from that baseline with the region protected or omit smoothing | Requires pre-edit source and confirmed region | Reintroducing unrelated defects or changing nearby surfaces | Conditional proposal
Reconstructed content: If no reliable source exists, do not invent the original notch. Any illustrative reconstruction stays on a separately labeled derivative and cannot substitute for recovery evidence.
Comparison checks: Identify source lineage; inspect notch profile and neighboring surface using matched views; obtain owner interpretation; check that a proposed recovery preserves adjacent detail and its annotations.
Disposition: Revise or withhold the affected derivative pending investigation. No file restored; notch authenticity remains unresolved.
Handoff: Retain the smoothed version, historical source if obtained, event note, local comparison views and review decision. Flag any downstream copies that may require a corrected replacement.
```

Review verdict: The rig procedure produced a discriminating interaction matrix without universal certification; scan cleanup preserved the difference between a measured region, a proposed repair and a missing source. No blocking issue identified in these six cases. No actual scene, physical scan, restoration or cross-runtime behavior was tested.
