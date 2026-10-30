---
id: GLA-010
name: language-practice-dialogue-scaffold
domain: Language Transfer and Translation
subdomain: Analysis
version: 1.1
description: Prepare language practice dialogue scaffold from supplied evidence; use when the request concerns communicative situation.
triggers: ["language practice dialogue scaffold", "prepare language practice dialogue scaffold", "review my language practice dialogue scaffold", "help me with language practice dialogue scaffold", "turn communicative situation into an actionable plan"]
not_for: ["Translation brief preparation [GLA-001]", "Translation ambiguity query log [GLA-002]"]
requires: []
risk_level: low
---

# Language practice dialogue scaffold

## Purpose
Produce language practice dialogue scaffold that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Communicative situation** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Learner ability** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Target expressions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Define the practical outcome of the conversation.
3. Choose expressions that directly support that outcome.
4. Write a short model exchange with clear speaker roles.
5. Remove selected support for a second attempt.
6. Add an unexpected but plausible response that tests repair language.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Collect source and target language, intended reader and purpose. Distinguish a translation from an explanation or adaptation. Never invent a target-language equivalent when competence or evidence is insufficient: mark the phrase for review by a qualified speaker. Treat examples here as fictional English source revisions or English glosses, not verified translations. Preserve negation, modality, referents and names before improving fluency.



## Decision rules
- IF the learner memorizes without responding THEN change one conversational condition BECAUSE flexible use matters beyond recitation.
- IF a phrase is beyond demonstrated ability THEN offer a simpler equivalent BECAUSE practice should permit an independent response.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Dialogue stage | Support | Learner action | Check
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
- **Task-specific shortcut**: calling memorized repetition a successful conversation. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional learner Bea practices asking a colleague to repeat an instruction in English.

**Output:**
```text
Scope: Prepare language practice dialogue scaffold for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Dialogue stage | Support | Learner action | Check
Model | Could you repeat the last step? | Ask for clarification | Specific missing part named
Variation | Colleague speaks too quickly | Could you say that more slowly? | Repair request matches obstacle

Artifact: Model: Colleague: Put the note beside the draft. Learner: Could you repeat the last step? Colleague: Put the note beside the draft. Variation: if the colleague repeats too quickly, ask Could you say that more slowly? These are proposed practice lines.
Next action: The requester or assigned reviewer will complete this task-specific check: Add an unexpected but plausible response that tests repair language. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Specific missing part named.
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
> Fictional test request: Fictional learner can repeat a model but cannot ask for clarification when the response changes.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
