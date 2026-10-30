---
id: CBG-011
name: bottom-up-market-sizing-ledger
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare bottom-up market sizing ledger from supplied evidence; use when the request concerns defined customer unit and territory.
triggers: ["bottom-up market sizing ledger", "prepare bottom-up market sizing ledger", "review my bottom-up market sizing ledger", "help me with bottom-up market sizing ledger", "turn defined customer unit and territory into an actionable plan"]
not_for: ["Primary metric guardrail design [CBG-012]", "Source-grounded daily brief [CBG-013]"]
requires: []
risk_level: medium
---

# Bottom-up market sizing ledger

## Purpose
Produce bottom-up market sizing ledger that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Defined customer unit and territory** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Count sources and overlap assumptions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Purchase frequency and price assumptions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Define who counts as an eligible buying unit and distinguish users from payers.
3. Build a count from traceable segments while removing overlap.
4. Separate observed counts from eligibility, reach and conversion assumptions.
5. Compute scenarios with consistent time units and distinguish potential spend from obtainable revenue.
6. Identify which uncertain input most changes the decision and how to verify it.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF segments overlap THEN deduplicate or state a bound BECAUSE adding them would count some buyers twice.
- IF purchase frequency is unknown THEN show separate scenarios BECAUSE a single annual total would conceal the assumption.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Component | Fictional input | Calculation | Limit
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
- **Task-specific shortcut**: presenting total potential spending as revenue the business will capture. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional planner Nia supplies two disjoint buyer groups of40 and60 organizations, an assumed10 units of currency per purchase and one purchase per year. These are invented planning assumptions, not market data.

**Output:**
```text
Scope: Prepare bottom-up market sizing ledger for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Component | Fictional input | Calculation | Limit
Buyer count | 40plus60 | 100 organizations | Disjoint only by premise
Annual potential | 100times10times1 | 1000 currency units | Not forecast sales

Artifact: Sizing ledger: eligible organizations=40+60=100. Assumed annual spend per organization=10×1=10 currency units. Illustrative annual potential=100×10=1000 currency units. At two purchases per year the same assumptions give2000, illustrating frequency sensitivity. Obtain actual count provenance, eligibility and purchase evidence before using this outside the fictional exercise. No market-share forecast is supplied.
Next action: The requester or assigned reviewer will complete this task-specific check: Identify which uncertain input most changes the decision and how to verify it. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Disjoint only by premise.
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
> Fictional test request: Fictional planner supplies overlapping segments and asks for a precise market total without deduplication.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
