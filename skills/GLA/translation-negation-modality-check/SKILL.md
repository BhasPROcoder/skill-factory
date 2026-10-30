---
id: GLA-003
name: translation-negation-modality-check
domain: Language Transfer and Translation
subdomain: Analysis
version: 1.1
description: Prepare translation negation and modality check from supplied evidence; use when the request concerns source and target drafts.
triggers: ["translation negation and modality check", "prepare translation negation and modality check", "review my translation negation and modality check", "help me with translation negation and modality check", "turn source and target drafts into an actionable plan"]
not_for: ["Translation terminology decision log [GLA-004]", "Translation register alignment [GLA-005]"]
requires: []
risk_level: low
---

# Translation negation and modality check

## Purpose
Produce translation negation and modality check that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Source and target drafts** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Instruction context** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Known terminology** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Extract negation, permission, obligation and possibility expressions.
3. Align each expression with its target counterpart.
4. Check the scope of negation over actions and conditions.
5. Compare who is allowed or required to act.
6. Flag altered commitments for bilingual review before stylistic polishing.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Collect source and target language, intended reader and purpose. Distinguish a translation from an explanation or adaptation. Never invent a target-language equivalent when competence or evidence is insufficient: mark the phrase for review by a qualified speaker. Treat examples here as fictional English source revisions or English glosses, not verified translations. Preserve negation, modality, referents and names before improving fluency.



## Decision rules
- IF may becomes must THEN flag obligation escalation BECAUSE permission and obligation differ.
- IF not required becomes prohibited THEN restore the distinction BECAUSE absence of duty does not imply a ban.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Source meaning | Draft meaning | Change | Correction instruction
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
- **Task-specific shortcut**: accepting fluent wording with changed duty. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional bilingual reviewer Lio supplies English glosses: source You may submit a note; target You must submit a note.

**Output:**
```text
Scope: Prepare translation negation and modality check for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Source meaning | Draft meaning | Change | Correction instruction
May submit | Must submit | Permission became obligation | Restore optional submission
Note | Note | Object preserved | Keep same referent

Artifact: Review finding: source permission became a target obligation in the supplied English gloss. Required meaning: submitting a note is optional. Ask the bilingual reviewer to restore that meaning and confirm the target wording.
Next action: The requester or assigned reviewer will complete this task-specific check: Flag altered commitments for bilingual review before stylistic polishing. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Restore optional submission.
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
> Fictional test request: Fictional reviewer sees not required rendered as not allowed in a supplied target-language gloss.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
