---
id: CTG-007
name: model-adaptation-intervention-diagnosis
domain: Applied AI Workflow Engineering
subdomain: Evaluation
version: 1.0
description: Produce model adaptation intervention diagnosis from representative failed tasks; use when this decision must be made from explicit evidence.
triggers: ["model adaptation intervention diagnosis", "help with model adaptation intervention diagnosis", "review my model adaptation intervention diagnosis", "prepare model adaptation intervention diagnosis", "check model adaptation intervention diagnosis"]
not_for: ["Investigate general model error slices [TML-006]", "Build an evaluation harness after selecting criteria [CTG-008]"]
requires: []
risk_level: medium
---

# Model adaptation intervention diagnosis

## Purpose
Produce a usable model adaptation intervention diagnosis from the supplied material, keeping observed behavior separate from a proposed design. The deliverable should let another practitioner identify the next decision and reproduce the evidence check without assuming an unavailable platform, tool, or permission.

## Inputs to collect
1. **Task material** — representative failed tasks; available source knowledge; current instructions and retrieval outputs; held-out evaluation cases; these determine whether the method applies. Default: unknown, with unsupported portions left provisional.
2. **Acceptance boundary** — the outcome the user needs, the permitted work, and any consequential constraints. Default: prepare a reviewable artifact from supplied evidence, with no external execution implied.
3. **Evidence provenance** — where observations came from, their version or date when relevant, and which checks actually ran. Default: supplied text only, not independent verification.
4. **Available environment** — supported tools, runtime, and source access when execution matters. Default: a portable plan and offline fixture, not a claim that integration exists.
If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue independent parts without filling the missing answer from memory.



## Procedure
1. Classify each failure by whether needed knowledge was absent, retrieval missed it, instructions were unclear, output structure failed, or task capability remained inadequate.
2. Test whether supplying the correct evidence and a clear task description resolves the failure before proposing training.
3. Choose the smallest plausible intervention for each diagnosed cause and specify what it cannot repair.
4. Compare the baseline and candidate on the same held-out task set while preserving source access and evaluation criteria.
5. Inspect remaining error slices and interactions instead of treating prompt changes, retrieval, and training as mutually exclusive.
6. Recommend a bounded next experiment with data rights, maintenance burden, latency, and deployment constraints made explicit.
7. ⚠️ Check each factual conclusion against the specific evidence inspected; label proposals and unexecuted checks instead of presenting a plausible plan as a result.
8. Produce the artifact in the output template and revise any item that fails the quality checklist.

Use this task prompt with the real inputs:
```text
Perform model adaptation intervention diagnosis for the supplied task material.
Keep the stated acceptance boundary and distinguish observations, proposed actions, and unresolved facts.
Return Scope, Evidence, Decision, Artifact, Verification, and Next action.
Do not invent missing measurements or imply that a proposed action was executed.
```

For any current provider feature, runtime interface, rate, or external requirement, check the current value in its official documentation and the actual configured environment. If access is unavailable, write `[VERIFY: the exact current requirement and its responsible official source]`. A general method does not guarantee a provider implements a feature or that a local environment supports it.

The following Python 3 standard-language fixture checks one narrow invariant in the fictional example. Save and run it with the available Python 3 interpreter, record the interpreter version actually used, and keep execution results separate from code merely shown in a document. It does not exercise a real model, user interface, or external system.
```python
observed = {'without_current_evidence': False, 'with_current_evidence': True}
assert observed['with_current_evidence'] and not observed['without_current_evidence']
conclusion = 'candidate retrieval repair, not universal diagnosis'
assert 'not universal' in conclusion
```

## Decision rules
- IF the answer depends on changing external knowledge THEN test a maintainable knowledge-access path BECAUSE training alone does not keep facts current.
- IF the correct supplied passage still produces a wrong answer THEN investigate reasoning or instruction failure BECAUSE retrieval success does not establish answer correctness.
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
- **Task-specific shortcut**: choosing adaptation from a fixed example-count threshold or a preferred model rather than a diagnosed failure. Fix: use the task-specific procedure and retain the missing evidence explicitly.
- **Universal threshold**: importing an arbitrary limit from another project. Fix: obtain the actual acceptance criterion and explain its scope.
- **Artifact substitution**: writing advice to create a deliverable instead of the deliverable. Fix: include the concrete fields, rules, or draft needed for this case.
- **Execution inflation**: describing a proposed test as successful. Fix: state the actual command or observation evidence, or mark it pending.

## Worked example
**Input:**
> Fictional team Elm asks about its changing internal policy. The model gives an old answer. When supplied the current policy paragraph in a controlled trial, it answers correctly. No training dataset or broader trial is supplied.

**Output:**
```text
Scope: Apply model adaptation intervention diagnosis to this fictional case only.
Evidence: The supplied fictional observations and constraints; no live system or current external rule has been independently checked.
Decision: Use the bounded result below and retain its explicitly stated unknowns.
Artifact: Diagnosis supported by this case: missing current evidence is a plausible cause. Candidate: improve retrieval of the authoritative current policy paragraph and preserve its version reference. Baseline comparison: original input versus the same task with verified current evidence. Limit: one successful evidence-supplied case does not prove all failures are retrieval failures. Next experiment: held-out policy questions with checked relevant passages and answer criteria; training remains undecided.
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
> Fictional team retrieves the correct source but produces malformed structured output and asks whether adding more documents will fix it. Diagnose the intervention and define a controlled comparison.

**Assertions:**
1. The answer follows the specified output labels in order and contains a concrete task artifact.
2. It applies the task-specific decision branches to the new case rather than repeating the worked example.
3. It preserves missing or conflicting evidence and does not claim an unexecuted check passed.
4. It gives a bounded next action whose completion can be observed.
