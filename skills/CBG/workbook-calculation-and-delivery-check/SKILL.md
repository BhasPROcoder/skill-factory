---
id: CBG-004
name: workbook-calculation-and-delivery-check
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare workbook creation editing and verification from supplied evidence; use when the request concerns workbook purpose and supplied file.
triggers: ["workbook creation editing and verification", "prepare workbook creation editing and verification", "review my workbook creation editing and verification", "help me with workbook creation editing and verification", "turn workbook purpose and supplied file into an actionable plan"]
not_for: ["Structured document creation and editing [CBG-005]", "Presentation creation editing and delivery [CBG-006]"]
requires: []
risk_level: medium
---

# Workbook creation editing and verification

## Purpose
Produce workbook creation editing and verification that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Workbook purpose and supplied file** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Input and formula specification** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Target spreadsheet application** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Define sheets, input cells, formulas, units and outputs from the requested model; inspect the existing workbook before editing.
3. Create or edit the workbook with an available compatible spreadsheet tool, separating inputs from formulas and preserving required features.
4. Populate formulas and labels, then trace representative references and test normal and boundary cases against independent calculations.
5. Recalculate in the intended application and distinguish cached display values from verified results.
6. Save the requested file, reopen it, inspect displayed errors and layout, and deliver its path with any unexecuted checks.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF a formula exists but has not recalculated THEN mark the displayed result unverified BECAUSE formula text alone does not prove the shown value.
- IF the workbook contains macros THEN preserve them only through a compatible authorized workflow BECAUSE format conversion can silently change behavior.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Check | Fixture | Expected evidence | Status
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
- **Task-specific shortcut**: saying formulas work because their cells contain an equals sign. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional analyst Inez has a workbook whose quantity is 3 and unit cost is 4, with a total formula. The file has not been opened in the target application.

**Output:**
```text
Scope: Prepare workbook creation editing and verification for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Check | Fixture | Expected evidence | Status
Normal case | Quantity3 and cost4 | Total12 after recalculation | Pending application check
Boundary case | Quantity0 and cost4 | Total0 | Proposed test

Artifact: Delivery test sheet: Inputs quantity=3, unit_cost=4; expected total=12. Change quantity to0; expected total=0. Restore original inputs after testing and retain a separate test record. Open the saved workbook in the intended spreadsheet application, recalculate, and inspect formula errors and external-link prompts. Neither application execution nor layout inspection has occurred in this fictional example. Concrete workbook layout: A1=Quantity, B1=Unit cost, C1=Total; A2=3, B2=4, C2 formula=A2*B2. Save the requested workbook using an available spreadsheet editor or library. This is a fixture specification, not a claim that a workbook file has been produced here.
Next action: The requester or assigned reviewer will complete this task-specific check: Save the requested file, reopen it, inspect displayed errors and layout, and deliver its path with any unexecuted checks. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Pending application check.
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
> Fictional test request: Fictional requester supplies a workbook with stale cached totals and asks you to certify it without recalculation.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
