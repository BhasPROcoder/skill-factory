---
id: RNT-004
name: rental-usage-meter-reading-reconciliation
domain: Rental Asset Operations
subdomain: Usage readings
version: 1.0
description: Reconcile rental meter observations into supported usage intervals when units, resets, replacements or transcription conflicts make subtraction unreliable.
triggers: ["reconcile rental meter readings", "check usage between checkout and return", "the return counter is lower", "meter was replaced during hire", "resolve conflicting hour readings"]
not_for: ["rental invoice or tax calculations", "meter calibration or equipment repair", "inference billing allocation [CTG-002]"]
requires: []
risk_level: medium
---

# Rental usage meter reading reconciliation

## Purpose
Produce an evidence-based usage ledger for an identified rented asset and counter. Calculate only intervals whose endpoints, units and counter continuity are supported, retaining gaps instead of converting an implausible subtraction into a customer charge.

## Inputs to collect
1. **Asset and counter identity:** Obtain the rental unit, meter identifier and what it measures. This prevents mixing counters on the same machine. Default: none; required for a usage conclusion.
2. **Endpoint observations:** Collect checkout and return readings with original images or logs, units, observer and observation times. This defines the interval. Default: no endpoint invented from an expected use pattern.
3. **Counter behavior:** Obtain the applicable documentation for cumulative, resettable or wrapping behavior and display precision. This determines valid arithmetic. Default: undocumented discontinuity remains unresolved; verify the current applicable device documentation with its owner or manufacturer.
4. **Intervening events:** Collect resets, counter replacement, asset swaps and any before-and-after readings. This establishes whether subtraction spans one continuous counter. Default: continuity unknown if contradictory readings suggest a break.
5. **Included usage boundary:** Obtain the intended possession interval and any evidenced setup or workshop usage to distinguish. Default: report observed intervals without assigning all usage to the renter.
6. **Output unit:** Obtain any approved conversion basis. This controls arithmetic presentation. Default: retain source units; do not infer a conversion from a label abbreviation.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Identify the rental unit and specific counter in every observation. Separate distance, elapsed-operation and cycle counters even if their displayed values happen to be similar.
2. Transcribe each reading exactly as observed, preserving decimal marks, displayed units and source references. Keep an uncertain digit explicit rather than silently selecting the value that produces a plausible total.
3. Sort observations by observation time. Retain upload or entry times separately where they differ; do not rearrange readings merely to make the counter increase.
4. Mark each event that changes the counter's identity or continuity. Create distinct segments at evidenced resets, replacements and asset swaps instead of subtracting across those boundaries.
5. ⚠️ Check a decreasing reading against supplied counter behavior and event records. A decrease alone does not prove rollover, tampering or transcription error; list those as unresolved mechanisms only if relevant evidence supports investigating them.
6. Calculate end minus start within each continuous segment using the same counter and unit. Show the operands so the reviewer can reproduce the result; do not round intermediate differences unless the supplied measurement policy requires it.
7. Aggregate only complete, nonoverlapping segments with a consistent unit and a documented link to the requested scope. Keep missing segments visibly separate from the subtotal so a known minimum cannot be mistaken for complete usage.
8. ⚠️ Separate measured usage from attribution and billing. Workshop runs, transport or a delayed reading may fall outside the renter's interval even when the counter total is valid.
9. Specify the exact missing observation or counter documentation needed to resolve each gap. If no retrospective evidence exists, preserve the unknown interval rather than estimating it without a separately authorized estimation method.
10. Deliver the calculation ledger and its limits. Record whether the output is a complete supported total, a supported subtotal or an unresolved comparison; do not label it an invoice-ready charge.

## Decision rules
- IF a counter was replaced THEN split the timeline at replacement BECAUSE values from different counters do not share a continuous baseline.
- IF the return value is lower without an evidenced reset or documented wrap THEN leave usage unresolved BECAUSE adding an assumed display maximum invents the missing mechanism.
- IF an interval has compatible endpoints but uncertain custody attribution THEN report the measured interval separately BECAUSE measurement and responsibility are different conclusions.
- IF one segment lacks an endpoint THEN label any other segment sum a subtotal BECAUSE partial evidence cannot establish the full rental usage.

