---
id: GPO-008
name: poem-concrete-language-compression
domain: Poetry Craft and Revision
subdomain: Analysis
version: 1.1
description: Prepare poem concrete language compression from supplied evidence; use when the request concerns poem draft.
triggers: ["poem concrete language compression", "prepare poem concrete language compression", "review my poem concrete language compression", "help me with poem concrete language compression", "turn poem draft into an actionable plan"]
not_for: ["Poem ending alternatives [GPO-009]", "Poem reading performance markup [GPO-010]"]
requires: []
risk_level: low
---

# Poem concrete language compression

## Purpose
Produce poem concrete language compression that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Poem draft** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Essential images** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Meaning that must remain** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify abstract explanation after a concrete image.
3. Test removing the explanation while preserving the image.
4. Replace weak general verbs with accurate actions from the scene.
5. Cut redundant modifiers without adding a new fact.
6. Compare the compressed draft with the intended meaning.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use original invented text for demonstrations. Describe craft through observable effects: image placement, repeated sounds, line endings, stanza breaks, syntax and changes in perspective. A craft device is a choice, not a guarantee of emotional impact. Preserve the user intended voice; do not impose rhyme, meter or a named form unless requested. Read drafts aloud or describe the intended pauses without pretending a recording was heard.



## Decision rules
- IF a cut removes necessary context THEN restore a concise cue BECAUSE compression is not obscurity.
- IF a stronger verb changes the action THEN reject it BECAUSE precision matters more than intensity.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Draft element | Function | Compression | Meaning check
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
- **Task-specific shortcut**: replacing every word with a dramatic synonym. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional poet Edda writes The empty chair was very empty and made me feel the absence of her presence.

**Output:**
```text
Scope: Prepare poem concrete language compression for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Draft element | Function | Compression | Meaning check
Empty repeated | Redundant emphasis | Her chair stands empty. | Keeps absence
Emotional explanation | Names implied feeling | Test removing it | Reader sees chair detail

Artifact: Compressed proposed line: Her chair stands empty. The revision removes the repeated empty and the explanatory absence of her presence. Keep additional context elsewhere if the reader cannot tell why this chair matters.
Next action: The requester or assigned reviewer will complete this task-specific check: Compare the compressed draft with the intended meaning. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Keeps absence.
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
> Fictional test request: Fictional poet wants a shorter draft while keeping the setting and implied relationship.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
