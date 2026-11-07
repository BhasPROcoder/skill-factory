# GAS-011 independent forward tests

Evaluator: finish_prt, separate from author. Read the skill and applied its procedure to the fresh fictional requests below. These are actual text outputs produced during this review, not model-runtime or grading-system tests. No grade or external record was changed.

## Ordinary: authorized unchanged evidence

Request: Fictional learner Elm submits attempts First and Second for the Harbor task. Receipt R identifies First before Second. The rubric is unchanged: Sources asks for attributable source descriptions; Reasoning asks for an explanation of the conclusion. First section S lists source descriptions, and Second section S is identical. Reviewer Dana's First judgment on Sources was sufficient. First section R has a bare conclusion, and Second section R adds an explanation. Instructor instruction I permits carrying forward unchanged criterion evidence but requires fresh review of revised evidence. Prepare the handoff.

Actual output:
```text
Review scope: Compare Elm's Harbor task First and Second using the supplied unchanged rubric and instructor instruction I.
Attempt order: First then Second, established by receipt R.
Policy basis: Instruction I permits carrying forward unchanged criterion evidence and requires review of revised evidence. This record does not alter grades.
Criterion | Prior attempt and evidence | Revised attempt and evidence | Change | Review disposition
Sources | First section S; attributable source descriptions; Dana judged sufficient | Second section S, identical supplied content | Unchanged | Carry forward Dana's First judgment under instruction I with its original anchor
Reasoning | First section R, bare conclusion | Second section R adds explanation | Revised | Fresh reviewer assessment against the Reasoning descriptor; no improvement judgment inferred
Dependencies: None identified in supplied artifacts.
Pending: None.
Handoff: Reviewer retains the anchored Sources disposition and evaluates Second section R before issuing the revised Reasoning judgment.
```

Assertions: PASS—sequence cites receipt; carry-forward cites permission and original judgment; revised explanation is routed for review rather than awarded a mark; no invented policy. No arithmetic required.

## Missing input: unreadable replacement and unattributed feedback

Request: Fictional learner Ash provides readable document X and unreadable file Y. A note says “your comparison lacks detail” but identifies no attempt. The instructor says Y was received after X. No rubric or resubmission instructions are supplied. Produce only the available evidence record.

Actual output:
```text
Review scope: Record Ash's supplied X and unreadable Y, preserving comparison limits.
Attempt order: X then Y according to the instructor's receipt confirmation; receipt does not establish inspectability.
Policy basis: Rubric and resubmission instructions unavailable. Criterion judgments, carry-forward and grade decisions remain pending.
Criterion | Prior attempt and evidence | Revised attempt and evidence | Change | Review disposition
Unidentified criterion | X readable; comment lacks attempt and location anchor | Y received but unreadable | Not assessable | Organize artifacts only; do not attribute the comment or compare performance
Dependencies: The comment's criterion and attempt relationship are unresolved.
Pending: Instructor/reviewer: provide the applicable rubric and resubmission instructions. Reviewer: identify the attempt and location behind the comparison comment. Submission owner: provide an accessible copy of Y tied to the recorded submission.
Handoff: Assigned reviewer obtains accessible Y and missing anchors before conducting criterion-level comparison.
```

Assertions: PASS—received order preserved without treating Y as reviewed; unreadability is explicit; the comment remains unanchored; three consolidated requests and no invented penalty. No arithmetic required.

## Edge: partial replacement with explicit composite basis

Request: Fictional learner Fern supplies original O with Methods section M and Results section R. Instructor instruction P explicitly says only Results is resubmitted and Methods in O remains operative. Replacement N contains revised Results only. Receipts establish O before N. Same rubric applies. O Methods cites dataset D-old; N Results cites D-new. No evidence states that the original method works with D-new. Prior Methods judgment on O was sufficient. Produce the lineage handoff.

Actual output:
```text
Review scope: Compare Fern's permitted partial resubmission using O Methods and N Results as the explicit composite basis.
Attempt order: O then N, established by receipts.
Policy basis: Instruction P retains O Methods and replaces Results with N Results. It does not establish that the retained method supports the changed dataset.
Criterion | Prior attempt and evidence | Revised attempt and evidence | Change | Review disposition
Methods | O section M uses D-old; prior judgment sufficient | O section M remains operative under P; N Results uses D-new | Method text retained; dataset dependency changed | Preserve original judgment as history; request dependency review before treating it as sufficient for the composite basis
Results | O section R | N Results cites D-new | Replaced Results and dataset reference | Fresh Results review against unchanged rubric, including method compatibility
Dependencies: O Methods for D-old must be compared with N Results for D-new; compatibility is not evidenced.
Pending: Instructor/reviewer: does O Methods support the D-new analysis, or is an authorized method revision needed?
Handoff: Reviewer assesses the composite basis and resolves dataset compatibility without silently replacing retained Methods or issuing an unsupported grade.
```

Assertions: PASS—partial submission does not create a missing-Methods error; exact composite basis is explicit; changed dependency prevents blind carry-forward; no unauthorized revision or grade. No arithmetic required.

## Review result

Three fresh cases applied; no blocker found. The scope differs from rubric design and general feedback rewriting: it preserves attempt-level evidence lineage, authorized carry-forward and composite assessment basis. Specific statements in the skill are procedural or fictional; current grading rules are supplied inputs. The tests establish text-level handling of these scenarios only.
