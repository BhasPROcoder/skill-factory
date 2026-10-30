---
id: GLA-007
name: translation-idiom-function-adaptation
domain: Language Transfer and Translation
subdomain: Analysis
version: 1.1
description: Prepare translation idiom function adaptation from supplied evidence; use when the request concerns source idiom in context.
triggers: ["translation idiom function adaptation", "prepare translation idiom function adaptation", "review my translation idiom function adaptation", "help me with translation idiom function adaptation", "turn source idiom in context into an actionable plan"]
not_for: ["Translation review disagreement resolution [GLA-008]", "Language learner error feedback [GLA-009]"]
requires: []
risk_level: low
---

# Translation idiom function adaptation

## Purpose
Produce translation idiom function adaptation that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Source idiom in context** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Intended communicative effect** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Audience familiarity** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Determine what the idiom accomplishes in the passage.
3. Separate literal imagery from the intended meaning.
4. Check whether a known target expression carries the same tone and implication.
5. Prefer a plain paraphrase when a reliable equivalent is unavailable.
6. Explain significant adaptation choices in the handoff.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Collect source and target language, intended reader and purpose. Distinguish a translation from an explanation or adaptation. Never invent a target-language equivalent when competence or evidence is insufficient: mark the phrase for review by a qualified speaker. Treat examples here as fictional English source revisions or English glosses, not verified translations. Preserve negation, modality, referents and names before improving fluency.



## Decision rules
- IF literal imagery would confuse the reader THEN use a meaning-preserving paraphrase BECAUSE understanding is the relevant function.
- IF an alleged equivalent changes blame or intensity THEN reject it BECAUSE similar imagery does not ensure similar force.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Expression | Intended function | Adaptation | Caution
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
- **Task-specific shortcut**: replacing an idiom with an unverified dictionary-like invention. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional speaker Jo says We are on the same page after colleagues agree on the plan.

**Output:**
```text
Scope: Prepare translation idiom function adaptation for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Expression | Intended function | Adaptation | Caution
Same page | Agreement | We agree on the plan. | English gloss only
Tone | Collaborative | Keep inclusive we | Do not imply full agreement beyond plan

Artifact: Plain meaning gloss: We agree on the plan. Preserve the collaborative tone. This is an English paraphrase for the translator brief, not a verified equivalent in an unspecified target language.
Next action: The requester or assigned reviewer will complete this task-specific check: Explain significant adaptation choices in the handoff. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: English gloss only.
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
> Fictional test request: Fictional writer uses a metaphor whose literal target-language reading would suggest a physical action.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
