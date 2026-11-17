Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-022
name: paired-graph-retrieval-evidence-evaluation
domain: Graph Engineering Foundations
subdomain: Retrieval evidence evaluation
version: 1.0
description: Compare graph and passage retrieval on matched questions using adjudicated evidence sufficiency and answer correctness separately when deciding whether graph retrieval improves a bounded workload.
triggers: ["evaluate graph retrieval evidence", "compare graph and passage retrieval", "score alternative evidence paths", "find unsupported correct answers", "diagnose graph retrieval regressions"]
not_for: ["building a question evidence packet [GRF-021]", "general model evaluation design [CTG-008]", "context handoff [CTG-005]", "choosing training and validation splits [TML-001]", "automatically adjudicating source truth"]
requires: []
risk_level: medium
---

# Paired Graph Retrieval Evidence Evaluation

## Purpose
Compare graph-assisted and passage-only retrieval with question-level evidence judgments that preserve alternative valid paths and expose failed entity joins. Score evidence sufficiency separately from answer correctness so a correct unsupported answer cannot conceal a retrieval failure. Conclusions apply to the frozen workload, sources and resources actually evaluated.

## Inputs to collect
1. **Evaluation questions** — obtain stable IDs, factual needs, answerability labels and held-out status. Why: comparing different questions changes the workload. Default: no aggregate until matched IDs exist; unknown answerability stays unresolved.
2. **Snapshots and configurations** — collect source inventory, graph revision, extraction revision, seed resolution and both retrieval settings. Why: source availability and identity changes can imitate retrieval improvements. Default: missing provenance blocks a paired performance claim.
3. **Run artifacts** — obtain retrieved passages, paths, omissions, generated answers and observed resource use for each question and system. Why: an answer alone cannot reveal how evidence was obtained. Default: absent runs remain missing, never scored as observed failures.
4. **Evidence rubric** — define what supports each factual need, permissible alternative paths, qualifications and accepted answer variants. Why: exact path equality can reject valid support. Default: draft rubric awaiting adjudication; no automatic semantic labels.
5. **Resource contract** — define the comparable source access and retrieval/answering budgets. Why: unequal resources change the comparison. Default: disclose differences and withhold a fair-budget claim.
6. **Decision owner and costs** — collect critical slices and acceptable regressions. Why: aggregate gains need not justify a harmful failure mode. Default: report observed tradeoffs without a promotion recommendation.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze questions, source and graph revisions, configurations, resource contract and judging rubric before inspecting comparison outcomes.
2. Confirm that question IDs and run provenance align across both systems, preserving missing or invalid runs in a separate ledger.
3. For each question, identify its required facts and whether the authorized source snapshot supports an answer.
4. Inspect retrieved graph paths for correct seed identity, edge direction, endpoint continuity and semantic compatibility of joined relationships.
5. Inspect source passages for every factual need, preserving conditions, attribution and contradictions that graph edges may omit.
6. ⚠️ Adjudicate alternative evidence paths by whether their inspected sources support the required facts; do not require identical edge sequences or accept connectivity alone.
7. Label evidence sufficiency independently of generated answer correctness, retaining unresolved judgments and reviewer reasons.
8. Assign observable failure causes: wrong seed, invalid join, missing source, search omission, packet truncation, unsupported interpretation or answer error; allow several causes when warranted.
9. Compute matched outcome counts only over the explicitly eligible adjudicated questions; report exclusions and denominators alongside every rate.
10. Examine paired wins and losses by critical slice, including correct answers with insufficient evidence and sufficient evidence followed by incorrect answers.
11. Compare observed resource use and baseline access against the frozen contract; investigate mismatches before deciding on promotion.
12. Deliver the question ledger and bounded decision, using a separate development set for tuning before a fresh held-out evaluation.

