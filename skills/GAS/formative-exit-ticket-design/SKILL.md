---
id: GAS-005
name: formative-exit-ticket-design
domain: Learning Assessment
subdomain: Analysis
version: 1.1
description: Prepare formative exit ticket design from supplied evidence; use when the request concerns lesson objective.
triggers: ["formative exit ticket design", "prepare formative exit ticket design", "review my formative exit ticket design", "help me with formative exit ticket design", "turn lesson objective into an actionable plan"]
not_for: ["Learner error pattern analysis [GAS-006]", "Actionable feedback rewrite [GAS-007]"]
requires: []
risk_level: low
---

# Formative exit ticket design

## Purpose
Produce formative exit ticket design that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Lesson objective** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Likely learner errors** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Next lesson decision** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Choose the single teaching decision the exit ticket should inform.
3. Write a short task that distinguishes the relevant understanding patterns.
4. Define response categories before collecting answers.
5. Assign an instructional response to each category.
6. Check that the task can be completed under the actual classroom conditions.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Assess the stated performance rather than unrelated fluency, presentation polish, or access to outside help. Define criteria before judging the work, and preserve examples of what each criterion looks like. Separate an observed response from an inference about the learner. When a task is revised, check whether the construct being assessed has also changed. Use feedback that points to a repairable feature of the work. Do not claim that a score has a level of precision or comparability that the task design and scoring evidence do not support.



## Decision rules
- IF the response will not change instruction THEN revise the ticket purpose BECAUSE collection alone is not formative use.
- IF a question invites only confidence ratings THEN add performance evidence BECAUSE confidence may differ from understanding.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Response pattern | Evidence task | Interpretation | Next teaching action
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
- **Task-specific shortcut**: collecting tickets without deciding what different answers will trigger. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional teacher Mina needs to know whether learners distinguish a claim from its evidence.

**Output:**
```text
Scope: Prepare formative exit ticket design for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Response pattern | Evidence task | Interpretation | Next teaching action
Correct distinction | Label claim and support | Ready for comparison | Use new argument
Reversed labels | Same task | Concept distinction unclear | Use contrast example

Artifact: Proposed exit ticket: Our reading group should choose a quieter room because members could not hear the last discussion. Underline the claim, circle the reason, and explain the link.
Response branch: correct labels and explanation -> attempt comparison using a new argument.
Response branch: reversed labels -> compare a recommendation with a supporting observation before retrying.
Response branch: unclear explanation -> ask a short follow-up before assigning a concept difficulty.
These are planned teaching responses, not collected results.
Next action: The requester or assigned reviewer will complete this task-specific check: Check that the task can be completed under the actual classroom conditions. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Use new argument.
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
> Fictional test request: Fictional teacher Uri asks for an exit ticket but plans identical next steps regardless of responses.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
