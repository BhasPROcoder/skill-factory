---
id: GAS-009
name: portfolio-evidence-selection
domain: Learning Assessment
subdomain: Analysis
version: 1.0
description: Prepare learning portfolio evidence selection from supplied evidence; use when the request concerns portfolio purpose.
triggers: ["learning portfolio evidence selection", "prepare learning portfolio evidence selection", "review my learning portfolio evidence selection", "help me with learning portfolio evidence selection", "turn portfolio purpose into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: low
---

# Learning portfolio evidence selection

## Purpose
Produce learning portfolio evidence selection that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Portfolio purpose** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Available work** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Learning criteria** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Map each criterion to possible evidence artifacts.
3. Choose artifacts that show the learner contribution and process.
4. Include a revision pair where change is relevant to the purpose.
5. Add a short annotation explaining what each artifact demonstrates.
6. Identify criteria still unsupported instead of filling space with unrelated work.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Assess the stated performance rather than unrelated fluency, presentation polish, or access to outside help. Define criteria before judging the work, and preserve examples of what each criterion looks like. Separate an observed response from an inference about the learner. When a task is revised, check whether the construct being assessed has also changed. Use feedback that points to a repairable feature of the work. Do not claim that a score has a level of precision or comparability that the task design and scoring evidence do not support.



## Decision rules
- IF an artifact is impressive but irrelevant THEN exclude or reframe it BECAUSE portfolio size is not evidence coverage.
- IF group work hides contribution THEN add individual evidence BECAUSE the portfolio must support claims about the learner.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Criterion | Artifact | Evidence claim | Gap
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
- **Task-specific shortcut**: selecting only attractive artifacts regardless of learning criteria. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional learner Kira has a polished group poster and an earlier individual draft for a writing portfolio.

**Output:**
```text
Scope: Prepare learning portfolio evidence selection for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Criterion | Artifact | Evidence claim | Gap
Individual reasoning | Individual draft | Shows own argument choices | Needs revision evidence
Presentation polish | Group poster | Contribution unclear | Add role evidence or omit
Next action: The requester supplies the unresolved evidence and confirms the proposed next step before implementation.
Unresolved: Which missing source or observation would change the provisional conclusion?
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
> Fictional test request: Fictional learner Theo wants a portfolio made entirely of final group products.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
