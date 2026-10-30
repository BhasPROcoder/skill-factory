---
id: CTG-003
name: software-continuation-state-reconciliation
domain: Applied AI Workflow Engineering
subdomain: Delivery
version: 1.0
description: Produce software continuation state reconciliation from current repository or working files; use when this decision must be made from explicit evidence.
triggers: ["software continuation state reconciliation", "help with software continuation state reconciliation", "review my software continuation state reconciliation", "prepare software continuation state reconciliation", "check software continuation state reconciliation"]
not_for: ["Prepare an initial business execution plan [BPL-001]", "Compact conversational context without changing code [CTG-005]"]
requires: []
risk_level: medium
---

# Software continuation state reconciliation

## Purpose
Produce a usable software continuation state reconciliation from the supplied material, keeping observed behavior separate from a proposed design. The deliverable should let another practitioner identify the next decision and reproduce the evidence check without assuming an unavailable platform, tool, or permission.

## Inputs to collect
1. **Task material** — current repository or working files; prior handoff and task objective; test evidence; authorized change boundary; these determine whether the method applies. Default: unknown, with unsupported portions left provisional.
2. **Acceptance boundary** — the outcome the user needs, the permitted work, and any consequential constraints. Default: prepare a reviewable artifact from supplied evidence, with no external execution implied.
3. **Evidence provenance** — where observations came from, their version or date when relevant, and which checks actually ran. Default: supplied text only, not independent verification.
4. **Available environment** — supported tools, runtime, and source access when execution matters. Default: a portable plan and offline fixture, not a claim that integration exists.
If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue independent parts without filling the missing answer from memory.



## Procedure
1. Extract the intended outcome and acceptance conditions from the user request without treating an old progress note as current truth.
2. Inspect the relevant current files, change status, and repository instructions before proposing the next edit.
3. Compare each handoff claim against an observable artifact and classify it as confirmed, contradicted, pending, or no longer relevant.
4. Identify the smallest bounded change that advances an unmet acceptance condition while preserving unrelated work.
5. Run the verification appropriate to that change and distinguish executed checks from planned checks.
6. Write a continuation ledger with remaining work, concrete file references, unresolved decisions, and the next startable action.
7. ⚠️ Check each factual conclusion against the specific evidence inspected; label proposals and unexecuted checks instead of presenting a plausible plan as a result.
8. Produce the artifact in the output template and revise any item that fails the quality checklist.

Use this task prompt with the real inputs:
```text
Perform software continuation state reconciliation for the supplied task material.
Keep the stated acceptance boundary and distinguish observations, proposed actions, and unresolved facts.
Return Scope, Evidence, Decision, Artifact, Verification, and Next action.
Do not invent missing measurements or imply that a proposed action was executed.
```

For any current provider feature, runtime interface, rate, or external requirement, check the current value in its official documentation and the actual configured environment. If access is unavailable, write `[VERIFY: the exact current requirement and its responsible official source]`. A general method does not guarantee a provider implements a feature or that a local environment supports it.

The following Python 3 standard-language fixture checks one narrow invariant in the fictional example. Save and run it with the available Python 3 interpreter, record the interpreter version actually used, and keep execution results separate from code merely shown in a document. It does not exercise a real model, user interface, or external system.
```python
claims = {'empty_check': 'confirmed', 'all_validation': 'contradicted'}
ready = all(value == 'confirmed' for value in claims.values())
assert not ready
```

## Decision rules
- IF the handoff says a test passed but no result or current run supports it THEN mark the assertion unverified BECAUSE a narrative is not execution evidence.
- IF current edits conflict with the proposed next step THEN reconcile their purpose first BECAUSE resuming should not silently overwrite another contributor.
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
- **Task-specific shortcut**: continuing from a stale checklist without inspecting the actual working tree. Fix: use the task-specific procedure and retain the missing evidence explicitly.
- **Universal threshold**: importing an arbitrary limit from another project. Fix: obtain the actual acceptance criterion and explain its scope.
- **Artifact substitution**: writing advice to create a deliverable instead of the deliverable. Fix: include the concrete fields, rules, or draft needed for this case.
- **Execution inflation**: describing a proposed test as successful. Fix: state the actual command or observation evidence, or mark it pending.

## Worked example
**Input:**
> Fictional maintainer Mina resumes a form fix. The handoff says validation is complete, but the current form file contains only an empty-field check and the supplied test output reports a malformed-address failure. The authorized scope is form validation; no deployment is requested.

**Output:**
```text
Scope: Apply software continuation state reconciliation to this fictional case only.
Evidence: The supplied fictional observations and constraints; no live system or current external rule has been independently checked.
Decision: Use the bounded result below and retain its explicitly stated unknowns.
Artifact: Objective: reject malformed addresses as well as empty fields. Confirmed: empty-field branch exists. Contradicted: the supplied failing test does not support validation-complete status. Next bounded change: implement the missing address-condition branch in the form validator and rerun the failing case plus the existing empty-field check. Deployment: outside this task. Handoff: retain the failing-test reference until new execution evidence replaces it.
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
> Fictional developer resumes a task whose handoff says merged, while the current branch still contains an uncommitted implementation and no merge evidence. Reconcile state before choosing an action.

**Assertions:**
1. The answer follows the specified output labels in order and contains a concrete task artifact.
2. It applies the task-specific decision branches to the new case rather than repeating the worked example.
3. It preserves missing or conflicting evidence and does not claim an unexecuted check passed.
4. It gives a bounded next action whose completion can be observed.
