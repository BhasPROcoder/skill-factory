---
id: GLA-009
name: language-learner-error-feedback
domain: Language Transfer and Translation
subdomain: Analysis
version: 1.1
description: Prepare language learner error feedback from supplied evidence; use when the request concerns learner sentence.
triggers: ["language learner error feedback", "prepare language learner error feedback", "review my language learner error feedback", "help me with language learner error feedback", "turn learner sentence into an actionable plan"]
not_for: ["Language practice dialogue scaffold [GLA-010]", "Translation brief preparation [GLA-001]"]
requires: []
risk_level: low
---

# Language learner error feedback

## Purpose
Produce language learner error feedback that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Learner sentence** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Intended meaning** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Learning focus** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Ask what the learner intended if meaning is uncertain.
3. Separate meaning-blocking problems from optional style changes.
4. Correct only the selected learning focus first.
5. Explain the pattern using the supplied sentence and a contrasting example.
6. Ask for a new sentence to check transfer rather than copying.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Collect source and target language, intended reader and purpose. Distinguish a translation from an explanation or adaptation. Never invent a target-language equivalent when competence or evidence is insufficient: mark the phrase for review by a qualified speaker. Treat examples here as fictional English source revisions or English glosses, not verified translations. Preserve negation, modality, referents and names before improving fluency.



## Decision rules
- IF intended meaning is unclear THEN ask before rewriting BECAUSE a grammatical sentence may express the wrong idea.
- IF many errors overwhelm the learner THEN prioritize one recurring pattern BECAUSE feedback needs an actionable next attempt.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Learner wording | Intended meaning | Feedback | Transfer task
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
- **Task-specific shortcut**: rewriting everything without showing the learner what changed. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional learner Uma writes Yesterday I walk to school and confirms a completed past event.

**Output:**
```text
Scope: Prepare language learner error feedback for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Learner wording | Intended meaning | Feedback | Transfer task
Walk | Completed past action | Use walked in this sentence. | Write another completed event.
Yesterday | Past time cue | Keep the cue while changing the verb. | Explain how the wording matches time.

Artifact: Corrected example: Yesterday I walked to school. You confirmed a completed past event, so walked fits this sentence. Try a new sentence about another completed event; then explain which word marks the action as past.
Next action: The requester or assigned reviewer will complete this task-specific check: Ask for a new sentence to check transfer rather than copying. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Write another completed event..
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
> Fictional test request: Fictional learner requests feedback on one recurring tense pattern in a short sentence.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
