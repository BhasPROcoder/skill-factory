---
id: CTG-002
name: inference-action-cost-accounting
domain: Applied AI Workflow Engineering
subdomain: Execution
version: 1.0
description: Produce inference action cost accounting from billable usage records; use when this decision must be made from explicit evidence.
triggers: ["inference action cost accounting", "help with inference action cost accounting", "review my inference action cost accounting", "prepare inference action cost accounting", "check inference action cost accounting"]
not_for: ["Evaluate model quality before promotion [TML-010]", "Measure local inference feasibility [CTG-009]"]
requires: []
risk_level: high
---

# Inference action cost accounting

## Purpose
Produce a usable inference action cost accounting from the supplied material, keeping observed behavior separate from a proposed design. The deliverable should let another practitioner identify the next decision and reproduce the evidence check without assuming an unavailable platform, tool, or permission.

## Inputs to collect
1. **Task material** — billable usage records; current rate definitions and units; action-to-request mapping; quality and latency constraints; these determine whether the method applies. Default: unknown, with unsupported portions left provisional.
2. **Acceptance boundary** — the outcome the user needs, the permitted work, and any consequential constraints. Default: prepare a reviewable artifact from supplied evidence, with no external execution implied.
3. **Evidence provenance** — where observations came from, their version or date when relevant, and which checks actually ran. Default: supplied text only, not independent verification.
4. **Available environment** — supported tools, runtime, and source access when execution matters. Default: a portable plan and offline fixture, not a claim that integration exists.
If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue independent parts without filling the missing answer from memory.

Collect jurisdiction and accounting context before any tax, reporting, or legal interpretation; there is no silent jurisdiction default. Knowledge has a cutoff: verify current billing and applicable rules with official provider documentation and the responsible authority. Refer consequential tax or accounting treatment to a licensed professional in the relevant jurisdiction. This skill provides operational expense allocation, not financial advice or a tax determination.

## Procedure
1. Define the completed user action being costed and retain failed or abandoned attempts in its allocation rule.
2. Map each request, retry, retrieval operation, and local resource charge to the action without counting a shared charge twice.
3. Normalize recorded usage and current verified rates to compatible units, keeping unknown charges explicit.
4. Separate directly variable expense from shared capacity allocation and document the chosen allocation basis.
5. Calculate observed cost per completed action and compare alternatives only over comparable task quality, latency, and workload.
6. Reconcile the calculated line items against available billing evidence and explain residual differences before projecting a larger workload.
7. ⚠️ Check each factual conclusion against the specific evidence inspected; label proposals and unexecuted checks instead of presenting a plausible plan as a result.
8. Produce the artifact in the output template and revise any item that fails the quality checklist.

Use this task prompt with the real inputs:
```text
Perform inference action cost accounting for the supplied task material.
Keep the stated acceptance boundary and distinguish observations, proposed actions, and unresolved facts.
Return Scope, Evidence, Decision, Artifact, Verification, and Next action.
Do not invent missing measurements or imply that a proposed action was executed.
```

For any current provider feature, runtime interface, rate, or external requirement, check the current value in its official documentation and the actual configured environment. If access is unavailable, write `[VERIFY: the exact current requirement and its responsible official source]`. A general method does not guarantee a provider implements a feature or that a local environment supports it.

The following Python 3 standard-language fixture checks one narrow invariant in the fictional example. Save and run it with the available Python 3 interpreter, record the interpreter version actually used, and keep execution results separate from code merely shown in a document. It does not exercise a real model, user interface, or external system.
```python
charges = {'success': 2, 'failed_retry': 1, 'retrieval': 1}
completed = 1
assert sum(charges.values()) / completed == 4
```

## Decision rules
- IF a request fails but is billed THEN include its measured expense in the stated allocation BECAUSE success-only accounting understates the delivered-action cost.
- IF an alternative is cheaper but misses the quality constraint THEN exclude it from equivalent-service savings BECAUSE a different service level is not a like-for-like saving.
- IF evidence from different versions conflicts THEN preserve the conflict and identify the relevant version BECAUSE combining incompatible observations can produce a false conclusion.
- IF a necessary verification cannot run THEN keep the dependent status provisional BECAUSE an absent check is neither a pass nor a demonstrated failure.

