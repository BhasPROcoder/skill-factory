---
id: IPR-003
name: transactional-edit-history-branching
domain: Interactive Prototype Behavior
subdomain: Edit history
version: 1.0
description: Implement and test undo and redo history when multi-step editing must preserve transaction boundaries and discard abandoned redo branches after a new edit.
triggers: ["prototype undo redo", "group edits into one undo action", "test redo after a new edit", "define editor history boundaries", "avoid history snapshot mutation"]
not_for: ["reverting external payments or messages", "version-control branch management", "collaborative editing conflict resolution", "restoring persisted form drafts [IPR-001]"]
requires: []
risk_level: medium
---

# Transactional Edit History Branching

## Purpose
Create a runnable history model in which each undo action reverses one user-meaningful editing transaction. Keep document history separate from transient interface state and external actions, and make redo behavior explicit when editing continues from an earlier state.

## Inputs to collect
1. **Editable document state** — identify the content properties history should restore. Default: required; the reference model uses one fictional text value rather than assuming a complex document schema.
2. **Transaction boundaries** — obtain which grouped operations should undo together, such as a completed drag or a formatting command. Default: one explicit committed edit per history entry; no invented typing-time interval.
3. **Transient state** — identify selection, hover, loading or navigation state that should be outside content history. Default: exclude it unless the product explicitly defines its restoration behavior.
4. **History lifetime** — obtain reset, document-switch and retention rules. Default: one in-memory document session; no persistence or universal maximum history size.
5. **External effects** — identify publishing, file writes or other side effects triggered by editing. Default: local undo does not reverse those effects; their actual recovery contract is separate.

If a required input is missing and has no safe default, ask in one message, max 3 questions. Establish the document and transaction model before promising that an operation is reversible.

## Procedure
1. Define the history state as past snapshots, current document and future snapshots. Choose a representation whose old snapshots cannot be changed through shared mutable references.
2. Specify the commit boundary in user terms. Treat intermediate drag positions or provisional dialog values as a preview when the supplied interaction calls for one undoable transaction.
3. Implement undo by transferring the current snapshot to future and restoring the most recent past snapshot. When past is empty, return an unchanged state rather than creating a fictitious operation.
4. Implement redo as the inverse transfer for the stored branch. ⚠️ A new content edit after undo must clear the abandoned future; retaining it would permit replaying a state from a different editing path.
5. Specify no-op behavior. The reference model ignores a commit identical to current content, preserving the existing redo branch; change this only if the product has a meaningful non-content transaction to record.
6. Implement the Python 3 reference below and execute the assertions. Its snapshots are immutable strings, so it deliberately does not demonstrate deep copying of nested mutable documents.
7. Adapt transactions to the actual schema and interaction. For nested documents, test that later changes cannot mutate stored snapshots; for grouped editing, commit only the accepted final state and leave canceled previews out of history.
8. Connect button availability and labels to the model. Undo is available when past exists; redo is available when future exists; the next operation label should reflect the actual stored transaction if labels are implemented.
9. Exercise the real interaction separately when available. Verify grouped actions, canceled previews, boundary clicks and document switches without implying that a local history restoration reverses an external publication.

```python
def start(text=""):
    if not isinstance(text, str):
        raise ValueError("reference snapshots must be strings")
    return (), text, ()

def commit(history, text):
    if not isinstance(text, str):
        raise ValueError("reference snapshots must be strings")
    past, current, future = history
    if text == current:
        return history
    return past + (current,), text, ()

def undo(history):
    past, current, future = history
    if not past:
        return history
    return past[:-1], past[-1], (current,) + future

def redo(history):
    past, current, future = history
    if not future:
        return history
    return past + (current,), future[0], future[1:]

h0 = start("Seed")
h1 = commit(h0, "Seed garden")
h2 = commit(h1, "Paper garden")
assert redo(undo(h2)) == h2
back = undo(h2)
assert commit(back, back[1]) == back
branch = commit(back, "Stone garden")
assert branch[2] == () and redo(branch) == branch
assert h0[1] == "Seed" and h1[1] == "Seed garden"
assert undo(h0) == h0 and redo(h0) == h0
try:
    commit(h0, {"text": "unsupported mutable snapshot"})
except ValueError:
    pass
else:
    raise AssertionError("unsupported snapshot accepted")
print("edit history checks passed")
```

For a grouped operation, keep preview content outside this tuple and call commit once with the accepted final value. Canceling the operation discards the preview and leaves history unchanged. This explicit boundary is preferable to inventing a timing rule when the product has supplied none.

