---
id: SKR-001
name: repertoire-gap-selection
domain: Reusable Skill Engineering
subdomain: Selection
version: 1.0
description: Choose useful additions to a skill repertoire by comparing decisions, required evidence, and deliverables against existing procedures.
triggers: ["repertoire gap selection", "help with repertoire gap selection", "review my repertoire gap selection", "prepare repertoire gap selection", "apply repertoire gap selection to these materials"]
not_for: ["Specialized workflow generalization [SKR-002]", "Skill forward-test design [SKR-003]"]
requires: []
risk_level: low
---

# Repertoire gap selection

## Purpose
Produce a justified add, extend, route, or defer decision for each candidate. Treat reusable skill quality as a question about decisions and evidence, not the number of files or the polish of their titles. Keep the result within the supplied repertoire and intended use rather than claiming universal coverage.

## Inputs to collect
1. **Task material** — collect candidate task requests; existing skill descriptions and representative procedures; intended users and observed unmet needs. Default: none; request the material required for the selected decision instead of filling it with an imagined example.
2. **Intended user and context** — establish who will invoke the procedure, which decisions recur, and what they can observe. Default: a private review draft with no publishing or implementation authority implied.
3. **Evidence boundary** — distinguish original material, summaries, observations, and proposals. Default: only the supplied material is available; no unseen source has been inspected.
4. **Acceptance and constraints** — collect the expected artifact, source-use limits, and available testing capacity. Default: propose a bounded check and label it proposed rather than an established external standard.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent portions and name the missing input that blocks the remaining decision.

## Procedure
1. Express the candidate as a user situation, required decision, necessary inputs, and inspectable output; remove topic labels that do not change the work.
2. Find the nearest existing procedures using both task vocabulary and output vocabulary; record the actual candidates examined rather than claiming an exhaustive search.
3. ⚠️ Compare each nearby skill on decision rules, evidence prerequisites, failure handling, and deliverable structure; different names or industries alone do not establish a gap.
4. Describe the smallest case where the candidate requires a different action from its nearest neighbor; if no such case can be stated, propose routing or extension.
5. Check whether the added decision recurs in the supplied user needs or follows from a concrete workflow requirement; label predicted usefulness as a hypothesis when no usage evidence exists.
6. ⚠️ Choose add only when the distinct procedure is coherent enough to use independently; choose extend when a bounded branch fits the existing purpose without confusing selection.
7. Write a proposed trigger and an adjacent-task exclusion that would let another reader select the correct procedure in the contrast case.
8. Prepare a bounded validation task for the proposed addition and state the result that would cause you to merge, narrow, or abandon it.
9. Apply the decision rules to the actual case and fill the output template. Keep the decisive contrast visible so a reviewer can disagree with the reasoning without reconstructing hidden assumptions.
10. Run every quality checklist item. If a check fails, revise the affected claim or mark the dependent work unresolved; do not invent a successful result to complete the template.

Use this reusable reviewer prompt when handing off the artifact: "Read the supplied scope, inputs, procedure, and concrete output. Identify each decision-changing assumption. For every conclusion, quote the relevant supplied evidence or label the conclusion provisional. Describe a changed input that would require a different action. Do not treat an expected result as an observed result, and do not introduce external facts from memory. Return the unsupported claim, the missing evidence, and the smallest correction."

This prompt is an evaluation aid, not evidence that another reviewer has actually run. Record an independent review only when its output exists. For an external requirement, check the current responsible source and record the unresolved dependency when access is unavailable.

## Decision rules
- IF the candidate differs only in wording THEN route to the existing procedure BECAUSE synonyms do not add a new decision capability.
- IF the different context changes a prerequisite or failure branch THEN compare that branch explicitly before deciding whether to extend or split BECAUSE context matters when it changes action.
- IF the nearest existing skill has not been inspected THEN keep the uniqueness conclusion provisional BECAUSE catalog labels can conceal shared procedures.
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
> Fictional library owner Mira has a skill for repairing survey wording and a proposed skill named questionnaire wording cleanup. Both identify double questions and repair response options. Another proposal observes how respondents interpret questions before changing them; no existing procedure for collecting that evidence has been found in the supplied catalog.

**Output:**
```text
Decision: Route the synonym proposal to the existing skill; investigate the evidence-collection procedure as a distinct addition.
Scope: The supplied fictional case only; external coverage and live performance are not assumed.
Evidence: The facts explicitly supplied in the fictional input; absent source material remains unavailable.
Artifact: Candidate: questionnaire wording cleanup. Disposition: route to survey wording repair. Difference test: none supplied; both change the same wording from the same inputs.
Candidate: questionnaire cognitive pretest. Disposition: provisionally add. Distinct input: respondent explanations of comprehension, recall, judgment, and answer selection. Distinct decision: determine where interpretation fails before choosing a revision.
Trigger: find out how respondents interpret this draft questionnaire. Exclusion: direct wording edits without respondent evidence use the existing repair skill.
Revisit: inspect other research procedures before declaring the addition unique.
Check: The comparison names a decision-changing contrast, not merely a different title. This is the proposed acceptance criterion; no separate behavioral execution is claimed.
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
> Fictional curator Noel proposes a new skill called contract summary cleanup, but its supplied steps match an existing contract summary review. A second candidate reconciles conflicting clause versions before summary. Classify the candidates from the supplied procedures without claiming legal correctness.

**Assertions:**
1. The output uses Decision, Scope, Evidence, Artifact, Check, and Unresolved in that order.
2. It applies the task-specific distinction to the supplied evidence rather than returning only a general checklist.
3. It preserves a missing or conflicting premise instead of silently assuming a favorable result.
4. It distinguishes planned checks from actual execution and does not invent sources, current requirements, or pass results.
