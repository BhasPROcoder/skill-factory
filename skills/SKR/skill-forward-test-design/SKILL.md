---
id: SKR-003
name: skill-forward-test-design
domain: Reusable Skill Engineering
subdomain: Evaluation
version: 1.0
description: Design independent new tasks and checkable assertions to evaluate a skill, while separating test specifications, actual execution evidence, and unresolved reliability limits.
triggers: ["skill forward-test design", "help with skill forward-test design", "review my skill forward-test design", "prepare skill forward-test design", "apply skill forward-test design to these materials"]
not_for: ["Repertoire gap selection [SKR-001]", "Specialized workflow generalization [SKR-002]"]
requires: []
risk_level: low
---

# Skill forward-test design

## Purpose
Produce a forward-test specification and honest result ledger that can detect failures beyond repeating the worked example. Treat reusable skill quality as a question about decisions and evidence, not the number of files or the polish of their titles. Keep the result within the supplied repertoire and intended use rather than claiming universal coverage.

## Inputs to collect
1. **Task material** — collect candidate skill and intended boundaries; risks and known failure modes; execution environment and permitted observations. Default: none; request the material required for the selected decision instead of filling it with an imagined example.
2. **Intended user and context** — establish who will invoke the procedure, which decisions recur, and what they can observe. Default: a private review draft with no publishing or implementation authority implied.
3. **Evidence boundary** — distinguish original material, summaries, observations, and proposals. Default: only the supplied material is available; no unseen source has been inspected.
4. **Acceptance and constraints** — collect the expected artifact, source-use limits, and available testing capacity. Default: propose a bounded check and label it proposed rather than an established external standard.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent portions and name the missing input that blocks the remaining decision.

## Procedure
1. Extract the decisions and output invariants the skill promises, separating required behavior from illustrative choices in its example.
2. Design a fresh ordinary case with different surface details and evidence structure, so copying the worked example cannot satisfy it.
3. ⚠️ Create a boundary case that changes the decisive condition and therefore requires a different response, then state that contrast before any execution.
4. Create an insufficient-input case where a specific conclusion must remain unresolved; identify what independent work can still proceed.
5. Write observable assertions about evidence use, conditional decisions, output completeness, and forbidden unsupported claims; avoid demanding exact wording when equivalent reasoning is acceptable.
6. ⚠️ Prepare an evaluator prompt that cites the actual output for every judgment and records ambiguity rather than silently changing the expected answer.
7. Execute only in an available authorized environment; retain the task, skill version or snapshot, actual output, and evaluation basis when a run occurs.
8. Report each test as planned, executed with evidence, or blocked; revise the skill for demonstrated failures and rerun affected cases without claiming broader reliability than tested.
9. Apply the decision rules to the actual case and fill the output template. Keep the decisive contrast visible so a reviewer can disagree with the reasoning without reconstructing hidden assumptions.
10. Run every quality checklist item. If a check fails, revise the affected claim or mark the dependent work unresolved; do not invent a successful result to complete the template.

Use this reusable reviewer prompt when handing off the artifact: "Read the supplied scope, inputs, procedure, and concrete output. Identify each decision-changing assumption. For every conclusion, quote the relevant supplied evidence or label the conclusion provisional. Describe a changed input that would require a different action. Do not treat an expected result as an observed result, and do not introduce external facts from memory. Return the unsupported claim, the missing evidence, and the smallest correction."

This prompt is an evaluation aid, not evidence that another reviewer has actually run. Record an independent review only when its output exists. For an external requirement, check the current responsible source and record the unresolved dependency when access is unavailable.

## Decision rules
- IF the test repeats the worked example with renamed people THEN replace it with a new decision or evidence arrangement BECAUSE memorized structure can hide a failure to apply the method.
- IF no execution output exists THEN report the test as planned or blocked BECAUSE a test specification is not an observed pass.
- IF the answer differs in wording but satisfies the evidence and decision rules THEN evaluate the substantive assertions BECAUSE verbatim matching can reject correct reasoning.
- IF a reviewer disagrees THEN compare the evidence and decision condition explicitly BECAUSE unexplained consensus or disagreement cannot establish which procedure is useful.
- IF the task requests a live change beyond the review THEN apply the user's authorized scope to that action BECAUSE designing reusable instructions does not itself authorize unrelated execution.