## Decision rules
- IF a new content edit follows undo THEN clear the previous future branch BECAUSE those snapshots describe the abandoned path rather than the new transaction sequence.
- IF a proposed edit leaves document content unchanged THEN preserve history under the reference policy BECAUSE an empty transaction should not destroy an otherwise usable redo action.
- IF a compound operation is canceled before acceptance THEN discard its preview without a commit BECAUSE canceled provisional state is not a completed user action.
- IF a stored snapshot can be mutated through another reference THEN change the snapshot representation BECAUSE history must describe the earlier state rather than a shared object that keeps changing.
- IF the action already caused an external effect THEN distinguish local reversal from that effect's recovery BECAUSE restoring editor content does not unsend or unpublish it.

## Output template
```text
Document boundary: <content schema, lifetime and excluded effects; three lines maximum>
Transactions: <up to six operation, preview, commit and cancel rules>
History model: <runnable code or implementation reference>
Executed trace: <up to eight event -> current/past/future observations>
Checks: <up to six assertions and observed outcomes>
UI integration: <button state, grouping and remaining checks; up to four lines>
Limits: <unsupported persistence, collaboration or external reversal; two sentences>
```

## Quality checklist
- [ ] Stored snapshots cannot be changed by later edits through shared references.
- [ ] Each undo step corresponds to a defined transaction boundary.
- [ ] Undo and redo at empty boundaries leave state unchanged.
- [ ] A genuine new edit after undo clears the old redo branch.
- [ ] No-op commits follow an explicit policy and have a tested result.
- [ ] Canceled previews do not become committed history entries.
- [ ] Local reversal is separated from external effects.
- [ ] Model tests and actual interface tests are reported separately.

## Anti-patterns
- **Snapshot aliasing**: history stores repeated references to one changing object. Fix: use immutable snapshots or a tested independent-copy strategy.
- **Zombie redo**: a branch survives a different content edit. Fix: clear future on the new transaction.
- **Mouse-move history**: every intermediate preview becomes a separate undo step despite a grouped-action requirement. Fix: commit the accepted operation once.
- **Boundary fabrication**: clicking unavailable undo adds a new entry. Fix: preserve history at the empty boundary.
- **External reversal claim**: local undo is described as retracting a published result. Fix: disclose the actual side-effect state and its separate recovery process.

## Worked example
**Input:**
> Fictional editor Grove begins with Seed, commits Seed garden, then Paper garden. The user undoes once, commits the unchanged Seed garden, and then commits Stone garden. Only the Python model is available; no publication occurs.

**Output:**
```text
Document boundary: Grove single text document in memory; external publication is absent and outside local history.
Transactions: Each explicit changed text commits once; identical text is a no-op; previews commit only on acceptance and disappear on cancel.
History model: start, commit, undo and redo functions in the supplied reference.
Executed trace: Seed -> Seed garden -> Paper garden; undo restores Seed garden with Paper garden in future; identical commit preserves that future; Stone garden commit clears it; redo then leaves Stone garden unchanged.
Checks: Undo/redo round trip passes; no-op preserves branch; changed edit clears branch; empty boundaries remain unchanged; prior strings remain intact; mutable snapshot input is rejected.
UI integration: Enable undo when past exists and redo when future exists; rendered buttons and gesture grouping remain untested.
Limits: This checks a local single-document model. Persistent history, collaborative editing and external reversal are not implemented or claimed.
```

**Bad output:**
> After editing Stone garden, redo Paper garden from the old branch because it is the latest saved version.

This confuses saved chronology with the user's current transaction branch and restores an abandoned state.

## Edge cases
- **Document switch**: keep separate history identities or explicitly reset under the supplied policy; never apply one document's past to another.
- **Large grouped command**: retain one accepted before/after transaction when that matches the requested undo behavior, and test internal preview cancellation separately.
- **History capacity**: collect the product's memory or retention policy, then test eviction boundaries; do not invent a universal number of entries.
- **Save without content change**: treat saving and editing as distinct events unless the product explicitly makes save a content transaction.
- **Remote edits arrive**: leave the single-user model's guarantee bounded and request the application's collaboration strategy before adapting history.

## Test case
**Input:**
> Fictional editor changes A to B to C, undoes to B, previews D but cancels, then commits E. Show which operations preserve redo and which remove it, with executable checks.

**Assertions:**
1. Canceling the preview leaves B current and C available for redo.
2. Committing E clears the C redo branch.
3. A later redo cannot replace E with C.
4. The output identifies model checks separately from interface and external-effect behavior.
