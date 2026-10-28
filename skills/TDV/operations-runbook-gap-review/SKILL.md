---
id: TDV-008
name: operations-runbook-gap-review
domain: Deployment and Operations Planning
subdomain: Service operations
version: 1.0
description: Produce an operational runbook gap report; use when the task is to operations runbook gap review.
triggers: ["operations runbook gap review", "help with an operational runbook gap report", "review my an operational runbook gap report", "prepare an operational runbook gap report", "check operations runbook gap review evidence"]
not_for: ["deployment environment parity review [TDV-009]", "operations postincident action review [TDV-010]"]
requires: []
risk_level: medium
---

# Operations Runbook Gap Review

## Purpose
Create an operational runbook gap report that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect runbook steps, access needs, failure scenarios, operator role; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of an operational runbook gap report and name the source artifacts used; retain a version or observation date where available.
2. Walk through the runbook as the intended operator
3. Identify missing commands, preconditions, and expected observations
4. ⚠️ Separate diagnostic steps from state-changing steps Do not silently replace missing evidence with an assumed successful outcome.
5. Add stop and escalation conditions where evidence becomes ambiguous
6. Apply the domain check: Identify the owner, precondition, stop condition, and recovery action for every proposed live change; verify current provider behavior in official documentation.
7. Verify the proposed result with this task-specific check: Have an authorized reviewer rehearse the instructions in a nonproduction environment. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: Operational readiness depends on the exact artifact, configuration, environment, and observed workload. Rehearse state changes in an isolated environment and distinguish an available backup from a demonstrated recovery. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
required={'target','owner','success_signal','stop_condition'}; supplied={'action'}; assert required-supplied==required
```

## Decision rules
- IF a step says restart without naming impact or recovery checks THEN make the action specific BECAUSE an operator cannot assess success or harm from the verb alone.
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
- **Title-only answer**: restating the request without producing an operational runbook gap report. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that a step says restart without naming impact or recovery checks. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests an operational runbook gap report. A runbook says 'restart the worker' but names no worker, authority, expected recovery signal, or stop condition. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: an operational runbook gap report
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: The action is underspecified.
Decision: Add the target, authorized owner, expected signal, and escalation path before operational use.
Action: Team owner — Add stop and escalation conditions where evidence becomes ambiguous Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Have an authorized reviewer rehearse the instructions in a nonproduction environment.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking runbook steps, access needs, failure scenarios, operator role.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when a step says restart without naming impact or recovery checks, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for an operational runbook gap report. A runbook says 'restart the worker' but names no worker, authority, expected recovery signal, or stop condition. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: The action is underspecified.
3. It preserves this task-specific conclusion: Add the target, authorized owner, expected signal, and escalation path before operational use.
4. It includes the verification check or explicitly marks it pending: Have an authorized reviewer rehearse the instructions in a nonproduction environment.
5. It does not claim to have executed a production change or checked material that was not supplied.
