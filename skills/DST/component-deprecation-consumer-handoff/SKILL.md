---
id: DST-004
name: component-deprecation-consumer-handoff
domain: Design System Maintenance
subdomain: Component lifecycle
version: 1.0
description: Prepare a consumer-specific retirement handoff when a design-system component is being deprecated and its replacement may not preserve every supported behavior.
triggers: ["deprecate a shared component", "handoff component retirement", "migrate consumers from an old component", "check replacement component parity", "prepare component removal readiness"]
not_for: ["token identifier migration [DST-003]", "generic release notes [MPU-009]", "variant support definition [DST-002]"]
requires: []
risk_level: medium
---

# Component deprecation consumer handoff

## Purpose
Turn a decision to retire a shared component into an actionable migration contract for its actual consumers. Separate an announcement from removal readiness, and identify replacement behavior gaps before teams are asked to change imports or layouts.

## Inputs to collect
1. **Retirement decision:** Obtain the component identity, affected revisions, reason, and decision owner. Required; a proposal is not an approved removal.
2. **Consumer inventory:** Collect applications, screens, wrappers and packages using it, plus evidence of inventory coverage. Default: supplied consumers only; unknown downstream use stays unresolved.
3. **Existing behavior:** Identify supported uses, content patterns, interaction states and custom extensions. Required for claiming replacement parity; screenshots alone are insufficient.
4. **Replacement evidence:** Obtain the intended successor, supported contract, known gaps and actual test results. Default: replacement unverified, even when its name suggests equivalent behavior.
5. **Transition policy:** Ask for the project's warning, compatibility, versioning and removal rules. Default: no deadline, version bump or automatic replacement prescribed.
6. **Change authority:** Determine which consumer edits or communication are authorized. Default: prepare a handoff without publishing, editing applications or contacting teams.

If required inputs lack a safe default, ask in one message with at most three questions.

## Procedure
1. Record the retirement state precisely: proposed, announced, migration supported, or removal approved under the project's own process. Do not treat a deprecated label as permission to delete code.
2. Build a consumer list from supplied evidence and trace wrappers separately from direct use. A shared wrapper may hide many screens; a dependency declaration may exist without active runtime use.
3. Extract the behavior each consumer relies on. Include initialization, selection, validation, focus, keyboard interaction, state persistence, content overflow and error recovery when those are relevant to the supplied use.
4. Compare each required behavior with the successor's demonstrated or documented support. ⚠️ A similar appearance is not proof that input handling, events or state serialization remain compatible.
5. Classify each consumer path as direct migration, adaptation required, blocked by a gap, or unknown pending inspection. Tie each classification to evidence rather than estimating ease from line count.
6. Specify the migration artifact for each path: changed composition, prop mapping, adapter, content revision or explicit retention. State which team or role must make the decision, without inventing commitments.
7. Define a focused acceptance check from the old behavior contract. Verify an observable user task before and after, rather than merely asserting that the old import string disappeared.
8. Order shared dependency changes and consumer changes so the successor is available before use. Keep compatibility support and rollback behavior explicit; an adapter is only a proposal until implemented and tested.
9. Reconcile migration evidence at the removal gate. ⚠️ Distinguish code search, build success, observed user behavior, and owner acknowledgment; each proves a different part of readiness.
10. Deliver the handoff, remaining blockers and a bounded removal recommendation. Preserve the prior component or recovery path according to the supplied release process until an authorized decision closes the transition.

