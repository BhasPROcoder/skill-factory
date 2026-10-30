---
id: CBG-003
name: community-operating-loop-design
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare community operating loop design from supplied evidence; use when the request concerns member purpose.
triggers: ["community operating loop design", "prepare community operating loop design", "review my community operating loop design", "help me with community operating loop design", "turn member purpose into an actionable plan"]
not_for: ["Workbook creation editing and verification [CBG-004]", "Structured document creation and editing [CBG-005]"]
requires: []
risk_level: medium
---

# Community operating loop design

## Purpose
Produce community operating loop design that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Member purpose** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Available moderation capacity** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Participation and incident evidence** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Define a recurring member need that interaction can satisfy.
3. Specify the contribution and response loop with an owner for unanswered requests.
4. Choose participation rituals compatible with member availability and moderator capacity.
5. Separate healthy participation measures from raw message volume.
6. Define escalation, consent and review routes before growing the loop.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF activity rises while questions remain unanswered THEN review response coverage BECAUSE message volume does not show member value.
- IF moderation depends on unconfirmed volunteers THEN reduce scope until ownership exists BECAUSE enthusiasm is not a staffing commitment.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Loop element | Proposed behavior | Owner | Evidence
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
- **Task-specific shortcut**: treating member count as proof of a functioning community. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional community Birch exchanges practice feedback. Members post drafts but replies are inconsistent; no volunteer has accepted moderation duties.

**Output:**
```text
Scope: Prepare community operating loop design for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Loop element | Proposed behavior | Owner | Evidence
Feedback request | Ask for one specific kind of feedback | Author | Request is answerable
Response coverage | Track unanswered requests | Organizer pending assignment | No volunteer assumed

Artifact: Operating loop: A member posts a short draft and names the feedback sought. A willing peer responds with an observation and a suggested revision. The author acknowledges what they will try. The organizer reviews unanswered requests at a feasible agreed interval and adjusts the intake if response capacity is insufficient. Escalation and moderator assignments remain pending; do not recruit or message people automatically.
Next action: The requester or assigned reviewer will complete this task-specific check: Define escalation, consent and review routes before growing the loop. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Request is answerable.
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
> Fictional test request: Fictional organizer wants daily activities despite having no confirmed moderator or response coverage.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
