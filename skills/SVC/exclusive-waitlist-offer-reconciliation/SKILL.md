---
id: SVC-002
name: exclusive-waitlist-offer-reconciliation
domain: Service Appointment Operations
subdomain: Waitlist offers
version: 1.0
description: Reconcile exclusive waitlist offers, expiry and late replies before reallocating a released service appointment.
triggers: ["handle a late waitlist acceptance", "reallocate an expired appointment offer", "reconcile overlapping waitlist offers", "check who owns a released slot", "design waitlist offer transitions"]
not_for: ["resource occupancy conflict review [SVC-001]", "sales lead prioritization", "clinical urgency or emergency triage"]
requires: []
risk_level: medium
---

# Exclusive waitlist offer reconciliation

## Purpose
Prepare a defensible disposition when a released appointment is offered to waiting customers under an exclusive-offer policy. Preserve the difference between an offer, a reply and a confirmed booking so late or duplicated messages do not create competing promises.

## Inputs to collect
1. **Slot identity:** Obtain appointment date, time, service, resources and current availability evidence. This identifies exactly what may be allocated. Default: an unverified slot cannot be promised.
2. **Queue policy:** Obtain eligibility, ordering, contact rules and any authorized priority exceptions. Default: do not invent first-come or priority ordering.
3. **Offer record:** Collect recipient, offer identifier, creation and expiry semantics, delivery evidence and status. Default: missing timestamps or recipient identity leave the offer unresolved.
4. **Acceptance rule:** Obtain which event counts as timely acceptance, including clock source and boundary treatment. Default: message arrival and customer sending time are not assumed interchangeable.
5. **Booking evidence:** Obtain any resulting hold, accepted response, confirmed booking, cancellation or reallocation. Default: a reply alone is not proof that a booking exists.
6. **Authority:** Identify who can extend, withdraw, reissue or confirm the offer. Default: prepare a disposition without contacting customers or changing records.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Establish the slot's current authoritative state before reading queue order. A release notice may be outdated because a booking has already been confirmed.
2. Link replies to their exact offer and slot identifiers. A customer responding to a different date must not acquire the current slot through a name match.
3. Reconstruct an event sequence using the supplied timestamp semantics. Preserve uncertain ordering rather than sorting incomparable client and server clocks into a false chronology.
4. Apply the supplied expiry rule to each reply, including the exact boundary. Record the rule and evidence alongside the timely, late or unresolved classification.
5. ⚠️ Check for an active exclusive offer or confirmed booking before proposing a new offer. Silence, delivery failure or a late reply does not automatically release the resource unless the supplied policy says so.
6. Separate eligibility from acceptance. A timely reply may still fail a service prerequisite, while an eligible customer may not have replied within the offered window.
7. Evaluate a late reply against the current slot state and the authority to make exceptions. Do not revoke another customer's confirmed booking to accommodate an earlier recipient without the applicable process and agreement.
8. Draft the next action with an explicit precondition, such as “recheck slot free, then issue the next authorized offer.” Record a unique proposed action identity so repeated handling of the same reply does not create multiple allocations.
9. Specify how duplicates and corrections are recorded. Retain the original offer and reply history; an amended expiry should not erase evidence of which terms the customer originally received.
10. Deliver the disposition and customer-message draft if requested. Label drafts as unsent and confirmations as pending until the actual booking evidence exists.

## Decision rules
- IF a reply is timely but the slot record shows a conflicting booking THEN hold the allocation decision BECAUSE timely acceptance alone cannot resolve two commitments.
- IF an offer has expired under the supplied rule and the slot remains free THEN consider reissue only through the authorized queue policy BECAUSE expiry does not establish who is eligible next.
- IF delivery failed THEN consult the supplied retry or expiry policy BECAUSE an undelivered offer may still occupy an exclusive hold.
- IF duplicate replies refer to one offer THEN reconcile them as one acceptance attempt BECAUSE message count is not booking count.
- IF an expiry extension is proposed after another offer exists THEN expose the competing promise BECAUSE retroactive extension can invalidate the current allocation.

