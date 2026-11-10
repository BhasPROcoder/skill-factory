---
id: TDS-012
name: dataset-withdrawal-lineage-impact-plan
domain: Dataset Intake and Documentation
subdomain: Withdrawal impact and lineage
version: 1.0
description: Map an already authorized data withdrawal decision across evidence-backed dataset descendants; use when owners need a per-artifact removal, rebuild, retention-review, or verification plan.
triggers: ["trace a data withdrawal through dataset derivatives", "plan removal of a withdrawn record from derived datasets", "map downstream datasets affected by a withdrawal", "review training and export impacts of a data withdrawal", "create a dataset withdrawal impact plan"]
not_for: ["deciding whether a person has a legal withdrawal right", "designing consent flows or legal basis [COP-003]", "general dataset provenance mapping [TDS-002]"]
requires: []
risk_level: high
---

# Dataset Withdrawal Lineage Impact Plan

## Purpose
Turn an already authorized withdrawal decision into an evidence-linked plan across dataset descendants. Do not decide legal validity, mutate data, or claim model influence has been removed.

## Inputs to collect
1. **Approved withdrawal decision** — scope and approving role. Why: the workflow acts only on an approved decision. Default: otherwise return intake gaps.
2. **Jurisdiction/context** — applicable locations, agreement, and current official requirements. Default: ask; use `[VERIFY: current law, agreement, and official authority]` until checked.
3. **Record-matching evidence** — approved internal reference and limits. Default: minimize identifiers; never guess.
4. **Artifact lineage** — IDs/versions, parents, transformations, destinations, and storage classes. Default: undocumented links stay unresolved.
5. **Shared-data/rebuild facts** — affected membership, unaffected records, reproducible inputs, and checks. Default: rebuild only with evidence and approval.
6. **Backup/model context** — retention, restore paths, model artifacts, owners. Default: unresolved items need owner/privacy review.
7. **Execution authority** — artifact owner and completion evidence. Default: plan only; perform no changes.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Confirm approval and scope; if unclear, stop and ask the authorized owner.
2. Record jurisdiction/context; verify current official requirements and refer legal interpretation to licensed local privacy counsel.
3. Use a minimized approved reference; keep reidentification keys in their authorized system.
4. Build a directed graph only from manifests, dependency records, or owner-confirmed links. Record artifact/version, parent, owner, destination, and evidence per edge.
5. Match covered source records using approved evidence; a failed match does not prove absence.
6. Include the covered source artifacts and traverse evidenced descendants; mark undocumented parents, consumers, and exports unresolved. Do not claim graph completeness.
7. Determine per artifact whether it contains the record, a derived contribution, or only an indirect dependency. Require evidence for each effect.
8. For shared derivatives, scope affected and unaffected data from membership or reproducible transformations. Rebuild from unaffected inputs only with owner approval and validation checks.
9. For editable copies/exports, propose a scoped action only when decision and dependency evidence support it. Name the owner and closure evidence.
10. ⚠️ For immutable backups, legal holds, or retention conflicts, do not bypass controls; refer handling and restore behavior to the owner and qualified privacy reviewer.
11. For models or indirect artifacts, record dependency evidence and owner. Source-row deletion alone does not demonstrate influence removal; do not claim unlearning or retraining is required or sufficient.
12. Define per-action checks against changed artifacts, unaffected data, owner confirmation, or approved exceptions.
13. Separate planned, authorized, performed, and verified states. A notice or job request is not completed deletion.

For a small artifact graph, this optional Python 3 standard-library snippet lists descendants in the supplied parent map. It identifies only recorded links; it cannot establish that the map is complete or that an artifact contains the withdrawn record.

```python
from collections import defaultdict

parents = {
    "masked-copy": ["raw"],
    "features": ["masked-copy", "catalog"],
    "training-snapshot": ["features"],
    "research-export": ["features"],
    "summary-view": ["catalog"],
}

children = defaultdict(list)
for child, direct_parents in parents.items():
    for parent in direct_parents:
        children[parent].append(child)

source = "raw"
seen = {source}
pending = list(children.get(source, []))
while pending:
    artifact = pending.pop()
    if artifact not in seen:
        seen.add(artifact)
        pending.extend(children.get(artifact, []))

descendants = sorted(seen - {source})
print(descendants)
assert descendants == ["features", "masked-copy", "research-export", "training-snapshot"]
```

On this fictional graph the snippet prints `['features', 'masked-copy', 'research-export', 'training-snapshot']`; `summary-view` is excluded because its recorded parent is `catalog`, not a descendant of `raw`.

## Decision rules
- IF no approved scope exists THEN ask the authority questions and propose no artifact changes BECAUSE a request alone does not authorize action.
- IF a descendant link is undocumented THEN leave it unresolved pending owner evidence BECAUSE assumed lineage can miss copies or implicate unrelated data.
- IF a derivative mixes affected and unaffected records THEN rebuild only with evidence, approval, and validation BECAUSE whole-artifact deletion may remove unrelated data.
- IF backups or retention controls conflict with action THEN stop that node for owner and qualified privacy review BECAUSE exceptions cannot be assumed.
- IF a model may encode affected information THEN report dependency separately BECAUSE source deletion does not demonstrate influence removal.
- IF completion evidence is missing THEN preserve any evidenced performed state and mark verification pending; otherwise keep execution unconfirmed BECAUSE performance and verification are separate claims.
- IF legal obligations are requested THEN require jurisdiction, current official checks, and qualified local counsel BECAUSE requirements cannot be assumed.

