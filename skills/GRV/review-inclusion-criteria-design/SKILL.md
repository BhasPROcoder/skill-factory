---
id: GRV-002
name: review-inclusion-criteria-design
domain: Evidence Review and Synthesis
subdomain: Analysis
version: 1.1
description: Prepare review inclusion criteria from supplied evidence; use when the request concerns review question.
triggers: ["review inclusion criteria", "prepare review inclusion criteria", "review my review inclusion criteria", "help me with review inclusion criteria", "turn review question into an actionable plan"]
not_for: ["Abstract screening decision log [GRV-003]", "Study evidence extraction sheet [GRV-004]"]
requires: []
risk_level: medium
---

# Review inclusion criteria

## Purpose
Produce review inclusion criteria that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Review question** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Candidate study types** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Scope constraints** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Define eligible populations or materials.
3. Specify the phenomenon, intervention or exposure relevant to the question.
4. Define eligible outcomes and evidence types.
5. Separate substantive criteria from convenience limits.
6. Test criteria on borderline examples before screening.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use a reproducible account of what was searched, included and excluded. A source reference must identify a real source that was supplied or actually retrieved; never fabricate authors, titles, dates, quotations or links. Distinguish an author claim from the evidence supporting it. Compare studies only after checking their populations, interventions or phenomena, outcomes, and methods. If evidence is incomplete, describe the bounded search and remaining uncertainty rather than claiming exhaustiveness. Preserve contradictory findings and avoid turning a count of positive studies into an unsupported estimate of effect.



## Decision rules
- IF a criterion is changed after seeing a favored result THEN record the change and reason BECAUSE selection rules should not hide outcome-driven choices.
- IF an abstract lacks needed information THEN mark uncertain for fuller review BECAUSE missing detail is not automatic ineligibility.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Criterion | Operational rule | Borderline case | Resolution
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
- **Task-specific shortcut**: excluding studies because their conclusions are inconvenient. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional reviewer Sam includes studies of service users but encounters a report about staff perceptions only. A separate abstract has unclear outcome coverage and needs full-text review.

**Output:**
```text
Scope: Prepare review inclusion criteria for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Criterion | Operational rule | Borderline case | Resolution
Population | Users required | Staff-only report | Exclude unless question is revised
Outcome | User access experience | Abstract unclear | Seek full text

Next action: The requester or assigned reviewer will complete this task-specific check: Test criteria on borderline examples before screening. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Exclude unless question is revised.
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
> Fictional test request: Fictional reviewer Nola wants to include only studies supporting the proposed intervention.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
