---
id: RNT-006
name: rental-turnaround-readiness-handoff
domain: Rental Asset Operations
subdomain: Turnaround readiness
version: 1.0
description: Reconcile rental turnaround task evidence into a release handoff when physical return, completed work and authorization to reallocate are separate states.
triggers: ["is this returned rental ready again", "prepare the turnaround release handoff", "reconcile open rental preparation tasks", "unit marked available before checks complete", "close a rental turnaround hold"]
not_for: ["technical repair or safety inspection", "appointment resource scheduling [SVC-001]", "serial assignment to reservations [RNT-001]", "designing maintenance standards"]
requires: []
risk_level: medium
---

# Rental turnaround readiness handoff

## Purpose
Produce an evidence-based handoff showing whether a returned rental unit has completed its supplied turnaround requirements and obtained the applicable release decision. Treat physical possession, task completion, technical acceptance and allocation availability as separate states so an administrative status cannot substitute for required work.

## Inputs to collect
1. **Unit and return event:** Obtain the physical identity, receiving event and current location. These bind the handoff to the returned object. Default: no readiness conclusion for an unidentified unit.
2. **Applicable turnaround requirements:** Collect the approved task list, revision and applicability conditions for this unit and next use. This defines what must be completed. Default: none; do not invent inspection, cleaning or maintenance requirements.
3. **Task evidence:** Obtain completion records, results, performer, time and any accepted deviations. This distinguishes claimed completion from evidenced acceptance. Default: unprovided results remain unknown, not passed.
4. **Dependencies and holds:** Collect task prerequisites, open defects, quarantine or administrative holds and what can invalidate earlier checks. This prevents premature release. Default: unresolved supplied holds remain open.
5. **Release authority:** Obtain the authorized decision-maker and the evidence required for release. This determines whether preparation completion is enough. Default: recommendation only; no inferred authority to mark available.
6. **Downstream need:** Obtain the next intended use or reservation and the actual handoff checkpoint. This reveals configuration-specific requirements. Default: unit-level readiness only, with no promise about a particular future use.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Define the unit, return event and requirement revision covered by this readiness review. Keep prior rental records as history rather than treating their approvals as automatically applicable to the new cycle.
2. Convert the supplied turnaround requirements into accountable rows with applicability, dependency, evidence and accepting role. Mark inapplicable tasks only with the supplied reason; do not remove them silently.
3. Associate each completion record with the exact unit, task and turnaround cycle. A batch-level claim may need an item-level link before it supports this particular unit.
4. Distinguish task execution from its result and acceptance. A test marked performed may have failed, and a completed repair may still await the specified follow-up check.
5. ⚠️ Evaluate dependencies in their supplied order. If a later task can invalidate an earlier result, require the designated recheck; do not reuse the earlier pass merely to fill the readiness grid.
6. Reconcile each hold with its closure evidence and authority. Keep resolved work separate from an unresolved hold release so the next operator can see exactly what remains blocked.
7. Identify the smallest remaining work package: task, prerequisite, responsible role and evidence needed. Do not replace a missing qualified inspection with an agent's interpretation of photos or a generic checklist.
8. ⚠️ Compare the proposed readiness state with the evidence grid. Physical return supports possession; complete work supports preparation; only the supplied acceptance and authority rules support release.
9. Prepare a release recommendation or blocked handoff that names the intended downstream use. If a new reservation changes the required configuration, flag that change for applicability review rather than silently carrying over the old decision.
10. Record the actual execution state separately. A recommendation to release, an authorized release record and a changed availability flag are distinct events; claim only those supported by evidence.

## Decision rules
- IF a task is performed but its result is missing THEN retain an unresolved acceptance state BECAUSE execution alone does not establish a pass.
- IF later work invalidates an earlier check under the supplied procedure THEN reopen that check BECAUSE its evidence no longer describes the final configuration.
- IF all applicable tasks are accepted but release authority is absent THEN recommend review rather than mark released BECAUSE task completion does not confer decision authority.
- IF a supplied hold remains open THEN preserve the block BECAUSE an availability flag cannot cancel the hold's evidence requirement.
- IF the intended use changes THEN revisit task applicability BECAUSE readiness may depend on configuration and use, not just the unit identifier.

