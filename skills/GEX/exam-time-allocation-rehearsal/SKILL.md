---
id: GEX-008
name: exam-time-allocation-rehearsal
domain: Exam Preparation Methods
subdomain: Analysis
version: 1.1
description: Prepare exam time allocation rehearsal from supplied evidence; use when the request concerns verified exam structure.
triggers: ["exam time allocation rehearsal", "prepare exam time allocation rehearsal", "review my exam time allocation rehearsal", "help me with exam time allocation rehearsal", "turn verified exam structure into an actionable plan"]
not_for: ["Final review triage [GEX-009]", "Exam-day logistics checklist [GEX-010]"]
requires: []
risk_level: low
---

# Exam time allocation rehearsal

## Purpose
Produce exam time allocation rehearsal that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Verified exam structure** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Practice timing records** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Completion priorities** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify task types and constraints from the current official format.
3. Use practice records to estimate where time is actually spent.
4. Choose provisional move-on checkpoints rather than rigid guesses.
5. Rehearse the plan on a comparable practice set.
6. Revise allocations using completion and answer-quality evidence.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the official current syllabus, format and permitted materials as inputs rather than reproducing them from memory. Separate learning a topic from performing it under exam conditions. Track errors by cause and revisit whether practice is actually changing performance. Treat practice scores as evidence from particular tasks, not guaranteed predictions of a future result. Protect time for sleep and ordinary breaks without prescribing medical guidance. If the requested plan exceeds available capacity, show the tradeoff explicitly rather than promising that every topic can receive full treatment.



## Decision rules
- IF a task repeatedly overruns THEN inspect the cause before shrinking all other tasks BECAUSE method difficulty and perfectionism require different repairs.
- IF official rules restrict navigation THEN build those restrictions into rehearsal BECAUSE an unrestricted practice plan may not transfer.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Task stage | Observed timing issue | Provisional rule | Rehearsal evidence
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
- **Task-specific shortcut**: promising a universal number of minutes for every question. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional candidate Ivo can revisit questions but spends too long perfecting early responses. In the supplied rehearsal log, no time remained for the review pass.

**Output:**
```text
Scope: Prepare exam time allocation rehearsal for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Task stage | Observed timing issue | Provisional rule | Rehearsal evidence
First pass | Over-polishing | Move after sufficient draft | Check later-question coverage
Review pass | No time remains | Reserve review only after coverage | Compare answer quality

Artifact: Provisional rehearsal rule: on the first pass, move beyond an answer once it meets the task's essential demands; mark unresolved improvements for a permitted return.
Coverage gate: attempt the remaining required tasks before using remaining time to polish earlier wording.
Observation record: move-on decision, later-task coverage, and any loss of necessary reasoning.
Retain or revise the rule from the next comparable rehearsal. Use official navigation restrictions and actual timing records; no invented minutes per question.
Next action: The requester or assigned reviewer will complete this task-specific check: Revise allocations using completion and answer-quality evidence. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Check later-question coverage.
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
> Fictional test request: Fictional candidate Fia wants timing advice without giving the exam structure or practice observations.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
