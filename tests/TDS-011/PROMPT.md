Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: TDS-011
name: dataset-annotation-disagreement-adjudication
domain: Dataset Intake and Documentation
subdomain: Adjudication records
version: 1.0
description: Resolve case-level differences between dataset annotations under an approved label rule; use when independent reviewers disagree and the dataset needs traceable dispositions.
triggers: ["adjudicate conflicting dataset labels", "resolve annotator disagreements", "create an annotation adjudication log", "review disputed labels record by record", "preserve original labels while resolving disagreements"]
not_for: ["audit or rewrite label definitions [TDS-006]", "measure model performance", "estimate annotator reliability from an unapproved metric"]
requires: []
risk_level: medium
---

# Dataset Annotation Disagreement Adjudication

## Purpose
Create a traceable, case-level disposition for records whose independent annotations differ. Apply an approved rule to the supplied evidence, retain the original annotations, and leave a record unresolved when the rule or evidence cannot support a decision. This produces an adjudication record; it does not prove label validity or annotator reliability.

## Inputs to collect
1. **Dataset and record scope** — version, records, use, and access limits. Why: bound the evidence. Default: supplied records only.
2. **Original independent annotations** — stable IDs, reviewer aliases, labels, and rationales. Why: preserve auditability. Default: never reconstruct missing originals.
3. **Approved label rule and version** — instructions, examples, hierarchy. Why: adjudication applies a rule. Default: if unclear, route to TDS-006.
4. **Record evidence and context** — fields or excerpts needed for the rule. Why: decisions depend on permitted evidence. Default: mark gaps.
5. **Adjudication authority and unresolved path** — decision-maker, abstention route, and change approver. Why: recommendations do not authorize mutation. Default: propose a log only.
6. **Output and privacy constraints** — limits on shared IDs or reviewer references. Why: logs may expose sensitive information. Default: store only necessary traceability in an authorized location.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Preserve the original annotations and record dataset and instruction versions.
2. Select records with differing labels or a documented review request; do not add cases based on presumed difficulty.
3. Confirm each record ID, context, independent labels, and rule version align; record whether required fields are present, empty, unreadable, or absent.
4. ⚠️ Classify from evidence: application error, rule ambiguity, missing evidence, context mismatch, tool/transcription issue, or unknown. Keep unsupported classifications provisional.
5. Apply the approved rule. Cite a supplied rule/example identifier or quote a short rule fragment; never invent a citation.
6. If required by the approved workflow, conceal initial labels until the adjudicator records a provisional answer; otherwise follow and report the supplied process.
7. Record each disposition: selected label, abstain/unresolved, or return for correction. Explain the decisive evidence and rule; do not force consensus.
8. Keep the adjudicated label in a separate field or table from every original label. Never overwrite the source values during analysis.
9. Summarize reason counts only when categories and denominators are defined. Raw counts are scoped descriptions, not reliability scores or quality guarantees.
10. For a small supplied set, use this optional exact-agreement count in Python 3 with its standard library. It compares two labels per row only; it does not adjust for chance, validate the rule, or generalize beyond the supplied rows.

```python
pairs = [
    ("item-a", "approve", "reject"),
    ("item-b", "reject", "reject"),
    ("item-c", "approve", "reject"),
]

if not pairs:
    raise ValueError("No annotation pairs supplied")

agreements = sum(left == right for _, left, right in pairs)
disagreements = [row for row in pairs if row[1] != row[2]]
print(f"records={len(pairs)} exact_agreements={agreements} disagreements={len(disagreements)}")
```

On the fictional three-pair fixture below, the observed output is `records=3 exact_agreements=1 disagreements=2`; this is a raw, case-limited count.

11. Check that each input appears at most once, original labels remain unchanged, and each proposed label has a rationale.
12. Route rule gaps separately; rerun affected cases only after owner approval of a clarified definition.
13. Deliver the log, unresolved cases, calculation scope, owner actions, and data-change status.

## Decision rules
- IF the instructions do not determine a disputed case THEN mark it unresolved and request a rule clarification BECAUSE voting cannot define an ambiguous label.
- IF evidence is missing or two supplied sources conflict THEN preserve both facts and abstain or request the specific missing evidence BECAUSE a forced label would hide uncertainty.
- IF a required field is present but empty THEN apply the approved rule to the empty value; if the field or source is absent or unreadable, mark the case unresolved BECAUSE observed empty content differs from unavailable evidence.
- IF an adjudicator decision differs from both initial labels THEN record the decisive rule and evidence explicitly BECAUSE the change needs an auditable basis.
- IF an input appears corrupted, misaligned, or attached to the wrong record THEN return it for source correction before choosing a label BECAUSE adjudication cannot repair an identity or context error by guessing.
- IF a raw agreement count is calculated THEN report numerator, denominator, and included records BECAUSE a scoped count is not a chance-adjusted reliability measure.
- IF the user requests that labels be overwritten or redistributed THEN confirm the authorized owner, destination, and exact change scope before acting BECAUSE preparing a decision log does not authorize a data mutation or release.

