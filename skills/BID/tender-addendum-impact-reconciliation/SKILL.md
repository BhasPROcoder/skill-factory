---
id: BID-003
name: tender-addendum-impact-reconciliation
domain: Procurement Evidence Decisions
subdomain: Tender revisions
version: 1.0
description: Trace an issued tender change into affected bid drafts and sign-offs when the response already has a working baseline.
triggers: ["update a bid after an addendum", "which response sections must change", "reconcile conflicting tender updates", "trace a revised bid quantity", "check our bid against this amendment"]
not_for: ["comparing supplier offers [BID-001]", "adjudicating a contract dispute", "general vendor selection [MOP-004]"]
requires: []
risk_level: medium
---

# Tender addendum impact reconciliation

## Purpose
Prepare a change ledger for a response already under development when the issuing organization changes its request. Use the ledger to tell response owners which artifacts need revision, which existing decisions still hold, and which questions prevent a reliable update.

## Inputs to collect
1. **Baseline packet.** Obtain the version used to prepare the current response, including the relevant schedules. Without it, report what the new notice says but mark comparisons to previous requirements unavailable.
2. **Change evidence.** Request the actual addendum and the evidence connecting it to this request, lot, and version. If only a forwarded summary exists, retain it as a lead and ask for the issuer's published notice.
3. **Draft inventory.** Identify the working response sections, prices, forms, supporting evidence, and internal sign-offs. If drafts cannot be inspected, label impact predictions as checks for the owner.
4. **Authority and sequence.** Ask for the issuer's applicable ordering instructions and any intervening changes. Do not assume that the most recently downloaded file controls.
5. **Working boundary.** Establish whether the user wants analysis, edits to named drafts, or a handoff for someone else. Default to analysis; neither sending questions nor submitting a response is part of this review.

If required inputs lack a safe default, ask for them in one message with at most three questions.

## Procedure
1. Identify the exact response package under review. Preserve its baseline identity even if a new version will eventually replace it. Keep similarly titled lots apart.
2. Locate the changed passage in its surrounding section. Capture a usable locator such as a supplied schedule name and row label. When pagination differs between copies, use a distinctive heading and the affected item instead of guessing a page.
3. Separate each change into a single instruction. Distinguish replacing a value, withdrawing an item, introducing a new obligation, and clarifying a term. Record an unresolved relationship if the notice does not say how its wording affects an existing requirement.
4. ⚠️ Reconstruct the applicable sequence from the issuer's references. A later message may discuss a different lot or merely announce a future notice. Preserve incompatible instructions side by side until an authoritative source resolves the conflict.
5. For each resolved change, write a before-and-after statement with its evidence. Keep an unrelated baseline condition in a separate unchanged field when the user might otherwise assume it has changed too.
6. Trace the change into the response. Start with the directly affected artifact, then follow actual dependencies: a revised quantity can affect an extended price, a narrative commitment, and an approval based on the old total. Do not invent downstream artifacts that were never supplied.
7. Record the needed action for every affected item. Separate a proposed edit from an edit actually inspected. If a signed or submitted artifact is implicated, flag its state and ask for the applicable revision process rather than silently treating it as an editable draft.
8. ⚠️ Check copied values and linked calculations in both directions. A spreadsheet can contain the new amount while a cover letter still cites the old amount. Conversely, changing every occurrence of a number may corrupt a different lot that retains its original quantity.
9. Produce a handoff that assigns each open check to a supplied owner or a proposed role. State the source or decision needed to close it. Reconcile open checks before calling the response internally consistent; issuer acceptance remains a separate event.

## Decision rules
- IF the notice identifies only one lot THEN limit automatic impact mapping to that lot BECAUSE adjacent lots may share labels without sharing requirements.
- IF the original requirement is unavailable THEN record the new instruction without inventing a previous value BECAUSE a change summary needs an evidenced baseline.
- IF two applicable notices conflict without established precedence THEN hold the affected response item and draft a precise question BECAUSE file order is not proof of authority.
- IF a price changes but a sign-off refers to the earlier amount THEN flag the sign-off for review BECAUSE arithmetic alone cannot renew someone's approval.
- IF the reported change is still a proposal THEN preserve the current baseline and track the proposal separately BECAUSE preparing for a possible update is different from treating it as issued.

