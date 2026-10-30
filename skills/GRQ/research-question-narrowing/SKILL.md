---
id: GRQ-001
name: research-question-narrowing
domain: Research Question and Study Design
subdomain: Analysis
version: 1.1
description: Prepare research question narrowing from supplied evidence; use when the request concerns broad research interest.
triggers: ["research question narrowing", "prepare research question narrowing", "review my research question narrowing", "help me with research question narrowing", "turn broad research interest into an actionable plan"]
not_for: ["Construct operationalization map [GRQ-002]", "Observational design inference-boundary review [GRQ-003]"]
requires: []
risk_level: medium
---

# Research question narrowing

## Purpose
Produce research question narrowing that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Broad research interest** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Available population or materials** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Feasibility constraints** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Separate the topic from the question to be answered.
3. Specify the unit of analysis and setting.
4. Identify the outcome or phenomenon requiring observation.
5. Choose a comparison or descriptive boundary that makes the question answerable.
6. State what the proposed evidence could and could not establish.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Distinguish a study design proposal from completed research. Define the unit being studied and the comparison needed before naming a method. Record feasibility, consent, privacy and institutional review requirements relevant to the actual setting, using current institutional guidance instead of assumed exemptions. Do not invent recruitment access, instruments, prior findings, sample-size justifications or causal identification. A design can be useful while a required decision remains open; state exactly which conclusion the missing decision prevents. Use only fictional participant details in examples.



## Decision rules
- IF the question contains several independent outcomes THEN split it into primary and secondary questions BECAUSE one unfocused question makes design choices unclear.
- IF required data are inaccessible THEN revise scope before choosing analysis BECAUSE a method cannot compensate for unavailable observations.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Question element | Proposed scope | Evidence needed | Limit
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
- **Task-specific shortcut**: selecting a fashionable method before defining the question. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional researcher Mara wants to study remote learning but can access only one course discussion archive.

**Output:**
```text
Scope: Prepare research question narrowing for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Question element | Proposed scope | Evidence needed | Limit
Population | One course archive | Archived contributions | Cannot represent all students
Phenomenon | Participation patterns | Defined contribution measures | Cannot infer motives alone

Next action: The requester or assigned reviewer will complete this task-specific check: State what the proposed evidence could and could not establish. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Cannot represent all students.
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
> Fictional test request: Fictional researcher Eli wants to prove a broad social claim using a small convenience archive.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
