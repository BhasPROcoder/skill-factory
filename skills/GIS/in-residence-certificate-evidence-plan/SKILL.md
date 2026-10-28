---
id: GIS-005
name: in-residence-certificate-evidence-plan
domain: India Citizen Service Preparation
subdomain: Analysis
version: 1.0
description: Prepare residence certificate evidence plan from supplied evidence; use when the request concerns certificate purpose and locality.
triggers: ["residence certificate evidence plan", "prepare residence certificate evidence plan", "review my residence certificate evidence plan", "help me with residence certificate evidence plan", "turn certificate purpose and locality into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: high
---

# Residence certificate evidence plan

## Purpose
Produce residence certificate evidence plan that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Certificate purpose and locality** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Official eligibility wording** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Address history and evidence** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.
5. **Jurisdiction and personal context** — country, state or locality, responsible authority and current case stage are required; there is no silent jurisdiction default.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify the exact certificate and receiving institution because similar labels can describe different requirements.
3. Extract each residence-related criterion from the current responsible-authority instructions.
4. Place address evidence on a timeline without assuming possession of a document proves duration.
5. Map gaps or conflicting addresses to specific verification questions.
6. Prepare an evidence plan that separates administrative completeness from the authority decision on eligibility.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat the country as India but collect the state, locality, responsible office, service category, and case stage separately. Use the responsible agency or state service portal to check the current application route, accepted evidence, fees, appointments, and processing statements. Save the source title and access date in the working notes. A receipt is evidence of submission, not evidence of approval. Do not request full identity numbers in a shared draft; use masked references and let the applicant supply sensitive values directly to the official service.

Before applying a legal, financial, eligibility, or safety interpretation, verify the current rule in the responsible authority's official publication; model knowledge has a cutoff. Use `[VERIFY: the disputed requirement and the responsible official source]` when confirmation is unavailable. Refer a contested right, consequential deadline, or individualized legal conclusion to a licensed professional qualified in the relevant jurisdiction. This workflow prepares information; it does not determine legal entitlement.

## Decision rules
- IF the receiving institution names a different certificate THEN clarify its accepted document before applying BECAUSE a locally issued certificate may not answer the receiving requirement.
- IF address duration is unsupported THEN mark the duration criterion unresolved BECAUSE a current address alone does not establish a historical period.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Criterion | Available evidence | Gap | Verification route
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
- **Task-specific shortcut**: equating a current address proof with every residence-duration requirement. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional applicant Priya needs a residence certificate for a fictional college; a current utility statement is available but historical residence evidence is not.

**Output:**
```text
Scope: Prepare residence certificate evidence plan for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Criterion | Available evidence | Gap | Verification route
Certificate identity | College request summary | Exact title unclear | Ask college for accepted certificate wording
Residence history | Current utility statement | Earlier period unsupported | Check issuing authority evidence rules
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
> Fictional test request: Fictional applicant Asha has several addresses and asks you to declare eligibility from the newest address proof.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
