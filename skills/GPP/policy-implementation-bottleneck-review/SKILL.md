---
id: GPP-005
name: policy-implementation-bottleneck-review
domain: Public Policy Analysis
subdomain: Analysis
version: 1.1
description: Prepare policy implementation bottleneck review from supplied evidence; use when the request concerns policy delivery process.
triggers: ["policy implementation bottleneck review", "prepare policy implementation bottleneck review", "review my policy implementation bottleneck review", "help me with policy implementation bottleneck review", "turn policy delivery process into an actionable plan"]
not_for: ["Policy indicator definition sheet [GPP-006]", "Public consultation response coding [GPP-007]"]
requires: []
risk_level: medium
---

# Policy implementation bottleneck review

## Purpose
Produce policy implementation bottleneck review that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Policy delivery process** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Observed delays** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Responsible actors** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Map the delivery sequence from eligibility intake to completed service.
3. Place observed queues or failures at specific handoffs.
4. Distinguish demand pressure from capacity, rework and unclear ownership.
5. Identify which constraints affect downstream throughput.
6. Propose a small diagnostic change with a measurable observation.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Keep descriptive evidence separate from value judgments about what public action should prioritize. State the geography, population, implementation stage, and source period before comparing options. Use current official publications for administrative facts and primary research for empirical claims, and preserve disagreement when the available evidence does not resolve it. Do not convert a stakeholder preference into a population statistic. A useful policy output names who experiences a benefit or burden, what mechanism connects the intervention to the outcome, and what evidence could contradict that mechanism.



## Decision rules
- IF the same work repeatedly returns upstream THEN investigate rework cause BECAUSE adding capacity alone may preserve the loop.
- IF delay evidence lacks timestamps THEN collect stage observations before assigning blame BECAUSE total duration does not identify the bottleneck.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Stage | Observed symptom | Possible constraint | Diagnostic action
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
- **Task-specific shortcut**: blaming the slowest visible office without tracing upstream rework. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional service Birchgate has applications returned repeatedly for unclear attachments. The fictional process log also shows that final processing starts late after attachment rework.

**Output:**
```text
Scope: Prepare policy implementation bottleneck review for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Stage | Observed symptom | Possible constraint | Diagnostic action
Intake review | Repeated returns | Instruction ambiguity possible | Inspect rejection reasons
Final processing | Late starts | Upstream rework dependency | Track arrival after corrections

Next action: The requester or assigned reviewer will complete this task-specific check: Propose a small diagnostic change with a measurable observation. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Inspect rejection reasons.
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
> Fictional test request: Fictional policy team sees long total turnaround but has no stage-level observations.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
