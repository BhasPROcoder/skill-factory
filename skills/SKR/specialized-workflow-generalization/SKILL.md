---
id: SKR-002
name: specialized-workflow-generalization
domain: Reusable Skill Engineering
subdomain: Generalization
version: 1.0
description: Turn an authorized specialized workflow into reusable instructions by preserving decision invariants and moving changing or case-specific facts into inputs and verification steps.
triggers: ["specialized workflow generalization", "help with specialized workflow generalization", "review my specialized workflow generalization", "prepare specialized workflow generalization", "apply specialized workflow generalization to these materials"]
not_for: ["Repertoire gap selection [SKR-001]", "Skill forward-test design [SKR-003]"]
requires: []
risk_level: low
---

# Specialized workflow generalization

## Purpose
Produce a portable procedure with explicit inputs, decision branches, and an example that does not mistake one case for a universal rule. Treat reusable skill quality as a question about decisions and evidence, not the number of files or the polish of their titles. Keep the result within the supplied repertoire and intended use rather than claiming universal coverage.

## Inputs to collect
1. **Task material** — collect authorized source workflow; representative cases and failure examples; intended reuse scope and source-use constraints. Default: none; request the material required for the selected decision instead of filling it with an imagined example.
2. **Intended user and context** — establish who will invoke the procedure, which decisions recur, and what they can observe. Default: a private review draft with no publishing or implementation authority implied.
3. **Evidence boundary** — distinguish original material, summaries, observations, and proposals. Default: only the supplied material is available; no unseen source has been inspected.
4. **Acceptance and constraints** — collect the expected artifact, source-use limits, and available testing capacity. Default: propose a bounded check and label it proposed rather than an established external standard.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent portions and name the missing input that blocks the remaining decision.

## Procedure
1. Confirm what material may be used and what may be retained in the resulting artifact; omit identifying or restricted details that are unnecessary for the reusable method.
2. Annotate each source step as a decision, evidence requirement, action, local convention, or incidental case fact; keep the original distinctions visible during extraction.
3. ⚠️ For each decision, state the condition that selects an action and the reason the action follows; avoid replacing judgment with an unexplained instruction to be careful.
4. Identify variables that change across intended uses, including jurisdiction, platform, recipient, version, deadline, and available authority; collect them as inputs with safe defaults or explicit questions.
5. Move any changing requirement into a verification instruction naming the responsible official source; do not copy a remembered value into the reusable rule.
6. ⚠️ Test the proposed invariant against a case with a different context and a case with missing evidence; narrow its scope when the same action no longer follows.
7. Draft a concrete output template and a clearly fictional worked artifact; label newly invented scenario details as fiction instead of attributing them to the source.
8. Review the abstraction for lost dependencies, unearned universal claims, and accidental copying of case-specific wording; retain source-use notes separately when needed.
9. Apply the decision rules to the actual case and fill the output template. Keep the decisive contrast visible so a reviewer can disagree with the reasoning without reconstructing hidden assumptions.
10. Run every quality checklist item. If a check fails, revise the affected claim or mark the dependent work unresolved; do not invent a successful result to complete the template.

Use this reusable reviewer prompt when handing off the artifact: "Read the supplied scope, inputs, procedure, and concrete output. Identify each decision-changing assumption. For every conclusion, quote the relevant supplied evidence or label the conclusion provisional. Describe a changed input that would require a different action. Do not treat an expected result as an observed result, and do not introduce external facts from memory. Return the unsupported claim, the missing evidence, and the smallest correction."

This prompt is an evaluation aid, not evidence that another reviewer has actually run. Record an independent review only when its output exists. For an external requirement, check the current responsible source and record the unresolved dependency when access is unavailable.

## Decision rules
- IF a source uses a local deadline or fee THEN replace the value with a current-source verification step BECAUSE a reusable procedure must not freeze changing requirements.
- IF a rule fails when the recipient changes THEN make the recipient condition explicit or narrow the skill BECAUSE one successful case does not establish a universal method.
- IF the source material cannot be reused as supplied THEN extract only an authorized general method or request suitable material BECAUSE access alone does not establish permission to reproduce content.
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
> Fictional coordinator Inez has an authorized internal checklist for a permit application. It tells staff to copy a previously used fee, attach a site sketch, and record submission confirmation. The intended reusable workflow spans different authorities, whose current fee and attachment requirements have not been supplied.

**Output:**
```text
Decision: Generalize evidence mapping and confirmation handling; keep authority-specific fees and attachments conditional.
Scope: The supplied fictional case only; external coverage and live performance are not assumed.
Evidence: The facts explicitly supplied in the fictional input; absent source material remains unavailable.
Artifact: Inputs: responsible authority, application type, current official instructions, supplied supporting documents, and submission evidence. No jurisdiction default.
Invariant: map each confirmed requirement to evidence before calling the pack ready.
Verification branch: [VERIFY: current fee and attachment requirements in the responsible authority's official application instructions].
Preparation rule: include a site sketch only when the verified instructions require it or the user has an appropriate separate reason to supply it.
Completion rule: distinguish prepared materials from submitted materials; record the actual confirmation if submission occurs.
Draft output fields: requirement; official basis; supplied evidence; unresolved gap; next action. No fee amount is carried forward.
Check: The draft contains no copied current fee or universal attachment requirement and distinguishes preparation from submission. This is the proposed acceptance criterion; no separate behavioral execution is claimed.
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
> Fictional operator Sana supplies a workflow that always emails a named manager for approval. Generalize it for teams with different approval owners, preserving the need for actual authority without inventing a role assignment.

**Assertions:**
1. The output uses Decision, Scope, Evidence, Artifact, Check, and Unresolved in that order.
2. It applies the task-specific distinction to the supplied evidence rather than returning only a general checklist.
3. It preserves a missing or conflicting premise instead of silently assuming a favorable result.
4. It distinguishes planned checks from actual execution and does not invent sources, current requirements, or pass results.
