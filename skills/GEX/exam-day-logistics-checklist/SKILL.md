---
id: GEX-010
name: exam-day-logistics-checklist
domain: Exam Preparation Methods
subdomain: Analysis
version: 1.1
description: Prepare exam-day logistics checklist from supplied evidence; use when the request concerns official candidate instructions.
triggers: ["exam-day logistics checklist", "prepare exam-day logistics checklist", "review my exam-day logistics checklist", "help me with exam-day logistics checklist", "turn official candidate instructions into an actionable plan"]
not_for: ["Exam syllabus coverage map [GEX-001]", "Mastery-dependent study sequence [GEX-002]"]
requires: []
risk_level: low
---

# Exam-day logistics checklist

## Purpose
Produce exam-day logistics checklist that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Official candidate instructions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Travel or access plan** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Permitted materials** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Extract arrival, identification and permitted-material requirements from current official instructions.
3. Separate confirmed facts from assumptions about the venue or platform.
4. Prepare materials without including prohibited or unverified items.
5. Create a contingency contact plan using official support information.
6. Have the candidate check the final list against the latest notice.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the official current syllabus, format and permitted materials as inputs rather than reproducing them from memory. Separate learning a topic from performing it under exam conditions. Track errors by cause and revisit whether practice is actually changing performance. Treat practice scores as evidence from particular tasks, not guaranteed predictions of a future result. Protect time for sleep and ordinary breaks without prescribing medical guidance. If the requested plan exceeds available capacity, show the tradeoff explicitly rather than promising that every topic can receive full treatment.



## Decision rules
- IF instructions changed after an earlier notice THEN compare the current notice and confirm conflicts BECAUSE an old checklist may no longer apply.
- IF a required item is unavailable THEN contact the official support route BECAUSE invented substitutes may not be accepted.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Logistics item | Official basis | Readiness | Action
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
- **Task-specific shortcut**: treating advice from another candidate as authoritative instructions. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional candidate Edda has a venue notice but relies on a friend description of accepted identification.

**Output:**
```text
Scope: Prepare exam-day logistics checklist for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Logistics item | Official basis | Readiness | Action
Identification | Friend description only | Unverified | Check official candidate instructions
Venue | Official notice supplied | Address available | Confirm travel plan

Artifact: Identification: unresolved; a friend's account is not the official requirement. [VERIFY: accepted identification and any exception process in the current official candidate instructions].
Venue: use the supplied official notice; compare with any later official update.
Travel or access: prepare from the confirmed venue or platform instructions.
Materials: pack only items confirmed permitted by the official instructions.
Blocked item: contact the official support route for clarification; do not promise that an unlisted substitute will be accepted.
Next action: The requester or assigned reviewer will complete this task-specific check: Have the candidate check the final list against the latest notice. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Check official candidate instructions.
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
> Fictional test request: Fictional candidate Kai asks you to guarantee entry using an identification substitute not mentioned in the official notice.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
