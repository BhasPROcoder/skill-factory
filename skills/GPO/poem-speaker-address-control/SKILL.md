---
id: GPO-006
name: poem-speaker-address-control
domain: Poetry Craft and Revision
subdomain: Analysis
version: 1.1
description: Prepare poem speaker and address control from supplied evidence; use when the request concerns draft pronouns.
triggers: ["poem speaker and address control", "prepare poem speaker and address control", "review my poem speaker and address control", "help me with poem speaker and address control", "turn draft pronouns into an actionable plan"]
not_for: ["Poem repetition and variation plan [GPO-007]", "Poem concrete language compression [GPO-008]"]
requires: []
risk_level: low
---

# Poem speaker and address control

## Purpose
Produce poem speaker and address control that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Draft pronouns** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Speaker identity** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Intended addressee** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify who speaks and what the reader can infer about them.
3. Track each you, we and they to a plausible referent.
4. Mark shifts between self-address, another person and a wider audience.
5. Choose whether ambiguity is intentional or needs a clarifying detail.
6. Revise pronouns and address cues without inventing biography.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use original invented text for demonstrations. Describe craft through observable effects: image placement, repeated sounds, line endings, stanza breaks, syntax and changes in perspective. A craft device is a choice, not a guarantee of emotional impact. Preserve the user intended voice; do not impose rhyme, meter or a named form unless requested. Read drafts aloud or describe the intended pauses without pretending a recording was heard.



## Decision rules
- IF you changes referent unintentionally THEN add a cue or change the pronoun BECAUSE the reader needs a navigable address.
- IF speaker identity is deliberately open THEN preserve relevant ambiguity BECAUSE clarity does not require a full biography.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Address cue | Possible referent | Risk | Revision
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
- **Task-specific shortcut**: treating every first-person poem as the author autobiography. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional poet Lea addresses an absent sister, then writes you never know to mean people generally.

**Output:**
```text
Scope: Prepare poem speaker and address control for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Address cue | Possible referent | Risk | Revision
Opening you | Sister | Clear from supplied context | Retain
You never know | General reader | Unmarked shift | Try no one knows

Artifact: Address edit: retain you for the absent sister; replace the generalizing you never know with no one knows. This keeps the sister as the direct addressee while allowing a general statement.
Next action: The requester or assigned reviewer will complete this task-specific check: Revise pronouns and address cues without inventing biography. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Retain.
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
> Fictional test request: Fictional poet wants a dramatic speaker distinct from the author and a consistent addressee.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
