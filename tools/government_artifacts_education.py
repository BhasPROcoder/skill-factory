"""Concrete proposed education artifacts; observations remain in supplied cases."""

ARTIFACTS = {
'learning-objective-rewrite': '''Revised objective: Given a short argument, identify its claim and supporting reason, then explain how the reason is intended to support the claim.
Proposed assessment stimulus: Our club should meet in the larger room because the current room cannot seat everyone.
Learner prompt: Mark the proposed action, mark its reason, and explain their relationship.
Evidence criterion: distinguishes the recommendation from the seating reason. A definition alone does not meet the objective.''',
'prerequisite-knowledge-check': '''Proposed prerequisite probe: The club should move its meeting because the present room cannot seat everyone. For example, some members stood during the last meeting.
Prompt: Identify the main claim, its reason, and the example. Explain your labels.
Interpretation: a learner who finds the details but treats the standing example as the main recommendation needs claim/example contrast before paragraph synthesis.
Follow-up: use a new short paragraph without labels. These are proposed checks, not observed new learner results.''',
'worked-example-lesson-sequence': '''Proposed teaching texts: A says the club needs a larger room because members stood; B says the current room is adequate because it fits the usual attendance.
Model: compare their meanings of adequate and the attendance evidence they use; neither text alone establishes which attendance is relevant.
Completion task: supply the missing comparison question: Which attendance pattern should the decision cover?
Independent task: compare new texts that disagree about an opening time because they describe different users.
Check: learner names the relevant difference, not just that authors disagree.''',
'misconception-contrast-activity': '''Proposed contrast:
A: The room is ideal. It is excellent, splendid, wonderful, and clearly the best place for every meeting.
B: The room fits the stated attendance and has the required seating.
Before explaining, ask: Which argument has more relevant support, and which exact words make you think so?
Discussion: A repeats judgments; B supplies relevant conditions, subject to verification.
Transfer: give a new pair with different lengths. Ask whether length alone settles support quality.''',
'lesson-practice-alignment-review': '''Replacement practice: Read: We should extend the opening hours because customers asked for later access. Identify the claim, the support, and one missing fact that could change the decision.
Proposed response criteria: identifies the opening-hours recommendation; names the reported requests; asks about relevant missing evidence such as actual demand or operating constraints.
Keep vocabulary recall as preparation, then require individual analysis before the final critique task.
Do not count listening to the teacher's critique as the learner's own practice.''',
'scaffold-fading-plan': '''Trial task: organize a new paragraph using the learner's own sequence, while retaining the existing sentence starters.
Removed support: supplied outline.
Retained support: sentence starters only.
Observe: whether the ideas form a coherent sequence without an outline.
If sequence breaks down: ask the learner to explain the intended order, then restore an outline prompt only for that difficulty.
Next trial: consider reducing sentence starters after independent organization remains evident. No trial result is assumed.''',
'lesson-question-sequence': '''Diagnostic: What makes a source trustworthy for this particular question?
Evidence probe: Point to something in the source that supports your judgment.
Proposed contrast: one polished source gives no basis for its claim; a plain source explains its method and limits. Which features matter for our question, and why?
Revision: Would you change your original criterion? Explain.
Transfer: apply your revised criterion to a new source. Separate appearance from evidence and relevance.''',
'accessible-learning-material-review': '''Revised worksheet instruction: Read each item. Write the category name beside it. Explain one choice using the category definition.
Presentation rule: show the category name wherever color previously carried the distinction; retain color only as additional information.
Check version: remove color and verify that labels and instructions still identify the categories.
Unresolved: the actual category names and any additional learner access needs must come from the teacher's material; do not invent them.''',
'project-learning-milestone-design': '''Milestone: source selection. Deliverable: an annotated source list with each proposed exhibit claim, the source used, and the reason that source is suitable.
Feedback gate: revise unsupported selections before building the exhibit text.
Milestone: exhibit draft. Deliverable: each displayed claim linked to its supporting source.
Individual evidence: each learner explains one inclusion or exclusion decision in their own words.
Completion: a reviewer can trace claims and distinguish individual reasoning from group presentation polish.''',
'learning-reflection-prompt-design': '''Prompt: Choose one passage from your essay that you think needs work. What exactly is it trying to establish?
Evidence prompt: Point to the wording or missing support that caused your concern; do not use bad as the entire explanation.
Revision prompt: What single change would address that concern, and how would a reader notice the difference?
Process prompt: If drafting stalled, describe where; propose an outline only if it addresses that obstacle.
Check: compare the revision with the identified issue.''',
'analytic-rubric-design': '''Proposed criterion: connection between claim and evidence.
Evidence linked: identifies relevant evidence and explains why it supports the claim.
Evidence listed: includes relevant evidence but leaves the connection unexplained.
Claim only: supplies a conclusion without supporting evidence.
Keep length outside this criterion; additional detail earns no automatic credit.
Calibration request: apply these descriptors to supplied contrasting samples and revise any ambiguous boundary before use.''',
'assessment-task-validity-review': '''Revised task frame: Using the supplied passage, identify the proposed cause, describe the claimed effect, and explain which information supports that relationship. Name an alternative explanation if the passage leaves one open.
Access revision: explain unfamiliar terms that are incidental to causal reasoning; preserve the causal relationships the learner must analyze.
Scoring boundary: judge the reasoning demonstrated, while recording any remaining vocabulary barrier.
The actual source passage is still required; this is a proposed prompt, not a finding about unseen responses.''',
'multiple-choice-item-review': '''Proposed replacement item: You need evidence about what happened during a meeting. Which source most directly documents that event?
A. A contemporaneous account that describes the meeting and identifies its basis.
B. A later opinion that does not identify what happened at the meeting.
C. A general description of how meetings usually work.
Provisional key: A, because it directly addresses the stated evidence task; still inspect reliability and completeness before relying on it.
This illustrates a stated criterion, not a universal ranking of source types.''',
'short-answer-scoring-guide': '''Required element: identify the disagreement between the supplied sources.
Acceptable evidence: a correct paraphrase of what each source says; exact model-answer wording is unnecessary.
Required reasoning: explain a relevant contextual difference supported by the sources.
Partial response: names the disagreement but does not explain it; recognize identification while keeping explanation incomplete.
Alternative valid route: accept another supported explanation and record its evidence rather than rejecting it for being absent from the initial key.''',
'formative-exit-ticket-design': '''Proposed exit ticket: Our reading group should choose a quieter room because members could not hear the last discussion. Underline the claim, circle the reason, and explain the link.
Response branch: correct labels and explanation -> attempt comparison using a new argument.
Response branch: reversed labels -> compare a recommendation with a supporting observation before retrying.
Response branch: unclear explanation -> ask a short follow-up before assigning a concept difficulty.
These are planned teaching responses, not collected results.''',
'learner-error-pattern-analysis': '''Follow-up probe: label claim and evidence in a short text comparable to the successful item; then try another with only one added demand.
Record separately: label accuracy, the learner's explanation, and the changed demand.
If confusion appears even in the simpler case: revisit the claim/evidence distinction.
If it appears only after added complexity: investigate that demand before inferring general conceptual failure.
Do not close the diagnosis from the single reversed-label response.''',
'feedback-comment-rewrite': '''Replacement for unclear: This claim has no supporting source in the passage reviewed. Add relevant evidence, then explain how it supports the claim. I should be able to trace the claim to that evidence.
Optional comparison feedback, only if the comparison is actually present: You name both sources; now explain why their difference matters to your conclusion.
Do not present the optional comment as an observed strength unless the learner's work supports it.''',
'assessment-moderation-session': '''Discussion prompt: Show the words where the essay connects evidence to its conclusion. Is that connection explicit, inferred, or absent?
Proposed descriptor clarification: listing evidence is different from explaining why it supports a claim.
Review record: each reviewer records the same cited passage, criterion interpretation, and remaining disagreement.
Recheck: independently judge another anonymized sample after agreeing the descriptor.
Do not average away the original disagreement or claim improved agreement before the recheck.''',
'portfolio-evidence-selection': '''Selected evidence: individual draft, annotated to identify the learner's own argument choices.
Conditional evidence: group poster, only with an account and supporting evidence of the learner's contribution relevant to writing.
Missing evidence: a revision paired with the earlier individual draft, if development is a portfolio criterion.
Annotation prompt: What decision did I make here, what evidence shows it, and what does this artifact not establish?
Do not substitute visual polish for individual writing evidence.''',
'assessment-results-communication': '''Draft explanation: In this short assessment, Lio identified the claims accurately. The responses did not yet explain how the supporting evidence connects to those claims. This describes the supplied work, not a fixed limit on ability.
Next practice: choose a new short claim and write a sentence explaining how a specific piece of evidence supports it.
Review: check the link in the new response before deciding whether further support is needed.''',
'exam-syllabus-coverage-map': '''Coverage entry: topic explanation; notes available; no explanation practice supplied; readiness remains un demonstrated.
Next resource requirement: a task that requires an independently written explanation and a basis for checking its reasoning.
Separate entry: definition recall, only if actual recall evidence is supplied; do not infer mastery from notes.
Official-source check: confirm the current syllabus version and the exact task boundary before treating the map as complete.'''.replace('un demonstrated','undemonstrated'),
'exam-study-capacity-plan': '''Proposed sequencing rule: check the prerequisite skill before assigning dependent exam practice. If the diagnostic shows a missing prerequisite, place a focused repair task in a reliable study block, followed by a fresh check; release the dependent task only when that check supports readiness.
Nia's first repair: distinguish the recommendation from a supporting example in a short paragraph. Use a new paragraph for the advance check; require both a correct label and an explanation.
If a prerequisite is already demonstrated: move directly to the next dependent task rather than filling time with comfortable repetition.
Next dependent task: compare arguments only after the claim-identification check supports readiness. Available block durations and exam weighting remain unknown.''',
'exam-practice-error-log': '''Entry: selected a familiar method without checking its applicability condition.
Repair prompt: Before solving, write the condition that must hold for this method and identify whether the question supplies it.
Retest: use a new question where the condition changes; require method selection and justification before calculation.
Closure rule: independent justification and a suitable method on the retest, not copying the earlier solution.
Arithmetic drills are not assigned without evidence of an execution error.''',
'exam-mock-review': '''Observed sequence: polishing an earlier answer consumed time; a later long response remained blank.
Next-mock experiment: draft an answer sufficient for the task, then move on under a provisional checkpoint compatible with the exam's actual navigation rules.
Record: which task was left, why, and whether later work was attempted.
Review both coverage and answer quality before retaining the change; completion alone is not a quality guarantee.
No universal timing limit is inferred from this case.''',
'exam-retrieval-practice-design': '''Proposed card front: In the following text, identify the claim and the example, then explain the difference: The club needs a larger room. Last time, several members stood.
Back, hidden until response: the proposed need is the claim; the standing episode is an example supporting it. Equivalent wording is acceptable.
Retest prompt: use a new paragraph without visible labels.
Record independent recall separately from recognizing the answer after revealing the back.''',
'exam-interleaved-practice-selection': '''Selection plan: choose unlabeled items requiring each already learned approach, plus an item with familiar wording but a different governing condition.
Before each solution, learner writes: The relevant condition is ...; therefore I choose ... .
Review columns: chosen method; condition cited; execution result; repair needed.
If the method is unfamiliar, supply an initial example before including it in mixed selection practice.
Actual subject problems are required; do not invent a method-specific answer key from keywords.''',
'exam-answer-structure-practice': '''Proposed answer outline:
Criterion: [common decision-relevant basis supported by the question].
Proposal A: evidence and implication on that criterion.
Proposal B: evidence and implication on the same criterion.
Comparison: the meaningful similarity or difference, with support.
Conclusion: judgment justified by the comparison and any stated limitations.
Repeat only for necessary criteria; two unrelated descriptions do not by themselves answer a comparison task.''',
'exam-time-allocation-rehearsal': '''Provisional rehearsal rule: on the first pass, move beyond an answer once it meets the task's essential demands; mark unresolved improvements for a permitted return.
Coverage gate: attempt the remaining required tasks before using remaining time to polish earlier wording.
Observation record: move-on decision, later-task coverage, and any loss of necessary reasoning.
Retain or revise the rule from the next comparable rehearsal. Use official navigation restrictions and actual timing records; no invented minutes per question.''',
'exam-final-review-triage': '''Priority task: annotate the conditions in fresh exam-style prompts before choosing an answer method.
Completion evidence: the candidate identifies the condition and uses it correctly in an independent attempt.
Lower-priority maintenance: brief checks of definitions already recalled reliably.
Stop or adjust: if condition errors persist, inspect the reasoning; do not replace targeted repair with an entire new resource collection.
Keep the review within the confirmed exam scope and actual remaining time.''',
'exam-day-logistics-checklist': '''Identification: unresolved; a friend's account is not the official requirement. [VERIFY: accepted identification and any exception process in the current official candidate instructions].
Venue: use the supplied official notice; compare with any later official update.
Travel or access: prepare from the confirmed venue or platform instructions.
Materials: pack only items confirmed permitted by the official instructions.
Blocked item: contact the official support route for clarification; do not promise that an unlisted substitute will be accepted.''',
}
