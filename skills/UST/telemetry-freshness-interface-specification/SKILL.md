---
id: UST-001
name: telemetry-freshness-interface-specification
domain: Interface State Contracts
subdomain: Data freshness
version: 1.0
description: Specify visible freshness states and recovery behavior for monitoring interfaces when delayed or missing observations could be mistaken for live data.
triggers: ["design stale telemetry states", "show when sensor data is old", "distinguish live and cached readings", "specify dashboard freshness", "handle delayed monitoring updates", "design reconnect display behavior"]
not_for: ["general empty-state writing [MPU-002]", "generic transition-test matrix construction [TST-003]", "device control or safety interlock design", "responsive component composition [CTG-011]"]
requires: []
risk_level: medium
---

# Telemetry Freshness Interface Specification

## Purpose
Produce a design contract that prevents a displayed observation from silently implying it is current. The contract separates transport availability, observation freshness, and missing evidence so designers and implementers can agree on display behavior before building it.

## Inputs to collect
1. **Observation meaning:** Identify the monitored quantity, its unit, and the task the viewer performs. These determine what a reading represents. Default: none; required for a concrete specification.
2. **Timestamp semantics:** Collect observation time, receipt time, clock source, timezone treatment, and any ordering identifier. These establish whether age can be interpreted. Default: unknown timestamps remain unknown; receipt time is not silently substituted.
3. **Freshness policy:** Obtain the task owner's acceptable observation age and boundary convention. This defines the state predicate. Default: no numerical threshold; present a policy question rather than invent one.
4. **Delivery behavior:** Collect update cadence, reconnect behavior, duplicate handling, and historical backfill behavior. These affect visible transitions. Default: unspecified delivery behavior is an open dependency.
5. **Interface scope:** List single readings, aggregate cards, charts, and available refresh actions. This defines where status must appear. Default: one read-only value card with no control authority.
6. **Consequence and audience:** Identify whether viewers may use the display for consequential operational decisions. This controls escalation of unresolved semantics. Default: information display only; safety-critical control design is outside scope.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Define the observation identity, including source and measurement type, so updates cannot silently replace a different signal's value.
2. Separate the evidence fields for observation age, transport status, and validity. A connected channel is not evidence that the newest observation is fresh.
3. ⚠️ Establish timestamp comparability before calculating age. When the source clock cannot be compared with the viewing clock, label age unknown instead of producing an apparently precise duration.
4. Write the freshness predicate using the supplied policy, including what happens exactly at its boundary. Keep missing, invalid, stale, and fresh observations distinct in the specification even if some share a visual container.
5. Assign visible content to each state: value visibility, status wording, observation time, and available action. Preserve the distinction between a historical value and an empty measurement; never replace missing data with zero.
6. Specify transition precedence. An invalid observation cannot become trusted merely because it arrived recently; a connection recovery cannot refresh an old observation's timestamp.
7. ⚠️ Define late-arrival behavior from observation ordering. A delayed historical sample may belong on a chart without replacing the latest value card. Where ordering is unresolved, flag the conflict instead of inventing precedence.
8. Specify recovery feedback separately from recovery success. A refresh request may show a pending state, but the display becomes fresh only after qualifying observation evidence arrives.
9. Walk through normal update, stale transition, disconnection, reconnect with old data, and fresh recovery using supplied or clearly fictional events. Record the expected value and status after each event.
10. Deliver the state contract and unresolved dependencies. Label it a design specification; implementation, rendering, accessibility evaluation, and device verification require their own evidence.

## Decision rules
- IF transport is connected but the last comparable observation exceeds the supplied age policy THEN show stale data alongside connected transport BECAUSE connection status does not establish measurement recency.
- IF timestamp semantics are missing or incompatible THEN show freshness unknown BECAUSE a precise age would imply evidence that is unavailable.
- IF no observation exists THEN show an explicit unavailable value BECAUSE zero is a measurement rather than a synonym for absence.
- IF reconnect delivers only historical observations THEN retain historical labeling BECAUSE successful delivery does not make old events current.
- IF the product is used for safety-critical control THEN route control and alarm requirements to qualified domain review BECAUSE this display contract does not establish safe operating decisions.

