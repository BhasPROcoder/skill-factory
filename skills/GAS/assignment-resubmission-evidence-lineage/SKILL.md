---
id: GAS-011
name: assignment-resubmission-evidence-lineage
domain: Learning Assessment
subdomain: Analysis
version: 1.0
description: Reconcile assignment attempts, criterion evidence and feedback when a resubmission must be reviewed without mixing versions or inventing grading policy.
triggers: ["compare this assignment resubmission", "which attempt did this feedback assess", "track revised criterion evidence", "reconcile assignment versions", "prepare a resubmission review", "carry forward unchanged assessment evidence"]
not_for: ["designing a rubric [GAS-001]", "rewriting feedback comments [GAS-007]", "moderating different reviewers [GAS-008]", "deciding academic misconduct"]
requires: []
risk_level: low
---

# Assignment Resubmission Evidence Lineage

## Purpose
Build a criterion-level record connecting each assessment observation to the actual assignment attempt it describes. Preserve the original judgment while identifying what the revised work makes available for a new review; this record does not itself authorize a grade change.

## Inputs to collect
1. **Attempt artifacts** — obtain each supplied submission with its stable identifier, attachment list and recorded submission event; these establish what was handed in. Default: none, required for comparison; a filename alone does not establish order.
2. **Criterion versions** — collect the rubric or assessment brief used for each attempt because wording changes can invalidate a direct comparison. Default: unknown; organize artifacts but leave criterion conclusions pending.
3. **Feedback anchors** — collect comments, criterion identifiers, cited passages and the attempt each reviewer saw. Default: no prior feedback available, not evidence that no feedback existed.
4. **Resubmission scope** — obtain the instructor's current instructions about eligible sections, carried-forward judgments and replacement attempts. Default: no grade or eligibility decision; request the applicable course instructions from the responsible instructor.
5. **Reviewer and audience** — identify who will use the record and which learner identifier is sufficient. Default: private reviewer working note with a pseudonymous learner label.

If a required input is missing and has no safe default, ask in one message, max 3 questions. Combine requests for related artifacts and identify which comparison must wait.

## Procedure
1. Inventory the supplied attempt artifacts without changing their names or contents. Assign readable local labels and record the source identifier, file components and claimed sequence beside each label.
2. Establish the attempt order from submission records or an explicit instructor confirmation. ⚠️ When a modified timestamp or a filename containing “final” conflicts with the submission record, preserve the discrepancy rather than silently treating that file as the latest accepted attempt.
3. Attach each prior comment to the attempt actually reviewed and to an observable location in that attempt. Keep comments with unknown attempt identity in an unresolved group; do not attach them to whichever passage looks similar.
4. Align the assessment criteria across attempts. Mark each criterion unchanged, explicitly mapped by the instructor, or not comparable because the supplied descriptors or task changed. Retain both criterion labels when a mapping exists.
5. Compare evidence within each comparable criterion. Quote a short supplied excerpt or identify an exact page, paragraph, figure or attachment; record whether relevant evidence was added, removed, revised or left unchanged. Do not equate changed wording with a stronger performance.
6. Determine the review action using the supplied resubmission instructions. Distinguish a proposed carry-forward from an authorized carry-forward, and a new observation from a new mark. If eligibility instructions are absent, recommend review routing without inventing an attempt limit or penalty.
7. Check whether changed evidence affects another criterion. For example, a revised conclusion may depend on a replaced data table; cite that dependency and request review of both locations rather than carrying the old interpretation forward automatically.
8. Produce the lineage table and unresolved questions. Keep the original feedback intact in its source artifact and make each proposed disposition reversible by retaining its basis.
9. Check the record against the actual attachments. ⚠️ A revision note claiming an appendix was added is not the appendix; if it is missing from the supplied attempt, mark that evidence unavailable and request the artifact.

## Decision rules
- IF the reviewer cannot identify the attempt behind a comment THEN leave its disposition unresolved BECAUSE applying it to a different attempt can misrepresent what was assessed.
- IF a criterion or underlying task changed without a supplied mapping THEN separate the observations rather than asserting improvement BECAUSE the judgments may address different performance requirements.
- IF relevant evidence is unchanged and carry-forward is explicitly permitted THEN retain the prior judgment with its attempt anchor BECAUSE unnecessary reassessment can obscure which decision was actually made.
- IF a revision removes previously supporting evidence THEN flag a fresh review even when the learner describes the change as cosmetic BECAUSE the current artifact must support the current observation.
- IF the requester wants a grade change but supplies no grading authority or policy THEN return the evidence record and pending decision owner BECAUSE an organized comparison is not permission to alter results.

