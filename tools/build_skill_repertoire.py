"""Author a small repertoire-engineering collection without registry mutation."""
import json
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DOMAIN = dict(code='SKR', name='Reusable Skill Engineering', macro='Prompt Engineering & LLM Ops', scope='Select distinct reusable procedures, generalize specialized workflows, and design independent behavioral checks with truthful evidence.', subdomains=['Selection','Generalization','Evaluation'])
RECORDS = [
dict(name='repertoire-gap-selection', title='Repertoire gap selection', subdomain='Selection', description='Choose useful additions to a skill repertoire by comparing decisions, required evidence, and deliverables against existing procedures.', inputs='candidate task requests; existing skill descriptions and representative procedures; intended users and observed unmet needs', goal='a justified add, extend, route, or defer decision for each candidate',
steps=[
'Express the candidate as a user situation, required decision, necessary inputs, and inspectable output; remove topic labels that do not change the work.',
'Find the nearest existing procedures using both task vocabulary and output vocabulary; record the actual candidates examined rather than claiming an exhaustive search.',
'Compare each nearby skill on decision rules, evidence prerequisites, failure handling, and deliverable structure; different names or industries alone do not establish a gap.',
'Describe the smallest case where the candidate requires a different action from its nearest neighbor; if no such case can be stated, propose routing or extension.',
'Check whether the added decision recurs in the supplied user needs or follows from a concrete workflow requirement; label predicted usefulness as a hypothesis when no usage evidence exists.',
'Choose add only when the distinct procedure is coherent enough to use independently; choose extend when a bounded branch fits the existing purpose without confusing selection.',
'Write a proposed trigger and an adjacent-task exclusion that would let another reader select the correct procedure in the contrast case.',
'Prepare a bounded validation task for the proposed addition and state the result that would cause you to merge, narrow, or abandon it.'],
rules=[('the candidate differs only in wording','route to the existing procedure','synonyms do not add a new decision capability'),('the different context changes a prerequisite or failure branch','compare that branch explicitly before deciding whether to extend or split','context matters when it changes action'),('the nearest existing skill has not been inspected','keep the uniqueness conclusion provisional','catalog labels can conceal shared procedures')],
case='Fictional library owner Mira has a skill for repairing survey wording and a proposed skill named questionnaire wording cleanup. Both identify double questions and repair response options. Another proposal observes how respondents interpret questions before changing them; no existing procedure for collecting that evidence has been found in the supplied catalog.',
artifact='Candidate: questionnaire wording cleanup. Disposition: route to survey wording repair. Difference test: none supplied; both change the same wording from the same inputs.\nCandidate: questionnaire cognitive pretest. Disposition: provisionally add. Distinct input: respondent explanations of comprehension, recall, judgment, and answer selection. Distinct decision: determine where interpretation fails before choosing a revision.\nTrigger: find out how respondents interpret this draft questionnaire. Exclusion: direct wording edits without respondent evidence use the existing repair skill.\nRevisit: inspect other research procedures before declaring the addition unique.',
result='Route the synonym proposal to the existing skill; investigate the evidence-collection procedure as a distinct addition.',
check='The comparison names a decision-changing contrast, not merely a different title.',
test='Fictional curator Noel proposes a new skill called contract summary cleanup, but its supplied steps match an existing contract summary review. A second candidate reconciles conflicting clause versions before summary. Classify the candidates from the supplied procedures without claiming legal correctness.'),
dict(name='specialized-workflow-generalization', title='Specialized workflow generalization', subdomain='Generalization', description='Turn an authorized specialized workflow into reusable instructions by preserving decision invariants and moving changing or case-specific facts into inputs and verification steps.', inputs='authorized source workflow; representative cases and failure examples; intended reuse scope and source-use constraints', goal='a portable procedure with explicit inputs, decision branches, and an example that does not mistake one case for a universal rule',
steps=[
'Confirm what material may be used and what may be retained in the resulting artifact; omit identifying or restricted details that are unnecessary for the reusable method.',
'Annotate each source step as a decision, evidence requirement, action, local convention, or incidental case fact; keep the original distinctions visible during extraction.',
'For each decision, state the condition that selects an action and the reason the action follows; avoid replacing judgment with an unexplained instruction to be careful.',
'Identify variables that change across intended uses, including jurisdiction, platform, recipient, version, deadline, and available authority; collect them as inputs with safe defaults or explicit questions.',
'Move any changing requirement into a verification instruction naming the responsible official source; do not copy a remembered value into the reusable rule.',
'Test the proposed invariant against a case with a different context and a case with missing evidence; narrow its scope when the same action no longer follows.',
'Draft a concrete output template and a clearly fictional worked artifact; label newly invented scenario details as fiction instead of attributing them to the source.',
'Review the abstraction for lost dependencies, unearned universal claims, and accidental copying of case-specific wording; retain source-use notes separately when needed.'],
rules=[('a source uses a local deadline or fee','replace the value with a current-source verification step','a reusable procedure must not freeze changing requirements'),('a rule fails when the recipient changes','make the recipient condition explicit or narrow the skill','one successful case does not establish a universal method'),('the source material cannot be reused as supplied','extract only an authorized general method or request suitable material','access alone does not establish permission to reproduce content')],
case='Fictional coordinator Inez has an authorized internal checklist for a permit application. It tells staff to copy a previously used fee, attach a site sketch, and record submission confirmation. The intended reusable workflow spans different authorities, whose current fee and attachment requirements have not been supplied.',
artifact='Inputs: responsible authority, application type, current official instructions, supplied supporting documents, and submission evidence. No jurisdiction default.\nInvariant: map each confirmed requirement to evidence before calling the pack ready.\nVerification branch: [VERIFY: current fee and attachment requirements in the responsible authority\'s official application instructions].\nPreparation rule: include a site sketch only when the verified instructions require it or the user has an appropriate separate reason to supply it.\nCompletion rule: distinguish prepared materials from submitted materials; record the actual confirmation if submission occurs.\nDraft output fields: requirement; official basis; supplied evidence; unresolved gap; next action. No fee amount is carried forward.',
result='Generalize evidence mapping and confirmation handling; keep authority-specific fees and attachments conditional.',
check='The draft contains no copied current fee or universal attachment requirement and distinguishes preparation from submission.',
test='Fictional operator Sana supplies a workflow that always emails a named manager for approval. Generalize it for teams with different approval owners, preserving the need for actual authority without inventing a role assignment.'),
dict(name='skill-forward-test-design', title='Skill forward-test design', subdomain='Evaluation', description='Design independent new tasks and checkable assertions to evaluate a skill, while separating test specifications, actual execution evidence, and unresolved reliability limits.', inputs='candidate skill and intended boundaries; risks and known failure modes; execution environment and permitted observations', goal='a forward-test specification and honest result ledger that can detect failures beyond repeating the worked example',
steps=[
'Extract the decisions and output invariants the skill promises, separating required behavior from illustrative choices in its example.',
'Design a fresh ordinary case with different surface details and evidence structure, so copying the worked example cannot satisfy it.',
'Create a boundary case that changes the decisive condition and therefore requires a different response, then state that contrast before any execution.',
'Create an insufficient-input case where a specific conclusion must remain unresolved; identify what independent work can still proceed.',
'Write observable assertions about evidence use, conditional decisions, output completeness, and forbidden unsupported claims; avoid demanding exact wording when equivalent reasoning is acceptable.',
'Prepare an evaluator prompt that cites the actual output for every judgment and records ambiguity rather than silently changing the expected answer.',
'Execute only in an available authorized environment; retain the task, skill version or snapshot, actual output, and evaluation basis when a run occurs.',
'Report each test as planned, executed with evidence, or blocked; revise the skill for demonstrated failures and rerun affected cases without claiming broader reliability than tested.'],
rules=[('the test repeats the worked example with renamed people','replace it with a new decision or evidence arrangement','memorized structure can hide a failure to apply the method'),('no execution output exists','report the test as planned or blocked','a test specification is not an observed pass'),('the answer differs in wording but satisfies the evidence and decision rules','evaluate the substantive assertions','verbatim matching can reject correct reasoning')],
case='Fictional reviewer Tomas evaluates a skill that resolves inconsistent contact records by asking the responsible owner, without assuming the newest document is correct. Its example compares a worksheet with an invoice. Tomas can design tests but has no execution output.',
artifact='Test A: a recent draft website lists one contact, while an owner-signed correction explicitly supersedes it. Expected: use the explicit correction within its stated scope, not recency alone.\nTest B: two current internal records disagree and neither has authoritative confirmation. Expected: preserve both and request owner confirmation; do not choose silently.\nTest C: only a directory title is supplied without any contact values. Expected: request the missing records and avoid inventing a discrepancy.\nLedger: A planned; B planned; C planned. Actual outputs: none supplied. Overall result: execution pending, no pass rate claimed.',
result='Prepare distinct tests and mark all results unexecuted until actual outputs are available.',
check='The report distinguishes expected behavior from observed output and contains no invented pass result.',
test='Fictional reviewer Oren has one output from a new boundary case and two tests that have not run. The output makes an unsupported assumption. Prepare an evidence-based ledger that neither counts unrun tests as passes nor generalizes one failure to all possible uses.')
]


