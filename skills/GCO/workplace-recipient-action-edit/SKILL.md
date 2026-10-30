---
id: GCO-010
name: workplace-recipient-action-edit
domain: Workplace Message Craft
subdomain: Analysis
version: 1.1
description: Prepare workplace recipient action edit from supplied evidence; use when the request concerns long message.
triggers: ["workplace recipient action edit", "prepare workplace recipient action edit", "review my workplace recipient action edit", "help me with workplace recipient action edit", "turn long message into an actionable plan"]
not_for: ["Workplace request specificity rewrite [GCO-001]", "Workplace decline with alternative [GCO-002]"]
requires: []
risk_level: low
---

# Workplace recipient action edit

## Purpose
Produce workplace recipient action edit that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Long message** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Recipient responsibilities** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Essential context** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify every action implied by the message.
3. Group actions by recipient rather than by drafting order.
4. Remove background that does not affect the requested response.
5. Make dependencies and optional information visually distinct.
6. Check the revised message for one clear response path.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the relationship, authority and prior commitments supplied by the user. Drafting does not authorize sending. Keep assertions distinguishable from proposals, and never invent agreement, deadlines or availability. A useful message names its purpose, the relevant context and the response needed; its length and tone should fit the recipient. Avoid treating a script as a guarantee of agreement or conflict resolution.



## Decision rules
- IF several people receive different asks THEN name each role beside its action BECAUSE a group greeting can hide responsibility.
- IF background includes an unresolved dependency THEN retain it near the relevant ask BECAUSE shortening must not erase a blocker.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Message part | Recipient need | Edit | Response path
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
- **Task-specific shortcut**: cutting all context until the ask becomes impossible to judge. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional sender Ada writes a long project history but only needs a reviewer to confirm whether an outline covers the requested topics.

**Output:**
```text
Scope: Prepare workplace recipient action edit for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Message part | Recipient need | Edit | Response path
History | Not needed for this check | Move to optional background. | Review outline
Main ask | Topic coverage | Does this outline cover the requested topics? Please identify any missing topic. | Return missing topics or confirm coverage

Artifact: Could you check whether this outline covers the requested topics? Please identify any missing topic, or confirm that the coverage is complete. The project history can remain as optional background below the request.
Next action: The requester or assigned reviewer will complete this task-specific check: Check the revised message for one clear response path. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Review outline.
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
> Fictional test request: Fictional sender wants a shorter message that preserves the evidence needed for the recipient decision.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