## Output template
```text
Scope: <one sentence naming the decision and boundaries>
Evidence: <up to four inspected inputs and their limits>
Decision: <supported choice or explicit provisional status>
Artifact: <the actual task-specific contract, ledger, protocol, or composition; not a promise to create it>
Verification: <executed checks and results; separately list pending checks>
Next action: <responsible role, one startable action, and observable completion evidence>
```
Keep the first response within the task's useful review size: summarize repeated evidence and retain source references rather than copying an entire log. Include enough artifact detail to act without guessing a critical condition. If additional evidence is needed, state which decision it could change.

## Quality checklist
- [ ] The scope matches the user's decision rather than the source author's original personal situation.
- [ ] The artifact contains concrete states, fields, criteria, or actions appropriate to this task.
- [ ] Every observed fact is traceable to an inspected input.
- [ ] Proposed changes and pending checks are visibly distinguished from executed work.
- [ ] Each task-specific conditional branch was considered.
- [ ] Changing external facts have a current official source check or remain unresolved.
- [ ] Arithmetic and fixture assertions have been checked before reporting a result.
- [ ] The next action names a role and observable completion evidence without expanding authorization.

## Anti-patterns
- **Task-specific shortcut**: calling local inference free because there is no per-request vendor invoice. Fix: use the task-specific procedure and retain the missing evidence explicitly.
- **Universal threshold**: importing an arbitrary limit from another project. Fix: obtain the actual acceptance criterion and explain its scope.
- **Artifact substitution**: writing advice to create a deliverable instead of the deliverable. Fix: include the concrete fields, rules, or draft needed for this case.
- **Execution inflation**: describing a proposed test as successful. Fix: state the actual command or observation evidence, or mark it pending.

## Worked example
**Input:**
> Fictional project Cedar records two requests for one completed action. Its fictional billing sheet charges 2 cost units for the successful request and 1 cost unit for a failed retry. A retrieval operation costs 1 cost unit. There are no shared charges in this fixture; these are invented accounting units, not vendor prices.

**Output:**
```text
Scope: Apply inference action cost accounting to this fictional case only.
Evidence: The supplied fictional observations and constraints; no live system or current external rule has been independently checked.
Decision: Use the bounded result below and retain its explicitly stated unknowns.
Artifact: Action Cedar-A: successful request 2 units; failed retry 1 unit; retrieval 1 unit. Observed allocated expense: 4 units for one completed action. No shared-capacity expense is claimed. Current real rates, tax treatment, currency conversion, future workload mix, and any cache billing remain unverified. Compare another route only after establishing equivalent acceptable outcomes.
Verification: The supplied observations support this provisional artifact. The offline fixture can check its narrow invariant; real integration and any unprovided measurements remain pending.
Next action: The responsible practitioner reviews the artifact against the named missing evidence, performs the pending task-specific check, and retains the resulting output before changing its status.
```

**Bad output:**
> Everything is ready. Apply the same configuration everywhere; no further evidence is needed.

This fails because it erases the case's unresolved conditions, replaces a bounded result with a universal claim, and implies verification that did not occur.

## Edge cases
- **Only a summary is available**: identify which conclusion relies on the summary and request the original excerpt if its wording changes the decision.
- **A proposed action exceeds authority**: finish the reviewable artifact and leave that action unexecuted until the required authorization exists.
- **The environment changes after a check**: retain the old result with its configuration and rerun only checks affected by the changed condition.
- **Evidence is too sparse for comparison**: state the smaller supported conclusion and name a discriminating next observation rather than ranking unsupported options.

## Test case
**Input:**
> Fictional project compares a cheap route with frequent failed retries against a more expensive successful route, but provides no failed-request usage. Produce a provisional comparison without inventing savings.

**Assertions:**
1. The answer follows the specified output labels in order and contains a concrete task artifact.
2. It applies the task-specific decision branches to the new case rather than repeating the worked example.
3. It preserves missing or conflicting evidence and does not claim an unexecuted check passed.
4. It gives a bounded next action whose completion can be observed.
