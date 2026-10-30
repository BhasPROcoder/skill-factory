---
id: CTG-009
name: local-inference-operating-envelope
domain: Applied AI Workflow Engineering
subdomain: Execution
version: 1.0
description: Produce local inference operating envelope from available hardware and runtime; use when this decision must be made from explicit evidence.
triggers: ["local inference operating envelope", "help with local inference operating envelope", "review my local inference operating envelope", "prepare local inference operating envelope", "check local inference operating envelope"]
not_for: ["Plan general service workload capacity tests [TDV-006]", "Account for inference expense [CTG-002]"]
requires: []
risk_level: medium
---

# Local inference operating envelope

## Purpose
Produce a usable local inference operating envelope from the supplied material, keeping observed behavior separate from a proposed design. The deliverable should let another practitioner identify the next decision and reproduce the evidence check without assuming an unavailable platform, tool, or permission.

## Inputs to collect
1. **Task material** — available hardware and runtime; model and precision configuration; target workload shapes; measured quality and latency requirements; these determine whether the method applies. Default: unknown, with unsupported portions left provisional.
2. **Acceptance boundary** — the outcome the user needs, the permitted work, and any consequential constraints. Default: prepare a reviewable artifact from supplied evidence, with no external execution implied.
3. **Evidence provenance** — where observations came from, their version or date when relevant, and which checks actually ran. Default: supplied text only, not independent verification.
4. **Available environment** — supported tools, runtime, and source access when execution matters. Default: a portable plan and offline fixture, not a claim that integration exists.
If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue independent parts without filling the missing answer from memory.



## Procedure
1. Record the actual available memory and competing resource use rather than relying on the hardware label alone.
2. Verify model, runtime, precision, and device compatibility against current official documentation before a trial.
3. Choose representative sequence lengths, batch sizes, and concurrency levels from the intended workload.
4. Change one workload dimension at a time and retain peak resource use, latency, errors, and output-quality observations.
5. Identify the largest tested acceptable region and distinguish interpolation, untested combinations, and observed failures.
6. Propose deployment limits and fallback behavior from measured evidence, with remeasurement triggers when the workload or runtime changes.
7. ⚠️ Check each factual conclusion against the specific evidence inspected; label proposals and unexecuted checks instead of presenting a plausible plan as a result.
8. Produce the artifact in the output template and revise any item that fails the quality checklist.

Use this task prompt with the real inputs:
```text
Perform local inference operating envelope for the supplied task material.
Keep the stated acceptance boundary and distinguish observations, proposed actions, and unresolved facts.
Return Scope, Evidence, Decision, Artifact, Verification, and Next action.
Do not invent missing measurements or imply that a proposed action was executed.
```

For any current provider feature, runtime interface, rate, or external requirement, check the current value in its official documentation and the actual configured environment. If access is unavailable, write `[VERIFY: the exact current requirement and its responsible official source]`. A general method does not guarantee a provider implements a feature or that a local environment supports it.

The following Python 3 standard-language fixture checks one narrow invariant in the fictional example. Save and run it with the available Python 3 interpreter, record the interpreter version actually used, and keep execution results separate from code merely shown in a document. It does not exercise a real model, user interface, or external system.
```python
trials = {'short_isolated': 'pass', 'long_concurrent': 'resource_error'}
allowed = {name for name, result in trials.items() if result == 'pass'}
assert allowed == {'short_isolated'}
assert 'long_isolated' not in trials
```

## Decision rules
- IF a short isolated request succeeds THEN do not infer concurrent long-request feasibility BECAUSE memory and latency depend on workload shape.
- IF a configuration fits memory but fails task quality THEN exclude it from the acceptable envelope BECAUSE resource feasibility alone does not satisfy the service requirement.
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
- **Task-specific shortcut**: promising that a model fits from parameter count alone or calling an untested configuration production-ready. Fix: use the task-specific procedure and retain the missing evidence explicitly.
- **Universal threshold**: importing an arbitrary limit from another project. Fix: obtain the actual acceptance criterion and explain its scope.
- **Artifact substitution**: writing advice to create a deliverable instead of the deliverable. Fix: include the concrete fields, rules, or draft needed for this case.
- **Execution inflation**: describing a proposed test as successful. Fix: state the actual command or observation evidence, or mark it pending.

## Worked example
**Input:**
> Fictional operator Sora tests a local runtime. Short isolated requests meet the supplied quality and latency criteria; long concurrent requests fail with a resource error. Exact memory quantities are not supplied and no intermediate combinations were tested.

**Output:**
```text
Scope: Apply local inference operating envelope to this fictional case only.
Evidence: The supplied fictional observations and constraints; no live system or current external rule has been independently checked.
Decision: Use the bounded result below and retain its explicitly stated unknowns.
Artifact: Tested acceptable region: short isolated requests only. Observed failure region: long concurrent requests. Unknown: long isolated and short concurrent combinations. Proposed initial limit: admit only the tested short isolated workload until additional controlled trials establish broader capacity. Fallback: queue or reject outside-envelope requests according to the agreed service contract; no unsupported promise that cache clearing fixes the error.
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
> Fictional operator tests one short prompt successfully, then asks to enable long prompts with several simultaneous users. Define the missing trials and a bounded current envelope.

**Assertions:**
1. The answer follows the specified output labels in order and contains a concrete task artifact.
2. It applies the task-specific decision branches to the new case rather than repeating the worked example.
3. It preserves missing or conflicting evidence and does not claim an unexecuted check passed.
4. It gives a bounded next action whose completion can be observed.
