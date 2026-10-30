---
id: GEX-002
name: exam-study-capacity-plan
domain: Exam Preparation Methods
subdomain: Analysis
version: 1.1
description: Prepare mastery-dependent study sequence from supplied evidence; use when the request concerns diagnostic attempts.
triggers: ["mastery-dependent study sequence", "prepare mastery-dependent study sequence", "review my mastery-dependent study sequence", "help me with mastery-dependent study sequence", "turn diagnostic attempts into an actionable plan"]
not_for: ["Exam practice error log [GEX-003]", "Mock exam review [GEX-004]"]
requires: []
risk_level: low
---

# Mastery-dependent study sequence

## Purpose
Produce mastery-dependent study sequence that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Diagnostic attempts** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Topic prerequisites** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Available study blocks** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify which prerequisite errors block the target exam task from the supplied diagnostic work.
3. Group tasks by prerequisite rather than by chapter order alone.
4. Place a short diagnostic and repair opportunity before dependent practice.
5. Define an observable transfer attempt that permits advancing to the next task.
6. Reallocate remaining blocks when evidence shows a prerequisite is still unstable instead of copying the original timetable.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the official current syllabus, format and permitted materials as inputs rather than reproducing them from memory. Separate learning a topic from performing it under exam conditions. Track errors by cause and revisit whether practice is actually changing performance. Treat practice scores as evidence from particular tasks, not guaranteed predictions of a future result. Protect time for sleep and ordinary breaks without prescribing medical guidance. If the requested plan exceeds available capacity, show the tradeoff explicitly rather than promising that every topic can receive full treatment.



## Decision rules
- IF a prerequisite error persists THEN repair it before increasing dependent complexity BECAUSE more advanced attempts may repeat the same obstacle.
- IF a familiar item is correct but a changed item fails THEN retain transfer practice BECAUSE recognition is not yet flexible mastery.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Learning dependency | Diagnostic evidence | Study sequence | Advance condition
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
- **Task-specific shortcut**: assigning equal time to every topic without checking prerequisite bottlenecks. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional candidate Nia can recall definitions but misidentifies claims in unfamiliar paragraphs. She has study blocks available; no durations or exam weighting are supplied.

**Output:**
```text
Scope: Prepare mastery-dependent study sequence for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Learning dependency | Diagnostic evidence | Study sequence | Advance condition
Claim identification | Unfamiliar paragraph error | Contrast claim with supporting example | Correctly explain distinction in a new paragraph
Argument comparison | Requires claim identification | Practice after prerequisite check | Compare claims using explicit common criterion

Artifact: Proposed sequencing rule: check the prerequisite skill before assigning dependent exam practice. If the diagnostic shows a missing prerequisite, place a focused repair task in a reliable study block, followed by a fresh check; release the dependent task only when that check supports readiness.
Nia's first repair: distinguish the recommendation from a supporting example in a short paragraph. Use a new paragraph for the advance check; require both a correct label and an explanation.
If a prerequisite is already demonstrated: move directly to the next dependent task rather than filling time with comfortable repetition.
Next dependent task: compare arguments only after the claim-identification check supports readiness. Available block durations and exam weighting remain unknown.
Next action: The requester or assigned reviewer will complete this task-specific check: Reallocate remaining blocks when evidence shows a prerequisite is still unstable instead of copying the original timetable. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Correctly explain distinction in a new paragraph.
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
> Fictional test request: Fictional candidate memorizes definitions but fails unfamiliar applications and wants to progress to advanced tasks because the calendar says so.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
