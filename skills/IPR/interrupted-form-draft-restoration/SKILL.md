---
id: IPR-001
name: interrupted-form-draft-restoration
domain: Interactive Prototype Behavior
subdomain: Draft recovery
version: 1.0
description: Implement and test a form-draft recovery model when interrupted editing must resume without overwriting newer work or treating a saved draft as a submitted record.
triggers: ["prototype form draft recovery", "restore interrupted form edits", "test resume editing behavior", "keep newer input during restore", "separate draft save from submission"]
not_for: ["reviewing field purpose [MPU-004]", "restoring infrastructure backups [TDV-004]", "designing sensitive-data storage security", "resuming repository work [CTG-003]"]
requires: []
risk_level: medium
---

# Interrupted Form Draft Restoration

## Purpose
Create a runnable transition model that distinguishes saved drafts, current edits, restoration and submission. Use it to decide what the interface may restore and which fields require renewed input, without claiming the prototype supplies persistent storage or production data protection.

## Inputs to collect
1. **Form scope** — obtain the form identity, record identity and schema revision; these prevent restoring a draft into an unrelated task. Default: no restoration until identities are known.
2. **Recoverable fields** — obtain the explicit set of fields permitted in the draft and those that require renewed input. Default: no fields retained until the product owner defines the set; do not infer persistence permission from editability.
3. **Interruption cases** — identify navigation, reload or session return cases in scope. Default: an in-memory interruption model only, with browser and storage behavior untested.
4. **Conflict policy** — establish how saved values interact with edits made since recovery began. Default: preserve current edits and leave conflicting saved values available for explicit comparison.
5. **Completion signal** — obtain the application's authoritative submission-success event. Default: no submission is assumed from a button click, validation pass or draft save.

If a required input is missing and has no safe default, ask in one message, max 3 questions. Continue only the independent model structure while a policy is unresolved.

## Procedure
1. Define a draft envelope containing form identity, record identity, schema revision and permitted values. Keep a local editing revision separate from those identities so a new edit can invalidate an in-flight restoration decision.
2. Classify fields as recoverable, re-enter or unavailable under the supplied policy. Show this classification to the owner before adding persistence behavior; a prototype may use fictional values throughout.
3. Specify a restoration offer rather than silently merging values. Name the draft's source and scope in the offer, and distinguish declining the offer from deleting the underlying draft.
4. ⚠️ Check identity and schema when offering and again when accepting recovery. Bind the offer to those identities: switching records can preserve the same local revision number. Hold mismatches for a supplied migration or explicit review.
5. Define conflict behavior for edits made while the offer is open. Advance the revision for edits, recovery-policy changes and submission transitions so existing offers require renewed review. Keep revision identity unique while any old offer can still arrive.
6. Implement a small pure transition function before connecting storage or UI. The Python 3 model below accepts only string-valued fields and an explicit allowlist; its tuple token is a fictional local revision contract, not an authentication mechanism.
7. Execute the included traces and adapt them to actual field identities. Extend the assertions when the product permits per-field merging, multiple drafts or schema migration rather than pretending this whole-form model implements those features.
8. Connect accepted transitions to visible copy: draft available, restored for review, cannot restore and submission pending or confirmed. State which fields need renewed input after restoration.
9. Verify the rendered interaction separately in the authorized target environment. Check that offered values, preserved edits and renewed-input prompts match the model; report a model-only pass when no interface was exercised.

```python
def offer(saved, current, allowed):
    identity = ("form", "record", "schema")
    if any(saved.get(k) != current[k] for k in identity):
        return None
    return (tuple(current[k] for k in identity), current["revision"],
            {k: v for k, v in saved["values"].items()
             if k in allowed and isinstance(v, str)})

def accept(current, proposed):
    identity = tuple(current[k] for k in ("form", "record", "schema"))
    if (proposed is None or proposed[0] != identity
            or proposed[1] != current["revision"]):
        return current, "review-required"
    updated = dict(current)
    updated["values"] = dict(proposed[2])
    updated["revision"] += 1
    updated["submitted"] = False
    return updated, "restored-for-review"

current = dict(form="F", record="A", schema="S",
               revision=0, values={}, submitted=False)
saved = dict(form="F", record="A", schema="S",
             values={"title": "Paper garden", "code": "fictional"})
proposal = offer(saved, current, {"title"})
restored, state = accept(current, proposal)
assert state == "restored-for-review"
assert restored["values"] == {"title": "Paper garden"}
assert restored["submitted"] is False
assert offer(dict(saved, record="B"), current, {"title"}) is None
edited = dict(current, revision=1, values={"title": "New work"})
assert accept(edited, proposal) == (edited, "review-required")
assert accept(current, None) == (current, "review-required")
switched = dict(current, record="B", values={"title": "Other record"})
assert accept(switched, proposal) == (switched, "review-required")
print("draft transition checks passed")
```