## Output template
```text
## Scope
- Dataset/version and records:
- Label rule/version:
- Intended use and evidence limits:

## Adjudication table
| Record ID | Original label(s) | Reason category | Rule/evidence applied | Proposed disposition | Unresolved item |
|---|---|---|---|---|---|

## Count summary
- Included record count:
- Exact agreements/disagreements, if computed:
- Calculation scope and limitation:

## Owner actions
1. [action] — [owner role] — [completion evidence]

## Data changes
- Proposed / authorized / performed; identify exact artifact and evidence, or state “none performed.”

## Unresolved
- [record or rule] — [specific missing evidence or decision owner]
```

## Quality checklist
- [ ] Dataset, rule version, and reviewed record set are identified
- [ ] Original labels remain visible and are not silently overwritten
- [ ] Each case disposition traces to supplied rule text and record evidence
- [ ] Ambiguous-rule, insufficient-evidence, and data-integrity cases remain distinct
- [ ] An unresolved or abstain option is used where evidence does not decide the label
- [ ] Any count states its numerator, denominator, and included scope
- [ ] Raw agreement is not presented as annotator reliability or label validity
- [ ] Data changes are reported separately from proposed decisions and require an identified authority

## Anti-patterns
- **Majority as truth**: treat the most common initial label as authoritative. Fix: apply the approved rule and preserve unresolved cases.
- **Overwriting history**: replace initial labels with adjudicated values. Fix: add a separate decision field and retain source values.
- **Rule drift**: change the definition while deciding a batch. Fix: pause affected cases, request owner clarification, and version the rule before resuming.
- **Metric inflation**: interpret exact agreement as reliability or accuracy. Fix: report only the scoped count and state its limitations.
- **Evidence laundering**: cite a rule or record that was not supplied. Fix: name the absent evidence and mark the case unresolved.
- **Unapproved mutation**: write proposed labels directly into a production dataset. Fix: prepare a separate change set and require the named data owner’s approval.

## Worked example
**Input:** Fictional Pine uses this rule: “approve” only for explicit approval in the supplied note; otherwise “reject.” Item-a says “Approved for release” with conflicting labels. Item-b has a present empty note and both chose reject. Item-c has conflicting labels but its source note is unavailable. Proposed decisions only.

**Output:**
```text
## Scope
- Dataset/version and records: fictional Pine dataset, three supplied records.
- Label rule/version: supplied explicit-approval rule; version not stated.
- Intended use and evidence limits: proposed dispositions only; no dataset mutation authorized.

## Adjudication table
| Record ID | Original label(s) | Reason category | Rule/evidence applied | Proposed disposition | Unresolved item |
|---|---|---|---|---|---|
| item-a | approve / reject | apparent application error | “Approved for release” contains explicit approval | approve | None in supplied evidence |
| item-b | reject / reject | no disagreement | Present empty note; rule says otherwise reject | retain reject | None in supplied evidence |
| item-c | approve / reject | missing record evidence | Source note unavailable; rule cannot be applied without it | unresolved | Retrieve the source note or route to the owner |

## Count summary
- Included record count: 3
- Exact agreements/disagreements, if computed: 1 agreement / 3 pairs; 2 disagreements / 3 pairs.
- Calculation scope and limitation: raw comparison of the supplied reviewer pairs only; not a reliability or validity score.

## Owner actions
1. Resolve item-c — dataset owner — provide the source note or confirm an unresolved disposition.

## Data changes
- Proposed only; none performed.

## Unresolved
- item-c — source note unavailable; owner decision required.
```

**Bad output:**
> Two of the three cases have the same majority label, so assign that label to every disputed record and replace the old labels.

Fails because the undisputed record is not a vote on other cases, item-c lacks evidence, and original labels must remain preserved.

## Edge cases
- **Present but empty field**: apply the rule to the empty value. If the field or source is missing or unreadable, leave the case unresolved and request that specific evidence.
- **Multiple labels are permitted**: apply the documented multi-label rule and retain separate label sets; do not force a single class.
- **Evidence conflicts with the rule’s examples**: preserve the conflict and ask the owner to reconcile the rule before applying it to affected records.
- **Annotator rationale is absent**: adjudicate from the approved rule and record evidence only; do not attribute intent or competence.
- **Personal or sensitive content appears**: minimize quoted text and store the detailed trace only in an authorized location identified by the user.

## Test case
**Input:**
> Fictional team Pine supplies an approved rule: approve only if the available note contains explicit approval; otherwise reject. Record A says “Approved for release” and has labels approve/reject. Record B has a present but empty note and labels approve/reject. Record C has labels approve/reject but its source note is unavailable. Produce proposed adjudications without changing the dataset.

**Assertions:**
1. Record A is proposed as approve with the supplied rule and note as its rationale.
2. Record B is proposed as reject because the available empty note does not contain explicit approval and the rule specifies otherwise reject.
3. Record C remains unresolved because the source note is unavailable, unlike a present empty note.
4. The output preserves initial labels and states that no dataset change was performed.
5. Any agreement calculation is scoped to supplied pairs and is not described as a reliability score.
</skill>

<user_request>
Fictional team Pine supplies an approved rule: approve only if the available note contains explicit approval; otherwise reject. Record A says “Approved for release” and has labels approve/reject. Record B has a present but empty note and labels approve/reject. Record C has labels approve/reject but its source note is unavailable. Produce proposed adjudications without changing the dataset.
</user_request>
