---
id: GEX-003
name: exam-practice-error-log
domain: Exam Preparation Methods
subdomain: Analysis
version: 1.1
description: Prepare exam practice error log from supplied evidence; use when the request concerns attempted questions.
triggers: ["exam practice error log", "prepare exam practice error log", "review my exam practice error log", "help me with exam practice error log", "turn attempted questions into an actionable plan"]
not_for: ["Mock exam review [GEX-004]", "Retrieval practice set [GEX-005]"]
requires: []
risk_level: low
---

# Exam practice error log

## Purpose
Produce exam practice error log that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Attempted questions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Marked answers** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Learner explanations** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Record the question task and attempted reasoning.
3. Classify the error as knowledge, method selection, execution or interpretation using evidence.
4. Write a correction that explains the failed decision.
5. Assign a new practice item that tests the same decision with changed details.
6. Review whether the error recurs before closing the log entry.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the official current syllabus, format and permitted materials as inputs rather than reproducing them from memory. Separate learning a topic from performing it under exam conditions. Track errors by cause and revisit whether practice is actually changing performance. Treat practice scores as evidence from particular tasks, not guaranteed predictions of a future result. Protect time for sleep and ordinary breaks without prescribing medical guidance. If the requested plan exceeds available capacity, show the tradeoff explicitly rather than promising that every topic can receive full treatment.



## Decision rules
- IF the learner copied the solution without explanation THEN keep the entry open BECAUSE recognition is not evidence of independent correction.
- IF the error category is uncertain THEN use a diagnostic reattempt BECAUSE the remedy depends on the cause.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Error | Evidence of cause | Repair | Retest
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
- **Task-specific shortcut**: labeling every mistake careless. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional candidate Amir selected a familiar method without checking the question condition.

**Output:**
```text
Scope: Prepare exam practice error log for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Error | Evidence of cause | Repair | Retest
Method selection | Ignored condition | State applicability test | Try changed-condition item
Execution | No evidence of arithmetic issue | Do not assign arithmetic drills | Observe next attempt

Artifact: Entry: selected a familiar method without checking its applicability condition.
Repair prompt: Before solving, write the condition that must hold for this method and identify whether the question supplies it.
Retest: use a new question where the condition changes; require method selection and justification before calculation.
Closure rule: independent justification and a suitable method on the retest, not copying the earlier solution.
Arithmetic drills are not assigned without evidence of an execution error.
Next action: The requester or assigned reviewer will complete this task-specific check: Review whether the error recurs before closing the log entry. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Try changed-condition item.
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
> Fictional test request: Fictional candidate Jo repeats an error after memorizing the answer and asks to mark it fixed.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
