---
id: GUS-005
name: us-local-permit-intake-checklist
domain: US Citizen Service Preparation
subdomain: Analysis
version: 1.0
description: Prepare local permit intake checklist from supplied evidence; use when the request concerns proposed project description.
triggers: ["local permit intake checklist", "prepare local permit intake checklist", "review my local permit intake checklist", "help me with local permit intake checklist", "turn proposed project description into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: high
---

# Local permit intake checklist

## Purpose
Produce local permit intake checklist that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Proposed project description** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **City or county jurisdiction** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Official permit intake instructions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.
5. **Jurisdiction and personal context** — country, state or locality, responsible authority and current case stage are required; there is no silent jurisdiction default.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Describe the physical work and location without deciding that a permit is or is not legally required.
3. Identify the local authority responsible for the project category.
4. Map required plans, owner information and supporting documents from current intake instructions.
5. Separate intake completeness from technical review and approval.
6. Prepare focused questions for ambiguous scope or multiple reviewing offices.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Collect the state, county or city, responsible agency, exact service, and stage of the case. Federal, state, and local labels are routing clues, not a substitute for confirming the responsible office. Check the current value of fees, form editions, accepted identity evidence, appointment rules and processing guidance on the responsible agency site. Record what was verified and what remains unknown. Mask personal identifiers in working documents, retain original source records, and have the applicant review every declaration before any authorized submission.

Before applying a legal, financial, eligibility, or safety interpretation, verify the current rule in the responsible authority's official publication; model knowledge has a cutoff. Use `[VERIFY: the disputed requirement and the responsible official source]` when confirmation is unavailable. Refer a contested right, consequential deadline, or individualized legal conclusion to a licensed professional qualified in the relevant jurisdiction. This workflow prepares information; it does not determine legal entitlement.

## Decision rules
- IF project scope changes THEN recheck the permit category and evidence list BECAUSE the earlier checklist may no longer cover the work.
- IF multiple offices appear involved THEN map each responsibility and dependency BECAUSE one intake acknowledgment does not cover all reviews.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Project element | Supplied detail | Intake uncertainty | Authority question
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
- **Task-specific shortcut**: calling an application complete merely because a fee was paid. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional owner Sage proposes an interior alteration but has not supplied dimensions or the local permit category.

**Output:**
```text
Scope: Prepare local permit intake checklist for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Project element | Supplied detail | Intake uncertainty | Authority question
Work scope | Interior alteration | Category unverified | Which intake route covers this scope?
Supporting plans | Not supplied | Requirements unknown | What current plans are required?
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
> Fictional test request: Fictional owner Taylor asks you to confirm no permit is needed from a vague project description.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
