---
id: GAD-005
name: application-rejection-error-triage
domain: Administrative Casework
subdomain: Analysis
version: 1.1
description: Prepare application rejection error triage from supplied evidence; use when the request concerns rejection message.
triggers: ["application rejection error triage", "prepare application rejection error triage", "review my application rejection error triage", "help me with application rejection error triage", "turn rejection message into an actionable plan"]
not_for: ["Administrative case timeline [GAD-006]", "Administrative status tracker [GAD-007]"]
requires: []
risk_level: medium
---

# Application rejection error triage

## Purpose
Produce application rejection error triage that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Rejection message** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Submitted form snapshot** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Official validation guidance** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Preserve the exact rejection text and identify whether it concerns format, evidence or substantive review.
3. Compare the submitted value with the stated field requirement.
4. Separate a technical upload failure from an agency decision.
5. Change only the identified error after the applicant verifies the intended value.
6. Prepare a retry checklist that records the new acknowledgment without claiming approval.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Build a case file that can be checked by someone who did not take part in the original exchange. Preserve received wording, distinguish official instructions from applicant notes, and keep references consistent across attachments. Check the current official route whenever the task depends on a portal, form, fee, office contact, or service rule. Never turn a tracking label into a promise of approval. The output is an administrative working document; the requester remains responsible for reviewing declarations and authorizing any external submission.



## Decision rules
- IF error text is generic THEN ask for the affected field or official support clarification BECAUSE random edits can introduce new inaccuracies.
- IF the message is a substantive denial THEN stop treating it as a formatting retry BECAUSE the response route may differ.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Error | Observed input | Diagnosis status | Safe next step
<one row per finding; each cell one concise sentence>

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
- **Task-specific shortcut**: changing factual declarations until a portal accepts them. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional applicant Sana receives an unreadable-file error after uploading a blurred scan; no substantive decision is shown.

**Output:**
```text
Scope: Prepare application rejection error triage for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Error | Observed input | Diagnosis status | Safe next step
Upload error | Blurred scan | Likely file-quality issue | Prepare a readable copy
Decision status | No decision shown | Unknown | Check acknowledgment after retry

Next action: The requester or assigned reviewer will complete this task-specific check: Prepare a retry checklist that records the new acknowledgment without claiming approval. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Prepare a readable copy.
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
> Fictional test request: Fictional applicant Leo gets a generic error and asks you to alter answers randomly until submission succeeds.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