## Output template
```text
Scope: <one sentence stating the signal and viewer task>
Evidence: <timestamp semantics, transport evidence, and policy; up to four lines>
State contract:
<state | predicate | value treatment | status text | user action>
<four to seven rows>
Transition walkthrough:
<event | resulting value/state | reason>
<four to six rows>
Open dependencies: <up to five unresolved items, or none>
Delivery status: <specification only; identify unperformed implementation checks>
```

## Quality checklist
- [ ] Observation and receipt timestamps have separate meanings.
- [ ] Every numerical freshness boundary is supplied or explicitly fictional.
- [ ] The boundary convention is stated rather than implied.
- [ ] Unknown, absent, invalid, stale, and fresh observations have defined handling.
- [ ] Connection recovery alone cannot produce a fresh label.
- [ ] Late samples cannot silently overwrite newer observations.
- [ ] Status is expressed in words rather than color alone.
- [ ] The walkthrough includes old data delivered after reconnect.
- [ ] Delivery wording distinguishes a specification from an implemented interface.

## Anti-patterns
- **Receipt-time laundering:** Treating a newly received old sample as current. Fix: evaluate the observation time under the supplied clock policy.
- **Green connection shortcut:** Coloring every connected sensor as healthy. Fix: present transport and observation freshness separately.
- **Invented timeout:** Choosing a familiar refresh interval as a universal stale boundary. Fix: obtain the task owner's age policy and explain unresolved cases.
- **Zero substitution:** Displaying zero when a sample is missing. Fix: use an unavailable indicator and retain any historical value as historical.
- **Optimistic recovery:** Clearing stale status when refresh is clicked. Fix: distinguish request pending from qualifying evidence received.

## Worked example
**Input:**
Fictional exhibit studio Lumen monitors a decorative fountain's water-height display. This is a read-only demonstration, not a safety system. Its supplied policy defines fresh as an observation no more than 2 minutes old, including exactly 2 minutes. Observation and viewer clocks are comparable. At 10:00 the latest valid reading is 40 display units, observed at 09:57. The link is connected. At 10:01 it disconnects, at 10:02 it reconnects with that same old observation, and at 10:03 it delivers a valid reading of 41 observed at 10:03.

**Output:**
```text
Scope: Show the recency of the decorative fountain's read-only height observation.
Evidence: Observation time determines age; viewer and source clocks are comparable.
Transport is supplied independently. Fresh means age at most 2 minutes, inclusive.
State contract:
Fresh | valid comparable age at most 2 minutes | show value | Current observation | none required
Stale | valid comparable age over 2 minutes | retain as historical | Last observation is old | request update if available
Unknown | clock comparison unavailable | qualify value | Freshness unknown | inspect timestamp source
Unavailable | no observation | no numeric value | No observation received | inspect source
Invalid | validity rejected | do not present as trusted | Observation invalid | inspect evidence
Transition walkthrough:
10:00 connected | 40, stale | 3-minute observation age exceeds policy
10:01 disconnected | 40, stale plus disconnected | no replacement observation
10:02 reconnect with 09:57 sample | 40, stale plus connected | observation remains historical
10:03 new valid 10:03 sample | 41, fresh plus connected | observation age is zero
Open dependencies: Whether an authorized manual update action is available.
Delivery status: Specification only; no interface implementation or rendering checks performed.
```

**Bad output:**
“The reconnected card becomes green and live at 10:02; show zero while disconnected.”
This confuses transport with recency and fabricates a numerical measurement during missing delivery.

## Edge cases
- A timestamp appears in the future: flag incompatible clock evidence; do not silently clamp the age to zero.
- A chart contains mixed-age samples: retain event ordering and mark the latest qualifying observation separately from historical backfill.
- An aggregate mixes fresh and stale sources: disclose constituent coverage and define aggregation eligibility before presenting a current total.
- The interface remains open without new events: specify age reevaluation so a once-fresh value can become stale without a new delivery.

## Test case
**Input:**
> Fictional studio Fern receives a reading observed yesterday through a connection that recovered just now. Observation and viewer clocks are comparable, but no acceptable age policy has been supplied. Draft the display contract without inventing a timeout.

**Assertions:**
1. Connection recovery is separated from observation recency.
2. The output does not classify the reading as fresh based only on receipt time.
3. The missing freshness policy is an explicit question or dependency without an invented boundary.
4. Historical observation time remains visible or explicitly required in the contract.
