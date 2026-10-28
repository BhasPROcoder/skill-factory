---
id: GUS-007
name: us-benefit-renewal-notice-triage
domain: US Citizen Service Preparation
subdomain: Analysis
version: 1.0
description: Prepare benefit renewal notice triage from supplied evidence; use when the request concerns full renewal notice.
triggers: ["benefit renewal notice triage", "prepare benefit renewal notice triage", "review my benefit renewal notice triage", "help me with benefit renewal notice triage", "turn full renewal notice into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: high
---

# Benefit renewal notice triage

## Purpose
Produce benefit renewal notice triage that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Full renewal notice** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Agency and jurisdiction** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Applicant response history** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.
5. **Jurisdiction and personal context** — country, state or locality, responsible authority and current case stage are required; there is no silent jurisdiction default.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Separate notice facts from the applicant interpretation and transcribe action language accurately.
3. Identify the exact program and issuing office before comparing instructions.
4. Extract requested evidence, stated dates and allowed response channels from the supplied notice.
5. Check whether prior submissions correspond to the same renewal request.
6. Prepare an action tracker that flags disputed or unclear instructions for qualified assistance.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Collect the state, county or city, responsible agency, exact service, and stage of the case. Federal, state, and local labels are routing clues, not a substitute for confirming the responsible office. Check the current value of fees, form editions, accepted identity evidence, appointment rules and processing guidance on the responsible agency site. Record what was verified and what remains unknown. Mask personal identifiers in working documents, retain original source records, and have the applicant review every declaration before any authorized submission.

Before applying a legal, financial, eligibility, or safety interpretation, verify the current rule in the responsible authority's official publication; model knowledge has a cutoff. Use `[VERIFY: the disputed requirement and the responsible official source]` when confirmation is unavailable. Refer a contested right, consequential deadline, or individualized legal conclusion to a licensed professional qualified in the relevant jurisdiction. This workflow prepares information; it does not determine legal entitlement.

## Decision rules
- IF the notice states a consequential date THEN preserve it exactly and verify promptly with the issuer BECAUSE a generic timeline could cause harmful delay.
- IF the applicant disputes the underlying decision THEN refer the dispute to an appropriate licensed professional or qualified adviser BECAUSE document organization is not a rights determination.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Notice item | Exact source | Applicant status | Next action
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
- **Task-specific shortcut**: assuming any earlier upload satisfies a new renewal request. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional applicant Jordan has a renewal notice asking for an income document; a prior upload relates to a different notice.

**Output:**
```text
Scope: Prepare benefit renewal notice triage for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Notice item | Exact source | Applicant status | Next action
Requested document | Current notice excerpt | Not matched to current case | Confirm required response
Prior upload | Different reference | May not satisfy renewal | Ask agency to reconcile references
Next action: The requester supplies the unresolved evidence and confirms the proposed next step before implementation.
Unresolved: Which missing source or observation would change the provisional conclusion?
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
> Fictional test request: Fictional applicant Casey has a partial notice image that omits the response date and asks you to declare no action is needed.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
