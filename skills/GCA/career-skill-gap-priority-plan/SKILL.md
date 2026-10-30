---
id: GCA-006
name: career-skill-gap-priority-plan
domain: Career Development
subdomain: Analysis
version: 1.1
description: Prepare career skill gap priority plan from supplied evidence; use when the request concerns target work tasks.
triggers: ["career skill gap priority plan", "prepare career skill gap priority plan", "review my career skill gap priority plan", "help me with career skill gap priority plan", "turn target work tasks into an actionable plan"]
not_for: ["Portfolio case study draft [GCA-007]", "Informational interview agenda [GCA-008]"]
requires: []
risk_level: low
---

# Career skill gap priority plan

## Purpose
Produce career skill gap priority plan that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Target work tasks** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Current capability evidence** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Learning resources and time** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Translate the target role into concrete tasks.
3. Compare current independent performance against those tasks.
4. Separate missing knowledge from lack of practice or missing evidence.
5. Prioritize gaps that block several important tasks.
6. Define a small demonstration that would show progress on each gap.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the person actual experience as the source of claims. Do not invent credentials, employers, outcomes, dates or performance numbers to make an application sound stronger. Distinguish a draft statement from a verified accomplishment, and retain placeholders where the person must confirm details. Current job requirements, hiring processes and platform features should be checked against the employer or platform official material. A career document can present relevant strengths without promising an interview or offer. Drafting outreach does not authorize sending it or sharing the person information.



## Decision rules
- IF the gap is only a missing credential THEN check whether the task actually requires it BECAUSE credential acquisition and capability development are different decisions.
- IF a skill is already present but undocumented THEN create evidence rather than unnecessary retraining BECAUSE the gap may be visibility.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Target task | Current evidence | Gap type | Demonstration
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
- **Task-specific shortcut**: buying a course for every keyword in a job advertisement. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional candidate Ria can organize project notes but has no example showing prioritization under constraints.

**Output:**
```text
Scope: Prepare career skill gap priority plan for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Target task | Current evidence | Gap type | Demonstration
Documentation | Existing work sample | Evidence available | Refine sample
Prioritization | No demonstrated tradeoff | Practice and evidence gap | Produce a constrained task plan

Next action: The requester or assigned reviewer will complete this task-specific check: Define a small demonstration that would show progress on each gap. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Refine sample.
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
> Fictional test request: Fictional candidate Eli lists many tools but cannot identify which work tasks the target role requires.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
