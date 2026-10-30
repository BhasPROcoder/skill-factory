---
id: TAM-002
name: audio-reference-listening-brief
domain: Audio and Music Production Planning
subdomain: Arrangement
version: 1.1
description: Create a reference listening brief from supplied evidence; use when preparing or reviewing reference listening brief decisions.
triggers: ["audio reference listening brief", "help with a reference listening brief", "review my reference listening brief", "prepare a reference listening brief", "check the evidence for this reference listening brief"]
not_for: ["audio vocal comp selection plan [TAM-003]", "audio dialogue edit plan [TAM-004]"]
requires: []
risk_level: medium
---

# Audio Reference Listening Brief

## Purpose
Create a reference listening brief that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect authorized reference tracks, target audience, creative goal, available audio; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a reference listening brief and name the source artifacts used; retain a version or observation date where available.
2. Translate broad style words into observable listening dimensions
3. Separate arrangement, performance, mix, and mastering observations
4. ⚠️ Identify which dimensions fit the user's own material. Do not silently replace missing evidence with an assumed successful outcome.
5. Write comparison questions without copying a reference composition
6. Apply the domain check: Keep source recordings and reversible edits; verify current delivery requirements with the recipient instead of inventing loudness, format, or platform targets.
7. Verify the proposed result with this task-specific check: Listen to the authorized reference and distinguish observed features from proposed choices. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Produce the actual requested artifact: concrete contract fields, matrix rows, comparison values, script lines, or ordered plan steps as appropriate. A recommendation to create the artifact is not the artifact; use the example's concrete deliverable as a structural illustration while replacing its facts with the user's supplied material.
9. Populate the output template with the artifact, decision, evidence, and next action; separate instructions to execute from results already observed.

Domain context: Describe sound choices through observable features such as entry timing, instrument density, foreground level, phrase spacing, and audible transitions. If audio is unavailable, offer a listening plan rather than claiming to hear clipping, noise, pitch problems, or balance defects. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

This is a planning procedure. No executable change or platform operation is needed to apply it. Verify the plan by tracing each proposed action to an input, an owner, and an observable completion condition. Do not convert a planning example into a claim that a build, submission, interview, or deployment has actually happened.

## Decision rules
- IF the reference audio is unavailable THEN state questions to evaluate later BECAUSE track reputation does not establish audible details.
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
- **Title-only answer**: restating the request without producing a reference listening brief. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that the reference audio is unavailable. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a reference listening brief. The user asks for an intimate vocal sound but supplies no playable reference. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a reference listening brief
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: No reference-specific listening observations are available.
Decision: Propose checking vocal distance, room audibility, accompaniment density, and phrase detail when audio is supplied.
Artifact: Listening questions: how close does the vocal feel relative to room sound; how exposed is it against accompaniment; how much phrase space remains? Intended direction: intimate vocal. Reference observations: unavailable until playable audio is supplied.
Action: Team owner — Write comparison questions without copying a reference composition Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Listen to the authorized reference and distinguish observed features from proposed choices.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking authorized reference tracks, target audience, creative goal, available audio.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when the reference audio is unavailable, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a reference listening brief. The user asks for an intimate vocal sound but supplies no playable reference. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all eight output fields in the specified order and Artifact contains concrete task output rather than only a recommendation to produce it.
2. It reflects this fixture-specific finding: No reference-specific listening observations are available.
3. It preserves this task-specific conclusion: Propose checking vocal distance, room audibility, accompaniment density, and phrase detail when audio is supplied.
4. It includes the verification check or explicitly marks it pending: Listen to the authorized reference and distinguish observed features from proposed choices.
5. It does not claim to have executed a production change or checked material that was not supplied.
