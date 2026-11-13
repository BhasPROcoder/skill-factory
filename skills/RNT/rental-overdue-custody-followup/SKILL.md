---
id: RNT-005
name: rental-overdue-custody-followup
domain: Rental Asset Operations
subdomain: Custody follow-up
version: 1.0
description: Prepare an evidence-based follow-up for an apparently overdue rental when due-date changes, pickup arrangements or unposted returns leave custody uncertain.
triggers: ["rental still shows overdue", "check before chasing a return", "reconcile an unposted rental return", "customer says the item was collected", "prepare overdue equipment follow-up"]
not_for: ["debt collection or legal recovery", "late-fee calculation", "appointment no-show classification [SVC-003]", "theft investigation"]
requires: []
risk_level: medium
---

# Rental overdue custody follow-up

## Purpose
Create a custody timeline and a targeted draft inquiry before treating an overdue system flag as an established nonreturn. Separate agreed due time, actual possession, transport events and administrative posting so the next contact asks about the real gap.

## Inputs to collect
1. **Rental and asset identities:** Collect the transaction, unique units and any separately tracked accessories. This prevents a returned portion from closing the entire rental. Default: no asset identity inferred from a customer name alone.
2. **Due agreement:** Obtain the applicable due time, time zone and approved extensions. This defines the expected event. Default: an overdue label without its due basis is unverified.
3. **Custody evidence:** Collect checkout, collection, drop-off, receiving and transfer records with event times and actors. These identify the last supported holder. Default: no custody transfer inferred from a planned pickup.
4. **Posting history:** Obtain entry times, reversal records and open return-processing tasks. This separates administrative delay from physical nonreturn. Default: posting state alone does not establish location.
5. **Communications and authority:** Obtain relevant recipient statements and approved contact channel or sender. This supports a precise draft. Default: prepare the message without sending it.
6. **Operational dependencies:** Collect affected future reservations or urgent location needs. This sets internal follow-up priority. Default: do not promise a new customer that the overdue asset will be available.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Fix the rental snapshot and the units included in the overdue flag. Break a multi-unit rental into asset-level rows if different return events are possible.
2. Establish the latest supported due agreement, preserving prior terms and the evidence of any extension. An extension request awaiting approval remains a request rather than a revised deadline.
3. Build a chronological event ledger with event time, posting time, actor, unit and event type. Label scheduled pickups, customer reports and observed receipts distinctly.
4. ⚠️ Determine the last evidenced custody transfer for each unit. A carrier booking is a plan; a pickup receipt may establish collection without establishing depot receipt, depending on what the receipt actually records.
5. Compare the due agreement's required event with the observed timeline. If the agreement distinguishes customer drop-off, carrier pickup and depot receipt, use that supplied distinction rather than imposing one meaning of returned.
6. Classify the situation as overdue supported by supplied evidence, administrative posting gap, return in transit, disputed custody or insufficient evidence. Include the specific source that prevents a stronger conclusion.
7. Select the next evidence holder: depot receiver for an unposted receipt, pickup operator for an uncertain collection, or renter for an unconfirmed retained unit. Avoid sending the same accusation to every participant.
8. ⚠️ Draft a neutral inquiry with the rental reference, relevant asset, known event and one actionable evidence request. Do not include payment demands, legal threats or unsupported allegations in this operational follow-up.
9. Record an internal owner and the supplied review checkpoint. If no checkpoint is provided, propose one for owner confirmation rather than inventing a universal overdue escalation schedule.
10. Deliver the timeline, classification and draft with an execution note. A prepared draft is not a sent message, and a corrected return posting is not a physical custody event.

## Decision rules
- IF a receiving record identifies the unit before the due event but posting is missing THEN route the administrative mismatch internally BECAUSE a stale flag does not establish customer nonreturn.
- IF a pickup is merely scheduled THEN retain the prior custody evidence BECAUSE an appointment does not prove collection.
- IF a supplied receipt supports collection but not depot delivery THEN distinguish transit from depot possession BECAUSE those are separate transfers.
- IF an extension is unapproved THEN preserve both the applicable due agreement and pending request BECAUSE an inquiry does not amend the commitment by itself.
- IF custody is disputed THEN request the missing transfer evidence without blame BECAUSE inconsistent records do not establish intentional withholding.