The reference covers one editing lifetime with a fixed allowlist. Its caller must advance the revision for every transition that invalidates recovery. On closing and reopening the same record, discard old offers before resetting revisions, or add a unique lifetime identifier to the offer and acceptance guard. Otherwise a reused identity and revision can accidentally accept an earlier session's offer. The snippet does not implement storage events, submission callbacks or policy updates itself.

## Decision rules
- IF the stored draft has another record or schema identity THEN decline automatic restoration BECAUSE identical field labels do not establish compatible meaning.
- IF editing changed after an offer was generated THEN preserve current values and reopen comparison BECAUSE accepting an old snapshot would erase newer work.
- IF a field is outside the recovery allowlist THEN omit it from restored values and request renewed input when needed BECAUSE available storage is not permission to retain every field.
- IF a draft restores successfully THEN present it for review rather than mark it submitted BECAUSE recovery and authoritative acceptance are separate transitions.

## Output template
```text
Recovery scope: <form, record, schema and tested environment; up to three lines>
Field policy: <up to eight field/group classifications and supplied basis>
Transitions: <up to eight event -> guard -> visible state entries>
Implementation: <runnable model or exact implementation reference>
Executed traces: <case, input events, observed result and assertion; up to six>
Open decisions: <up to three policy questions or None>
Verification boundary: <model, interface and persistence checks distinguished; two sentences>
```

## Quality checklist
- [ ] Form, record and schema identity are checked at offer creation and acceptance.
- [ ] The recovery field set is explicit rather than inferred from all form fields.
- [ ] Acceptance detects edits made since the offer was generated.
- [ ] Restored values remain unsubmitted until authoritative acceptance.
- [ ] Missing or incompatible drafts have a visible resolution path.
- [ ] Tests exercise normal restore, identity mismatch and intervening edits.
- [ ] A model run is not represented as a browser or durable-storage test.

## Anti-patterns
- **Blind hydration**: saved keys overwrite the active form on load. Fix: offer recovery with identity and revision guards.
- **Label migration**: matching names justify a schema change. Fix: require a supplied migration rule or leave the draft for review.
- **Saved means sent**: recovery shows a submission receipt. Fix: retain draft state until the real completion event.
- **Token overclaim**: a revision number is described as access control. Fix: limit the model to editing order and use the actual application's authorization design separately.

## Worked example
**Input:**
> Fictional notebook prototype Cedar restores only title. Draft F/A/S contains title Paper garden and a code. An offer is created at revision 0. Before acceptance, the user edits title to New work, advancing revision to 1. No UI or storage integration is available.

**Output:**
```text
Recovery scope: Cedar form F, record A, schema S; Python transition model only.
Field policy: title recoverable; code excluded by supplied rule.
Transitions: offer at revision 0 -> user edit reaches revision 1 -> acceptance requires renewed review and retains New work.
Implementation: offer and accept functions in the supplied runnable model.
Executed traces: normal acceptance restores only title and remains unsubmitted; foreign record produces no offer; intervening edit returns review-required with New work unchanged; missing offer returns review-required.
Open decisions: None for the bounded in-memory policy.
Verification boundary: Python assertions exercise the stated state transitions. No rendered UI, durable storage or real submission was tested.
```

**Bad output:**
> Restore every saved value and show “Submitted” so users know their work survived.

This overwrites active work, bypasses the field policy and invents a submission event.

## Edge cases
- **Several available drafts**: show their supplied identities and provenance for selection; do not pick one solely from an ambiguous filename.
- **Schema changed**: preserve the original draft and use only a supplied, tested migration; otherwise offer human-readable review without automatic application.
- **Submit response is delayed**: keep submission pending separately from saved-draft status and reconcile the actual response before clearing a draft.
- **Fields become conditionally inapplicable**: re-evaluate dependencies after restoration and expose excluded values for review only when the policy permits it.

## Test case
**Input:**
> Fictional form F for record B receives a draft belonging to A. The user also edited B while the restore offer was loading. Build a recovery decision and run a model trace; no record migration is authorized.

**Assertions:**
1. No A values are applied to B.
2. Current B edits remain intact.
3. The output separates draft recovery from successful submission.
4. Executed model checks and untested UI or storage behavior are identified separately.
