---
id: CTG-008
name: language-model-evaluation-harness
domain: Applied AI Workflow Engineering
subdomain: Evaluation
version: 1.0
description: Produce language model evaluation harness from task distribution and risk slices; use when this decision must be made from explicit evidence.
triggers: ["language model evaluation harness", "help with language model evaluation harness", "review my language model evaluation harness", "prepare language model evaluation harness", "check language model evaluation harness"]
not_for: ["Design tests for a reusable skill rather than model configurations [SKR-003]", "Compare ordinary model baselines [TML-002]"]
requires: []
risk_level: medium
---

# Language model evaluation harness

## Purpose
Produce a usable language model evaluation harness from the supplied material, keeping observed behavior separate from a proposed design. The deliverable should let another practitioner identify the next decision and reproduce the evidence check without assuming an unavailable platform, tool, or permission.

## Inputs to collect
1. **Task material** — task distribution and risk slices; baseline and candidate outputs; deterministic constraints; grounded judging rubric and adjudication process; these determine whether the method applies. Default: unknown, with unsupported portions left provisional.
2. **Acceptance boundary** — the outcome the user needs, the permitted work, and any consequential constraints. Default: prepare a reviewable artifact from supplied evidence, with no external execution implied.
3. **Evidence provenance** — where observations came from, their version or date when relevant, and which checks actually ran. Default: supplied text only, not independent verification.
4. **Available environment** — supported tools, runtime, and source access when execution matters. Default: a portable plan and offline fixture, not a claim that integration exists.
If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue independent parts without filling the missing answer from memory.



## Procedure
1. Freeze task identifiers, input versions, source evidence, and acceptance criteria before comparing candidates.
2. Separate deterministic checks from grounded qualitative judgments and assign each criterion an appropriate evaluator.
3. Calibrate qualitative judging on examples with human-reviewed reasoning and expose disagreement rather than hiding it in a mean.
4. Run comparable baseline and candidate cases with retained configuration and repeated trials when variability matters.
5. Report results by failure slice as well as aggregate outcome, preserving invalid runs and missing observations.
6. Make promotion depend on the user-defined constraints and unresolved regressions rather than a universal score cutoff.
7. ⚠️ Check each factual conclusion against the specific evidence inspected; label proposals and unexecuted checks instead of presenting a plausible plan as a result.
8. Produce the artifact in the output template and revise any item that fails the quality checklist.

Use this task prompt with the real inputs:
```text
Perform language model evaluation harness for the supplied task material.
Keep the stated acceptance boundary and distinguish observations, proposed actions, and unresolved facts.
Return Scope, Evidence, Decision, Artifact, Verification, and Next action.
Do not invent missing measurements or imply that a proposed action was executed.
```

For any current provider feature, runtime interface, rate, or external requirement, check the current value in its official documentation and the actual configured environment. If access is unavailable, write `[VERIFY: the exact current requirement and its responsible official source]`. A general method does not guarantee a provider implements a feature or that a local environment supports it.

The following Python 3 standard-language fixture checks one narrow invariant in the fictional example. Save and run it with the available Python 3 interpreter, record the interpreter version actually used, and keep execution results separate from code merely shown in a document. It does not exercise a real model, user interface, or external system.
```python
cases = {'A': {'structure': False, 'grounding': True}, 'B': {'structure': True, 'grounding': False}}
passed = {name: all(checks.values()) for name, checks in cases.items()}
assert passed == {'A': False, 'B': False}
```

## Decision rules
- IF a judge rewards a confident unsupported answer THEN repair the evidence criterion and rejudge affected cases BECAUSE fluency is not correctness.
- IF an aggregate improves while a critical slice regresses THEN surface that regression before promotion BECAUSE averages can hide an unacceptable failure mode.
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
- **Task-specific shortcut**: treating a model judge as an unquestionable oracle or replacing semantic correctness with expected keywords. Fix: use the task-specific procedure and retain the missing evidence explicitly.
- **Universal threshold**: importing an arbitrary limit from another project. Fix: obtain the actual acceptance criterion and explain its scope.
- **Artifact substitution**: writing advice to create a deliverable instead of the deliverable. Fix: include the concrete fields, rules, or draft needed for this case.
- **Execution inflation**: describing a proposed test as successful. Fix: state the actual command or observation evidence, or mark it pending.

## Worked example
**Input:**
> Fictional team Alder evaluates two responses to a source-bounded question. Every factual claim in response A is supported by the supplied evidence, but A has an invalid required field. Response B satisfies the supplied structural requirements but invents a fact. The team requires both valid structure and grounded content; no output satisfies both.

**Output:**
```text
Scope: Apply language model evaluation harness to this fictional case only.
Evidence: The supplied fictional observations and constraints; no live system or current external rule has been independently checked.
Decision: Use the bounded result below and retain its explicitly stated unknowns.
Artifact: Case ledger: A structure fail, grounding pass, overall fail. B structure pass, grounding fail, overall fail. Deterministic evaluator checks required fields; grounded reviewer links each factual claim to supplied evidence. Promotion: neither passes this fixture. A model judge may assist only with retained explanations and disagreement review. No keyword count is used as a substitute for grounding.
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
> Fictional candidate improves average score but fails the missing-evidence slice by inventing answers. Produce a promotion report that retains the slice failure and judge limitations.

**Assertions:**
1. The answer follows the specified output labels in order and contains a concrete task artifact.
2. It applies the task-specific decision branches to the new case rather than repeating the worked example.
3. It preserves missing or conflicting evidence and does not claim an unexecuted check passed.
4. It gives a bounded next action whose completion can be observed.
