---
id: CBG-010
name: initiative-continuation-gate
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare initiative continuation gate from supplied evidence; use when the request concerns initiative evidence and original hypothesis.
triggers: ["initiative continuation gate", "prepare initiative continuation gate", "review my initiative continuation gate", "help me with initiative continuation gate", "turn initiative evidence and original hypothesis into an actionable plan"]
not_for: ["Bottom-up market sizing ledger [CBG-011]", "Primary metric guardrail design [CBG-012]"]
requires: []
risk_level: medium
---

# Initiative continuation gate

## Purpose
Produce initiative continuation gate that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Initiative evidence and original hypothesis** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Future resource needs** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Outstanding obligations** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Restate the outcome the initiative was intended to test or deliver.
3. Separate past expenditure from future costs and avoid treating effort as proof of value.
4. Compare continue, reduce, pause and stop options using evidence and reversible consequences.
5. Check obligations and dependencies that constrain a transition.
6. Record a conditional decision with a review trigger and transition owner.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF sunk effort is the main reason to continue THEN evaluate future value and obligations separately BECAUSE past cost cannot be recovered by repeating it.
- IF stopping would strand commitments THEN plan an authorized transition BECAUSE a strategic preference does not cancel obligations.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Option | Evidence basis | Dependency | Gate
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
- **Task-specific shortcut**: using a universal score cutoff to terminate every initiative. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional team Alder has a pilot with no repeat use in the observed period and one promised participant handoff still pending. Future demand is uncertain.

**Output:**
```text
Scope: Prepare initiative continuation gate for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Option | Evidence basis | Dependency | Gate
Pause expansion | Repeat use absent in supplied period | Complete promised handoff | Revisit with new demand evidence
Continue unchanged | No new support supplied | Requires additional effort | Not justified by past effort alone

Artifact: Decision draft: Pause expansion while completing the promised handoff. Do not infer permanent lack of demand from the observed period alone. The owner should record remaining obligations, preserve reusable artifacts, and define what new demand evidence would reopen expansion. No cancellation, notification, data deletion or spending change is authorized by this review alone.
Next action: The requester or assigned reviewer will complete this task-specific check: Record a conditional decision with a review trigger and transition owner. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Revisit with new demand evidence.
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
> Fictional test request: Fictional team wants to cancel an initiative immediately because a generic scorecard says so despite unresolved commitments.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
