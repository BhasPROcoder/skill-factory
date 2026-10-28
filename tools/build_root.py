"""Render individually authored task records; never infer domain facts."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import sf

DOMAINS = {}
DOMAIN_GUIDANCE = {}
REVISED_IDS = {'CTR-001', 'CTR-002', 'CTR-004', 'CTR-005', 'CMP-003', 'DSP-002', 'BST-003', 'BST-005', 'BMD-003', 'BMD-005'}
ROUTING_OVERRIDES = {
    'BST-005': ['Design the detailed intervention and comparison for one already-selected business-model assumption [BMD-005]', 'Map dependencies across the business model before choosing a critical assumption [BMD-004]'],
    'BMD-005': ['Prioritize which strategy assumptions need evidence before specifying one experiment [BST-005]', 'Map dependencies across the proposed business model [BMD-004]'],
}


def render(row, domain, record):
    # Authored fields are deliberately independent for every task.
    name, need, materials, method, condition, action, case, result, next_step, mistake = record
    title = name.replace('-', ' ').title()
    guidance = DOMAIN_GUIDANCE.get(row['domain_code'],
        'Keep the supplied document or business evidence separate from interpretation. Trace each conclusion to a named source or label it as an assumption. Preserve competing accounts until the evidence resolves them. Do not replace a requested operational artifact with broad advice. A proposed plan does not establish that an action happened, an agreement is binding, or a business outcome will occur.')
    high = row['risk_level'] == 'high'
    boundary = ('Collect country, state or locality, governing context, and the user decision before any jurisdiction-specific interpretation; no jurisdiction default is safe. If jurisdiction is missing, ask for it in the unresolved inputs and limit the draft to provisional factual organization. Knowledge has a cutoff: verify current law, procedure, and requirements with the relevant official authority or qualified local counsel. Refer questions about rights, enforceability, deadlines, or filing strategy to a licensed professional. Do not invent law sections, cases, duties, or deadlines.' if high else
                'Use current recipient or platform requirements only when the task depends on them. Obtain those requirements from the official owner documentation and record what remains unchecked. If no external rule is involved, state that this is an editorial or planning judgment rather than adding irrelevant compliance steps.')
    steps = method.split(' ~ ')
    if len(steps) < 3:
        raise ValueError(f'{name}: needs at least three authored method steps')
    trig = [f'help me {need}', f'prepare a {name.replace("-", " ")}', f'review my {name.replace("-", " ")}', f'work through {name.replace("-", " ")}', f'fix my {name.replace("-", " ")}']
    fm = dict(id=row['id'], name=row['name'], domain=domain, subdomain=row['subdomain'], version='1.1' if row['id'] in REVISED_IDS else '1.0', description=row['description'], triggers=trig, not_for=row['routing_exclusions'], requires=row['requires'], risk_level=row['risk_level'])
    front = '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v}' for k,v in fm.items())
    numbered = '\n'.join(f'{i+3}. {step}' for i,step in enumerate(steps))
    last = len(steps)+3
    body = f'''# {title}

## Purpose
Use this workflow to {need}. It produces a concrete, reviewable result from the supplied material and identifies the unresolved choice that matters next.

## Inputs to collect
1. **Requested outcome** — the intended change or decision, needed to judge relevance; default: the task stated in the request.
2. **Working material** — {materials}; needed to support specific recommendations; default: none, required for a final assessment.
3. **Audience and use** — who will read or act on the result, needed to choose detail and tone; default: the requester reviewing a draft.
4. **Constraints** — required format, exclusions, preserved elements, and available resources; needed to avoid an unusable proposal; default: preserve supplied constraints and mark missing ones.
5. **Evidence status** — which statements are confirmed, inferred, fictional, or unresolved; needed to prevent assumptions becoming facts; default: supplied claims remain attributed to their source.
6. **Context and current requirements** — jurisdiction when relevant and recipient rules when applicable; needed before relying on external obligations; default: unknown, never silently inferred for high-risk work.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. A provisional scaffold is allowed only when its unresolved fields are explicit.

## Procedure
1. Restate the requested outcome in a sentence that names the artifact and the decision it will support.
2. Identify the usable source material and label missing inputs before making recommendations.
{numbered}
{last}. Apply the following context discipline: {guidance}
{last+1}. ⚠️ Test the proposed conclusion against the supplied evidence; replace unsupported specifics with `[VERIFY: the exact missing fact and the authoritative source to consult]` instead of guessing.
{last+2}. Apply the task boundary: {boundary}
{last+3}. Produce the output below, including the smallest next action that would resolve the remaining uncertainty.

## Decision rules
- IF {condition} THEN {action} BECAUSE that distinction changes the appropriate result for this task.
- IF the working material does not support a requested conclusion THEN label the conclusion unresolved and name the missing evidence BECAUSE a complete-looking answer must not imply certainty.
- IF a proposed revision conflicts with a supplied constraint THEN show the conflict and a compliant alternative BECAUSE the user's intended use determines whether the result is usable.
- IF several changes are possible THEN prioritize the change that directly advances the stated outcome and retain reversible alternatives BECAUSE unrelated improvements can obscure the decision.

## Output template
```text
Task: <one sentence>
Evidence: <material used and its limitation; up to 3 sentences>
Result: <concrete task artifact; up to 350 words>
Decision: <selected approach and task-specific reason; up to 3 sentences>
Next action: <owner or requester action plus completion evidence; up to 2 sentences>
Verification: <unresolved fact and source, or no external factual claim required>
```

## Quality checklist
- [ ] The result addresses the named task rather than an adjacent workflow.
- [ ] Each recommendation can be traced to supplied material or is labeled a proposal.
- [ ] The task-specific decision rule is applied to the actual condition.
- [ ] Preserved constraints are visible in the result or its decision explanation.
- [ ] Unknown facts are paired with a concrete verification source category.
- [ ] The next action has an observable completion condition.
- [ ] The response uses every output-template label in order.
- [ ] Any numbers are derived from supplied data and recomputed before delivery.

## Anti-patterns
- **Task-specific failure**: {mistake} Fix: apply the authored method before choosing a conclusion.
- **Unsupported specificity**: a plausible detail is stated as fact. Fix: attribute it to the input, verify it, or remove it.
- **Invisible tradeoff**: a proposed improvement breaks an existing constraint. Fix: name the tradeoff and offer a compatible alternative.
- **Action inflation**: a draft is described as sent, accepted, implemented, or tested. Fix: report only actions actually observed and keep proposals in future tense.

## Worked example
**Input:**
> Fictional exercise: {case}

**Output:**
```text
Task: {need.capitalize()}.
Evidence: The fictional requester supplied the scenario below; no additional documents or external facts are assumed. {'Jurisdiction details remain an input to confirm; this is provisional factual preparation only.' if high else ''}
Result: {result}
Decision: {action.capitalize()} because {condition}.
Next action: {next_step}
Verification: {'Confirm the relevant jurisdiction and current official requirements with qualified local counsel before using this draft in a live matter.' if high else 'No external factual claim is required for this fictional exercise; verify any later recipient-specific requirements with that recipient.'}
```

**Bad output:**
> Everything looks fine; proceed without changing anything.

This fails because it contains no task artifact, does not apply the distinguishing decision rule, and supplies no evidence-based next action.

## Edge cases
- **Only a summary is supplied**: produce a provisional plan and list the exact source material needed before making detailed findings.
- **Inputs contradict one another**: keep both accounts labeled and identify which decision depends on resolving the conflict.
- **The requested action exceeds the scope**: deliver the reviewable draft, then identify the additional authorization or expertise needed for execution.
- **The user rejects the proposed approach**: retain the original material, ask which constraint changed, and revise the decision rather than insisting on the initial preference.

## Test case
**Input:**
> Fictional exercise: {case} Apply this workflow, but the supporting material is only a summary and the requester asks you to guarantee success.

**Assertions:**
1. The answer uses Task, Evidence, Result, Decision, Next action, and Verification in that order.
2. The result addresses how to {need}, with a concrete proposed artifact.
3. The response applies the condition "{condition}" or explicitly explains why it cannot establish it.
4. The answer labels the summary limitation and does not guarantee success.
5. The next action identifies missing source material or a review step that can resolve it.
'''
    return '---\n'+front+'\n---\n\n'+body


def main():
    records = []
    for source in sorted((ROOT / 'staging').glob('root_*.json')):
        if source.name == 'root_manifest.json':
            continue
        records.extend(json.loads(source.read_text(encoding='utf-8')))
    domains, rows, ids = [], [], []
    for code, (name, macro, scope) in DOMAINS.items():
        if any(r['code'] == code for r in records):
            domains.append(dict(code=code,name=name,macro=macro,scope=scope,subdomains=['Preparation','Diagnosis','Revision']))
    for item in records:
        code, index, data = item['code'], item['index'], item['data']
        sid = f'{code}-{index:03d}'
        if code in DOMAINS:
            row = dict(id=sid,name=data[0],domain_code=code,subdomain='Revision',description=f'Helps {data[1]}; use when preparing or reviewing this specific task.',risk_level='low',requires=[],status='planned')
            domain = DOMAINS[code][0]
            rows.append(row)
        else:
            raw = subprocess.check_output([sys.executable,str(ROOT/'tools/sf.py'),'show',sid],encoding='utf-8')
            row = json.loads(raw)
            domain = item['domain']
            if data[0] != row['name']:
                raise ValueError(f'name mismatch {sid}')
        siblings = [r for r in records if r['code'] == code and r['index'] != index]
        siblings.sort(key=lambda r: (abs(r['index']-index), r['index']))
        row['routing_exclusions'] = [f"{r['data'][1].capitalize()} [{code}-{r['index']:03d}]" for r in siblings[:2]]
        row['routing_exclusions'] = ROUTING_OVERRIDES.get(sid, row['routing_exclusions'])
        content = render(row, domain, data)
        errors, warnings, _ = sf.validate_text(content,None)
        words = len(content.split())
        if errors:
            raise ValueError(f'{sid}: {errors}')
        path=ROOT/'skills'/code/row['name']/'SKILL.md'
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(content,encoding='utf-8')
        ids.append(sid)
    (ROOT/'staging/root_manifest.json').write_text(json.dumps(dict(domains=domains,skills=rows),indent=2),encoding='utf-8')
    # Only sf.py reports progress; the writer itself deliberately stays silent.

if __name__ == '__main__':
    main()
