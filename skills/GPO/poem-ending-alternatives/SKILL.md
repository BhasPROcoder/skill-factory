---
id: GPO-009
name: poem-ending-alternatives
domain: Poetry Craft and Revision
subdomain: Analysis
version: 1.1
description: Prepare poem ending alternatives from supplied evidence; use when the request concerns draft poem.
triggers: ["poem ending alternatives", "prepare poem ending alternatives", "review my poem ending alternatives", "help me with poem ending alternatives", "turn draft poem into an actionable plan"]
not_for: ["Poem reading performance markup [GPO-010]", "Poem image bank development [GPO-001]"]
requires: []
risk_level: low
---

# Poem ending alternatives

## Purpose
Produce poem ending alternatives that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Draft poem** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Current ending** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Desired openness** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify what the poem has already established.
3. Classify the current ending as image, statement, question or return.
4. Draft alternatives that change the degree of closure.
5. Check whether each alternative adds an unsupported moral.
6. Choose the ending whose final emphasis fits the poem movement.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use original invented text for demonstrations. Describe craft through observable effects: image placement, repeated sounds, line endings, stanza breaks, syntax and changes in perspective. A craft device is a choice, not a guarantee of emotional impact. Preserve the user intended voice; do not impose rhyme, meter or a named form unless requested. Read drafts aloud or describe the intended pauses without pretending a recording was heard.



## Decision rules
- IF the ending explains an image already clear THEN test ending on the image BECAUSE repetition of meaning may weaken the final emphasis.
- IF an open ending removes essential context THEN restore enough orientation BECAUSE ambiguity should remain interpretable.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Ending option | Closure | Effect | Choice condition
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
- **Task-specific shortcut**: assuming every poem needs a universal lesson. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional poet Mina ends a scene with an unopened letter on a table and the line This means I am afraid.

**Output:**
```text
Scope: Prepare poem ending alternatives for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Ending option | Closure | Effect | Choice condition
Keep explanation | Explicit | Names emotion | Use only if direct declaration fits voice
End on letter | Open | Leaves action unresolved | Use if scene supports uncertainty

Artifact: Ending A: The letter waits unopened. / I am afraid to read it. Ending B: The letter waits unopened. A names the fear; B ends on the unresolved action. Both are invented alternatives for the supplied scene.
Next action: The requester or assigned reviewer will complete this task-specific check: Choose the ending whose final emphasis fits the poem movement. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Use only if direct declaration fits voice.
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
> Fictional test request: Fictional poet asks for contrasting endings without changing the events already in the draft.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
