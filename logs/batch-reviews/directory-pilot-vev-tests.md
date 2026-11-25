# Independent VEV pilot execution record

Reviewer: directory_interfaces agent, which authored UST rather than VEV. Inputs: coordinator fixtures in plans/directory-pilot-tests.md. Reviewed both VEV procedures and executed the following fresh requests as text tasks. Assertions were visible to the reviewer, so these are assertion-guided executions rather than blind tests. These are actual reviewer-produced outputs, not live renders or external factual verification. Structural checks and final acceptance remain the coordinator's responsibility.

## VEV-001 ordinary: museum source types

Input: Original wall fragment, later eyewitness sketch, and artist-invented roof in a fictional museum reconstruction.

```text
Scene scope: Distinguish the supplied surviving wall, later sketch interpretation, and invented roof in one reconstruction.
Claim ledger:
Claim | Depiction | Status | Supplied support | Remaining uncertainty
W | Surviving wall fragment | Documented within supplied premise | Original fragment; source identifier missing | Measurements, hidden surfaces, and authenticity review not supplied
S | Features depicted in later sketch | Unresolved pending claim-level support | Eyewitness sketch; identifier missing | Exact dimensions and relation to each depicted feature unknown
R | Artist's roof | Illustrative | Supplied artist-invention statement | Historical roof form unknown
Visual encoding: Documented = text plus solid boundary; unresolved = text plus dotted boundary; illustrative = text plus patterned boundary.
Visitor labels: W: Surviving wall fragment; unmeasured dimensions are not established. S: Later eyewitness depiction; exact dimensions remain unverified. R: Roof invented for this illustration; historical roof form unknown.
View and export rules: Keep the roof label in the default view. Attach local labels to cropped views. Retain the status legend in standalone exports.
Verification: Proposed crop inspection only; no actual scene or image was supplied.
Open decisions: Request source identifiers, wall measurements, and the sketch's claim-level rationale before approving further documented or inferred labels.
```

Assertion results: PASS source types separated; PASS roof visibly labeled illustrative; PASS sketch does not establish exact dimensions. No invented source identifiers were substituted for missing archive records.

## VEV-001 missing: photorealistic image without sources

```text
Scene scope: Prepare evidence labels for an unspecified photorealistic reconstruction with no provenance packet.
Claim ledger:
Claim | Depiction | Status | Supplied support | Remaining uncertainty
U | Scene features, pending inventory | Unresolved | Image appearance only | Source basis for geometry, position, material, and function absent
Visual encoding: Unresolved = persistent text label and dotted callout boundary; do not encode any feature as documented yet.
Visitor labels: U: Reconstruction source evidence has not been supplied; visual realism does not verify the depicted history.
View and export rules: Retain the unresolved-evidence caption in every standalone image. Add claim-level labels after a feature inventory is supplied. Do not remove the caveat for promotional crops.
Verification: Pending inspection; the request describes an image but provides no inspectable visual or source record in this fixture.
Open decisions: Which features are depicted? What source records support their shape, placement, and finish? Which additions were inferred or invented by the reconstruction team?
```

Assertion results: PASS realism not treated as evidence; PASS provenance requested; PASS unknown features not classified as verified. Questions are consolidated into three items.

## VEV-001 edge: conflicting doorway evidence

```text
Scene scope: Preserve disagreement between two supplied doorway-location records in a fictional reconstruction.
Claim ledger:
Claim | Depiction | Status | Supplied support | Remaining uncertainty
D | Doorway location | Disputed | Two supplied records; exact identifiers missing | Which location is better supported remains unresolved
Visual encoding: Disputed = text label plus patterned outline; alternative A and B carry equally persistent explanatory labels.
Visitor labels: D: Source records disagree about the doorway location; these alternatives show the unresolved interpretations.
View and export rules: Present separate labeled alternatives rather than blending them. Retain the disagreement caption in crops. Do not make one option the unlabeled definitive view.
Verification: Proposed alternative-view review only; no rendering was supplied.
Open decisions: Request the two source identifiers, their depicted locations, and the editorial rationale for evaluating the conflict before selecting a preferred reconstruction.
```

Assertion results: PASS conflict visible; PASS alternatives preserve uncertainty; PASS no confidence percentage invented.

## VEV-002 ordinary: measured, simulated, and interpolated values

