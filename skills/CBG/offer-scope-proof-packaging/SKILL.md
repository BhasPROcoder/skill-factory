---
id: CBG-015
name: offer-scope-proof-packaging
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare offer scope and proof packaging from supplied evidence; use when the request concerns intended customer outcome.
triggers: ["offer scope and proof packaging", "prepare offer scope and proof packaging", "review my offer scope and proof packaging", "help me with offer scope and proof packaging", "turn intended customer outcome into an actionable plan"]
not_for: ["Meeting behavior evidence review [CBG-001]", "Regional market access fit [CBG-002]"]
requires: []
risk_level: medium
---

# Offer scope and proof packaging

## Purpose
Produce offer scope and proof packaging that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Intended customer outcome** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Delivery capacity and exclusions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Available proof and commercial constraints** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Translate the requested outcome into a deliverable the provider can actually control.
3. Specify customer responsibilities and prerequisites that affect delivery.
4. Separate supported benefits from unproven outcome promises.
5. Build coherent scope options whose differences are operationally meaningful.
6. Write a clear next action and a method for testing comprehension and fit.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF the desired outcome depends on customer behavior THEN state the dependency BECAUSE a deliverable does not guarantee that outcome.
- IF proof is absent THEN use a bounded proposal rather than invented results BECAUSE confidence language cannot replace evidence.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Offer element | Supported scope | Dependency | Claim boundary
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
- **Task-specific shortcut**: inventing a refund guarantee or minimum price because a template recommends one. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional studio Juniper can map an invoicing workflow and deliver a prioritized change brief. It has no measured savings result and cannot implement changes within this engagement.

**Output:**
```text
Scope: Prepare offer scope and proof packaging for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Offer element | Supported scope | Dependency | Claim boundary
Deliverable | Workflow map and change brief | Access to process notes | No implementation included
Benefit | Clarify improvement options | Customer review | No guaranteed savings

Artifact: Offer draft: We will map your current invoicing workflow from supplied notes and interviews, then deliver a prioritized change brief explaining the evidence and dependencies behind each option. Implementation and guaranteed savings are outside this scope. You provide access to relevant process information and a reviewer for factual corrections. Next step: confirm the workflow boundary and available inputs before preparing an agreed quote.
Next action: The requester or assigned reviewer will complete this task-specific check: Write a clear next action and a method for testing comprehension and fit. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: No implementation included.
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
> Fictional test request: Fictional provider asks for a savings promise without measurement or control over implementation.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
