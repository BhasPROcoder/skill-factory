---
id: GRQ-005
name: research-interview-guide
domain: Research Question and Study Design
subdomain: Analysis
version: 1.1
description: Prepare repeated-wave interview protocol from supplied evidence; use when the request concerns prior-wave interview and participant reference.
triggers: ["repeated-wave interview protocol", "prepare repeated-wave interview protocol", "review my repeated-wave interview protocol", "help me with repeated-wave interview protocol", "turn prior-wave interview and participant reference into an actionable plan"]
not_for: ["Questionnaire cognitive pretest [GRQ-006]", "Research pilot protocol [GRQ-007]"]
requires: []
risk_level: medium
---

# Repeated-wave interview protocol

## Purpose
Produce repeated-wave interview protocol that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Prior-wave interview and participant reference** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Stable research question** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Follow-up consent and contact constraints** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Separate core questions needed for within-participant comparison from exploratory probes.
3. Retain the wording and ordering of the core unless a documented comprehension problem requires revision.
4. Ask about concrete events since the previous wave without presuming improvement or deterioration.
5. Record changed context and instrument revisions separately from reported experience changes.
6. Code missing waves and withdrawals explicitly instead of constructing a continuous narrative.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Distinguish a study design proposal from completed research. Define the unit being studied and the comparison needed before naming a method. Record feasibility, consent, privacy and institutional review requirements relevant to the actual setting, using current institutional guidance instead of assumed exemptions. Do not invent recruitment access, instruments, prior findings, sample-size justifications or causal identification. A design can be useful while a required decision remains open; state exactly which conclusion the missing decision prevents. Use only fictional participant details in examples.



## Decision rules
- IF a core question changes THEN flag the comparability break BECAUSE wording effects can resemble experience changes.
- IF a participant misses a wave THEN retain the missing observation BECAUSE silence does not establish stability.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Protocol part | Stable element | Wave-specific probe | Comparison limit
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
- **Task-specific shortcut**: rewriting every question between waves and attributing every response difference to the participant. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional researcher Lena follows the same service users over time. Her prior core prompt was Tell me about your most recent booking. One participant misses the follow-up; no new response is available.

**Output:**
```text
Scope: Prepare repeated-wave interview protocol for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Protocol part | Stable element | Wave-specific probe | Comparison limit
Core prompt | Most recent booking | What changed since our previous conversation? | Do not assume a change occurred
Missed wave | Participant reference retained | No interview fabricated | Experience during gap unknown

Artifact: Follow-up script: Tell me about your most recent booking. Since our previous conversation, has anything about booking changed or stayed the same? Please describe a particular occasion. Keep the original core prompt unchanged, record new probes separately, and enter missing wave for the absent participant. Do not turn a missing interview into a statement that nothing changed.
Next action: The requester or assigned reviewer will complete this task-specific check: Code missing waves and withdrawals explicitly instead of constructing a continuous narrative. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Do not assume a change occurred.
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
> Fictional test request: Fictional researcher receives a changed interview guide and a missing follow-up wave, then asks for a continuous account of improvement.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
