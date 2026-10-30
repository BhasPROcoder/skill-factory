---
id: GED-003
name: worked-example-lesson-sequence
domain: Lesson and Learning Design
subdomain: Analysis
version: 1.1
description: Prepare worked example lesson sequence from supplied evidence; use when the request concerns target procedure.
triggers: ["worked example lesson sequence", "prepare worked example lesson sequence", "review my worked example lesson sequence", "help me with worked example lesson sequence", "turn target procedure into an actionable plan"]
not_for: ["Misconception contrast activity [GED-004]", "Lesson practice alignment review [GED-005]"]
requires: []
risk_level: low
---

# Worked example lesson sequence

## Purpose
Produce worked example lesson sequence that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Target procedure** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Common learner errors** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Practice conditions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Select a complete example that exposes the decisions in the procedure.
3. Annotate why each step is chosen rather than merely naming the operation.
4. Create a partially completed counterpart that requires a meaningful missing decision.
5. Follow with an independent task using changed surface details.
6. Compare learner explanations with the decision logic before increasing difficulty.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat the learner performance as the target: identify what the learner should be able to do, the conditions under which they should do it, and what would count as a successful attempt. Use supplied curriculum and learner work as the factual basis. Do not infer a diagnosis or fixed ability from one error. Match examples and practice to the actual goal, then use a small check to decide whether to advance, explain differently, or revisit a prerequisite. Label teaching choices as design choices rather than guaranteed learning effects.



## Decision rules
- IF the example skips a decision THEN make that choice visible BECAUSE learners cannot infer the intended judgment reliably.
- IF practice differs in underlying structure THEN label it as transfer work BECAUSE it is not simply another repetition.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Sequence stage | Learner action | Support | Check
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
- **Task-specific shortcut**: showing polished answers without revealing the decisions that produced them. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional teacher Noor teaches source comparison using a fully annotated pair of texts and then a new pair.

**Output:**
```text
Scope: Prepare worked example lesson sequence for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Sequence stage | Learner action | Support | Check
Annotated example | Explain why sources differ | Decision notes supplied | Learner names comparison basis
Independent pair | Compare new sources | No completed comparison | Check reasoning rather than copied phrases

Artifact: Proposed teaching texts: A says the club needs a larger room because members stood; B says the current room is adequate because it fits the usual attendance.
Model: compare their meanings of adequate and the attendance evidence they use; neither text alone establishes which attendance is relevant.
Completion task: supply the missing comparison question: Which attendance pattern should the decision cover?
Independent task: compare new texts that disagree about an opening time because they describe different users.
Check: learner names the relevant difference, not just that authors disagree.
Next action: The requester or assigned reviewer will complete this task-specific check: Compare learner explanations with the decision logic before increasing difficulty. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Learner names comparison basis.
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
> Fictional test request: Fictional teacher Bea asks for examples that change the numbers but never require a new decision.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
