---
id: MPU-011
name: runnable-mvp-slice-implementation
domain: Product Experience Review
subdomain: Product implementation
version: 1.0
description: Implement one runnable end-to-end product slice from a bounded user outcome when a prototype must become a testable MVP increment.
triggers: ["build a small MVP slice", "turn this prototype into a runnable feature", "implement one end-to-end user outcome", "scope a vertical slice for a demo", "make the smallest testable product increment"]
not_for: ["prototype usability scenario design [MPU-006]", "production release approval", "choosing a business model"]
requires: []
risk_level: medium
---

# Runnable MVP Slice Implementation

## Purpose
Turn one user outcome into a runnable product increment with an explicit boundary and verification path. Keep assumptions, missing services, and demo substitutions visible so a working demonstration is not mistaken for production readiness.

## Inputs to collect
1. **User outcome** — obtain actor, starting condition, action and observable completion. Why: this defines the slice. Default: none; ask if the request is only a feature label.
2. **Target project** — obtain repository, language, runtime, framework and available commands from supplied files or the user. Why: implementation must match the actual environment. Default: inspect the supplied repository; do not invent versions.
3. **Acceptance evidence** — obtain expected visible success and failure behavior. Why: it makes completion checkable. Default: propose checks, label them assumptions and request owner confirmation.
4. **Dependencies** — identify data, credentials, external services, permissions and fixtures. Why: this reveals which behavior can run. Default: use supplied local fixtures only when labeled demo-only.
5. **Scope boundary** — identify excluded users, flows, integrations and release expectations. Why: this prevents scope growth. Default: one outcome, one success path and a minimal meaningful failure path.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Inspect project entry points, existing conventions and available verification commands before editing.
2. Write a slice contract: actor, initial state, action, observable result and explicit exclusions.
3. Separate confirmed requirements from assumptions; identify who can validate each assumption and how.
4. Map the shortest state transition from initial state to completion, including one meaningful failure branch.
5. Choose the smallest existing integration point that demonstrates the whole transition. Add dependencies only when the accepted outcome requires them.
6. Identify the data shape and owner for every value crossing the slice boundary. Preserve existing contracts unless a change is approved.
7. Implement the happy path in small edits. Keep secrets outside source files and logs.
8. ⚠️ Before adding an external call, migration or credential requirement, confirm it is necessary; otherwise use a disclosed fixture and state what remains unintegrated.
9. Add meaningful checks for the observed success and selected failure behavior using the project’s existing test or run commands.
10. Run relevant checks and record the exact command and result. Mark blocked or unavailable commands unrun rather than passed.
11. Review the diff for unrelated changes, exposed secrets, unhandled input and assumptions that leaked into user-facing behavior.
12. Deliver the invocation path, acceptance evidence, known gaps and next production decision.

## Decision rules
- IF several independent outcomes are requested THEN choose one and list the others as excluded BECAUSE combining them obscures what was implemented.
- IF a required service is unavailable THEN use a labeled fixture only when it preserves the interaction being tested BECAUSE demo behavior must remain distinguishable from live integration.
- IF acceptance criteria conflict with existing behavior THEN stop and report the conflict BECAUSE silently changing a shared contract can break adjacent flows.
- IF a check passes only with fabricated production data THEN label the fixture and limit the claim BECAUSE a local demonstration does not prove real-data readiness.
- IF the artifact cannot be run in the supplied environment THEN state the exact missing prerequisite BECAUSE implementation without execution evidence is not verified as runnable.

## Output template
```text
Slice: <actor, initial state, action and observable result; maximum 60 words>
Boundary: <included path and exclusions; maximum 60 words>
Changes: <files or artifacts and purpose; up to 8 bullets>
Run: <exact invocation or prerequisite; up to 3 lines>
Verification: <command | observed result; mark unrun checks; up to 8 rows>
Assumptions: <assumption | owner | validation method; or None; up to 6 rows>
Gaps: <demo-only behavior, missing integration or production decision; up to 5 bullets>
Next: <one follow-up decision; maximum 40 words>
```

## Quality checklist
- [ ] Slice names one actor and one observable end state.
- [ ] Included and excluded behavior are explicit.
- [ ] Existing project conventions were inspected first.
- [ ] Assumptions are separated from confirmed requirements.
- [ ] Dependencies and demo fixtures are labeled accurately.
- [ ] Data ownership and changed contracts are identified.
- [ ] Success and failure checks are defined.
- [ ] Verification claims match commands actually run.
- [ ] Secrets and unrelated edits are absent from the delivered diff.

## Anti-patterns
- **Feature pile**: implement several outcomes in one MVP. Fix: select one complete path and defer independent outcomes.
- **Demo masquerade**: present a fixture as a live integration. Fix: label the substitution in output and interface.
- **Architecture detour**: replace project structure before proving the slice needs it. Fix: use existing seams and justify new dependencies.
- **Green-check inflation**: claim a test passed without executing it. Fix: report command and observed result.
- **Silent assumption**: invent roles, data or acceptance rules. Fix: mark the assumption and name its validation path.

## Worked example
**Input:** Fictional team Fern requests a runnable intake slice. A staff member enters a title and description, submits, then sees a saved request ID. No authentication or external service is available. The supplied repository has a local app entry point and existing test command. Keep authentication excluded and disclose local persistence as demo-only.

**Output:**
```text
Slice: Staff member submits title and description and sees the returned request ID.
Boundary: Includes local validation, save and confirmation. Excludes authentication, notifications and deployment.
Changes: Request form and submit handler; local repository adapter; success and required-field checks.
Run: Existing app command from repository root. Persistence is local and demo-only.
Verification: Existing test command | passed; valid submit | request ID displayed; empty title | blocked with field message.
Assumptions: One staff role | product owner | validate before adding access control.
Gaps: No external persistence, auth or notification. Production storage is unresolved.
Next: Decide whether the next slice adds authenticated ownership or an approved storage integration.
```

**Bad output:** “The MVP is production-ready because the form works on my machine.”
This claims operational readiness without evidence and hides the demo-only storage boundary.

## Edge cases
- **No project supplied**: return the slice contract and request the repository or stack before claiming implementation.
- **Acceptance criteria absent**: propose observable checks as assumptions and do not mark them approved.
- **Credentials missing**: keep integration unrun or disclose a fixture; never invent credentials.
- **Tests fail before edits**: record baseline failures separately and identify whether the slice changes them.
- **Production readiness requested**: list required operational decisions separately and identify the responsible owner.

## Test case
**Input:**
> Fictional team Fern has a local app and test command. Implement request intake: enter title and description, submit and show a request ID. No service credentials are provided. State what is implemented and verified.

**Assertions:**
1. Selects one intake outcome and names authentication and deployment as excluded.
2. Makes no live-service claim without credentials and execution evidence.
3. Reports observed test outcomes and marks unavailable checks unrun.
4. Labels local persistence demo-only and identifies the next production decision.