## Output template
```text
Readiness boundary: <unit, return cycle, requirement revision and intended use; up to four lines>
Task grid:
Task | Applicability/dependency | Evidence/result | Acceptance state | Remaining action
<up to twelve rows; attach a full grid if larger>
Holds: <open or closed hold with supporting reference; up to six lines>
Remaining package: <action, owner and needed evidence; up to six lines>
Recommendation: <blocked / ready for authorized release review / released on supplied evidence, with reason>
Handoff: <recipient and downstream limitation; up to three lines>
Execution state: <recommendation, release record and availability update distinguished; up to three lines>
```

## Quality checklist
- [ ] The review identifies one unit and turnaround cycle.
- [ ] Requirements come from a supplied applicable revision.
- [ ] Inapplicable rows have an explicit reason.
- [ ] Performed, passed and accepted states are distinct.
- [ ] Dependency invalidations are evaluated against the final configuration.
- [ ] Each hold has a current state and closure evidence if closed.
- [ ] Remaining actions name the necessary evidence and responsible role.
- [ ] The stated release and availability states match actual evidence.

## Anti-patterns
- **Returned equals ready:** depot possession becomes release. Fix: apply the supplied turnaround grid.
- **Checkbox acceptance:** a completed task is assumed passed. Fix: inspect its result and required acceptance.
- **Stale inspection reuse:** a pre-repair result approves a changed unit. Fix: apply the supplied invalidation and recheck rule.
- **Availability overrides hold:** a system flag erases an unresolved block. Fix: reconcile the hold's actual closure requirements.
- **Invented technical standard:** a generic checklist substitutes for the approved procedure. Fix: request the applicable requirements and qualified evidence.

## Worked example
**Input:** Fictional display-stand rental firm Rowan returned unit R9. Its supplied turnaround procedure requires surface cleaning, fitting replacement if damaged, and an alignment check after any replacement. Cleaning is accepted. A damaged fitting was replaced after an earlier alignment pass. No later alignment check exists. The release manager has not authorized release; the stock screen nevertheless says available.

**Output:**
```text
Readiness boundary: Rowan R9; current return cycle; supplied display-stand procedure; ordinary next display use.
Task grid:
Task | Applicability/dependency | Evidence/result | Acceptance state | Remaining action
Surface cleaning | required | completed and accepted | accepted | none evidenced
Fitting replacement | damaged fitting | completed after earlier alignment check | work complete; downstream check pending | retain replacement record
Alignment check | after replacement | only pre-replacement pass supplied | reopened under supplied rule | perform and accept required post-replacement check
Holds: Readiness unresolved pending alignment acceptance and release decision; no closure evidenced.
Remaining package: Assigned checker supplies the required post-replacement result; release manager reviews the completed evidence and records the decision.
Recommendation: Blocked; the earlier alignment result predates the replacement and does not satisfy the supplied procedure.
Handoff: Operations reconciles the premature availability flag before relying on R9 for fulfillment.
Execution state: Review only; no check performed, release authorized or availability flag changed.
```

**Bad output:** “All work is done and the stock screen says available, so R9 is ready.”
It ignores the supplied post-replacement dependency and invents a release decision.

## Edge cases
- A task was completed at another branch: require its unit and cycle linkage and the supplied acceptance evidence, not a repeat merely because the location differs.
- The requirement revision changes mid-turnaround: ask the process owner which revision governs and identify affected rows without silently mixing revisions.
- A unit is released for a limited use: state the supplied restriction in the handoff and avoid presenting it as unrestricted readiness.
- A new defect is reported after release: preserve the historical release and open a new review state according to the supplied process; do not rewrite history as if the earlier decision never occurred.

## Test case
**Input:**
> Fictional depot Cedar has every applicable turnaround task accepted for unit C5. Its procedure still requires a named manager's release record. No release record is supplied, but staff ask you to call it ready for dispatch.

**Assertions:**
1. Reports accepted preparation tasks separately from release authority.
2. Recommends authorized release review rather than claiming dispatch readiness.
3. Identifies the missing manager release record.
4. Does not change availability or claim a physical dispatch.
