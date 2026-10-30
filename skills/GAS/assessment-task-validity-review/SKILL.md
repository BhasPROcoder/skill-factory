---
id: GAS-002
name: assessment-task-validity-review
domain: Learning Assessment
subdomain: Analysis
version: 1.1
description: Prepare assessment task validity review from supplied evidence; use when the request concerns intended construct.
triggers: ["assessment task validity review", "prepare assessment task validity review", "review my assessment task validity review", "help me with assessment task validity review", "turn intended construct into an actionable plan"]
not_for: ["Multiple-choice item review [GAS-003]", "Short-answer scoring guide [GAS-004]"]
requires: []
risk_level: low
---

# Assessment task validity review

## Purpose
Produce assessment task validity review that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Intended construct** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Assessment prompt** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Allowed conditions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify the exact capability the task is meant to reveal.
3. List additional demands introduced by the prompt or format.
4. Check whether success can occur without the target capability.
5. Check whether irrelevant barriers can prevent a capable learner from demonstrating it.
6. Revise the task and state remaining limits on interpretation.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Assess the stated performance rather than unrelated fluency, presentation polish, or access to outside help. Define criteria before judging the work, and preserve examples of what each criterion looks like. Separate an observed response from an inference about the learner. When a task is revised, check whether the construct being assessed has also changed. Use feedback that points to a repairable feature of the work. Do not claim that a score has a level of precision or comparability that the task design and scoring evidence do not support.



## Decision rules
- IF the task rewards memorized wording while aiming at transfer THEN change the stimulus or required explanation BECAUSE recall alone does not demonstrate transfer.
- IF reading complexity is unrelated to the construct THEN reduce that barrier BECAUSE otherwise scores partly reflect an unintended demand.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Task demand | Relation to construct | Risk | Revision
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
- **Task-specific shortcut**: claiming a task measures only its intended skill without checking other demands. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional teacher Dara wants to assess causal reasoning but uses a dense unfamiliar passage.

**Output:**
```text
Scope: Prepare assessment task validity review for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Task demand | Relation to construct | Risk | Revision
Causal explanation | Target demand | Relevant | Retain reasoning question
Unfamiliar vocabulary | Incidental demand | May obscure reasoning | Clarify unnecessary terms

Artifact: Revised task frame: Using the supplied passage, identify the proposed cause, describe the claimed effect, and explain which information supports that relationship. Name an alternative explanation if the passage leaves one open.
Access revision: explain unfamiliar terms that are incidental to causal reasoning; preserve the causal relationships the learner must analyze.
Scoring boundary: judge the reasoning demonstrated, while recording any remaining vocabulary barrier.
The actual source passage is still required; this is a proposed prompt, not a finding about unseen responses.
Next action: The requester or assigned reviewer will complete this task-specific check: Revise the task and state remaining limits on interpretation. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Retain reasoning question.
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
> Fictional test request: Fictional assessor Bo wants to infer problem-solving ability from a task dominated by unfamiliar terminology.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