## Output template
```text
Scope: <asset, counter, requested interval and unit; up to three lines>
Reading ledger:
Source | Observation time | Counter | Reading/unit | Continuity event or uncertainty
<up to ten rows; attach a full timeline if larger>
Calculations: <one explicit subtraction per supported segment; up to eight lines>
Result: <complete total / subtotal / unresolved, with unit and scope>
Gaps: <missing evidence and its effect; up to five lines>
Attribution boundary: <what usage cannot yet be assigned or billed; up to three lines>
Next check: <owner and exact evidence request; up to three lines>
```

## Quality checklist
- [ ] Asset and counter identities are both recorded.
- [ ] Values retain their observed units and precision.
- [ ] Observation times are not replaced by upload times.
- [ ] Replacement or reset boundaries split the calculation.
- [ ] Every reported difference shows its operands.
- [ ] Aggregated segments do not overlap.
- [ ] Missing segments remain visible alongside subtotals.
- [ ] No unapproved fee or responsibility determination is made.

## Anti-patterns
- **Convenient rollover:** a lower reading is repaired with an invented maximum. Fix: obtain documented behavior and event evidence.
- **Counter blending:** an old counter start is subtracted from a replacement end. Fix: calculate separate continuous segments.
- **Plausibility transcription:** an unclear digit becomes the expected value. Fix: preserve ambiguity and request the original observation.
- **Subtotal promotion:** known intervals are presented as all usage. Fix: label the subtotal and missing span.
- **Automatic attribution:** every measured increment is assigned to the renter. Fix: reconcile the usage interval with the supplied custody boundary.

## Worked example
**Input:** Fictional rental firm Larch records unit U7's counter M1 at 120.5 hours on checkout and 124.0 immediately before documented replacement. New counter M2 is recorded at 0.0 on installation and 2.5 hours on return. The supplied event log establishes no unmeasured operating interval between those observations. Responsibility and rates are outside the request.

**Output:**
```text
Scope: Larch U7; M1 followed by M2; supplied checkout-to-return observations in hours.
Reading ledger:
Source | Observation time | Counter | Reading/unit | Continuity event or uncertainty
Checkout record | checkout | M1 | 120.5 hours | segment start
Replacement log | before replacement | M1 | 124.0 hours | M1 segment end
Installation log | installation | M2 | 0.0 hours | new counter baseline
Return record | return | M2 | 2.5 hours | M2 segment end
Calculations: M1: 124.0 - 120.5 = 3.5 hours. M2: 2.5 - 0.0 = 2.5 hours. Sum: 3.5 + 2.5 = 6.0 hours.
Result: Complete supported total across supplied continuous segments: 6.0 hours.
Gaps: None in the supplied measurement chain; exact clock times were not provided.
Attribution boundary: No allocation of responsibility or charge calculation performed.
Next check: Records owner confirms the supplied event log remains the applicable measurement record before downstream use.
```

**Bad output:** “Usage is 2.5 - 120.5 = -118.0 hours, so give a credit.”
The subtraction crosses counter identities and invents a billing consequence.

## Edge cases
- The display has a different decimal convention: retain the original string and resolve its interpretation using the applicable documentation before calculating.
- A counter wraps more than once: use evidenced wrap events or a separate complete log; endpoints alone may be insufficient.
- An asset swap occurs: make a separate ledger for each physical unit and combine only compatible, nonoverlapping evidenced intervals.
- A photo is captured after workshop activity: report the wider measured interval and isolate the unmeasured return-to-workshop span.

## Test case
**Input:**
> Fictional depot Moss supplies readings 98 and 3 from the same counter but no display range, reset record or intervening log. It asks for exact usage.

**Assertions:**
1. Does not infer a wrap maximum or exact usage.
2. Identifies a continuity or interpretation gap.
3. Requests applicable counter documentation and event evidence.
4. Makes no tampering accusation or fee calculation.
