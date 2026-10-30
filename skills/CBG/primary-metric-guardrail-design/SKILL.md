---
id: CBG-012
name: primary-metric-guardrail-design
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare primary metric guardrail design from supplied evidence; use when the request concerns user value hypothesis.
triggers: ["primary metric guardrail design", "prepare primary metric guardrail design", "review my primary metric guardrail design", "help me with primary metric guardrail design", "turn user value hypothesis into an actionable plan"]
not_for: ["Source-grounded daily brief [CBG-013]", "Negotiation package trade design [CBG-014]"]
requires: []
risk_level: medium
---

# Primary metric guardrail design

## Purpose
Produce primary metric guardrail design that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **User value hypothesis** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Candidate measures and definitions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Possible gaming and adverse outcomes** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. State the user outcome the primary metric is meant to represent.
3. Compare candidates for directness, observability and controllability.
4. Identify behaviors that could increase each candidate while harming the intended outcome.
5. Pair the selected metric with explicit quality or harm guardrails.
6. Define a review that tests the metric interpretation against real user outcomes.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF a metric rises while guardrails worsen THEN investigate the tradeoff BECAUSE growth in one number is not overall success.
- IF the relation to user value is only assumed THEN state a hypothesis and validation plan BECAUSE a metric name does not prove predictive validity.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Candidate | Value link | Failure mode | Guardrail
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
- **Task-specific shortcut**: claiming one number reliably predicts every business outcome. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional service Cedar tracks closed requests. Staff can close requests before users confirm resolution, and the team wants genuine resolution rather than faster closure alone.

**Output:**
```text
Scope: Prepare primary metric guardrail design for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Candidate | Value link | Failure mode | Guardrail
Closed requests | Operational throughput | Premature closure | Reopened or unresolved cases
Verified resolution | Closer to intended value | Confirmation may be missing | Report response coverage

Artifact: Metric proposal: Count requests with recorded resolution evidence within the chosen reporting window. Define what qualifies as evidence and report missing confirmation separately. Guardrails: unresolved/reopened cases and confirmation coverage. Review sampled cases to test whether the metric reflects actual resolution. Do not invent a target or claim this measure predicts revenue without evidence.
Next action: The requester or assigned reviewer will complete this task-specific check: Define a review that tests the metric interpretation against real user outcomes. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Reopened or unresolved cases.
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
> Fictional test request: Fictional team wants to reward higher completion counts despite evidence of repeated reopenings.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
