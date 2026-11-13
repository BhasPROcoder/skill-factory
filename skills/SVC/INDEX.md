# Service Appointment Operations (SVC)

Reconcile resource occupancy, exclusive waitlist offers and appointment attendance from supplied service policies and event evidence.

Macro-area: Operations & Supply Chain

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| SVC-001 | [appointment-resource-conflict-reconciliation](appointment-resource-conflict-reconciliation/SKILL.md) | Reconcile overlapping service bookings against shared resource occupancy when appointment times alone do not establish feasibility. | resolve overlapping appointments; check room and staff double booking; reconcile a booking conflict | validated |
| SVC-002 | [exclusive-waitlist-offer-reconciliation](exclusive-waitlist-offer-reconciliation/SKILL.md) | Reconcile exclusive waitlist offers, expiry and late replies before reallocating a released service appointment. | handle a late waitlist acceptance; reallocate an expired appointment offer; reconcile overlapping waitlist offers | validated |
| SVC-003 | [appointment-attendance-evidence-disposition](appointment-attendance-evidence-disposition/SKILL.md) | Reconcile attendance and cancellation evidence before labeling a service appointment a no-show or preparing follow-up. | check whether this appointment was a no-show; reconcile check-in and cancellation records; prepare an attendance follow-up | validated |
