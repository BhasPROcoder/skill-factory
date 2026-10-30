---
id: GRQ-006
name: survey-question-wording-review
domain: Research Question and Study Design
subdomain: Analysis
version: 1.1
description: Prepare questionnaire cognitive pretest from supplied evidence; use when the request concerns draft item and answer choices.
triggers: ["questionnaire cognitive pretest", "prepare questionnaire cognitive pretest", "review my questionnaire cognitive pretest", "help me with questionnaire cognitive pretest", "turn draft item and answer choices into an actionable plan"]
not_for: ["Research pilot protocol [GRQ-007]", "Research protocol decision log [GRQ-008]"]
requires: []
risk_level: medium
---

# Questionnaire cognitive pretest

## Purpose
Produce questionnaire cognitive pretest that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Draft item and answer choices** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Intended interpretation** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Consented pretest participants** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Ask the participant to answer the item without teaching its intended meaning.
3. Invite a paraphrase to identify how the wording was understood.
4. Probe what event or information the participant retrieved to answer.
5. Ask how the participant formed the judgment and mapped it to an answer option.
6. Separate observed response-process problems from proposed wording changes and retest the revision.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Distinguish a study design proposal from completed research. Define the unit being studied and the comparison needed before naming a method. Record feasibility, consent, privacy and institutional review requirements relevant to the actual setting, using current institutional guidance instead of assumed exemptions. Do not invent recruitment access, instruments, prior findings, sample-size justifications or causal identification. A design can be useful while a required decision remains open; state exactly which conclusion the missing decision prevents. Use only fictional participant details in examples.



## Decision rules
- IF the participant selects the expected answer for a different reason THEN record the mismatch BECAUSE answer agreement does not prove comprehension.
- IF a probe teaches the intended meaning THEN label subsequent responses as influenced BECAUSE coached interpretation cannot validate the original item.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Response stage | Probe | Observed evidence | Revision test
<one row per finding; each cell one concise sentence>

Artifact: <the actual draft, prompts, sequence, or other requested deliverable; mark proposals>
Next action: <one concrete action, its owner or role, and the evidence needed>
Unresolved: <up to three verification questions, or None>
```
Use at most 12 rows in the first response. If more are necessary, prioritize blockers and provide the remaining rows as a clearly labeled continuation when requested. Do not bury an unresolved prerequisite in a footnote or represent a draft as an approved result.

## Quality checklist
- [ ] The scope states the actual requested task and excludes unrelated decisions.
- [ ] Every table row is traceable to a supplied input or labeled assumption.
- [ ] The two task-specific conditional branches have been considered.
- [ ] Conflicting evidence remains visible rather than being averaged away.
- [ ] Unknown values remain unknown or have a named verification source.
- [ ] The next action has an identifiable owner or role and observable completion evidence.
- [ ] The example and final output use the same column order and field labels.
- [ ] Any arithmetic has been independently recomputed from the stated inputs.

## Anti-patterns
- **Unsupported certainty**: treating a plausible interpretation as an observed fact. Fix: attach the supporting input or mark the statement provisional.
- **Task-specific shortcut**: reporting a predicted wording problem as an observed participant difficulty. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional researcher tests an item asking whether a service was fast and helpful. No participant has answered yet; this is a pretest protocol, not a findings report.

**Output:**
```text
Scope: Prepare questionnaire cognitive pretest for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Response stage | Probe | Observed evidence | Revision test
Comprehension | What does this question ask in your own words? | Not collected | Check whether speed and helpfulness conflict
Answer mapping | How did you choose that option? | Not collected | Check whether available choices express the judgment

Artifact: Pretest script: Please answer the item as you normally would. What is it asking, in your own words? What occasion did you think of? How did you decide on your answer? How did you select an option? If speed and helpfulness led to different judgments, record that response-process evidence before proposing separate items. No participant findings have yet been collected.
Next action: The requester or assigned reviewer will complete this task-specific check: Separate observed response-process problems from proposed wording changes and retest the revision. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Check whether speed and helpfulness conflict.
```

**Bad output:**
> Everything is ready; proceed without further checks.

This fails because it suppresses the task-specific distinction visible in the table, invents completion, and provides no way to verify the remaining uncertainty.

## Edge cases
- **Only a summary is available**: label findings as based on that summary and request the original excerpt needed for the disputed point.
- **User cannot obtain a missing input**: identify a smaller output that can be completed without it and state the resulting limitation.
- **Two readers need different levels of detail**: preserve a single factual basis and give each reader the subset needed for their decision.
- **The situation changes during the task**: record which input changed, revisit the affected rows, and retain unaffected findings without pretending the entire analysis is new.

## Test case
**Input:**
> Fictional test request: Fictional researcher wants to call an item validated because a participant selected the expected option, without asking how the answer was produced.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
