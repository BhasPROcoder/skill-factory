---
id: TVE-006
name: video-pacing-revision-plan
domain: Video Editing Decisions
subdomain: Continuity
version: 1.0
description: Produce a pacing revision plan; use when the task is to video pacing revision plan.
triggers: ["video pacing revision plan", "help with a pacing revision plan", "review my a pacing revision plan", "prepare a pacing revision plan", "check video pacing revision plan evidence"]
not_for: ["video sound picture transition plan [TVE-007]", "video caption readability review [TVE-008]"]
requires: []
risk_level: medium
---

# Video Pacing Revision Plan

## Purpose
Create a pacing revision plan that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect current sequence, intended audience, information density, observed viewing notes; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a pacing revision plan and name the source artifacts used; retain a version or observation date where available.
2. Identify where a new idea or action begins and resolves
3. Distinguish slow comprehension from unnecessary repetition
4. ⚠️ Adjust holds and cuts according to information processing needs Do not silently replace missing evidence with an assumed successful outcome.
5. Review the revised rhythm without imposing a universal shot length
6. Apply the domain check: Preserve the source material and distinguish a paper edit from an executed timeline; verify current destination specifications with the recipient.
7. Verify the proposed result with this task-specific check: Review comprehension of each information-heavy moment rather than only total runtime. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: Describe edit choices through visible actions, shot duration relative to an action, framing, cut motivation, caption placement, and sound transitions. Never invent footage contents, dialogue, defects, or timecodes when the media has not been inspected. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

This is a planning procedure. No executable change or platform operation is needed to apply it. Verify the plan by tracing each proposed action to an input, an owner, and an observable completion condition. Do not convert a planning example into a claim that a build, submission, interview, or deployment has actually happened.

## Decision rules
- IF a cut removes time needed to read or understand THEN restore sufficient hold BECAUSE faster editing is not automatically clearer.
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
- **Title-only answer**: restating the request without producing a pacing revision plan. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that a cut removes time needed to read or understand. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a pacing revision plan. A supplied review note says the instruction card disappears before the reviewer can read the final line. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a pacing revision plan
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: The reported pacing problem is insufficient reading time.
Decision: Extend or simplify the card and retest with a representative viewer.
Action: Team owner — Review the revised rhythm without imposing a universal shot length Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Review comprehension of each information-heavy moment rather than only total runtime.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking current sequence, intended audience, information density, observed viewing notes.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when a cut removes time needed to read or understand, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a pacing revision plan. A supplied review note says the instruction card disappears before the reviewer can read the final line. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: The reported pacing problem is insufficient reading time.
3. It preserves this task-specific conclusion: Extend or simplify the card and retest with a representative viewer.
4. It includes the verification check or explicitly marks it pending: Review comprehension of each information-heavy moment rather than only total runtime.
5. It does not claim to have executed a production change or checked material that was not supplied.
