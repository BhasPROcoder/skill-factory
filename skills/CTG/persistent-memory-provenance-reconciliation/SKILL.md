---
id: CTG-004
name: persistent-memory-provenance-reconciliation
domain: Applied AI Workflow Engineering
subdomain: Context
version: 1.0
description: Produce persistent memory provenance reconciliation from explicitly permitted memory location; use when this decision must be made from explicit evidence.
triggers: ["persistent memory provenance reconciliation", "help with persistent memory provenance reconciliation", "review my persistent memory provenance reconciliation", "prepare persistent memory provenance reconciliation", "check persistent memory provenance reconciliation"]
not_for: ["Create a temporary task handoff [CTG-005]", "Organize general personal reference storage [GPR-009]"]
requires: []
risk_level: medium
---

# Persistent memory provenance reconciliation

## Purpose
Produce a usable persistent memory provenance reconciliation from the supplied material, keeping observed behavior separate from a proposed design. The deliverable should let another practitioner identify the next decision and reproduce the evidence check without assuming an unavailable platform, tool, or permission.

## Inputs to collect
1. **Task material** — explicitly permitted memory location; existing entries and source references; retention scope; conflicting or stale updates; these determine whether the method applies. Default: unknown, with unsupported portions left provisional.
2. **Acceptance boundary** — the outcome the user needs, the permitted work, and any consequential constraints. Default: prepare a reviewable artifact from supplied evidence, with no external execution implied.
3. **Evidence provenance** — where observations came from, their version or date when relevant, and which checks actually ran. Default: supplied text only, not independent verification.
4. **Available environment** — supported tools, runtime, and source access when execution matters. Default: a portable plan and offline fixture, not a claim that integration exists.
If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue independent parts without filling the missing answer from memory.



## Procedure
1. Separate durable preferences, current project state, dated observations, and unsupported inferences in the existing entries.
2. Attach source and observation context to each candidate retained fact before merging it with another entry.
3. Resolve conflicting claims using their relevance and authoritative evidence rather than automatically preferring the newest timestamp.
4. Draft minimal edits that preserve unresolved conflicts, remove redundant wording, and avoid retaining unnecessary sensitive details.
5. Apply changes only within the permitted memory scope while retaining an appropriate recoverable prior version.
6. Check that indexes still resolve and that a future reader can distinguish a preference, a temporary condition, and an open question.
7. ⚠️ Check each factual conclusion against the specific evidence inspected; label proposals and unexecuted checks instead of presenting a plausible plan as a result.
8. Produce the artifact in the output template and revise any item that fails the quality checklist.

Use this task prompt with the real inputs:
```text
Perform persistent memory provenance reconciliation for the supplied task material.
Keep the stated acceptance boundary and distinguish observations, proposed actions, and unresolved facts.
Return Scope, Evidence, Decision, Artifact, Verification, and Next action.
Do not invent missing measurements or imply that a proposed action was executed.
```

For any current provider feature, runtime interface, rate, or external requirement, check the current value in its official documentation and the actual configured environment. If access is unavailable, write `[VERIFY: the exact current requirement and its responsible official source]`. A general method does not guarantee a provider implements a feature or that a local environment supports it.

The following Python 3 standard-language fixture checks one narrow invariant in the fictional example. Save and run it with the available Python 3 interpreter, record the interpreter version actually used, and keep execution results separate from code merely shown in a document. It does not exercise a real model, user interface, or external system.
```python
entry = {'review': 'delayed', 'delivery_evidence': None}
status = 'complete' if entry['delivery_evidence'] else 'unknown'
assert status == 'unknown'
```

## Decision rules
- IF a deadline elapsed without outcome evidence THEN retain completion as unknown BECAUSE time passing does not prove delivery.
- IF a one-time choice conflicts with an explicit standing preference THEN record the local exception unless the user changed the preference BECAUSE contextual behavior need not redefine a durable rule.
- IF evidence from different versions conflicts THEN preserve the conflict and identify the relevant version BECAUSE combining incompatible observations can produce a false conclusion.
- IF a necessary verification cannot run THEN keep the dependent status provisional BECAUSE an absent check is neither a pass nor a demonstrated failure.

