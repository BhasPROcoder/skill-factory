---
id: TML-004
name: model-threshold-selection-plan
domain: Model Evaluation Design
subdomain: Deployment comparison
version: 1.0
description: Produce a threshold selection worksheet; use when the task is to model threshold selection plan.
triggers: ["model threshold selection plan", "help with a threshold selection worksheet", "review my a threshold selection worksheet", "prepare a threshold selection worksheet", "check model threshold selection plan evidence"]
not_for: ["model probability calibration review [TML-005]", "model error slice investigation [TML-006]"]
requires: []
risk_level: medium
---

# Model Threshold Selection Plan

## Purpose
Create a threshold selection worksheet that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect validation scores, labels, acceptable tradeoff, deployment action; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a threshold selection worksheet and name the source artifacts used; retain a version or observation date where available.
2. List candidate thresholds without consulting final test outcomes
3. Compute action counts and error tradeoffs on validation data
4. ⚠️ Select using the stated decision criterion Do not silently replace missing evidence with an assumed successful outcome.
5. Freeze the threshold before final evaluation
6. Apply the domain check: Check separation of training, tuning, and final evaluation; connect the chosen metric to the real decision instead of assuming the leaderboard metric is sufficient.
7. Verify the proposed result with this task-specific check: Check boundary inclusivity and recompute selected records. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: A model score is conditional on a dataset, split, metric, and prediction-time information. Protect held-out data from model-selection decisions and retain simple baselines that make improvement interpretable. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
scores=[0.2,0.6,0.9]; assert [s>=0.5 for s in scores]==[False,True,True]
```

## Decision rules
- IF a threshold is selected on the final test labels THEN move selection to validation BECAUSE selection consumes information from the evaluation set.
- IF the task-specific verification cannot run on the supplied evidence THEN return a provisional result and name the missing artifact BECAUSE an unperformed check is not a pass.
- IF the proposed next action changes data, access, a live service, or a submitted artifact THEN identify the authorized owner and reversible preparation step BECAUSE analysis alone does not establish execution permission.
- IF an external platform rule, library behavior, or organizational requirement is relevant THEN check the current value in the official documentation or supplied governing policy BECAUSE a remembered value may not match the active environment.

## Output template
```text
Deliverable: <name; one line>
Scope: <artifacts, population, environment; at most two sentences>
Evidence: <observations with input references; at most six bullets>
Decision: <supported conclusion or provisional status; at most two sentences>
Action: <owner, concrete next step, completion condition; at most three bullets>
Verification: <performed checks and results, or explicitly pending checks; at most three bullets>
Open items: <missing information or current-source checks; at most three bullets, or none>
```

## Quality checklist
- [ ] The deliverable is limited to the named task rather than a general domain tutorial.
- [ ] Each factual observation can be traced to supplied material or an explicitly fictional fixture.
- [ ] The task-specific branch condition is evaluated, or the missing evidence is identified.
- [ ] The decision states its scope and does not imply an unseen system was checked.
- [ ] The next action includes a completion condition and an owner or an unassigned marker.
- [ ] Verification distinguishes performed checks from proposed checks.
- [ ] Every external rule or changing requirement has a current-source check instead of a remembered constant.
- [ ] The example arithmetic and executable assertions agree with the stated conclusion.

## Anti-patterns
- **Title-only answer**: restating the request without producing a threshold selection worksheet. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that a threshold is selected on the final test labels. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a threshold selection worksheet. Validation scores are 0.2, 0.6, and 0.9; the proposed threshold is 0.5 using greater-than-or-equal comparison. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a threshold selection worksheet
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: The threshold selects the latter two records for the positive action.
Decision: Evaluate that threshold's consequences on validation data before freezing it.
Action: Team owner — Freeze the threshold before final evaluation Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Check boundary inclusivity and recompute selected records.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking validation scores, labels, acceptable tradeoff, deployment action.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when a threshold is selected on the final test labels, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a threshold selection worksheet. Validation scores are 0.2, 0.6, and 0.9; the proposed threshold is 0.5 using greater-than-or-equal comparison. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: The threshold selects the latter two records for the positive action.
3. It preserves this task-specific conclusion: Evaluate that threshold's consequences on validation data before freezing it.
4. It includes the verification check or explicitly marks it pending: Check boundary inclusivity and recompute selected records.
5. It does not claim to have executed a production change or checked material that was not supplied.