## Output template
```text
Review scope: <one sentence; learner label, assignment and supplied attempts>
Attempt order: <up to five labels and evidence for sequence; unresolved if unknown>
Policy basis: <up to two sentences; supplied instruction and decision boundary>
Criterion | Prior attempt and evidence | Revised attempt and evidence | Change | Review disposition
<one row per criterion; each cell at most 35 words>
Dependencies: <up to four evidence links, or None identified in supplied artifacts>
Pending: <up to three questions with responsible role; None if resolved>
Handoff: <one sentence identifying the next reviewer action; no unsupported grade>
```
Use up to twelve criterion rows in the first response. For a longer assignment, state which criteria are deferred and preserve their order in a continuation; never present a selected subset as a complete review.

## Quality checklist
- [ ] Every attempt label resolves to an actual supplied artifact or a clearly missing item.
- [ ] The sequence basis is identified independently of ambiguous filenames.
- [ ] Each prior comment has an attempt anchor or an explicit unresolved status.
- [ ] Criterion changes and missing mappings remain visible.
- [ ] Revised evidence is located in the revised artifact rather than inferred from a revision note.
- [ ] Carry-forward decisions cite the supplied permission and original judgment.
- [ ] A changed supporting artifact triggers a dependency check.
- [ ] No eligibility rule, grade adjustment or submission penalty was invented.

## Anti-patterns
- **Latest-file guessing**: using a file's name to establish accepted submission order. Fix: reconcile the actual submission event or ask the instructor.
- **Comment migration**: pasting old comments onto new text without an anchor. Fix: identify the reviewed attempt before deciding whether feedback still applies.
- **Revision equals improvement**: treating any edit as criterion satisfaction. Fix: compare the criterion requirement with the revised evidence.
- **Silent grade replacement**: converting an evidence comparison into a changed mark. Fix: name the authorized grading step separately.
- **Missing attachment optimism**: crediting an appendix mentioned only in a cover note. Fix: record the missing artifact and leave its contribution unassessed.

## Worked example
**Input:**
> Fictional learner Lark submits Cedar Seminar report attempts A and B. Supplied receipt records establish A before B. The unchanged rubric has Claim and Evidence criteria. A paragraph 2 states a claim without explanation; its table 1 supports the evidence criterion. B paragraph 2 adds an explanation but omits table 1. Prior feedback on A says “explain the claim”; its Evidence judgment was sufficient. The instructor permits carrying forward unchanged criterion evidence. No marks are requested.

**Output:**
```text
Review scope: Compare Lark's Cedar Seminar report attempts A and B against the supplied unchanged criteria.
Attempt order: A then B, established by the supplied receipt records.
Policy basis: Instructor permits carrying forward unchanged criterion evidence. This is a review handoff, not a grade change.
Criterion | Prior attempt and evidence | Revised attempt and evidence | Change | Review disposition
Claim | A paragraph 2; claim without explanation; anchored feedback requests explanation | B paragraph 2; explanation added | Added explanation | Reviewer should assess the explanation against the Claim descriptor; satisfaction not presumed
Evidence | A table 1; prior judgment sufficient | B supplied report omits table 1 | Supporting table removed | Do not carry forward as unchanged; review current evidence and resolve whether the omission was intended
Dependencies: B explanation may rely on omitted table 1; reviewer must check that connection in the supplied paragraph.
Pending: Instructor: is omitted table 1 intended to remain part of B through a separately accepted attachment?
Handoff: Assigned reviewer assesses B's explanation and resolves the missing table before issuing a criterion disposition.
```

**Bad output:**
> B is newer and answers the feedback, so carry forward Evidence and increase Claim.

This fails because it credits a revision without criterion review and carries forward evidence that the revised artifact no longer contains.

## Edge cases
- **Identical filenames**: distinguish artifacts by supplied submission identifiers and recorded content; if identity remains ambiguous, request a disambiguated copy before comparison.
- **Partial resubmission**: retain the original sections only if the supplied instructions say they remain operative; record the resulting composite assessment basis explicitly.
- **Changed group membership**: request the instructor's attribution basis before transferring feedback between group and individual attempts; do not infer authorship from file possession.
- **Unreadable revised artifact**: record receipt separately from inspectability and request an accessible replacement without making a grading judgment about the fault.
- **Learner contests original feedback**: preserve the original record and route that challenge separately from describing revisions; do not rewrite history as if the disputed judgment never existed.

## Test case
**Input:**
> Fictional learner River supplies an original essay and a file named final-new. A comment says the conclusion lacks support but has no attempt identifier. The revised task changes the criterion from describing a source to evaluating it. No rubric mapping or resubmission policy is supplied. Prepare the review record.

**Assertions:**
1. The output leaves accepted attempt sequence unresolved unless submission evidence is supplied.
2. The unanchored comment is not automatically assigned to either essay.
3. The changed criterion is not treated as a directly comparable improvement measure.
4. Pending requests identify the missing sequence, feedback anchor and applicable assessment instructions without inventing a grade.
