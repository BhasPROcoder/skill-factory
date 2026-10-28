---
id: TAM-010
name: audio-delivery-requirement-review
domain: Audio and Music Production Planning
subdomain: Arrangement
version: 1.0
description: Produce an audio delivery specification sheet; use when the task is to audio delivery requirement review.
triggers: ["audio delivery requirement review", "help with an audio delivery specification sheet", "review my an audio delivery specification sheet", "prepare an audio delivery specification sheet", "check audio delivery requirement review evidence"]
not_for: ["audio recording session plan [TAM-001]", "audio reference listening brief [TAM-002]"]
requires: []
risk_level: medium
---

# Audio Delivery Requirement Review

## Purpose
Create an audio delivery specification sheet that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect recipient's current requirements, approved mix, version labels, metadata needs; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of an audio delivery specification sheet and name the source artifacts used; retain a version or observation date where available.
2. Obtain current format and measurement requirements from the recipient
3. Separate creative approval from technical compliance
4. ⚠️ Check the final artifact against the supplied requirements Do not silently replace missing evidence with an assumed successful outcome.
5. Package labeled versions with unresolved items explicitly noted
6. Apply the domain check: Keep source recordings and reversible edits; verify current delivery requirements with the recipient instead of inventing loudness, format, or platform targets.
7. Verify the proposed result with this task-specific check: Measure and inspect the actual export against the recipient's current supplied specification. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: Describe sound choices through observable features such as entry timing, instrument density, foreground level, phrase spacing, and audible transitions. If audio is unavailable, offer a listening plan rather than claiming to hear clipping, noise, pitch problems, or balance defects. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

This is a planning procedure. No executable change or platform operation is needed to apply it. Verify the plan by tracing each proposed action to an input, an owner, and an observable completion condition. Do not convert a planning example into a claim that a build, submission, interview, or deployment has actually happened.

## Decision rules
- IF no recipient target is supplied THEN request it instead of inventing a platform standard BECAUSE delivery requirements vary by destination and use.
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
- **Title-only answer**: restating the request without producing an audio delivery specification sheet. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that no recipient target is supplied. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests an audio delivery specification sheet. The client approves the mix but has not specified the required file format or loudness target. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: an audio delivery specification sheet
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: Creative approval is present; technical delivery requirements are missing.
Decision: Request the destination specification before final export acceptance.
Action: Team owner — Package labeled versions with unresolved items explicitly noted Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Measure and inspect the actual export against the recipient's current supplied specification.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking recipient's current requirements, approved mix, version labels, metadata needs.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when no recipient target is supplied, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for an audio delivery specification sheet. The client approves the mix but has not specified the required file format or loudness target. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: Creative approval is present; technical delivery requirements are missing.
3. It preserves this task-specific conclusion: Request the destination specification before final export acceptance.
4. It includes the verification check or explicitly marks it pending: Measure and inspect the actual export against the recipient's current supplied specification.
5. It does not claim to have executed a production change or checked material that was not supplied.
