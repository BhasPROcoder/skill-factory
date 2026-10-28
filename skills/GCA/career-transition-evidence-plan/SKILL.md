---
id: GCA-010
name: career-transition-evidence-plan
domain: Career Development
subdomain: Analysis
version: 1.0
description: Prepare career transition evidence plan from supplied evidence; use when the request concerns current work history.
triggers: ["career transition evidence plan", "prepare career transition evidence plan", "review my career transition evidence plan", "help me with career transition evidence plan", "turn current work history into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: low
---

# Career transition evidence plan

## Purpose
Produce career transition evidence plan that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Current work history** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Target work tasks** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Constraints on transition** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify capabilities shared between current and target work.
3. State where the target context changes the required judgment.
4. Choose a bounded project or practice task that reveals the missing capability.
5. Plan how to describe transferable experience without relabeling it inaccurately.
6. Define a review point based on completed evidence rather than optimism.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the person actual experience as the source of claims. Do not invent credentials, employers, outcomes, dates or performance numbers to make an application sound stronger. Distinguish a draft statement from a verified accomplishment, and retain placeholders where the person must confirm details. Current job requirements, hiring processes and platform features should be checked against the employer or platform official material. A career document can present relevant strengths without promising an interview or offer. Drafting outreach does not authorize sending it or sharing the person information.



## Decision rules
- IF a transition requires regulated credentials THEN check current official requirements BECAUSE transferable skill does not replace formal eligibility.
- IF the project only repeats current strengths THEN add the target-context challenge BECAUSE evidence should test the actual gap.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Transfer element | Existing evidence | Target difference | Next demonstration
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
- **Task-specific shortcut**: claiming the new job title before demonstrating its task demands. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional candidate Lina moves from event coordination toward service operations.

**Output:**
```text
Scope: Prepare career transition evidence plan for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Transfer element | Existing evidence | Target difference | Next demonstration
Scheduling | Event schedule experience | Ongoing service dependencies | Create recurring handoff plan
Issue handling | Event exception notes | Repeated-case learning | Analyze recurring causes
Next action: The requester supplies the unresolved evidence and confirms the proposed next step before implementation.
Unresolved: Which missing source or observation would change the provisional conclusion?
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
> Fictional test request: Fictional candidate Theo wants to rename past duties to look like a role never held.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
