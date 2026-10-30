---
id: GIS-007
name: in-information-request-scope-draft
domain: India Citizen Service Preparation
subdomain: Analysis
version: 1.1
description: Prepare public information request scope draft from supplied evidence; use when the request concerns records sought.
triggers: ["public information request scope draft", "prepare public information request scope draft", "review my public information request scope draft", "help me with public information request scope draft", "turn records sought into an actionable plan"]
not_for: ["Service application status follow-up [GIS-008]", "Government appointment preparation [GIS-009]"]
requires: []
risk_level: high
---

# Public information request scope draft

## Purpose
Produce public information request scope draft that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Records sought** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Suspected record-holding authority** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Current official request instructions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.
5. **Jurisdiction and personal context** — country, state or locality, responsible authority and current case stage are required; there is no silent jurisdiction default.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Convert broad questions into descriptions of existing records or recorded information.
3. Define the subject, date range and office context narrowly enough for a record search.
4. Separate a request for records from a demand that an official create an explanation.
5. Check the current official route, applicant requirements and handling provisions without inventing legal deadlines.
6. Draft a neutral request with alternatives for clarifying ambiguous record names.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat the country as India but collect the state, locality, responsible office, service category, and case stage separately. Use the responsible agency or state service portal to check the current application route, accepted evidence, fees, appointments, and processing statements. Save the source title and access date in the working notes. A receipt is evidence of submission, not evidence of approval. Do not request full identity numbers in a shared draft; use masked references and let the applicant supply sensitive values directly to the official service.

Before applying a legal, financial, eligibility, or safety interpretation, verify the current rule in the responsible authority's official publication; model knowledge has a cutoff. Use `[VERIFY: the disputed requirement and the responsible official source]` when confirmation is unavailable. Refer a contested right, consequential deadline, or individualized legal conclusion to a licensed professional qualified in the relevant jurisdiction. This workflow prepares information; it does not determine legal entitlement.

## Decision rules
- IF the user asks why an official acted THEN request the relevant recorded reasons or decision record BECAUSE the office may not hold a newly composed explanation.
- IF the record holder is uncertain THEN prepare a routing query instead of asserting jurisdiction BECAUSE possession of the records must be established.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Record sought | Scope boundary | Likely holder status | Verification
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
- **Task-specific shortcut**: claiming a universal response deadline without current official verification. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional requester Farah wants records showing how a local facility maintenance decision was made; she does not know the committee name. The request concerns the fictional Maple facility during its autumn maintenance review; the precise dates still need confirmation.

**Output:**
```text
Scope: Prepare public information request scope draft for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Record sought | Scope boundary | Likely holder status | Verification
Decision record | Named facility and review period | Dates and office unconfirmed | Confirm dates and record holder
Recorded reasons | Existing notes only | Record title unknown | Use descriptive wording

Artifact: Proposed record description: Existing meeting records, decision notes, and recorded reasons concerning the autumn maintenance review of the fictional Maple facility. Before sending, replace the seasonal description with confirmed start and end dates and identify the record-holding office. This requests existing recorded material, without asserting that a particular committee or document exists.
Next action: The requester or assigned reviewer will complete this task-specific check: Draft a neutral request with alternatives for clarifying ambiguous record names. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Confirm dates and record holder.
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
> Fictional test request: Fictional requester Harish asks for every record ever produced by a department and demands a guaranteed response date.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
