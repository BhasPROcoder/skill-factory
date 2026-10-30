"""Explicit fictional premises and substantive scope repairs from independent review.

These additions are authored fixture inputs, never assertions about real people.
"""

INPUT_ADDITIONS = {
 'in-information-request-scope-draft': 'The request concerns the fictional Maple facility during its autumn maintenance review; the precise dates still need confirmation.',
 'in-government-appointment-preparation': 'She has prepared copies but has not checked whether originals are required.',
 'us-agency-appointment-access-plan': 'The appointment itself has an official confirmation.',
 'us-service-denial-file-organization': 'Only the first page of the notice is available, without the review instructions.',
 'administrative-form-field-evidence-map': 'A current address statement is also supplied; its acceptability has not been checked.',
 'administrative-cover-note-draft': 'The office query and a labeled attachment are supplied for drafting, but transmission has not occurred.',
 'administrative-handoff-packet': 'The file includes a response draft but no sending receipt.',
 'policy-implementation-bottleneck-review': 'The fictional process log also shows that final processing starts late after attachment rework.',
 'policy-evidence-brief': 'A pilot report and regional demand records are supplied; the regional records contain no intervention comparison.',
 'accessible-learning-material-review': 'Its instructions also put several actions into one dense paragraph.',
 'feedback-comment-rewrite': 'A second comment says good work beside a comparison that names both sources without explaining why the contrast matters.',
 'assessment-moderation-session': 'The supplied disputed passage lists evidence but contains no explicit link; the reviewers disagree on whether the link may be inferred.',
 'exam-syllabus-coverage-map': 'The candidate also supplies flashcards and successful definition-recall attempts.',
 'exam-mock-review': 'A timing note records repeated revision of the earlier answer.',
 'exam-answer-structure-practice': 'The conclusion states a preference without relating it to any shared criterion.',
 'exam-time-allocation-rehearsal': 'In the supplied rehearsal log, no time remained for the review pass.',
 'research-pilot-protocol': 'The fictional pilot log records inconsistent interpretations and a skipped routing question that sent a participant down the wrong path.',
 'research-feasibility-gate-review': 'A public archive is available, although it would support only a narrower question.',
 'review-inclusion-criteria-design': 'A separate abstract has unclear outcome coverage and needs full-text review.',
 'abstract-screening-decision-log': 'A second abstract explicitly describes a different, excluded population.',
 'research-source-credibility-review': 'The report identifies its issuing organization.',
 'conflicting-study-findings-map': 'The reports concern different service offices.',
 'claim-source-traceability-audit': 'The writer also generalizes to every setting although the source covers a single setting.',
 'narrative-evidence-synthesis': 'Design A is described through qualitative accounts of access; Design B uses completion records.',
 'resume-bullet-evidence-rewrite': 'The candidate confirms that the team used the checklist and that it documented handoff responsibilities; no effect on consistency was measured.',
 'career-cover-letter-evidence-draft': 'The candidate confirms a motivation to make shared work clear and personally organized handoff notes showing the next responsibilities.',
 'interview-story-evidence-bank': 'She listed pending tasks, asked owners to confirm their next steps, and later introduced an ownership checklist.',
 'career-portfolio-case-study': 'The stated design problem was confusing intake notes.',
 'career-transition-evidence-plan': 'She supplies event schedules and exception notes as evidence of her previous work.',
 'personal-task-inbox-triage': 'The printer item refers to an existing order whose current status is unknown.',
 'personal-weekly-review': 'A confirmed appointment will reduce the next available work block.',
}


