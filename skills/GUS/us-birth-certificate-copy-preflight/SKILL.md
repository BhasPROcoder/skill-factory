---
id: GUS-001
name: us-birth-certificate-copy-preflight
domain: US Citizen Service Preparation
subdomain: Analysis
version: 1.0
description: Prepare birth certificate copy preflight from supplied evidence; use when the request concerns event jurisdiction.
triggers: ["birth certificate copy preflight", "prepare birth certificate copy preflight", "review my birth certificate copy preflight", "help me with birth certificate copy preflight", "turn event jurisdiction into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: high
---

# Birth certificate copy preflight

## Purpose
Produce birth certificate copy preflight that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Event jurisdiction** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Official records-office instructions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Requester relationship and evidence** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.
5. **Jurisdiction and personal context** — country, state or locality, responsible authority and current case stage are required; there is no silent jurisdiction default.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify the jurisdiction that holds the event record rather than the requester current address.
3. Distinguish a certified copy request from amendment or delayed registration.
4. Map the official requester-category requirements to the supplied relationship evidence.
5. Check record identifiers against existing documentation without inventing unknown details.
6. Prepare a submission inventory with fees and delivery options reserved for current official verification.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Collect the state, county or city, responsible agency, exact service, and stage of the case. Federal, state, and local labels are routing clues, not a substitute for confirming the responsible office. Check the current value of fees, form editions, accepted identity evidence, appointment rules and processing guidance on the responsible agency site. Record what was verified and what remains unknown. Mask personal identifiers in working documents, retain original source records, and have the applicant review every declaration before any authorized submission.

Before applying a legal, financial, eligibility, or safety interpretation, verify the current rule in the responsible authority's official publication; model knowledge has a cutoff. Use `[VERIFY: the disputed requirement and the responsible official source]` when confirmation is unavailable. Refer a contested right, consequential deadline, or individualized legal conclusion to a licensed professional qualified in the relevant jurisdiction. This workflow prepares information; it does not determine legal entitlement.

## Decision rules
- IF the requester category is unclear THEN ask the records office which evidence applies BECAUSE access requirements can depend on the request context.
- IF an error in the entry is reported THEN separate amendment from copy ordering BECAUSE ordering another copy does not correct the underlying entry.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Request component | Provided evidence | Open issue | Next check
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
- **Task-specific shortcut**: assuming residence in a state makes every record held there available. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional requester Elise seeks a copy of a relative birth record from a named state but has not supplied the permitted-requester instructions.

**Output:**
```text
Scope: Prepare birth certificate copy preflight for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Request component | Provided evidence | Open issue | Next check
Record location | State supplied | Office unverified | Confirm official records custodian
Requester category | Relative stated | Evidence requirements unknown | Check current requester rules
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
> Fictional test request: Fictional requester Jonah wants a certified copy but gives only a current address and no event jurisdiction.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