Use this Python 3 reference for transparent paired counts from already adjudicated labels. Record the interpreter version when executing it. It does not judge source meaning, path validity, answerability or fairness. The shared `scope` identifies the question set, source inventory and resource contract; each system's distinct graph/configuration revision belongs in its run ledger. Every question has Boolean `answerable`, and evidence/answer labels are `True`, `False` or `None` for unresolved. Unanswerable questions are retained for a separate abstention analysis, outside the answerable-success counts below.

```python
def paired_counts(graph, baseline):
    if graph["scope"] != baseline["scope"]:
        raise ValueError("mismatched evaluation scope")
    left, right = graph["rows"], baseline["rows"]
    if set(left) != set(right):
        raise ValueError("mismatched question IDs")
    counts = dict(eligible=0, excluded=0, both=0,
                  graph_only=0, baseline_only=0, neither=0,
                  graph_unsupported_correct=0,
                  baseline_unsupported_correct=0)
    for qid in sorted(left):
        a, b = left[qid], right[qid]
        if type(a["answerable"]) is not bool or type(b["answerable"]) is not bool:
            raise ValueError("answerability must be adjudicated")
        if a["answerable"] != b["answerable"]:
            raise ValueError("inconsistent answerability")
        labels = [r[k] for r in (a, b) for k in ("evidence", "answer")]
        if any(x is not None and type(x) is not bool for x in labels):
            raise ValueError("invalid judgment label")
        if not a["answerable"] or any(x is None for x in labels):
            counts["excluded"] += 1
            continue
        counts["eligible"] += 1
        ga, ba = a["evidence"] and a["answer"], b["evidence"] and b["answer"]
        key = "both" if ga and ba else "graph_only" if ga else "baseline_only" if ba else "neither"
        counts[key] += 1
        for name, row in (("graph", a), ("baseline", b)):
            counts[name + "_unsupported_correct"] += int(row["answer"] and not row["evidence"])
    return counts

def row(evidence, answer):
    return dict(answerable=True, evidence=evidence, answer=answer)

g = dict(scope="fiction-v1", rows={"q1": row(True, True),
         "q2": row(False, True), "q3": row(True, False)})
b = dict(scope="fiction-v1", rows={"q1": row(False, False),
         "q2": row(True, True), "q3": row(True, False)})
c = paired_counts(g, b)
assert (c["eligible"], c["graph_only"], c["baseline_only"], c["neither"]) == (3, 1, 1, 1)
assert c["graph_unsupported_correct"] == 1
print("paired outcomes and unsupported correct answers checked")
```

The code's combined success requires both sufficient evidence and a correct answer for answerable questions. Keep the underlying separate labels in the deliverable, including sufficient-evidence/incorrect-answer cases. If the eligible denominator is zero, report no eligible cases rather than a zero-percent success rate. Missing snapshot metadata cannot be repaired by assigning the same arbitrary scope string to incompatible runs.

## Decision rules
- IF an alternative path has adjudicated support for every required fact THEN accept its evidence sufficiency BECAUSE path spelling is not the evaluation target.
- IF an answer is correct but retrieved evidence is insufficient THEN retain both labels BECAUSE answer accuracy does not demonstrate successful retrieval.
- IF a path joins different entities with identical labels THEN reject that join BECAUSE display names do not establish identity.
- IF evidence labels are unresolved THEN exclude the pair from resolved counts and report it BECAUSE uncertainty is neither success nor failure.
- IF graph gains hide a critical baseline win THEN surface the regression BECAUSE aggregate counts omit failure costs.
- IF test questions guide tuning THEN evaluate the change on untouched questions BECAUSE the earlier held-out comparison no longer measures the revised configuration independently.

## Output template
```text
Contract: <question/source revisions, configurations and budgets; maximum 80 words>
Question ledger: <ID | answerability | graph evidence/answer | baseline evidence/answer | path/source justification | failure causes>
Paired counts: <eligible, excluded, both, graph-only, baseline-only, neither>
Support gaps: <correct-but-unsupported cases and sufficient-evidence answer failures>
Slices: <critical slice | paired tradeoff | unresolved judgments; maximum 8 rows>
Execution: <observed runs/checks and pending checks; maximum 70 words>
Decision: <bounded conclusion, owner criterion and next evaluation; maximum 80 words>
```