def apply(records):
    by_name = {r['slug']: r for r in records}
    for name, addition in INPUT_ADDITIONS.items():
        by_name[name]['situation'] += ' ' + addition
    by_name['in-information-request-scope-draft']['rows'][0] = 'Decision record;Named facility and review period;Dates and office unconfirmed;Confirm dates and record holder'
    by_name['resume-bullet-evidence-rewrite']['rows'][1] = 'Result;Checklist used by team;Documented handoff responsibilities in a team-used checklist.;No claim of improved consistency or speed'
    by_name['weekly-capacity-planning']['rows'][1] = 'Drafting;Uninterrupted work requested;Find an actual free block before scheduling;Reduce scope if none exists'
    by_name['research-protocol-decision-log']['rows'][1] = 'Original categories;Earlier definitions retained;Original timing unverified;Locate dated protocol before claiming prespecification'

    r = by_name['research-interview-guide']
    r.update(title='Repeated-wave interview protocol', inputs=['Prior-wave interview and participant reference','Stable research question','Follow-up consent and contact constraints'],
      steps=['Separate core questions needed for within-participant comparison from exploratory probes', 'Retain the wording and ordering of the core unless a documented comprehension problem requires revision', 'Ask about concrete events since the previous wave without presuming improvement or deterioration', 'Record changed context and instrument revisions separately from reported experience changes', 'Code missing waves and withdrawals explicitly instead of constructing a continuous narrative'],
      rules=['a core question changes=>flag the comparability break=>wording effects can resemble experience changes','a participant misses a wave=>retain the missing observation=>silence does not establish stability'],
      columns=['Protocol part','Stable element','Wave-specific probe','Comparison limit'],
      situation='Fictional researcher Lena follows the same service users over time. Her prior core prompt was Tell me about your most recent booking. One participant misses the follow-up; no new response is available.',
      rows=['Core prompt;Most recent booking;What changed since our previous conversation?;Do not assume a change occurred','Missed wave;Participant reference retained;No interview fabricated;Experience during gap unknown'],
      trap='rewriting every question between waves and attributing every response difference to the participant',
      test='Fictional researcher receives a changed interview guide and a missing follow-up wave, then asks for a continuous account of improvement.')

    r = by_name['survey-question-wording-review']
    r.update(title='Questionnaire cognitive pretest', inputs=['Draft item and answer choices','Intended interpretation','Consented pretest participants'],
      steps=['Ask the participant to answer the item without teaching its intended meaning', 'Invite a paraphrase to identify how the wording was understood', 'Probe what event or information the participant retrieved to answer', 'Ask how the participant formed the judgment and mapped it to an answer option', 'Separate observed response-process problems from proposed wording changes and retest the revision'],
      rules=['the participant selects the expected answer for a different reason=>record the mismatch=>answer agreement does not prove comprehension','a probe teaches the intended meaning=>label subsequent responses as influenced=>coached interpretation cannot validate the original item'],
      columns=['Response stage','Probe','Observed evidence','Revision test'],
      situation='Fictional researcher tests an item asking whether a service was fast and helpful. No participant has answered yet; this is a pretest protocol, not a findings report.',
      rows=['Comprehension;What does this question ask in your own words?;Not collected;Check whether speed and helpfulness conflict','Answer mapping;How did you choose that option?;Not collected;Check whether available choices express the judgment'],
      trap='reporting a predicted wording problem as an observed participant difficulty',
      test='Fictional researcher wants to call an item validated because a participant selected the expected option, without asking how the answer was produced.')

    r = by_name['study-design-question-fit']
    r.update(title='Observational design inference-boundary review',
      columns=['Threat','Available evidence','Proposed repair','Claim boundary'],
      rows=['Concurrent changes;Before-and-after totals only;Seek contemporaneous context and a suitable comparison if available;Describe timing without attributing the change to redesign','Measurement comparability;Definitions not supplied;Confirm the same attendance definition across periods;Magnitude is provisional until measures align'],
      steps=['State the causal or descriptive claim proposed for the already chosen observational design','Map when exposure and outcome are measured and which populations are compared','Identify plausible selection, measurement, timing, and concurrent-change threats grounded in the supplied design','Specify a feasible design repair or sensitivity check for each consequential threat','Write the strongest claim the available evidence can support and list stronger claims that remain untested'],
      rules=['other changes coincide with exposure=>retain them as competing explanations=>timing alone cannot isolate an effect','a proposed adjustment lacks measured variables=>mark it infeasible with current data=>naming a statistical remedy does not supply its inputs'],
      trap='selecting a sophisticated method by name without checking what the observational design measures')

    r = by_name['research-source-credibility-review']
    r.update(title='Publication version and correction-status check', inputs=['Publication identity or supplied copy','Claim being cited','Authoritative publication record access'],
      steps=['Match title and authors to the exact publication record without assuming similar titles identify the same work','Determine whether the supplied copy is a draft, accepted manuscript, or published version using its own provenance','Inspect the publisher or issuing body record for linked corrections, withdrawals, or retractions','Compare any confirmed notice with the particular claim being used','Record checked sources and unresolved status explicitly and update citation use only to the extent supported'],
      rules=['the official record cannot be accessed=>leave correction status unverified=>a missing check is not a clean record','a correction addresses a different claim=>record the actual scope=>one notice does not automatically invalidate every statement'],
      columns=['Identity element','Supplied evidence','Status','Required check'],
      situation='Fictional reviewer Bo has an undated report copy naming an organization but no link to its official version record. No external record has been accessed.',
      rows=['Version;Undated copy;Unverified;Match against issuing body publication record','Correction status;No notice supplied;Not checked;Inspect authoritative linked notices'],
      trap='claiming a publication has no correction because no notice appears in a detached copy',
      test='Fictional reviewer has a downloaded draft and asks you to certify there are no corrections without access to its publication record.')

    r = by_name['exam-study-capacity-plan']
    r.update(title='Mastery-dependent study sequence', inputs=['Diagnostic attempts','Topic prerequisites','Available study blocks'],
      steps=['Identify which prerequisite errors block the target exam task from the supplied diagnostic work','Group tasks by prerequisite rather than by chapter order alone','Place a short diagnostic and repair opportunity before dependent practice','Define an observable transfer attempt that permits advancing to the next task','Reallocate remaining blocks when evidence shows a prerequisite is still unstable instead of copying the original timetable'],
      rules=['a prerequisite error persists=>repair it before increasing dependent complexity=>more advanced attempts may repeat the same obstacle','a familiar item is correct but a changed item fails=>retain transfer practice=>recognition is not yet flexible mastery'],
      columns=['Learning dependency','Diagnostic evidence','Study sequence','Advance condition'],
      situation='Fictional candidate Nia can recall definitions but misidentifies claims in unfamiliar paragraphs. She has study blocks available; no durations or exam weighting are supplied.',
      rows=['Claim identification;Unfamiliar paragraph error;Contrast claim with supporting example;Correctly explain distinction in a new paragraph','Argument comparison;Requires claim identification;Practice after prerequisite check;Compare claims using explicit common criterion'],
      trap='assigning equal time to every topic without checking prerequisite bottlenecks',
      test='Fictional candidate memorizes definitions but fails unfamiliar applications and wants to progress to advanced tasks because the calendar says so.')

    r = by_name['weekly-capacity-planning']
    r['steps'] = ['Place fixed commitments on the actual personal calendar before assigning discretionary work','Identify free blocks and the attention or energy conditions each can realistically support','Match a bounded task output to a suitable block without overlapping its time','Leave carryover or interruption space based on the person observed availability','Remove or renegotiate tasks that have no feasible placement and review the next calendar against actual completion']

    r = by_name['uncertainty-to-information-question']
    r.update(title='Factual question source-routing map',
      steps=['State each unresolved factual question without turning it into a strategic assumption test','Identify which record holder or observation could actually establish the fact','Separate direct source access from hearsay and repeated copies of the same account','Order dependent questions so that an answer can identify the next responsible source','Stop the lookup when the fact is established for the needed context or access is exhausted and record the remaining uncertainty'],
      columns=['Question','Capable source','Answer dependency','Stopping condition'],
      rows=['What access arrangement applies to this room?;Venue accessibility contact or current room specification;Confirm exact room before using a general venue statement;Record current applicable answer or unresolved access','What color is the wallpaper?;Current room image;No stated access-decision dependency;Defer unless a relevant need is supplied'],
      trap='treating a confident intermediary as the record holder without checking their access to the requested fact')
    by_name['poem-reading-performance-markup']['rows'][0] = 'Capitals;Emphasis;YOU;Names recipient'
    by_name['workplace-disagreement-message']['situation'] += 'Those participants have told Nia about their unreliable access.'
