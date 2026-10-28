---
id: GRQ-007
name: research-pilot-protocol
domain: Research Question and Study Design
subdomain: Analysis
version: 1.0
description: Prepare research pilot protocol from supplied evidence; use when the request concerns proposed study procedure.
triggers: ["research pilot protocol", "prepare research pilot protocol", "review my research pilot protocol", "help me with research pilot protocol", "turn proposed study procedure into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: medium
---

# Research pilot protocol

## Purpose
Produce research pilot protocol that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Proposed study procedure** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Known uncertainties** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Pilot resources** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. List process uncertainties that a pilot can actually resolve.
3. Choose observations that reveal recruitment, comprehension or measurement problems.
4. Define what would trigger a protocol revision.
5. Run through the proposed participant journey using permitted test materials.
6. Document changes and unresolved issues without treating pilot results as definitive findings.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Distinguish a study design proposal from completed research. Define the unit being studied and the comparison needed before naming a method. Record feasibility, consent, privacy and institutional review requirements relevant to the actual setting, using current institutional guidance instead of assumed exemptions. Do not invent recruitment access, instruments, prior findings, sample-size justifications or causal identification. A design can be useful while a required decision remains open; state exactly which conclusion the missing decision prevents. Use only fictional participant details in examples.



## Decision rules
- IF pilot participants differ from target participants THEN limit conclusions about usability BECAUSE the actual group may encounter different barriers.
- IF the pilot changes the measure THEN record the version change BECAUSE later data need a clear instrument history.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Pilot question | Observation | Revision trigger | Record
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
- **Task-specific shortcut**: treating a successful dry run as proof of study validity. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional team Wrenfield pilots a questionnaire to check whether respondents interpret the reference period consistently.

**Output:**
```text
Scope: Prepare research pilot protocol for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Pilot question | Observation | Revision trigger | Record
Period comprehension | Participant paraphrase | Different periods inferred | Revise wording
Completion flow | Skipped routing question | Incorrect path followed | Repair instructions
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
> Fictional test request: Fictional researcher Mae wants a pilot that only confirms the materials look professional.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
