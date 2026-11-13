---
id: PRT-002
name: print-proof-change-disposition
domain: Print Production Handoffs
subdomain: Proof control
version: 1.0
description: Reconcile proof corrections against an exact production revision when comments, approvals and replacement files disagree.
triggers: ["check whether proof comments were fixed","reconcile a revised print proof","which proof version is approved","prepare proof change signoff","resolve conflicting proof corrections"]
not_for: ["general document creation [CBG-005]","legal interpretation of approval terms","releasing an uninspected production file"]
requires: []
risk_level: medium
---

# Print proof change disposition

## Purpose
Create a correction ledger that ties every requested proof change to the affected location, replacement evidence and approval state. Prevent an approval for an earlier proof from being silently transferred to changed content.

## Inputs to collect
1. **Proof baseline:** Obtain proof identifier, revision and the actual pages or views reviewed. Required; a generic filename is insufficient when several versions share it.
2. **Comment set:** Collect corrections with author, target and wording. Default: unattributed or ambiguous notes remain unresolved rather than treated as instructions.
3. **Replacement evidence:** Obtain the revised proof or file and its identifier. Default: no claim that a correction was implemented.
4. **Approval roles:** Identify who may approve text, imagery, color intent and production release. Default: recommendations only; one reviewer is not assumed to control every category.
5. **Comparison scope:** Specify whether the review concerns content, layout, production marks or another bounded feature. Default: inspect only supplied evidence and state untested categories.
6. **Release conditions:** Obtain the actual proof acceptance and change-control process. Default: no automatic release.

If required inputs have no safe default, ask in one message with at most three questions.

## Procedure
1. Establish the baseline and proposed replacement as distinct revisions. Preserve the original proof and comments so later reviewers can reconstruct what changed.
2. Give each correction a stable local identifier and a precise location. Use page plus visible text or an object label when pagination may change; do not invent a locator that was not inspected.
3. Separate mandatory corrections, suggestions and questions according to supplied authority. A casual comment is not automatically an approved change request.
4. ⚠️ Resolve contradictory instructions before checking implementation. If one reviewer asks to remove a caption and another asks to rewrite it, record the conflict and its owner rather than averaging the requests.
5. Compare each requested change against the replacement evidence. Classify implemented as requested, partly implemented, not implemented, superseded by an authorized decision, or not inspectable.
6. Inspect nearby dependencies after an implemented change. A longer heading may shift a line break, move a page reference or obscure adjacent content even when its words are correct.
7. Record unrequested differences separately. Ask whether each is intentional and authorized; a replacement proof should not gain silent changes merely because one requested correction passed.
8. Map prior approvals to their exact scope. Preserve an unchanged category's approval only where the actual process permits it; do not assume changing text preserves a whole-job sign-off.
9. Prepare a concise unresolved list with the evidence or decision needed to close each item. Mark the revised proof ready for a named review, not ready for production, unless the required release evidence is supplied.
10. Deliver the correction ledger, approval boundary and verification limits. If only screenshots are available, identify which pages, objects or production properties could not be compared.

Use [VERIFY: proof acceptance, revision identification and release authority in the printer's current job instructions] before applying external requirements. This method does not define legal consequences of an approval or guarantee printed appearance from a screen image.

## Decision rules
- IF a correction cannot be located uniquely THEN request a precise target BECAUSE a plausible edit to the wrong occurrence leaves the real issue unresolved.
- IF the replacement differs beyond the authorized correction THEN flag the extra difference BECAUSE implementing one request does not authorize unrelated revisions.
- IF approval refers to another revision THEN retain its original scope BECAUSE a filename reused for new content does not renew approval.
- IF a reviewer accepts a known deviation THEN retain the deviation and named decision BECAUSE silently marking it fixed would erase what was actually accepted.

## Output template
```text
Proof pair: <baseline and replacement identities; up to three lines>
Correction ledger: <up to ten rows; attach continuation for remaining items>
ID/location | Requested change | Replacement evidence | Disposition | Next owner/check
Unrequested differences: <up to six findings or none established>
Approval map: <role, category, revision and evidenced state>
Release boundary: <ready for which next review, or blocked>
Verification: <views inspected and unperformed checks; up to four lines>
```

## Quality checklist
- [ ] Each correction has a precise target and supplied origin.
- [ ] Conflicting instructions remain visible until resolved.
- [ ] Implemented changes cite the replacement evidence.
- [ ] Partial implementation is not called complete.
- [ ] Neighboring layout or reference effects are checked or pending.
- [ ] Unrequested differences have a separate disposition.
- [ ] Approvals are tied to category and revision.
- [ ] Production release is not inferred from a correction ledger.

## Anti-patterns
- **Comment count closure:** every note receives a checkmark without comparison. Fix: cite the actual replacement evidence for each disposition.
- **Approval inheritance:** an old sign-off automatically covers a new proof. Fix: establish revision and category applicability.
- **Silent extras:** unrelated changes are ignored because the main correction passed. Fix: retain an unrequested-difference list.
- **Ambiguous target:** the first matching word is edited. Fix: identify the intended page and occurrence before action.
- **Screenshot overclaim:** a small preview proves production quality. Fix: bound inspection to visible content and list untested properties.

## Worked example
**Input:** Fictional studio Hazel supplies proof P and replacement Q. Comment C asks to change the cover title from “River Map” to “River Guide.” Q visibly contains River Guide. P's back page lists contact Elm; Q lists contact Fir without a supplied request. Editor Neri approved only P's wording. No production approval is supplied.

**Output:**
```text
Proof pair: P baseline; Q replacement; supplied cover and back-page views only.
Correction ledger:
ID/location | Requested change | Replacement evidence | Disposition | Next owner/check
C/cover title | River Map to River Guide | Q visibly says River Guide | implemented in supplied view | check full layout if needed
Unrequested differences: Back contact changed from Elm to Fir; intent and authorization absent.
Approval map: Neri approved P wording. Q wording and production release have no supplied approval.
Release boundary: Hold release; ask content owner to resolve contact change and review Q.
Verification: Supplied text views compared; full file, color and physical proof not inspected.
```

**Bad output:** “The title is fixed, so Q is approved for printing.”
One correction does not resolve an unrequested change or supply a release decision.

## Edge cases
- A page moves after correction: retain old and new locators so a missing page number does not look like an omitted change.
- A reviewer withdraws a comment: record the withdrawal source and retain the original issue history.
- Two replacement proofs arrive: establish which revision is under review before combining their passing corrections.
- A correction affects every occurrence: enumerate or define the search boundary and report any occurrences not inspected.

## Test case
**Input:**
> Fictional proof Q fixes a phone number on page A but page B repeats the old number. The comment explicitly required both locations. A message says “looks good” without identifying a revision.

**Assertions:**
1. Classifies the correction as partial.
2. Identifies page B as unresolved.
3. Does not treat the ambiguous message as proof of Q release.
4. States which further evidence closes the issue.
