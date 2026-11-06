# Independent spatial pilot execution records

Reviewer: directory_visual_evidence agent, separate from the author. Inputs are the coordinator's six requests in plans/directory-pilot-tests.md. These are executed text-artifact tasks, not actual mesh imports or material renders. Structural checks are separate. Review found one clarity improvement: explicitly verify active material assignment and the candidate input's connection to the visible output before interpreting identical renders; author notified.

## SPD-001 ordinary

Asset: Fictional Alder chair; source and receiving revision identifiers pending.
Contract: Source centimeters, Z-up, front negative Y. Receiver meters, Y-up, front positive Z. Pivot and hierarchy requirements pending.
Conversion ownership: Assign length conversion once to the chosen transfer stage; verify that stage's actual behavior. Proposed direction mapping: source positive Z to target positive Y; source negative Y to target positive Z. Remaining axis/handedness behavior requires confirmation with an asymmetric witness.
Witnesses: Supplied width 80 centimeters gives expected width 0.8 meters. Request an asymmetric left/right feature and named origin landmark.
Results: Expected width 0.8 meters; no observed import. Orientation mapping is proposed, not verified. Pivot and inherited transforms untested.
Disposition: untested
Next check: Receiving scene team confirms pivot, hierarchy, remaining axis behavior and acceptance limits, then imports a copy and records width and orientation witnesses.

Assertions: PASS expected width; PASS explicit partial mapping with unresolved handedness; PASS no claim conversion occurred. Arithmetic checked independently: 80 / 100 = 0.8.

## SPD-001 missing input

Asset: Unidentified asset; source and destination revisions unknown.
Contract: Units and axes unknown. “Normal size” and “standard axes” do not establish physical interpretation. Pivot and hierarchy expectations unknown.
Conversion ownership: Unresolved; no conversion factor assigned.
Witnesses: Need an author-confirmed physical dimension, asymmetric orientation feature, and origin landmark.
Results: No expected physical dimensions or observed receiving measurements can be established from the supplied description.
Disposition: blocked
Next check: Please provide (1) the source and destination units and axis conventions, (2) one confirmed physical dimension plus named orientation/origin references, and (3) the transfer path and acceptance requirements.

Assertions: PASS no guessed convention; PASS questions consolidated into one three-question request; PASS blocked disposition.

## SPD-001 edge

Asset: Imported asset with mirrored asymmetric badge and shifted origin; revision identities pending.
Contract: Preserve badge orientation and intended origin role; matching dimensions are only one witness. Exact axis and pivot contracts require supplied confirmation.
Conversion ownership: Keep original asset untouched; inspect source, exporter, and importer transform ownership on a separate test copy before choosing a correction.
Witnesses: Named badge distinguishes reflection from mere size agreement. Named source-origin landmark tests pivot placement independently. Supplied dimensions remain the scale witness.
Results: Reported size agreement does not pass orientation or origin checks. Badge reversal suggests investigating axis/reflection handling; shifted origin requires a separate pivot/hierarchy investigation. No repair inspected.
Disposition: revise
Next check: Receiving team records handedness and axis mapping, then separately compares pivot and parent transforms against the original copy before any correction is accepted.

Assertions: PASS size alone insufficient; PASS reflection and origin separated; PASS original preserved.

## SPD-002 ordinary

Symptom: Fictional Noor wants to compare stripe width on a ceramic prop; rendered images also differ in light direction and camera.
Hypothesis: A selected stripe-width parameter may explain width changes, but the supplied images cannot isolate its effect.
Controls: Hold camera, light direction, geometry, object scale, coordinate source, render settings, and viewing transform fixed at one documented baseline. Preserve the original material.
Comparison: Request the supplied stripe parameter and baseline/trial settings; change only that parameter in a copied scene. Inspect stripe width on the same named surface region, with a plain region as an unrelated-appearance control.
Evidence: Two rendered images are reported, but their changed lighting and camera confound attribution; no new controlled pair was rendered.
Conclusion: inconclusive for the existing comparison; the proposed isolation study is untested.
Follow-up: Obtain actual parameter and scene settings, verify the input's dependency path, then render the fixed-camera/fixed-light pair and record visible stripe-width differences.

Assertions: PASS confounding identified; PASS camera and light fixed; PASS single intended parameter and observable result specified without fabricated slider values.

## SPD-002 missing input

Symptom: “Make the shader better” supplies no observable target or affected region.
Hypothesis: Unspecified; no node structure or candidate cause can be established.
Controls: Preserve the current material and scene as the baseline if available; actual settings remain unknown.
Comparison: Bounded study brief only: select one observable target, identify one evidenced candidate input, and compare a baseline/intervention pair under fixed scene conditions once those inputs are supplied.
Evidence: No graph, images, or execution result supplied; no edits performed.
Conclusion: untested; the requested improvement has no defined visual criterion.
Follow-up: Please provide (1) the observable change you want and its region or reference image, (2) available material connections/settings and scene evidence, and (3) whether a copied scene can be rendered for comparison.

Assertions: PASS requests target and evidence; PASS no invented nodes/edits; PASS bounded study brief.

## SPD-002 edge

Symptom: Changing the tested input produces identical screenshots; the request states that the input is not connected to the visible material.
Hypothesis: The current test does not reach the displayed material output; it therefore cannot establish the parameter's effect when connected.
Controls: Preserve baseline material, scene and screenshots. Keep camera, lighting, geometry, coordinate source, display transform and render settings fixed for any follow-up.
Comparison: Confirm active material assignment on the inspected surface and trace the candidate input to the visible output. Use a separate copy for any intentionally connected comparison; record that connection change as a new baseline rather than hiding it inside a one-parameter trial.
Evidence: Supplied disconnected path explains why the previous test is not a valid intervention on the visible material. No new render has been executed.
Conclusion: inconclusive about the parameter's general effect; the unchanged screenshots do not show universal ineffectiveness.
Follow-up: Verify the active assignment and dependency path, establish the connected baseline, then vary only the intended parameter and inspect the same regions.

Assertions: PASS active material/path checked before conclusion; PASS baseline preserved; PASS no universal ineffectiveness claim.

## Review disposition

All six text executions satisfy the supplied assertions. SPD-002 should make the active-assignment/path check explicit before final acceptance; this record does not imply rendering or cross-model testing. Independent semantic review distinguishes SPD-001's scale/orientation/pivot transfer contract from general reproducibility handoffs, and SPD-002's controlled procedural-material dependency diagnosis from general configuration capture.
