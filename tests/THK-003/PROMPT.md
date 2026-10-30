Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: THK-003
name: hackathon-team-interface-contract
domain: Hackathon Delivery
subdomain: Team execution
version: 1.1
description: Create a team integration contract from supplied evidence; use when preparing or reviewing team integration contract decisions.
triggers: ["hackathon team interface contract", "help with a team integration contract", "review my team integration contract", "prepare a team integration contract", "check the evidence for this team integration contract"]
not_for: ["hackathon risk first build order [THK-004]", "hackathon demo script [THK-005]"]
requires: []
risk_level: medium
---

# Hackathon Team Interface Contract

## Purpose
Create a team integration contract that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect component owners, data shapes, event timing, integration point; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a team integration contract and name the source artifacts used; retain a version or observation date where available.
2. Define each component's input and output with a concrete fixture
3. Assign one accountable owner to each interface
4. ⚠️ Agree how failures and partial results are represented. Do not silently replace missing evidence with an assumed successful outcome.
5. Schedule early integration using the shared fixture
6. Apply the domain check: Connect each commitment to the available team, schedule, permitted resources, and a fallback demonstration path.
7. Verify the proposed result with this task-specific check: Pass the same fixture through both component boundaries. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Produce the actual requested artifact: concrete contract fields, matrix rows, comparison values, script lines, or ordered plan steps as appropriate. A recommendation to create the artifact is not the artifact; use the example's concrete deliverable as a structural illustration while replacing its facts with the user's supplied material.
9. Populate the output template with the artifact, decision, evidence, and next action; separate instructions to execute from results already observed.

Domain context: A hackathon prototype needs a coherent user journey and demonstrable evidence of its central claim. Distinguish simulated components from implemented behavior, and read the current event rules instead of assuming submission or judging conventions. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
frontend={'summary_text'}; backend={'summary'}; assert frontend!=backend
```

## Decision rules
- IF components use different field names for the same payload THEN agree one contract before parallel implementation BECAUSE late translation surprises consume integration time.
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
- **Title-only answer**: restating the request without producing a team integration contract. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that components use different field names for the same payload. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a team integration contract. The frontend expects summary_text while the backend returns summary; both teams assume their shape is agreed. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a team integration contract
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: The interface names disagree.
Decision: Agree the payload contract and update both sides before further integration work.
Artifact: Proposed contract: success payload {"summary_text":"Example summary"}; backend produces this field and frontend renders it. Failure payload proposal: {"error":"processing_failed"}; frontend shows a failure state, not a blank success. Owners: backend lead and frontend lead must accept the proposal and run the shared fixture.
Action: Team owner — Schedule early integration using the shared fixture Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Pass the same fixture through both component boundaries.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking component owners, data shapes, event timing, integration point.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when components use different field names for the same payload, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a team integration contract. The frontend expects summary_text while the backend returns summary; both teams assume their shape is agreed. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all eight output fields in the specified order and Artifact contains concrete task output rather than only a recommendation to produce it.
2. It reflects this fixture-specific finding: The interface names disagree.
3. It preserves this task-specific conclusion: Agree the payload contract and update both sides before further integration work.
4. It includes the verification check or explicitly marks it pending: Pass the same fixture through both component boundaries.
5. It does not claim to have executed a production change or checked material that was not supplied.
</skill>

<user_request>
Fictional team Cedar Lantern asks for a team integration contract. The frontend expects summary_text while the backend returns summary; both teams assume their shape is agreed. Produce the assessment and identify what remains unverified.
</user_request>
