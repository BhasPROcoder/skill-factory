---
id: GPR-002
name: weekly-capacity-planning
domain: Personal Work Organization
subdomain: Analysis
version: 1.1
description: Prepare weekly capacity plan from supplied evidence; use when the request concerns fixed commitments.
triggers: ["weekly capacity plan", "prepare weekly capacity plan", "review my weekly capacity plan", "help me with weekly capacity plan", "turn fixed commitments into an actionable plan"]
not_for: ["Project next-action decomposition [GPR-003]", "Personal priority tradeoff [GPR-004]"]
requires: []
risk_level: low
---

# Weekly capacity plan

## Purpose
Produce weekly capacity plan that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Fixed commitments** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Task estimates** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Priority outcomes** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Place fixed commitments on the actual personal calendar before assigning discretionary work.
3. Identify free blocks and the attention or energy conditions each can realistically support.
4. Match a bounded task output to a suitable block without overlapping its time.
5. Leave carryover or interruption space based on the person observed availability.
6. Remove or renegotiate tasks that have no feasible placement and review the next calendar against actual completion.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the person actual commitments and constraints rather than an idealized day. Distinguish a desired outcome, a project, and the next action that can be performed. Keep external promises separate from private intentions, and avoid silently moving a commitment that affects someone else. A plan should show what will be deferred when capacity is insufficient. Treat a routine as an experiment with observable results, not a universal productivity law. Do not turn ordinary organization requests into psychological diagnoses or medical advice.



## Decision rules
- IF workload exceeds capacity THEN make a deferral or scope tradeoff BECAUSE a longer list does not increase available time.
- IF estimates are consistently wrong THEN revise them from actual records BECAUSE planning should learn from experience.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Commitment | Capacity effect | Planned handling | Tradeoff
<one row per finding; each cell one concise sentence>

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
- **Task-specific shortcut**: allocating the same hour to several priorities. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional user Rina has a fixed meeting during the only block originally assigned to drafting.

**Output:**
```text
Scope: Prepare weekly capacity plan for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Commitment | Capacity effect | Planned handling | Tradeoff
Fixed meeting | Consumes drafting block | Keep actual commitment | Move or reduce drafting
Drafting | Uninterrupted work requested | Find an actual free block before scheduling | Reduce scope if none exists

Next action: The requester or assigned reviewer will complete this task-specific check: Remove or renegotiate tasks that have no feasible placement and review the next calendar against actual completion. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Move or reduce drafting.
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
> Fictional test request: Fictional user Noel asks for a weekly plan that fits more work than the supplied available time.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