## Output template
```text
## Scope and authority
- Approved decision reference and scope:
- Jurisdiction/current-source review:
- Dataset and source reference:

## Evidence-backed lineage
| Artifact/version | Direct parent evidence | Contains affected record/contribution? | Owner | Evidence state |
|---|---|---|---|---|

## Action matrix
| Artifact | Proposed action | Unaffected data preserved? | Execution owner | Completion evidence | State |
|---|---|---|---|---|---|

## Special handling
- Shared derivatives:
- Backups/retention/restore:
- Models and indirect artifacts:

## Unresolved
- [artifact or legal question] — [evidence/owner/current-source check required]

## Conclusion
- Graph completeness: demonstrated for supplied evidence / incomplete / unknown
- Actions: proposed / authorized / performed / verified, stated separately
- No legal determination or complete-erasure claim is made by this plan.
```

## Quality checklist
- [ ] Approved decision and scope are evidenced
- [ ] Jurisdiction/current requirements are checked or flagged
- [ ] Each graph edge has evidence; unknown links remain visible
- [ ] Artifact impact is not inferred from reachability alone
- [ ] Shared derivatives preserve unaffected data or remain unresolved
- [ ] Backup/retention conflicts are escalated, never bypassed
- [ ] Model influence is not equated with source deletion
- [ ] State, owner, and completion evidence are recorded per action
- [ ] Unnecessary direct identifiers are excluded

## Anti-patterns
- **Consent inference**: treat a request as approval. Fix: require the authorized scope.
- **Name-based lineage**: infer edges from filenames. Fix: require manifests or owner evidence.
- **Delete-the-whole-table**: remove shared data blindly. Fix: scope and validate a rebuild.
- **Backup bypass**: evade retention controls. Fix: escalate and document restore handling.
- **Model-erasure claim**: equate source deletion with influence removal. Fix: report uncertainty to the model owner.
- **False completion**: mark a request or plan as deletion. Fix: require artifact checks or an approved exception.
- **Legal shortcut**: apply remembered rules. Fix: verify current requirements with qualified local review.

## Worked example
**Input:** Fictional Juniper Grove has approval for one pseudonymous record. Its manifest links `raw` → `masked-copy` → shared `features` → `research-export` and `training-snapshot`. Backup policy, model membership, jurisdiction, and owners are unknown. The team asks for a plan only.

**Output:**
```text
## Scope and authority
- Approved decision reference and scope: fictional approved instruction, one pseudonymous source record.
- Jurisdiction/current-source review: missing; [VERIFY: jurisdiction, current official requirements, supplied agreement].
- Dataset and source reference: Juniper Grove research dataset, source `raw`; plan only.

## Evidence-backed lineage
| Artifact/version | Direct parent evidence | Contains affected record/contribution? | Owner | Evidence state |
|---|---|---|---|---|
| raw | approved source scope | covered source record | unassigned | exact match pending |
| masked-copy | raw, manifest | unknown | unassigned | membership unchecked |
| features | masked-copy, manifest | shared; exact effect unknown | unassigned | row-level effect unchecked |
| research-export | features, manifest | unknown | unassigned | membership unchecked |
| training-snapshot | features, manifest | unknown | model owner unassigned | membership unchecked |

## Action matrix
| Artifact | Proposed action | Unaffected data preserved? | Execution owner | Completion evidence | State |
|---|---|---|---|---|---|
| raw | confirm approved match; prepare scoped removal | pending | source owner | source check and unaffected-record comparison | planned |
| masked-copy | check membership; prepare scoped update | pending | data owner | updated artifact check | planned |
| features | scope affected rows; rebuild from unaffected inputs if approved | pending | pipeline owner | validation and unaffected-row check | unresolved |
| research-export | check membership after feature decision | pending | export owner | corrected export/required receipt | unresolved |
| training-snapshot | assess membership and current policy; no erasure claim | unknown | model owner | owner decision and any authorized check | unresolved |
| backups | review current retention and restore controls | unknown | data owner/privacy counsel | approved handling record | unresolved |

## Special handling
- Shared derivatives: `features` contains other records; scoped rebuild only after evidence and approval.
- Backups: policy absent; current review required.
- Models: membership and influence unknown; no unlearning or erasure claim.

## Unresolved
- Jurisdiction/current requirements — official-source and qualified review needed.
- `training-snapshot` membership and model impact — model owner evidence needed.
- Backup/restore handling — current retention policy and owner decision needed.

## Conclusion
- Graph completeness: incomplete; only supplied edges were assessed.
- Actions: proposed or unresolved; none performed or verified.
- No legal determination or complete-erasure claim is made by this plan.
```

**Bad output:**
> We deleted the record from `raw`, so every copy, backup, export, and trained model is erased and the request is complete.

Fails because no downstream check or change was performed, and graph, model, and backup evidence is incomplete.

## Edge cases
- **No approval or unclear scope**: stop and ask the authorized owner.
- **Performed but unverified**: retain execution evidence and mark verification pending; do not relabel the action planned.
- **Possibly identifying aggregate**: do not call it anonymous; request current privacy review.
- **Immutable backup**: document the constraint and restore controls; do not claim completion.
- **Unknown model lineage**: report the gap; infer neither that deletion nor retraining resolves it.

## Test case
**Input:**
> A fictional team has approval for one source record. Its manifest traces raw → cleaned → shared feature table → export and training snapshot. Backup policy and model membership are missing. Prepare a plan only.

**Assertions:**
1. The response starts from the approved decision and does not infer legal validity beyond that input.
2. Every downstream action is tied to supplied dependency evidence; missing links or membership remain unresolved.
3. The shared feature table is not deleted wholesale; a rebuild is conditional on preserving other records and validation.
4. Backup handling remains unresolved; model existence and lineage are questions unless evidenced, with no complete-erasure claim.
5. The report separates proposed actions from performed and verified changes and includes current-jurisdiction verification.