## Output template
```text
Decision: <one sentence selecting the disposition or readiness state>
Scope: <materials examined and intended reuse boundary; at most three sentences>
Evidence: <source labels and the decisive observations, up to six entries>
Artifact: <actual comparison, reusable procedure, or test specification; up to 600 words>
Check: <observable criterion and actual result if available; otherwise planned>
Unresolved: <missing inputs and smallest next action, up to four entries>
```

## Quality checklist
- [ ] The decision names a concrete disposition or readiness state.
- [ ] Scope identifies what was actually examined and what was excluded.
- [ ] Every observation is traceable to supplied material rather than an invented source.
- [ ] The artifact contains a usable procedure, comparison, or test rather than a promise to write one later.
- [ ] At least one changed condition would produce a clearly different action.
- [ ] Changing external requirements remain inputs or precise verification steps.
- [ ] Expected behavior is separate from any observed execution result.
- [ ] Unresolved dependencies have a specific next evidence request.

## Anti-patterns
- **Title counting**: treating another name as proof of another capability. Fix: compare the decision, inputs, and artifact with the nearest procedure.
- **Example worship**: promoting incidental details of one successful case into universal requirements. Fix: test the rule against a changed context and state its boundary.
- **Evidence laundering**: calling a draft, expectation, or plausible inference an observation. Fix: label its actual status and retain the supporting record.
- **Vague acceptance**: asking whether the skill seems useful without a concrete task. Fix: state what the user must be able to decide or produce and how that can be checked.
- **Overclaiming coverage**: claiming all cases or all neighboring skills were reviewed after a sample. Fix: name the actual scope and remaining comparison work.

## Worked example
**Input:**
> Fictional reviewer Tomas evaluates a skill that resolves inconsistent contact records by asking the responsible owner, without assuming the newest document is correct. Its example compares a worksheet with an invoice. Tomas can design tests but has no execution output.

**Output:**
```text
Decision: Prepare distinct tests and mark all results unexecuted until actual outputs are available.
Scope: The supplied fictional case only; external coverage and live performance are not assumed.
Evidence: The facts explicitly supplied in the fictional input; absent source material remains unavailable.
Artifact: Test A: a recent draft website lists one contact, while an owner-signed correction explicitly supersedes it. Expected: use the explicit correction within its stated scope, not recency alone.
Test B: two current internal records disagree and neither has authoritative confirmation. Expected: preserve both and request owner confirmation; do not choose silently.
Test C: only a directory title is supplied without any contact values. Expected: request the missing records and avoid inventing a discrepancy.
Ledger: A planned; B planned; C planned. Actual outputs: none supplied. Overall result: execution pending, no pass rate claimed.
Check: The report distinguishes expected behavior from observed output and contains no invented pass result. This is the proposed acceptance criterion; no separate behavioral execution is claimed.
Unresolved: Obtain the missing comparison or execution evidence identified in the artifact before making a broader readiness claim.
```

**Bad output:**
> The skill is unique, generalized, and fully reliable because its title is new and its example looks correct.

This fails because a title does not establish a procedural difference, a single example does not establish transfer, and no observed execution evidence supports the reliability claim.

## Edge cases
- **Only descriptions are available**: perform provisional routing and request the nearest actual procedures before making a substantive uniqueness or generalization claim.
- **Source cases conflict**: preserve both and identify the contextual condition that might explain the difference; do not average incompatible actions into an unsupported rule.
- **Testing is unavailable**: deliver the test specification and identify execution as pending; a blocked run does not erase the useful planning artifact.
- **The requested scope expands**: reassess inputs and comparison coverage before extending conclusions; prior evidence applies only within its original boundary.

## Test case
**Input:**
> Fictional reviewer Oren has one output from a new boundary case and two tests that have not run. The output makes an unsupported assumption. Prepare an evidence-based ledger that neither counts unrun tests as passes nor generalizes one failure to all possible uses.

**Assertions:**
1. The output uses Decision, Scope, Evidence, Artifact, Check, and Unresolved in that order.
2. It applies the task-specific distinction to the supplied evidence rather than returning only a general checklist.
3. It preserves a missing or conflicting premise instead of silently assuming a favorable result.
4. It distinguishes planned checks from actual execution and does not invent sources, current requirements, or pass results.
