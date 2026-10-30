---
id: GPR-010
name: overdue-commitment-recovery-plan
domain: Personal Work Organization
subdomain: Analysis
version: 1.1
description: Prepare overdue commitment recovery plan from supplied evidence; use when the request concerns missed commitments.
triggers: ["overdue commitment recovery plan", "prepare overdue commitment recovery plan", "review my overdue commitment recovery plan", "help me with overdue commitment recovery plan", "turn missed commitments into an actionable plan"]
not_for: ["Task inbox triage [GPR-001]", "Weekly capacity plan [GPR-002]"]
requires: []
risk_level: low
---

# Overdue commitment recovery plan

## Purpose
Produce overdue commitment recovery plan that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Missed commitments** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Affected people** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Remaining work** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify what was promised and what remains incomplete.
3. Assess immediate consequences using known dependencies.
4. Choose a realistic revised scope or timing.
5. Draft an acknowledgment that states the miss and proposed repair.
6. Track the repair without making another unsupported promise.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the person actual commitments and constraints rather than an idealized day. Distinguish a desired outcome, a project, and the next action that can be performed. Keep external promises separate from private intentions, and avoid silently moving a commitment that affects someone else. A plan should show what will be deferred when capacity is insufficient. Treat a routine as an experiment with observable results, not a universal productivity law. Do not turn ordinary organization requests into psychological diagnoses or medical advice.



## Decision rules
- IF the new completion estimate is uncertain THEN offer a checkpoint rather than false certainty BECAUSE another missed promise compounds confusion.
- IF the commitment is no longer useful THEN ask whether to cancel or replace it BECAUSE completion for its own sake may waste effort.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Commitment | Current state | Repair proposal | Communication
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
- **Task-specific shortcut**: inventing a confident replacement deadline to reduce discomfort. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional user Ada missed a draft handoff and can provide an outline now but cannot confirm full completion.

**Output:**
```text
Scope: Prepare overdue commitment recovery plan for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Commitment | Current state | Repair proposal | Communication
Draft handoff | Incomplete | Offer outline and timing checkpoint | I missed the agreed handoff.
Next expectation | Full timing uncertain | Confirm after reviewing remaining work | I can share an outline now and update you after that review.

Artifact: Draft acknowledgment: I missed the agreed draft handoff. I can share an outline now, but I cannot yet confirm when the complete draft will be ready. I will review the remaining work and propose a checkpoint we can agree on. Would the outline still help, or has the need changed? Do not replace the uncertain estimate with a confident invented deadline.
Next action: The requester or assigned reviewer will complete this task-specific check: Track the repair without making another unsupported promise. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: I missed the agreed handoff..
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
> Fictional test request: Fictional user Ren asks for an apology that conceals the missed commitment.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
