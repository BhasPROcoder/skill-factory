---
id: TKG-009
name: kaggle-final-submission-selection
domain: Kaggle Competition Workflows
subdomain: Competition setup
version: 1.0
description: Produce a final submission selection brief; use when the task is to kaggle final submission selection.
triggers: ["kaggle final submission selection", "help with a final submission selection brief", "review my a final submission selection brief", "prepare a final submission selection brief", "check kaggle final submission selection evidence"]
not_for: ["kaggle post competition solution handoff [TKG-010]", "kaggle competition rules brief [TKG-001]"]
requires: []
risk_level: medium
---

# Kaggle Final Submission Selection

## Purpose
Create a final submission selection brief that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect current final-selection rules, candidate artifacts, validation records, deadlines; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a final submission selection brief and name the source artifacts used; retain a version or observation date where available.
2. Verify the current selection mechanism and permitted number of choices
3. Match each candidate to reproducible run provenance
4. ⚠️ Compare candidates using predeclared evidence and known uncertainty Do not silently replace missing evidence with an assumed successful outcome.
5. Prepare the exact final selection for authorized submission
6. Apply the domain check: Keep local validation, public feedback, final selection, and rule compliance as separate evidence; never infer hidden labels or redistribute restricted competition material.
7. Verify the proposed result with this task-specific check: Match the final artifact to its recorded configuration and check current official selection instructions. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: Use the specific competition page, rules, data description, evaluation definition, and submission instructions as inputs. Check their current versions; do not assume that limits, external-data permissions, team rules, or notebook requirements match another competition. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

This is a planning procedure. No executable change or platform operation is needed to apply it. Verify the plan by tracing each proposed action to an input, an owner, and an observable completion condition. Do not convert a planning example into a claim that a build, submission, interview, or deployment has actually happened.

## Decision rules
- IF the chosen file cannot be reproduced from its recorded run THEN resolve provenance before selection BECAUSE a remembered score does not identify a trustworthy artifact.
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
- **Title-only answer**: restating the request without producing a final submission selection brief. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that the chosen file cannot be reproduced from its recorded run. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a final submission selection brief. Candidate Birch has a verified run and artifact hash; candidate Elm has a score screenshot but no matching file. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a final submission selection brief
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: Elm's result cannot be tied to a reproducible submission artifact.
Decision: Resolve Elm's provenance or select only among traceable eligible candidates.
Action: Team owner — Prepare the exact final selection for authorized submission Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Match the final artifact to its recorded configuration and check current official selection instructions.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking current final-selection rules, candidate artifacts, validation records, deadlines.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when the chosen file cannot be reproduced from its recorded run, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a final submission selection brief. Candidate Birch has a verified run and artifact hash; candidate Elm has a score screenshot but no matching file. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: Elm's result cannot be tied to a reproducible submission artifact.
3. It preserves this task-specific conclusion: Resolve Elm's provenance or select only among traceable eligible candidates.
4. It includes the verification check or explicitly marks it pending: Match the final artifact to its recorded configuration and check current official selection instructions.
5. It does not claim to have executed a production change or checked material that was not supplied.
