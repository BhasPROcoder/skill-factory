# Independent behavioral review: TDS-011

Reviewer: independent agent pass
Artifact: `skills/TDS/dataset-annotation-disagreement-adjudication/SKILL.md`
Scope: compare actual procedure with TDS-006; execute the included Python snippet and evaluate the test request plus fresh ordinary, missing-rule, and conflicting-rule prompts. No source dataset or label policy was modified.

## Catalog comparison

- **TDS-006 dataset-label-definition-audit** writes operational label rules, compares examples to boundaries, distinguishes ambiguous definitions from annotation errors, and produces revised guidance/adjudication questions. It audits and repairs the rule.
- **TDS-011** applies a supplied approved, versioned rule to selected records where reviewers disagree, records per-case disposition and original labels, handles abstention/owner routing, and can compute a scoped raw agreement count. That is a downstream case-level workflow; its default route to TDS-006 for ambiguous rules preserves the boundary.
- **Finding:** The task and artifact are distinct from TDS-006 if TDS-011 never rewrites or resolves an ambiguous rule on its own.

## Executed code snippet

Ran the embedded Python 3 standard-library snippet unchanged. Observed output:

```text
records=3 exact_agreements=1 disagreements=2
```

Recomputation: three pairs; item-a approve/reject differs, item-b reject/reject agrees, item-c approve/reject differs. The reported 1 exact agreement and 2 disagreements are correct, and the skill correctly warns against interpreting this raw count as reliability or validity.

## Text evaluations

### 1. Embedded test request

Prompt: supplied approved rule requires explicit approval; record A says “Approved for release” with approve/reject originals; record B has a blank note and approve/reject originals; proposed adjudications only.

Response produced: A is proposed as approve with the supplied rule fragment and note as evidence. B remains unresolved because its evidence is blank and no supplied rule defines a default label for missing evidence. Both initial labels remain visible; no source mutation is claimed. If agreement is counted, it is explicitly limited to supplied pairs and is not called reliability.

Evaluation: assertions pass under the test's stated rule wording. The test omits an explicit fallback for blank evidence, so leaving B unresolved is appropriate.

### 2. Ordinary request

Prompt: “Fictional set Grove has an approved version R3 rule: label `urgent` only when the record contains the exact phrase `needs action today`; otherwise label `routine`. Record X contains that phrase and reviewers chose urgent/routine. Record Y says `please review later` and both reviewers chose routine. Prepare proposed adjudications; do not change the data.”

Response produced: record X → urgent with rule R3 and exact text; record Y → retain routine under the supplied fallback; both original labels remain visible; no data change; owner approval remains required before any label mutation.

Evaluation: deterministic cases are handled by the supplied rule, and the scope is bounded. Pass.

### 3. Missing approved rule

Prompt: “Two reviewers disagree on labels for these records. We have the records and original labels, but cannot find the approved label guide or version. Please decide the labels.”

Response produced: ask which approved rule/version is authorized and whether the data owner can supply it; do not adjudicate. If unavailable, return a provisional case inventory with original labels preserved and route definition ambiguity to TDS-006. No label is selected from a majority vote.

Evaluation: correct use of the missing-rule boundary and TDS-006 handoff. Pass.

### 4. Conflicting approved rule and example

Prompt: “The approved rule text for version R4 says blank notes should be `reject`, while its attached approved example labels an otherwise identical blank-note case `unresolved`. Two new blank-note records have approve/reject initial labels. What should we do?”

Response produced: preserve both R4 sources and the initial labels; do not apply either instruction to these cases until the owner resolves the conflict and versions the rule. Record the records as unresolved due to rule-source conflict and route the clarification to the rule owner, then rerun affected cases under the resolved version.

Evaluation: correct application of the edge case requiring conflicting rule/example evidence to be preserved. Pass.

## Blocking finding in initial draft

**Worked-example contradiction:** its rule states: “label `approve` only when the note contains explicit approval; otherwise label `reject`.” For item-c's blank note, this wording explicitly assigns `reject`, yet the worked output says `unresolved` because the rule cannot distinguish the labels. Those conclusions conflict. Correct the example either by changing the rule so blank evidence has no defined default, or by changing item-c's supplied rule/evidence so the unresolved disposition is justified. Re-run the example/test after repair. This is a blocker to acceptance because the example teaches the opposite of the stated rule.

## Re-review addendum — corrected draft

The author revised the example and test after the finding. The rule now explicitly maps a present-but-empty note to `reject`, which is consistent with “otherwise reject.” A separate item-c has an unavailable source note and remains unresolved because the rule cannot be applied without the source. The test case now checks both states independently.

Re-evaluation: item-a → approve from explicit text; item-b → reject from the present empty note and fallback rule; item-c → unresolved because the source note is unavailable. Original labels remain visible and no dataset mutation is claimed. The test distinguishes empty evidence from unavailable evidence and passes. The initial blocker is resolved in the current draft.

The embedded code snippet was rerun unchanged and again printed `records=3 exact_agreements=1 disagreements=2`. The rule-absent and conflicting-rule scenarios remain consistent with the current instructions: pause case decisions when no approved rule is supplied; preserve conflicting approved sources and request owner clarification before applying either to affected records.

## Other findings

1. **Original-label preservation and authority boundaries: pass.** The procedure keeps annotations separate and does not authorize data changes.
2. **Metrics boundary: pass.** The code and instructions report raw agreement only, with scope and denominator, and reject reliability claims.
3. **No numeric defect in code: pass.** The snippet and computed output agree.
4. **No production execution: pass.** No real annotations, access, or mutation were used.