## Output template
```text
Scope and due basis: <rental, units, snapshot and applicable agreement; up to four lines>
Timeline:
Event time | Posting time | Unit | Event and source | Evidence state
<up to ten rows; attach a full chronology if larger>
Custody conclusion: <last supported holder and uncertainty per unit; up to six lines>
Classification: <operational classification and reason; up to three lines>
Next action: <evidence holder, exact request, internal owner and review checkpoint; up to four lines>
Draft inquiry: <up to 120 words, or not needed with reason>
Execution note: <analysis, draft, contact and record-change states; up to two lines>
```

## Quality checklist
- [ ] The due event and time basis come from supplied agreement evidence.
- [ ] Pending extensions are not treated as approved.
- [ ] Each unit has its own custody conclusion when events differ.
- [ ] Event and posting times are distinguished.
- [ ] Scheduled actions are not promoted to completed transfers.
- [ ] The next request targets a specific evidence holder.
- [ ] The draft avoids unsupported blame, fees and legal claims.
- [ ] Sending and system-update states are explicit.

## Anti-patterns
- **Flag as verdict:** the dashboard label becomes proof of nonreturn. Fix: inspect the due and transfer evidence.
- **Booking as collection:** a pickup appointment closes custody. Fix: request an actual collection record.
- **Whole-rental closure:** one returned unit closes every asset. Fix: reconcile each unit separately.
- **Universal grace period:** an invented allowance changes the due basis. Fix: obtain the actual approved agreement.
- **Accusatory automation:** a threatening message is sent before reconciliation. Fix: prepare a neutral request and preserve sending authority.

## Worked example
**Input:** Fictional rental firm Elm shows unit E2 overdue after its agreed Tuesday 16:00 depot return. Receiving note R identifies E2 arriving Tuesday 15:40, with receiver Jo's acknowledgment. The note was entered Wednesday, and the return transaction remains unposted. No customer contact has occurred. Operations owns posting corrections.

**Output:**
```text
Scope and due basis: Elm E2; supplied Wednesday snapshot; agreement requires Tuesday 16:00 depot return in the supplied local-time basis.
Timeline:
Event time | Posting time | Unit | Event and source | Evidence state
Tuesday 15:40 | Wednesday | E2 | receiving note R, Jo acknowledgment | evidenced receipt
Custody conclusion: Depot receipt supported by R; return transaction remains administratively open.
Classification: Administrative posting gap; supplied receipt precedes the agreed due event.
Next action: Operations checks R against the transaction, records any authorized correction and confirms closure; review checkpoint to be set by the owner.
Draft inquiry: Not needed to the renter on supplied evidence. Internal request: Please reconcile E2's open return with receiving note R and confirm the resulting transaction state.
Execution note: Analysis and internal draft only; no message sent or transaction changed.
```

**Bad output:** “Your equipment is overdue; return it immediately or pay a penalty.”
It ignores the supported receipt and invents a penalty demand.

## Edge cases
- The contract uses a different return event than the dashboard: preserve both definitions and ask the process owner to reconcile the mismatch.
- A drop box is used without an immediate receipt: record the reported drop-off and seek the corresponding intake evidence without declaring either account false.
- An asset is returned to another branch: follow the identified branch's receipt and transfer chain rather than treating the original depot's absence as nonreturn.
- A customer reports an unauthorized collector: retain the statement and route the disputed transfer to the responsible incident owner without attempting a legal or theft determination.

## Test case
**Input:**
> Fictional depot Pine has a scheduled pickup for unit P3, but no collection record. The renter says a driver took it. The system says overdue.

**Assertions:**
1. Separates scheduled pickup from the reported collection.
2. Labels custody unresolved or disputed rather than assuming depot possession.
3. Requests the pickup operator's actual transfer evidence.
4. Does not send a message or assign blame without authorization and evidence.
