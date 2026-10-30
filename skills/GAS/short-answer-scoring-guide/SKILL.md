---
id: GAS-004
name: short-answer-scoring-guide
domain: Learning Assessment
subdomain: Analysis
version: 1.1
description: Prepare short-answer scoring guide from supplied evidence; use when the request concerns short-answer prompt.
triggers: ["short-answer scoring guide", "prepare short-answer scoring guide", "review my short-answer scoring guide", "help me with short-answer scoring guide", "turn short-answer prompt into an actionable plan"]
not_for: ["Formative exit ticket design [GAS-005]", "Learner error pattern analysis [GAS-006]"]
requires: []
risk_level: low
---

# Short-answer scoring guide

## Purpose
Produce short-answer scoring guide that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Short-answer prompt** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Expected reasoning** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Possible valid alternatives** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify the essential elements that answer the question.
3. Separate required reasoning from optional wording.
4. Describe partially correct responses by the elements present.
5. List common errors and how they affect the judgment.
6. Test the guide on paraphrases and alternative valid approaches.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Assess the stated performance rather than unrelated fluency, presentation polish, or access to outside help. Define criteria before judging the work, and preserve examples of what each criterion looks like. Separate an observed response from an inference about the learner. When a task is revised, check whether the construct being assessed has also changed. Use feedback that points to a repairable feature of the work. Do not claim that a score has a level of precision or comparability that the task design and scoring evidence do not support.



## Decision rules
- IF a response uses different wording but equivalent reasoning THEN credit the demonstrated element BECAUSE the target is meaning rather than phrase matching.
- IF the prompt permits several methods THEN include those routes BECAUSE a single model answer may be too narrow.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Required element | Acceptable evidence | Partial response | Scoring note
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
- **Task-specific shortcut**: treating a model answer as the only valid wording. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional teacher Noel asks learners to explain a source conflict and has a guide requiring one exact phrase.

**Output:**
```text
Scope: Prepare short-answer scoring guide for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Required element | Acceptable evidence | Partial response | Scoring note
Conflict identification | Meaningful paraphrase | Names disagreement only | Credit identified element
Reasoning | Explains context difference | No explanation | Do not require fixed wording

Artifact: Required element: identify the disagreement between the supplied sources.
Acceptable evidence: a correct paraphrase of what each source says; exact model-answer wording is unnecessary.
Required reasoning: explain a relevant contextual difference supported by the sources.
Partial response: names the disagreement but does not explain it; recognize identification while keeping explanation incomplete.
Alternative valid route: accept another supported explanation and record its evidence rather than rejecting it for being absent from the initial key.
Next action: The requester or assigned reviewer will complete this task-specific check: Test the guide on paraphrases and alternative valid approaches. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Credit identified element.
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
> Fictional test request: Fictional scorer Arin receives a correct alternative explanation absent from the initial answer key.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