def render(r, i):
    sid=f'SKR-{i:03d}'
    fm=dict(id=sid,name=r['name'],domain=DOMAIN['name'],subdomain=r['subdomain'],version='1.0',description=r['description'],triggers=[r['title'].lower(),f"help with {r['title'].lower()}",f"review my {r['title'].lower()}",f"prepare {r['title'].lower()}",f"apply {r['title'].lower()} to these materials"],not_for=[f"{x['title']} [SKR-{j:03d}]" for j,x in enumerate(RECORDS,1) if j!=i],requires=[],risk_level='low')
    front='\n'.join(f'{k}: {json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v}' for k,v in fm.items())
    steps='\n'.join(f'{j}. '+ ('⚠️ ' if j in (3,6) else '')+s for j,s in enumerate(r['steps'],1))
    rules='\n'.join(f'- IF {c} THEN {a} BECAUSE {b}.' for c,a,b in r['rules'])
    return f'''---
{front}
---

# {r['title']}

## Purpose
Produce {r['goal']}. Treat reusable skill quality as a question about decisions and evidence, not the number of files or the polish of their titles. Keep the result within the supplied repertoire and intended use rather than claiming universal coverage.

## Inputs to collect
1. **Task material** — collect {r['inputs']}. Default: none; request the material required for the selected decision instead of filling it with an imagined example.
2. **Intended user and context** — establish who will invoke the procedure, which decisions recur, and what they can observe. Default: a private review draft with no publishing or implementation authority implied.
3. **Evidence boundary** — distinguish original material, summaries, observations, and proposals. Default: only the supplied material is available; no unseen source has been inspected.
4. **Acceptance and constraints** — collect the expected artifact, source-use limits, and available testing capacity. Default: propose a bounded check and label it proposed rather than an established external standard.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent portions and name the missing input that blocks the remaining decision.

## Procedure
{steps}
9. Apply the decision rules to the actual case and fill the output template. Keep the decisive contrast visible so a reviewer can disagree with the reasoning without reconstructing hidden assumptions.
10. Run every quality checklist item. If a check fails, revise the affected claim or mark the dependent work unresolved; do not invent a successful result to complete the template.

Use this reusable reviewer prompt when handing off the artifact: "Read the supplied scope, inputs, procedure, and concrete output. Identify each decision-changing assumption. For every conclusion, quote the relevant supplied evidence or label the conclusion provisional. Describe a changed input that would require a different action. Do not treat an expected result as an observed result, and do not introduce external facts from memory. Return the unsupported claim, the missing evidence, and the smallest correction."

This prompt is an evaluation aid, not evidence that another reviewer has actually run. Record an independent review only when its output exists. For an external requirement, check the current responsible source and record the unresolved dependency when access is unavailable.

## Decision rules
{rules}
- IF a reviewer disagrees THEN compare the evidence and decision condition explicitly BECAUSE unexplained consensus or disagreement cannot establish which procedure is useful.
- IF the task requests a live change beyond the review THEN apply the user's authorized scope to that action BECAUSE designing reusable instructions does not itself authorize unrelated execution.

## Output template
```text
Decision: <one sentence selecting the disposition or readiness state>
Scope: <materials examined and intended reuse boundary; at most three sentences>
Evidence: <source labels and the decisive observations, up to six entries>
Artifact: <actual comparison, reusable procedure, or test specification; up to 600 words>
Check: <observable criterion and actual result if available; otherwise planned>
Unresolved: <missing inputs and smallest next action, up to four entries>
```

## Quality checklist
- [ ] The decision names a concrete disposition or readiness state.
- [ ] Scope identifies what was actually examined and what was excluded.
- [ ] Every observation is traceable to supplied material rather than an invented source.
- [ ] The artifact contains a usable procedure, comparison, or test rather than a promise to write one later.
- [ ] At least one changed condition would produce a clearly different action.
- [ ] Changing external requirements remain inputs or precise verification steps.
- [ ] Expected behavior is separate from any observed execution result.
- [ ] Unresolved dependencies have a specific next evidence request.

## Anti-patterns
- **Title counting**: treating another name as proof of another capability. Fix: compare the decision, inputs, and artifact with the nearest procedure.
- **Example worship**: promoting incidental details of one successful case into universal requirements. Fix: test the rule against a changed context and state its boundary.
- **Evidence laundering**: calling a draft, expectation, or plausible inference an observation. Fix: label its actual status and retain the supporting record.
- **Vague acceptance**: asking whether the skill seems useful without a concrete task. Fix: state what the user must be able to decide or produce and how that can be checked.
- **Overclaiming coverage**: claiming all cases or all neighboring skills were reviewed after a sample. Fix: name the actual scope and remaining comparison work.

## Worked example
**Input:**
> {r['case']}

**Output:**
```text
Decision: {r['result']}
Scope: The supplied fictional case only; external coverage and live performance are not assumed.
Evidence: The facts explicitly supplied in the fictional input; absent source material remains unavailable.
Artifact: {r['artifact']}
Check: {r['check']} This is the proposed acceptance criterion; no separate behavioral execution is claimed.
Unresolved: Obtain the missing comparison or execution evidence identified in the artifact before making a broader readiness claim.
```

**Bad output:**
> The skill is unique, generalized, and fully reliable because its title is new and its example looks correct.

This fails because a title does not establish a procedural difference, a single example does not establish transfer, and no observed execution evidence supports the reliability claim.

## Edge cases
- **Only descriptions are available**: perform provisional routing and request the nearest actual procedures before making a substantive uniqueness or generalization claim.
- **Source cases conflict**: preserve both and identify the contextual condition that might explain the difference; do not average incompatible actions into an unsupported rule.
- **Testing is unavailable**: deliver the test specification and identify execution as pending; a blocked run does not erase the useful planning artifact.
- **The requested scope expands**: reassess inputs and comparison coverage before extending conclusions; prior evidence applies only within its original boundary.

## Test case
**Input:**
> {r['test']}

**Assertions:**
1. The output uses Decision, Scope, Evidence, Artifact, Check, and Unresolved in that order.
2. It applies the task-specific distinction to the supplied evidence rather than returning only a general checklist.
3. It preserves a missing or conflicting premise instead of silently assuming a favorable result.
4. It distinguishes planned checks from actual execution and does not invent sources, current requirements, or pass results.
''',dict(id=sid,name=r['name'],domain_code='SKR',subdomain=r['subdomain'],description=r['description'],risk_level='low',requires=[],status='planned')

if __name__=='__main__':
    rows=[]; paths=[]
    for i,r in enumerate(RECORDS,1):
        text,row=render(r,i)
        assert 700 <= len(text.split('---',2)[2].split()) <= 1800
        path=ROOT/'skills'/'SKR'/r['name']/'SKILL.md'; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text,encoding='utf-8'); paths.append(str(path)); rows.append(row)
    (ROOT/'staging'/'skill_repertoire.json').write_text(json.dumps(dict(domains=[DOMAIN],skills=rows),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    raise SystemExit(subprocess.run([sys.executable,str(ROOT/'tools'/'sf.py'),'validate','--file',*paths],cwd=ROOT).returncode)