```text
Viewer task: Distinguish a fictional building's measured room temperature, next-day simulation, and interpolated missing sensor value.
Origin ledger:
Quantity | Origin | Source or scenario | Time and entity | Comparison limit
Measured temperature | Observed | Supplied measurement; identifier missing | Room and observation time require confirmation | Units and interval unknown
Next-day temperature | Scenario output | Supplied simulation; revision missing | Next day relative to an unspecified reference date | Horizon must be anchored before comparison
Filled sensor value | Derived estimate | Interpolation; method missing | Missing sensor interval and location unspecified | Not a direct measurement
Encoding: Observed = labeled solid marker; scenario = labeled outlined marker; derived estimate = labeled dashed marker with missing-observation cue.
Display states:
State | Visible label | Permitted comparison | Interpretation blocked
Observation only | Measured, observation time pending | Inspect supplied origin | Unqualified current-temperature claim
Scenario active | Simulated next day, anchored date pending | Separate exploratory view | Future value represented as measured
Estimated gap | Interpolated; sensor observation missing | View the estimate with gap context | Interpolation represented as sensor evidence
Incompatible comparison | Definitions unresolved | No numerical residual | Unjustified direct subtraction
Scenario and export rules: Preserve observation time, anchored forecast horizon, and origin labels in exports. Keep the missing-sensor cue with the estimate. Record model revision before interpreting changed scenarios.
Uncertainty note: No quantified bounds were supplied; do not invent them. Missing time, unit, and method details limit comparison.
Verification: Pending visual inspection; check a standalone export for all three origin classes once a display exists.
```

Assertion results: PASS three evidence classes labeled; PASS prediction horizon separated from observation time; PASS interpolation not shown as measured.

## VEV-002 missing: unlabeled temperature column

```text
Viewer task: Establish how to label a temperature column whose origin metadata is absent.
Origin ledger:
Quantity | Origin | Source or scenario | Time and entity | Comparison limit
Temperature column | Unknown | Lineage absent | Time, location, units, and aggregation unspecified | Cannot classify or compare as measured or simulated
Encoding: Unknown = persistent origin-unknown label plus dotted marker; numeric appearance does not determine origin.
Display states:
State | Visible label | Permitted comparison | Interpretation blocked
Unknown origin | Origin not supplied | Inspect raw values as unclassified | Claim that values are direct observations
Missing metadata | Definitions pending | No direct comparison with other streams | Implied matching units or intervals
Scenario unresolved | Scenario status unknown | No scenario inference | Guessing model provenance from formatting
Scenario and export rules: Preserve unknown-origin labeling in exported views. Add classification only after lineage is established.
Uncertainty note: Both origin and uncertainty evidence are missing; precision of formatting supplies neither.
Verification: Pending provenance review and visual inspection. Request source lineage and transformation history; represented time and entity; units and aggregation definition.
```

Assertion results: PASS class remains unknown; PASS lineage requested; PASS no classification inferred from numeric appearance. The skill supports an unknown-origin path without inventing data or executing code.

## VEV-002 edge: new simulation run with old input snapshot

```text
Viewer task: Explain a newly rerun simulation while retaining the age of its unchanged measured-input snapshot.
Origin ledger:
Quantity | Origin | Source or scenario | Time and entity | Comparison limit
Measured input snapshot | Observed input | Supplied unchanged snapshot; identifier pending | Older observation time, exact time missing | Not refreshed by the rerun
Updated model result | Scenario output | New run with changed assumptions; revision pending | Run time is newer; represented time unspecified | New computation does not establish a new observation
Encoding: Observed input = labeled solid marker with snapshot time; scenario output = outlined marker with run identity and changed-assumption caption.
Display states:
State | Visible label | Permitted comparison | Interpretation blocked
Original inputs | Observed input snapshot, old time | Inspect retained baseline | Treating input age as run age
New scenario | Rerun; assumptions changed | Inspect scenario separately | Calling the result a fresh measurement
Comparison pending | Represented time unspecified | No direct numerical residual | Unjustified accuracy conclusion
Scenario and export rules: Retain both observation time and run time. Record the changed assumptions and new revision. Preserve the original snapshot identifier. Include represented time before any aligned comparison.
Uncertainty note: No uncertainty bounds or validation result were supplied; a newer run does not establish better accuracy or fresher observations.
Verification: Pending inspection; check that a static export retains snapshot time, run time, revision, and assumption changes.
```

Assertion results: PASS both time concepts retained; PASS changed assumptions recorded as required metadata; PASS rerun not presented as fresh observation.

## Review findings

No blocking issue found in these six text executions. VEV-001 separates feature-level evidence from image realism and includes crop/export interpretation. VEV-002 separates measurement origin, transformations, scenario assumptions, and comparability. These scopes are distinct from UST-001: VEV-002 classifies what a value represents, while UST-001 specifies recency and transport recovery for an observation whose origin is already known. No live rendering, external historical verification, predictive validation, or cross-model reliability is demonstrated by this record.
