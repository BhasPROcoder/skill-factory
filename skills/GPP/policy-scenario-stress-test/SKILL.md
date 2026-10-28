---
id: GPP-009
name: policy-scenario-stress-test
domain: Public Policy Analysis
subdomain: Analysis
version: 1.0
description: Prepare policy scenario stress test from supplied evidence; use when the request concerns proposed policy design.
triggers: ["policy scenario stress test", "prepare policy scenario stress test", "review my policy scenario stress test", "help me with policy scenario stress test", "turn proposed policy design into an actionable plan"]
not_for: ["Unrelated tasks that need different source material", "Taking external actions or submitting documents without authorization"]
requires: []
risk_level: medium
---

# Policy scenario stress test

## Purpose
Produce policy scenario stress test that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Proposed policy design** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Uncertain drivers** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Acceptable performance conditions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify uncertainties that can change implementation or outcomes.
3. Build internally consistent contrasting scenarios without assigning unsupported probabilities.
4. Trace how the policy behaves in each scenario.
5. Identify failure points and actions that remain useful across scenarios.
6. Define observable signals that would trigger a design review.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Keep descriptive evidence separate from value judgments about what public action should prioritize. State the geography, population, implementation stage, and source period before comparing options. Use current official publications for administrative facts and primary research for empirical claims, and preserve disagreement when the available evidence does not resolve it. Do not convert a stakeholder preference into a population statistic. A useful policy output names who experiences a benefit or burden, what mechanism connects the intervention to the outcome, and what evidence could contradict that mechanism.



## Decision rules
- IF a scenario is only a preferred forecast THEN add a plausible adverse condition BECAUSE stress testing requires exposure to failure.
- IF an action helps in all tested scenarios THEN consider it a robust candidate BECAUSE its value is less dependent on one prediction.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Scenario | Policy pressure | Failure signal | Adaptation
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
- **Task-specific shortcut**: treating scenario narratives as probability forecasts. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional program Meadowford depends on partner staffing and tests stable staffing against staff turnover.

**Output:**
```text
Scope: Prepare policy scenario stress test for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Scenario | Policy pressure | Failure signal | Adaptation
Stable staffing | Routine delivery | Service targets still need observation | Monitor baseline
Staff turnover | Training and handoff pressure | Unassigned cases | Prepare documented handoffs
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
> Fictional test request: Fictional planner Hugo supplies only an optimistic future and asks whether the policy is resilient.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
