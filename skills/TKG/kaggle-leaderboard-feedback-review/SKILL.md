---
id: TKG-005
name: kaggle-leaderboard-feedback-review
domain: Kaggle Competition Workflows
subdomain: Experiments
version: 1.1
description: Create a leaderboard feedback interpretation from supplied evidence; use when preparing or reviewing leaderboard feedback interpretation decisions.
triggers: ["kaggle leaderboard feedback review", "help with a leaderboard feedback interpretation", "review my leaderboard feedback interpretation", "prepare a leaderboard feedback interpretation", "check the evidence for this leaderboard feedback interpretation"]
not_for: ["kaggle out of fold prediction assembly [TKG-006]", "kaggle ensemble eligibility review [TKG-007]"]
requires: []
risk_level: medium
---

# Kaggle Leaderboard Feedback Review

## Purpose
Create a leaderboard feedback interpretation that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect local scores, submission history, public scores, selection rationale; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a leaderboard feedback interpretation and name the source artifacts used; retain a version or observation date where available.
2. Separate locally measured performance from public leaderboard feedback
3. Record every decision influenced by the public score
4. ⚠️ Inspect disagreements for split mismatch or implementation defects. Do not silently replace missing evidence with an assumed successful outcome.
5. Choose further experiments from testable hypotheses rather than rank chasing
6. Apply the domain check: Keep local validation, public feedback, final selection, and rule compliance as separate evidence; never infer hidden labels or redistribute restricted competition material.
7. Verify the proposed result with this task-specific check: Trace selection decisions to the recorded evidence and inspect the local scoring pipeline. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Produce the actual requested artifact: concrete contract fields, matrix rows, comparison values, script lines, or ordered plan steps as appropriate. A recommendation to create the artifact is not the artifact; use the example's concrete deliverable as a structural illustration while replacing its facts with the user's supplied material.
9. Populate the output template with the artifact, decision, evidence, and next action; separate instructions to execute from results already observed.

Domain context: Use the specific competition page, rules, data description, evaluation definition, and submission instructions as inputs. Check their current versions; do not assume that limits, external-data permissions, team rules, or notebook requirements match another competition. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

This is a planning procedure. No executable change or platform operation is needed to apply it. Verify the plan by tracing each proposed action to an input, an owner, and an observable completion condition. Do not convert a planning example into a claim that a build, submission, interview, or deployment has actually happened.

## Decision rules
- IF public feedback repeatedly drives model selection THEN treat it as part of tuning BECAUSE it is no longer untouched confirmation.
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
- **Title-only answer**: restating the request without producing a leaderboard feedback interpretation. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that public feedback repeatedly drives model selection. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a leaderboard feedback interpretation. A team repeatedly chooses variants solely because their public score improves while local validation degrades. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a leaderboard feedback interpretation
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: Public feedback is driving tuning and conflicts with local evidence.
Decision: Investigate the validation mismatch before selecting another variant from rank alone.
Artifact: Evidence lanes: local validation is degrading; public leaderboard score is improving; selection repeatedly follows public score. Interpretation: public feedback is part of tuning. Next hypothesis: investigate split or implementation mismatch; do not treat public rank as untouched confirmation.
Action: Team owner — Choose further experiments from testable hypotheses rather than rank chasing Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Trace selection decisions to the recorded evidence and inspect the local scoring pipeline.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking local scores, submission history, public scores, selection rationale.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when public feedback repeatedly drives model selection, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a leaderboard feedback interpretation. A team repeatedly chooses variants solely because their public score improves while local validation degrades. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all eight output fields in the specified order and Artifact contains concrete task output rather than only a recommendation to produce it.
2. It reflects this fixture-specific finding: Public feedback is driving tuning and conflicts with local evidence.
3. It preserves this task-specific conclusion: Investigate the validation mismatch before selecting another variant from rank alone.
4. It includes the verification check or explicitly marks it pending: Trace selection decisions to the recorded evidence and inspect the local scoring pipeline.
5. It does not claim to have executed a production change or checked material that was not supplied.