## Output template
```text
Packet: <request, lot, baseline, addendum; one line>
Change ledger: <one row per material change>
Locator | Before | After | Evidence and disposition
Response impact: <one row per affected artifact>
Artifact | Required revision or check | Owner or proposed role | Status
Unchanged: <specific retained conditions relevant to this change>
Open questions: <up to three consolidated questions or none>
Release note: <what is ready, what is blocked, what was actually done>
```

## Quality checklist
- [ ] Each changed item has a source locator or an explicit missing-source note.
- [ ] Baseline and revised values are distinguishable from estimates.
- [ ] Lot and artifact identifiers remain attached to each affected row.
- [ ] Dates, quantities, and totals are changed only where source evidence supports the change.
- [ ] Recomputed arithmetic uses the same units as the draft and shows its basis.
- [ ] Conflicting revisions are recorded instead of silently ranked.
- [ ] The release note distinguishes proposed edits, completed checks, and external submission.

## Anti-patterns
- **Global replacement**: every identical number in the response changes. Fix: match the referenced lot, obligation, and artifact before editing.
- **Download-order authority**: the last file saved is declared authoritative. Fix: check the issuer's references and identify unresolved precedence.
- **Arithmetic-only review**: the price table is corrected but the signed narrative is ignored. Fix: trace dependencies through commitments and approvals.
- **False acknowledgment**: the handoff claims the bidder accepted the change. Fix: identify the required evidence and leave acknowledgment unconfirmed unless it is supplied.

## Worked example
**Input:** Fictional studio Vale is preparing a response for Lot Birch. In baseline Schedule Kits, the row “display kits” calls for six kits. Issued notice Amber explicitly replaces that row with eight kits and says delivery arrangements are unchanged. The draft price sheet charges five fictional credits per kit, the cover letter promises six kits, and the purchasing lead approved the original total of thirty credits. No files have been edited.

**Output:**
```text
Packet: Lot Birch | baseline Schedule Kits | issued notice Amber.
Change ledger:
Locator | Before | After | Evidence and disposition
Schedule Kits, display kits | six kits | eight kits | Amber explicitly replaces this row for Birch.
Response impact:
Artifact | Required revision or check | Owner or proposed role | Status
Price sheet | At five credits per kit, change six × five = thirty to eight × five = forty credits | proposed pricing owner | calculated, draft edit pending
Cover letter | Replace the six-kit commitment with eight kits for Birch | proposed response editor | edit pending
Original approval | Ask whether the revised forty-credit amount is approved | purchasing lead | approval pending
Unchanged: Delivery arrangements, explicitly retained by Amber.
Open questions: Does the purchasing lead approve the revised amount?
Release note: Change and arithmetic reconciled; draft updates and approval outstanding. Nothing submitted.
```

**Bad output:** “I submitted the updated bid for forty credits using the original approval.”
The example supplies neither submission authority nor approval for the revised amount.

## Edge cases
- A notice references an attachment that was not supplied: list the dependent response items and hold comparisons involving the missing attachment.
- A clarification is published after a response was already sent: record which version was submitted and verify the issuer's current amendment pathway before proposing resubmission.
- A replacement removes a line entirely: trace formulas and narrative references to the removed line; do not assume removal means a zero-priced deliverable.
- Two teams interpret the same phrase differently: record the practical consequence of each interpretation and draft one targeted clarification question without sending it.

## Test case
**Input:**
> Fictional supplier Sedge has a draft for Lots Oak and Elm. A verified notice changes only Oak's packaging requirement. A colleague says Elm changed too, but cannot supply an issuer notice. Prepare the handoff.

**Assertions:**
1. Oak's change is bounded to the verified notice; missing original wording is left unspecified.
2. Elm's reported change is separated as unverified rather than applied.
3. Affected packaging commitments are identified as checks if the draft content is unavailable.
4. No acknowledgment, approval, or submission is claimed.