## Quality checklist
- [ ] Both systems use matched question IDs and inspected provenance.
- [ ] Alternative paths are judged by supported facts.
- [ ] Seed and join identity errors are distinguished from missing passages.
- [ ] Answer correctness and evidence sufficiency remain separate labels.
- [ ] Missing and unresolved cases appear beside the denominator.
- [ ] Unanswerable cases retain a separate abstention review.
- [ ] Critical slice regressions remain visible in the decision.
- [ ] Tuning and held-out evaluation are separated.

## Anti-patterns
- **Golden-path literalism**: reject different valid evidence routes. Fix: adjudicate required facts and qualifications.
- **Correct-answer cover**: count unsupported correct answers as retrieval success. Fix: preserve independent evidence labels.
- **Name-based joining**: accept a route through similarly named entities. Fix: inspect scoped identity and relationship roles.
- **Hidden exclusions**: remove unresolved pairs without a denominator explanation. Fix: retain the excluded ledger.
- **Unfair resource comparison**: ignore unequal source access or budgets. Fix: align or explicitly limit the claim.

## Worked example
**Input:** Fictional adjudicated fixture uses the snippet labels. q1 has an approved alternative graph path; q2 has a correct graph answer without sufficient retrieved support; q3 has sufficient evidence but incorrect answers in both systems. Budgets and source inventory were matched; no promotion cost policy is supplied.

**Output:**
```text
Contract: fiction-v1 questions/sources; frozen graph and passage configurations; matched supplied budgets.
Question ledger: q1 | answerable | true/true | false/false | approved alternative path | baseline omission; q2 | answerable | false/true | true/true | graph support missing | unsupported answer; q3 | answerable | true/false | true/false | sufficient supplied evidence | answer errors.
Paired counts: eligible 3; excluded 0; both 0; graph-only 1; baseline-only 1; neither 1.
Support gaps: q2 graph correct but unsupported; q3 both systems sufficient evidence with incorrect answers.
Slices: No critical slice policy supplied; opposing q1/q2 outcomes retained.
Execution: Supplied adjudications; reference counts can be executed; no live retrieval performance measured here.
Decision: Neither system dominates these paired outcomes; obtain owner failure costs before promotion and preserve untouched questions for later evaluation.
```

**Bad output:** “Graph answers two questions correctly, so graph retrieval wins.”
This hides q2's missing support and ignores the paired baseline success.

## Edge cases
- **Source missing from both inventories**: reconsider answerability within the frozen scope; do not blame graph traversal alone.
- **Budget truncation**: retain the omission and observed resource limit as the cause; do not infer that evidence does not exist.
- **No eligible pairs**: report the exclusion reasons and no rate or winner.
- **Judge disagreement**: preserve both rationales and leave labels unresolved until adjudication.
- **Stochastic runs**: retain run identities and use a declared aggregation rule; do not select the best run after inspecting outcomes.

## Test case
**Input:**
> Fictional graph output uses a valid alternative evidence route, but answers incorrectly. Baseline gives the correct answer without evidence. Another question has unresolved source support in both systems. Produce paired evaluation findings.

**Assertions:**
1. Accepts the graph route's adjudicated evidence while retaining its answer failure.
2. Reports baseline's correct answer as unsupported.
3. Excludes the unresolved pair explicitly instead of scoring it false.
4. Claims no winner from answer correctness alone.
</skill>

<user_request>
Fictional graph output uses a valid alternative evidence route, but answers incorrectly. Baseline gives the correct answer without evidence. Another question has unresolved source support in both systems. Produce paired evaluation findings.
</user_request>
