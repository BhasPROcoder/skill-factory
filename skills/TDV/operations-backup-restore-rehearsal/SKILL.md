---
id: TDV-004
name: operations-backup-restore-rehearsal
domain: Deployment and Operations Planning
subdomain: Recovery
version: 1.1
description: Create a backup restoration rehearsal plan from supplied evidence; use when preparing or reviewing backup restoration rehearsal plan decisions.
triggers: ["operations backup restore rehearsal", "help with a backup restoration rehearsal plan", "review my backup restoration rehearsal plan", "prepare a backup restoration rehearsal plan", "check the evidence for this backup restoration rehearsal plan"]
not_for: ["operations alert actionability review [TDV-005]", "operations capacity test plan [TDV-006]"]
requires: []
risk_level: medium
---

# Operations Backup Restore Rehearsal

## Purpose
Create a backup restoration rehearsal plan that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect backup inventory, recovery objectives, dependencies, isolated destination; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a backup restoration rehearsal plan and name the source artifacts used; retain a version or observation date where available.
2. Identify the exact backup and necessary dependent artifacts
3. Define application-level recovery checks before restoration
4. ⚠️ Restore only into an authorized isolated destination. Do not silently replace missing evidence with an assumed successful outcome.
5. Compare recovered state and elapsed recovery with supplied objectives
6. Apply the domain check: Identify the owner, precondition, stop condition, and recovery action for every proposed live change; verify current provider behavior in official documentation.
7. Verify the proposed result with this task-specific check: Open restored data and run the agreed integrity and application checks. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Produce the actual requested artifact: concrete contract fields, matrix rows, comparison values, script lines, or ordered plan steps as appropriate. A recommendation to create the artifact is not the artifact; use the example's concrete deliverable as a structural illustration while replacing its facts with the user's supplied material.
9. Populate the output template with the artifact, decision, evidence, and next action; separate instructions to execute from results already observed.

Domain context: Operational readiness depends on the exact artifact, configuration, environment, and observed workload. Rehearse state changes in an isolated environment and distinguish an available backup from a demonstrated recovery. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
evidence={'archive_present':True,'checksum_checked':True,'restore_tested':False}; assert not evidence['restore_tested']
```

## Decision rules
- IF a backup exists but has never been restored THEN label recoverability unverified BECAUSE file presence does not demonstrate usable recovery.
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
- **Title-only answer**: restating the request without producing a backup restoration rehearsal plan. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that a backup exists but has never been restored. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a backup restoration rehearsal plan. The team has a backup archive and checksum but no restoration result. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a backup restoration rehearsal plan
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: Archive integrity evidence exists; application recovery remains untested.
Decision: Schedule an isolated restore and validate the recovered application state.
Artifact: Evidence: archive present; checksum checked; restoration not tested. Rehearsal: authorized isolated destination → restore exact backup and dependencies → inspect recovered data → run supplied application checks → compare to recovery objectives. Recovery remains unverified until observed.
Action: Team owner — Compare recovered state and elapsed recovery with supplied objectives Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Open restored data and run the agreed integrity and application checks.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking backup inventory, recovery objectives, dependencies, isolated destination.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when a backup exists but has never been restored, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a backup restoration rehearsal plan. The team has a backup archive and checksum but no restoration result. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all eight output fields in the specified order and Artifact contains concrete task output rather than only a recommendation to produce it.
2. It reflects this fixture-specific finding: Archive integrity evidence exists; application recovery remains untested.
3. It preserves this task-specific conclusion: Schedule an isolated restore and validate the recovered application state.
4. It includes the verification check or explicitly marks it pending: Open restored data and run the agreed integrity and application checks.
5. It does not claim to have executed a production change or checked material that was not supplied.
