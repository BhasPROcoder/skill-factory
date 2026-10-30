---
id: TAN-001
name: metric-denominator-definition
domain: Analytical Reasoning and Metrics
subdomain: Metric definitions
version: 1.1
description: Create a metric definition card from supplied evidence; use when preparing or reviewing metric definition card decisions.
triggers: ["metric denominator definition", "help with a metric definition card", "review my metric definition card", "prepare a metric definition card", "check the evidence for this metric definition card"]
not_for: ["cohort retention table design [TAN-002]", "funnel dropoff diagnosis [TAN-003]"]
requires: []
risk_level: medium
---

# Metric Denominator Definition

## Purpose
Create a metric definition card that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect numerator events, eligible population, deduplication rule, time window; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a metric definition card and name the source artifacts used; retain a version or observation date where available.
2. Define the eligible observation unit
3. Specify numerator membership and exclusion rules
4. ⚠️ Align the denominator with the same population and period. Do not silently replace missing evidence with an assumed successful outcome.
5. Compute a small hand-checkable example
6. Apply the domain check: State what a calculation can establish and what would require a different design; do not turn association into causal attribution.
7. Verify the proposed result with this task-specific check: Recompute both quantities and ensure the output label matches its denominator. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Produce the actual requested artifact: concrete contract fields, matrix rows, comparison values, script lines, or ordered plan steps as appropriate. A recommendation to create the artifact is not the artifact; use the example's concrete deliverable as a structural illustration while replacing its facts with the user's supplied material.
9. Populate the output template with the artifact, decision, evidence, and next action; separate instructions to execute from results already observed.

Domain context: A metric is defined by its population, unit, denominator, and time window. Comparisons need compatible definitions before arithmetic is meaningful. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
assert 2/10==0.2 and 4/10==0.4
```

## Decision rules
- IF the numerator counts events but the denominator counts people THEN clarify the intended quantity BECAUSE a rate and events per person answer different questions.
- IF the task-specific verification cannot run on the supplied evidence THEN return a provisional result and name the missing artifact BECAUSE an unperformed check is not a pass.
- IF the proposed next action changes data, access, a live service, or a submitted artifact THEN identify the authorized owner and reversible preparation step BECAUSE analysis alone does not establish execution permission.
- IF an external platform rule, library behavior, or organizational requirement is relevant THEN check the current value in the official documentation or supplied governing policy BECAUSE a remembered value may not match the active environment.

## Output template
```text
Deliverable: <name; one line>
Scope: <artifacts, population, environment; at most two sentences>
Evidence: <observations with input references; at most six bullets>
Decision: <supported conclusion or provisional status; at most two sentences>
Artifact: <the concrete requested deliverable, with actual fields, entries, or draft text; at most 300 words>
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
- **Title-only answer**: restating the request without producing a metric definition card. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that the numerator counts events but the denominator counts people. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a metric definition card. There are 4 purchases from 2 buyers among 10 eligible people. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a metric definition card
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: Buyer conversion is 2 of 10; purchases per eligible person is 4 of 10.
Decision: Choose the measure that matches the decision and name it explicitly.
Artifact: Buyer conversion=2 buyers/10 eligible people=0.2. Purchases per eligible person=4/10=0.4. These are different quantities. Choose the one matching the question and label numerator and denominator explicitly; do not call both the same conversion rate.
Action: Team owner — Compute a small hand-checkable example Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Recompute both quantities and ensure the output label matches its denominator.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking numerator events, eligible population, deduplication rule, time window.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when the numerator counts events but the denominator counts people, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a metric definition card. There are 4 purchases from 2 buyers among 10 eligible people. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all eight output fields in the specified order and Artifact contains concrete task output rather than only a recommendation to produce it.
2. It reflects this fixture-specific finding: Buyer conversion is 2 of 10; purchases per eligible person is 4 of 10.
3. It preserves this task-specific conclusion: Choose the measure that matches the decision and name it explicitly.
4. It includes the verification check or explicitly marks it pending: Recompute both quantities and ensure the output label matches its denominator.
5. It does not claim to have executed a production change or checked material that was not supplied.