## Output template
```text
Scope: <one sentence naming the decision and boundaries>
Evidence: <up to four inspected inputs and their limits>
Decision: <supported choice or explicit provisional status>
Artifact: <the actual task-specific contract, ledger, protocol, or composition; not a promise to create it>
Verification: <executed checks and results; separately list pending checks>
Next action: <responsible role, one startable action, and observable completion evidence>
```
Keep the first response within the task's useful review size: summarize repeated evidence and retain source references rather than copying an entire log. Include enough artifact detail to act without guessing a critical condition. If additional evidence is needed, state which decision it could change.

## Quality checklist
- [ ] The scope matches the user's decision rather than the source author's original personal situation.
- [ ] The artifact contains concrete states, fields, criteria, or actions appropriate to this task.
- [ ] Every observed fact is traceable to an inspected input.
- [ ] Proposed changes and pending checks are visibly distinguished from executed work.
- [ ] Each task-specific conditional branch was considered.
- [ ] Changing external facts have a current official source check or remain unresolved.
- [ ] Arithmetic and fixture assertions have been checked before reporting a result.
- [ ] The next action names a role and observable completion evidence without expanding authorization.

## Anti-patterns
- **Task-specific shortcut**: turning inferred personal traits into permanent facts or deleting unresolved state merely because it is old. Fix: use the task-specific procedure and retain the missing evidence explicitly.
- **Universal threshold**: importing an arbitrary limit from another project. Fix: obtain the actual acceptance criterion and explain its scope.
- **Artifact substitution**: writing advice to create a deliverable instead of the deliverable. Fix: include the concrete fields, rules, or draft needed for this case.
- **Execution inflation**: describing a proposed test as successful. Fix: state the actual command or observation evidence, or mark it pending.

## Worked example
**Input:**
> Fictional user Rina permits editing a project memory file. An older entry says the draft is due Friday; a newer note says review is delayed. Neither contains delivery evidence. A duplicate preference entry repeats that Rina wants concise summaries.

**Output:**
```text
Scope: Apply persistent memory provenance reconciliation to this fictional case only.
Evidence: The supplied fictional observations and constraints; no live system or current external rule has been independently checked.
Decision: Use the bounded result below and retain its explicitly stated unknowns.
Artifact: Proposed retained preference: concise summaries, supported by explicit preference entry; merge the duplicate wording in the proposed edit. Project state: review delayed according to the newer note. Completion: unknown; no delivery evidence supplied. Historical due day remains dated context, not proof of a missed or completed handoff. The proposed memory edit is limited to the permitted project file and retains the conflicting timeline references for later reconciliation. No file edit is claimed to have occurred.
Verification: The supplied observations support this provisional artifact. The offline fixture can check its narrow invariant; real integration and any unprovided measurements remain pending.
Next action: The responsible practitioner reviews the artifact against the named missing evidence, performs the pending task-specific check, and retains the resulting output before changing its status.
```

**Bad output:**
> Everything is ready. Apply the same configuration everywhere; no further evidence is needed.

This fails because it erases the case's unresolved conditions, replaces a bounded result with a universal claim, and implies verification that did not occur.

## Edge cases
- **Only a summary is available**: identify which conclusion relies on the summary and request the original excerpt if its wording changes the decision.
- **A proposed action exceeds authority**: finish the reviewable artifact and leave that action unexecuted until the required authorization exists.
- **The environment changes after a check**: retain the old result with its configuration and rerun only checks affected by the changed condition.
- **Evidence is too sparse for comparison**: state the smaller supported conclusion and name a discriminating next observation rather than ranking unsupported options.

## Test case
**Input:**
> Fictional user permits updating one project note, but related memories live elsewhere. Reconcile a contradiction without editing unrelated stores or inferring that an elapsed deadline proves completion.

**Assertions:**
1. The answer follows the specified output labels in order and contains a concrete task artifact.
2. It applies the task-specific decision branches to the new case rather than repeating the worked example.
3. It preserves missing or conflicting evidence and does not claim an unexecuted check passed.
4. It gives a bounded next action whose completion can be observed.