Use [VERIFY: current component API, event behavior and supported migration tooling in the installed library's official documentation] where implementation details are needed. Apply the project's own versioning rules; no universal release number or waiting interval is part of this method.

This standalone Python 3 fixture demonstrates a fictional acceptance ledger. It models a removal gate chosen for this example, not a mandatory organization policy. Execute with an available Python 3 interpreter and record the actual version. It does not inspect applications.

```python
consumers = {
    "search": {"migration": True, "behavior": True},
    "settings": {"migration": True, "behavior": False},
}
ready = all(all(checks.values()) for checks in consumers.values())
assert ready is False
consumers["settings"]["behavior"] = True
assert all(all(checks.values()) for checks in consumers.values())
```

## Decision rules
- IF a required behavior has no successor equivalent THEN classify that consumer as blocked or adaptation-required BECAUSE matching visual design does not preserve its user task.
- IF local references are gone but downstream consumers are unknown THEN withhold a global readiness claim BECAUSE repository scope is not deployment scope.
- IF the successor requires a different event contract THEN map that event explicitly BECAUSE replacing an import can leave application state updates broken.
- IF a consumer can migrate only through an untested adapter THEN keep its acceptance pending BECAUSE proposed compatibility is not observed compatibility.
- IF removal approval is absent THEN prepare the recommendation without removing the component BECAUSE migration evidence and release authority are separate.

## Output template
```text
Retirement boundary: <component, revisions, decision state; up to three lines>
Consumer handoff: <up to eight rows; attach remaining consumer inventory>
Consumer | Required behavior | Successor evidence | Migration action | Acceptance status
Sequence: <up to six ordered shared and consumer steps>
Blockers: <up to six distinct gaps, with owner or proposed role>
Removal gate: <supplied criteria, evidence and decision still needed; up to four lines>
Recovery: <preserved baseline and rollback condition; up to three lines>
```

## Quality checklist
- [ ] The retirement state and authority are explicit.
- [ ] Direct consumers and shared wrappers are distinguished.
- [ ] Replacement parity is tied to behavior rather than appearance alone.
- [ ] Each consumer has a concrete migration action or an unresolved gap.
- [ ] Acceptance checks exercise the relevant user task.
- [ ] Proposed adapters are not counted as demonstrated compatibility.
- [ ] Missing downstream inventory limits the readiness conclusion.
- [ ] Removal evidence is separate from approval to release.

## Anti-patterns
- **Import-only migration:** the old name disappears while events change silently. Fix: compare user-visible behavior and state updates.
- **Announcement equals removal:** a notice is treated as evidence that all teams migrated. Fix: retain a per-consumer acceptance ledger.
- **Replacement optimism:** a successor is assumed to cover every extension. Fix: check wrappers and explicitly unsupported behaviors.
- **Unowned gap:** a blocker has no next decision or evidence request. Fix: identify the supplied owner or propose a responsible role for confirmation.
- **Forced deadline:** a familiar sunset interval is invented. Fix: use the organization's actual approved transition policy.

## Worked example
**Input:** Fictional team Rowan proposes retiring Choice-A in favor of Choice-B. Screen Find uses a single choice and the supplied Choice-B contract supports it. Screen Filter requires several simultaneous choices, which Choice-B explicitly does not support. Both screens are only an inventory excerpt. No edits or runtime tests have been performed, and removal approval is absent.

**Output:**
```text
Retirement boundary: Choice-A to Choice-B; retirement proposed, affected revisions unspecified.
Consumer handoff:
Consumer | Required behavior | Successor evidence | Migration action | Acceptance status
Find | One selected option and application update | Supplied Choice-B single-choice contract | Map props/events and compare selection before/after | Proposed; runtime check pending
Filter | Several simultaneous choices | Choice-B explicitly lacks this behavior | Retain Choice-A pending alternate composition or owner-approved redesign | Blocked
Sequence: Confirm revisions and complete inventory; prepare Find mapping; implement on authorized branch; test selection/event updates; resolve Filter gap; review removal evidence.
Blockers: Filter multi-choice gap; unknown downstream consumers; no tested mapping; no removal approval. Component owner role proposed for decisions.
Removal gate: Not ready; obtain the actual policy and authorization after consumer evidence is reconciled.
Recovery: Preserve Choice-A baseline and consumer mappings; revert a tested migration if its selection behavior regresses under the project's recovery process.
```

**Bad output:** “Replace every Choice-A import with Choice-B and remove the old package.”
This breaks a known supported behavior and assumes authority and inventory completeness.

## Edge cases
- A wrapper adds a behavior the base component lacks: document the wrapper contract and test the composed successor, not merely the new base component.
- A consumer is dormant but still distributed: ask the owning team whether it must remain compatible; absence from recent activity is not proof it can be ignored.
- A critical gap has no approved replacement: keep removal blocked for that use and preserve an explicit exception instead of claiming a completed migration.
- Documentation uses the old component but runtime code does not: revise examples deliberately and verify they teach the supported new path.

## Test case
**Input:**
> Fictional team Elm reports that code search finds no old component imports, but a shared wrapper is published to unknown external consumers. The successor changes its selection event payload. No consumer test has run.

**Assertions:**
1. Does not equate the search result with complete migration.
2. Identifies wrapper and downstream coverage as unresolved.
3. Requires an explicit event mapping and observed consumer acceptance check.
4. Leaves removal readiness and authorization pending.
