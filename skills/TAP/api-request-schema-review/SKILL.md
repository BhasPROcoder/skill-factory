---
id: TAP-001
name: api-request-schema-review
domain: API Contract Engineering
subdomain: Requests
version: 1.0
description: Produce a request schema review; use when the task is to api request schema review.
triggers: ["api request schema review", "help with a request schema review", "review my a request schema review", "prepare a request schema review", "check api request schema review evidence"]
not_for: ["api error response contract [TAP-002]", "api pagination consistency plan [TAP-003]"]
requires: []
risk_level: medium
---

# Api Request Schema Review

## Purpose
Create a request schema review that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect request examples, required fields, field semantics, consumer expectations; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a request schema review and name the source artifacts used; retain a version or observation date where available.
2. Distinguish absent fields from explicit empty or null values
3. Identify fields whose type alone does not capture valid meaning
4. ⚠️ Define accepted and rejected boundary fixtures Do not silently replace missing evidence with an assumed successful outcome.
5. Return a schema change proposal with compatibility notes
6. Apply the domain check: Use explicit request and response fixtures; distinguish logical operation identity from transport attempts and preserve backward-compatibility assumptions.
7. Verify the proposed result with this task-specific check: Test omitted, null, empty-string, and ordinary-value requests separately. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: An API contract includes observable failure behavior and client assumptions as well as the happy path. Verify current framework and protocol details in official documentation before writing integration-specific code. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
omitted={}; clear={'nickname':None}; assert 'nickname' not in omitted and 'nickname' in clear
```

## Decision rules
- IF absence and explicit clearing have different meanings THEN represent them separately BECAUSE collapsing both loses user intent.
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
- **Title-only answer**: restating the request without producing a request schema review. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that absence and explicit clearing have different meanings. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a request schema review. Omitting nickname means keep it; sending nickname as null means clear it. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a request schema review
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: The contract assigns different semantics to absence and null.
Decision: Preserve that distinction in parsing and update logic.
Action: Team owner — Return a schema change proposal with compatibility notes Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Test omitted, null, empty-string, and ordinary-value requests separately.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking request examples, required fields, field semantics, consumer expectations.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when absence and explicit clearing have different meanings, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a request schema review. Omitting nickname means keep it; sending nickname as null means clear it. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: The contract assigns different semantics to absence and null.
3. It preserves this task-specific conclusion: Preserve that distinction in parsing and update logic.
4. It includes the verification check or explicitly marks it pending: Test omitted, null, empty-string, and ordinary-value requests separately.
5. It does not claim to have executed a production change or checked material that was not supplied.