## Output template
```text
Slot: <identity and latest authoritative state; up to two lines>
Policy basis: <queue, acceptance and expiry rules; up to four lines>
Event ledger:
Event | Offer/slot identity | Relevant time | Evidence | Interpretation
<up to eight rows; attach more history if needed>
Disposition: <acceptance classification and allocation state>
Next action: <one proposed action, preconditions and authorized role>
Customer wording: <optional unsent draft, at most four sentences>
Open evidence: <up to three consolidated questions>
Execution status: <observed actions versus proposals>
```

## Quality checklist
- [ ] Every reply is matched to an offer and slot.
- [ ] The acceptance timestamp rule is explicit.
- [ ] The expiry boundary is applied without an invented grace period.
- [ ] Active holds and confirmed bookings are checked separately.
- [ ] Queue ordering comes from supplied policy.
- [ ] Late acceptance does not silently displace another customer.
- [ ] Duplicate handling preserves one allocation attempt.
- [ ] Proposed messages and booking changes are not reported as executed.

## Anti-patterns
- **Reply equals booking:** an affirmative message becomes a confirmed appointment. Fix: check the actual allocation result.
- **Grace by habit:** an arbitrary extension is granted. Fix: obtain the exception policy and current slot state.
- **Queue invention:** the next name is selected from an unverified list. Fix: establish eligibility and ordering evidence.
- **History rewrite:** the original expiry is edited to make a late reply timely. Fix: preserve the original terms and record any authorized exception separately.
- **Double offer:** a new exclusive offer is sent while the first remains active. Fix: reconcile release evidence before preparing reallocation.

## Worked example
**Input:** Fictional repair studio Juniper offers slot Cedar to customer Nia. Supplied policy says server receipt before 14:00 is timely; exactly 14:00 or later is expired. Offer J closes at 14:00. Nia's acceptance reaches the server at 14:02. At 14:01, the studio confirmed customer Omar into Cedar under its authorized next-customer process. No cancellation authority or exception agreement is supplied.

**Output:**
```text
Slot: Cedar; latest supplied state is Omar's confirmed booking at 14:01.
Policy basis: Offer J requires server receipt before 14:00. Boundary is exclusive; no grace period supplied.
Event ledger:
Event | Offer/slot identity | Relevant time | Evidence | Interpretation
Expiry | J/Cedar | 14:00 | supplied terms | exclusive offer expired
New confirmation | Cedar | 14:01 | supplied booking record | Omar holds confirmed booking
Acceptance | J/Cedar | 14:02 | server receipt | late under supplied rule
Disposition: Nia's reply is late; Cedar is already confirmed to Omar. No override is authorized.
Next action: Authorized coordinator verifies current booking and offers Nia only alternatives supported by the queue and availability policy.
Customer wording: Unsent draft: Your reply reached us after the offer window, and that appointment has since been allocated. We can check the next available option for you.
Open evidence: Which alternative slots and queue actions are authorized for Nia?
Execution status: Records analyzed only; no messages sent or bookings changed.
```

**Bad output:** “Nia was offered first, so cancel Omar and confirm her.”
An earlier offer does not supply authority to reverse a later confirmed allocation.

## Edge cases
- The timestamp is exactly at expiry: apply the supplied inclusive or exclusive rule; if absent, preserve uncertainty.
- Client sending time precedes expiry but server receipt follows it: use the specified acceptance event, not whichever time favors a preferred outcome.
- A slot changes duration or service: treat the changed terms as a distinct offer requiring appropriate acceptance, not an automatic carryover.
- The acceptance is withdrawn before confirmation: reconcile withdrawal and booking events before making another promise.

## Test case
**Input:**
> Fictional studio Willow has two affirmative replies for the same offer identifier. The slot is marked held, but expiry and confirmation records are missing.

**Assertions:**
1. Treats replies as potentially duplicate events for one offer.
2. Does not equate held with confirmed or free.
3. Requests expiry and allocation evidence before reallocation.
4. Does not issue a new exclusive offer.
