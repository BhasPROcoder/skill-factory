# Independent TDS-012 review

Reviewed 2026-11-11. Scope: original draft, actual neighboring procedures, fictional scenario application, and embedded executable example. No real personal data, legal interpretation, external contacts, or artifact mutation was used. Registry untouched.

## Scope comparison

COP-003 traces consent and purpose from collection through recipients, retention and withdrawal; its main decision concerns the processing flow and legal questions. TDS-002 traces source and transformation records into artifact provenance, retaining unknown parents. TDS-003 inventories intended-use permissions and separates access from redistribution. TDS-012's narrower operational artifact is a per-version disposition plan after approval: distinguish actual contribution from mere dependency, preserve shared data, handle retention/restore constraints, and define per-node closure evidence. This is a materially different downstream decision task, provided its state and source-coverage defects are repaired.

## Executable check

Executed the Python block extracted directly from the draft using the available Python interpreter. Output:

```text
['features', 'masked-copy', 'research-export', 'training-snapshot']
```

The embedded assertion passed. The graph traversal returns recorded descendants and excludes unrelated summary-view; it does not establish row membership, deletion, or completeness. This is a graph fixture only.

## Scenario applications

### Ordinary approved request

Fictional input: approval A covers record r in raw V1; manifest links raw V1 to clean V1; membership evidence identifies r in both; jurisdiction/context supplied for owner review; no execution evidence. Data owner owns raw and pipeline owner owns clean. Prepare a plan.

Applied output: approval A and source r anchor scope. Raw V1 needs a scoped proposed action and owner check. Clean V1 is an evidenced descendant with confirmed membership; proposed rebuild/update requires an unaffected-record check and owner execution. Both remain proposed; neither is performed. Current legal requirements remain owner verification, not an inferred entitlement.

Finding: procedure supports this interpretation, but the worked example and descendant-focused matrix omit raw entirely. A weaker follower can omit the source action. Add a source-artifact row and explicit source-plus-descendant coverage rule, or evidence that the source is already handled/out of this operational scope.

### Approval absent

Fictional input: a request asks to remove r from all data but provides no approved decision or scope.

Applied response: Which authorized decision defines the covered records and artifacts? What jurisdiction and agreement govern this request? Who owns the source and descendants? Do not propose artifact changes until the scope is approved. Pass: missing approval stops dependent planning without inventing authority.

### Shared derivative

Fictional input: approved r is one of two records, r and s, in clean V1; aggregate A combines both; reconstruction inputs exist, but owner approval for rebuilding A is absent.

Applied output: clean V1 and A remain distinct rows. Membership and transformation evidence support affected contribution, but whole-artifact deletion is not proposed. Rebuild A from approved unaffected inputs only after owner approval; require validation that s remains represented and the requested r contribution is addressed. Proposed action is conditional, not completed. Pass.

### Backups and restore

Fictional input: backup B contains raw V1 and is described as immutable; no retention exception or restore policy supplied.

Applied output: B is an unresolved special-handling node. Preserve the constraint, identify backup owner/privacy review, and request applicable retention and restore handling. Do not bypass controls or state that a source update proves backup erasure. Pass. No particular retention duration or legal conclusion introduced.

### Training snapshot and possible model influence

Fictional input: manifest links clean V1 to training snapshot T; no model artifact or training run is supplied.

Applied output: T is an evidenced descendant whose record membership still needs evidence. Model existence, dependency, and influence remain unanswered questions for the owner. Source deletion demonstrates neither influence removal nor a need for a particular retraining/unlearning method. Pass in procedure; the draft test assertion demanding a trained-model node overstates supplied evidence. Replace it with a requirement to keep model linkage/influence unresolved without inventing an artifact.

### Performed but unverified action

Fictional input: an authenticated operation log shows the approved source update ran successfully, but no post-change artifact inspection exists.

Applied interpretation under step13: preserve performed evidence and mark verification pending. Applied interpretation under the completion-evidence decision rule: missing completion evidence means planned/unresolved. These instructions conflict. Mark this a blocking defect: an executed operation must not become an unexecuted plan merely because independent verification is absent. Specify separate execution evidence and verification evidence fields, or an explicit performed-unverified state.

## Findings

1. Blocking: preserve known performed state when verification is missing; do not downgrade it to planned. Reevaluate the performed/unverified scenario after repair.
2. Blocking: source-artifact action coverage is absent from the worked example, despite approved source-record scope. Include raw explicitly, with action and closure evidence or a justified prior-completion exclusion.
3. Repair: test assertion4 must not infer a trained model from a training snapshot alone.
4. Repair: the empty-field versus absent-source edge case references an unspecified rule and appears unrelated to this withdrawal procedure. Replace it with the concrete execution-versus-verification case.
5. Passed: semantic distinction, supplied graph traversal, shared-data preservation, approval gate, retention escalation, and cautious model-influence language.

Recommendation: hold acceptance until the state and source-coverage corrections are reviewed. Do not mark this original draft audited or behaviorally passed as a whole.

## Re-review after coordinator repairs

Inspected the amended procedure, decision rule, worked-example tables, edge case, and test assertion. Source artifacts are now explicitly included before descendant traversal; raw appears in both example tables with exact matching pending and a conditional scoped removal action. The performed-state rule now retains evidenced execution while marking verification pending; the unrelated empty-field edge was replaced by the corresponding performed/unverified case. Test assertion4 now treats model existence and lineage as questions unless evidenced.

Reapplied ordinary and execution-state scenarios: raw and clean each receive a proposed action with ownership and closure evidence; an execution log preserves performed state while absence of artifact inspection leaves verification pending. Reapplied snapshot-only scenario: T is a documented descendant; no trained model is invented. Shared-derivative and backup scenarios retain their prior correct boundaries. The executable graph code was unchanged from the successful run recorded above.

The original blockers are resolved. No remaining substantive blocker found in this bounded review. This is instruction and fictional-fixture evidence, not proof of a real withdrawal, legal compliance, production graph completeness, or removed model influence.
