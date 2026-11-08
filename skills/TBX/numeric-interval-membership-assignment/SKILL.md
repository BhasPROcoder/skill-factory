---
id: TBX-003
name: numeric-interval-membership-assignment
domain: Table Transformation Contracts
subdomain: Interval membership
version: 1.0
description: Assign supplied numeric observations to explicit intervals when endpoint inclusion, gaps or overlapping ranges can make category membership ambiguous.
triggers: ["assign values to interval labels", "check open and closed bin edges", "find ambiguous numeric categories", "preserve out of range observations", "classify measurements using supplied ranges"]
not_for: ["dataset range validity audit [TDQ-004]", "choosing statistically optimal histogram bins", "setting legal or medical thresholds"]
requires: []
risk_level: medium
---

# Numeric Interval Membership Assignment

## Purpose
Produce one traceable membership result for each observation using supplied range definitions. Expose absent values, unmatched values and multiple matches separately, without choosing a category from list order or treating an unassigned observation as invalid data.

## Inputs to collect
1. **Observations** — obtain stable observation identities, numeric text and a source snapshot. Identity preserves repeated measurements as separate rows. Default: none; do not replace missing values with zero.
2. **Interval definitions** — obtain unique labels, finite lower and upper endpoints, and an inclusion flag for each endpoint. These define the classification contract. Default: no thresholds or endpoint convention is inferred.
3. **Measurement meaning** — obtain the common unit and any prior conversion or rounding rule. Comparable numbers can still represent incompatible quantities. Default: no conversion or rounding; ask if units differ.
4. **Ambiguity policy** — establish whether multiple memberships are permitted downstream. Default: retain every match and label the row ambiguous; never select the first match silently.
5. **Output boundary** — identify the destination and required schema. Default: an in-memory diagnostic table with original values, labels and status; no source mutation or external write.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Group all missing endpoint conventions in one request for the range specification.

## Procedure
1. Freeze the selected observation and range snapshots. Retain original numeric text separately from parsed values so later correction does not erase the submitted evidence.
2. Validate unique observation identities and interval labels. Duplicate numeric values may remain, but duplicate identifiers must be resolved before producing an accepted keyed result.
3. Validate each range definition. Reject reversed endpoints, missing inclusion flags and empty ranges; equal endpoints describe a singleton only when both endpoints are included.
4. Parse observations under one explicit numeric representation. ⚠️ Do not use a floating-point approximation or an invented epsilon to decide decimal boundary membership; the reference uses exact decimal text comparisons without arithmetic or quantization.
5. Evaluate every interval for each parsed observation. Retain all matching labels, rather than stopping at the first successful comparison.
6. Assign exactly one diagnostic status per observation: missing, invalid, unmatched, assigned or ambiguous. Only assigned means exactly one matching interval; unmatched says nothing about whether the measurement itself is valid.
7. Test every supplied endpoint as an additional probe. ⚠️ Shared boundaries require checking both neighboring inclusion flags; a sorted label list cannot resolve double inclusion or double exclusion.
8. Reconcile output identities against the input identities. Count statuses and inspect missing, invalid, unmatched and ambiguous rows before a downstream consumer accepts a single-category table.

The runnable Python 3 reference accepts finite decimal strings and explicit None for missing values. Range tuples are label, lower text, upper text, lower-closed and upper-closed. Observation tuples are unique string identity and numeric text or None. Save the complete snippet and run it with the installed Python 3 interpreter, recording its version and results; external serializers and unit conversions are outside this model.

```python
from decimal import Decimal, InvalidOperation

def number(text):
    if not isinstance(text, str):
        raise ValueError("decimal text required")
    try:
        value = Decimal(text)
    except InvalidOperation as exc:
        raise ValueError("invalid decimal") from exc
    if not value.is_finite():
        raise ValueError("finite value required")
    return value

def assign(rows, definitions):
    labels, ranges = set(), []
    for label, lower, upper, lc, uc in definitions:
        if not isinstance(label, str) or not label or label in labels:
            raise ValueError("unique nonempty labels required")
        labels.add(label)
        if type(lc) is not bool or type(uc) is not bool:
            raise ValueError("explicit endpoint flags required")
        lo, hi = number(lower), number(upper)
        if lo > hi or (lo == hi and not (lc and uc)):
            raise ValueError("empty or reversed interval")
        ranges.append((label, lo, hi, lc, uc))
    seen, output = set(), []
    for key, text in rows:
        if not isinstance(key, str) or not key or key in seen:
            raise ValueError("unique nonempty row identities required")
        seen.add(key)
        matches = []
        if text is None:
            status = "missing"
        else:
            try:
                value = number(text)
            except ValueError:
                status = "invalid"
            else:
                matches = [label for label, lo, hi, lc, uc in ranges
                           if (value > lo or (lc and value == lo))
                           and (value < hi or (uc and value == hi))]
                status = ("unmatched" if not matches else
                          "assigned" if len(matches) == 1 else "ambiguous")
        output.append((key, text, status, matches))
    return output

ranges = [("low", "0", "5", True, False),
          ("middle", "5", "10", True, True),
          ("high", "10", "15", True, False)]
rows = [("a", "5"), ("b", "10"), ("c", "15"),
        ("d", None), ("e", "not measured")]
result = assign(rows, ranges)
assert [r[2] for r in result] == [
    "assigned", "ambiguous", "unmatched", "missing", "invalid"]
assert result[0][3] == ["middle"]
assert result[1][3] == ["middle", "high"]
assert assign([("p", "0.1")], [("point", "0.1", "0.1", True, True)])[0][3] == ["point"]
print("interval membership checks passed")
```

## Decision rules
- IF an observation matches several ranges THEN retain all labels and mark ambiguity BECAUSE category order does not authorize precedence.
- IF an observation matches no range THEN retain it as unmatched BECAUSE the supplied intervals may intentionally leave gaps.
- IF an endpoint inclusion flag is absent THEN request the definition before assigning BECAUSE equality cannot be resolved from the endpoint number alone.
- IF a missing or nonfinite observation appears THEN preserve a distinct diagnostic status BECAUSE zero substitution changes membership evidence.
- IF single-label output is required but ambiguity remains THEN withhold that accepted output BECAUSE arbitrary tie-breaking would change the classification contract.

## Output template
```text
Contract: <snapshot, unit, numeric representation and endpoint definitions; four lines>
Membership: <identity, original value, status, all matching labels; first twelve rows plus full artifact if longer>
Endpoint probes: <tested endpoint, matches and interpretation; up to eight rows plus full artifact>
Reconciliation: <input/output counts and counts by status; two lines>
Disposition: <accepted diagnostic output or blocked single-label output, with required clarification; two lines>
Limits: <two sentences on coverage, meaning and external execution>
```

## Quality checklist
- [ ] Every interval has both endpoint inclusion flags.
- [ ] Reversed and empty intervals fail before assignment.
- [ ] Original observation identities and values are retained.
- [ ] Every interval is evaluated for each parsed observation.
- [ ] Multiple matches remain visible without implicit precedence.
- [ ] Missing, invalid and unmatched are distinct statuses.
- [ ] Shared endpoints receive explicit probes.
- [ ] Status counts sum to the original observation count.

## Anti-patterns
- **First-match bias**: interval order selects the category. Fix: collect all memberships before choosing a status.
- **Boundary guess**: familiar bracket conventions are assumed. Fix: require each inclusion flag explicitly.
- **Gap erasure**: unmatched observations are discarded. Fix: retain their identities and diagnostic status.
- **Epsilon repair**: an arbitrary tolerance nudges values into a preferred bin. Fix: obtain an authorized rounding policy or compare the supplied decimal values exactly.
- **Validity overclaim**: membership is treated as evidence the measurement is correct. Fix: distinguish classification from measurement quality.

## Worked example
**Input:**
> Fictional sensor table Juniper S uses a common arbitrary unit and decimal text. Ranges are low [0,5), middle [5,10], high [10,15). Rows a=5, b=10, c=15, d=null and e="not measured". Produce diagnostic memberships, without single-label precedence.

**Output:**
```text
Contract: Juniper S; common supplied unit; exact decimal comparisons. low=[0,5), middle=[5,10], high=[10,15).
Membership: a,5,assigned,[middle]; b,10,ambiguous,[middle,high]; c,15,unmatched,[]; d,null,missing,[]; e,not measured,invalid,[].
Endpoint probes: 0->[low]; 5->[middle]; 10->[middle,high]; 15->[]. Shared 10 is included twice; outer 15 is excluded.
Reconciliation: 5 input rows and 5 output rows. Assigned=1, ambiguous=1, unmatched=1, missing=1, invalid=1; total=5.
Disposition: Diagnostic output accepted. A complete single-label table requires resolving b and specifying handling of c, d and e.
Limits: Observed memberships and listed endpoints were evaluated; exhaustive coverage over an intended universe was not established. No measurement validity or external write is claimed.
```

**Bad output:** "Assign b to middle because it appears first, replace d with zero and delete c."
This invents precedence, changes a missing observation and hides an unmatched one.

## Edge cases
- **No ranges supplied**: ask whether an empty classification scheme is intentional; if confirmed, every finite observation is unmatched rather than assigned a default label.
- **Equal endpoints**: accept only a closed singleton; reject other equal-endpoint definitions as empty rather than silently ignoring them.
- **Unbounded ranges**: request an explicit extension of the finite-endpoint contract; do not disguise infinity as a very large number.
- **Rounded source values**: classify the supplied representation and disclose that boundary uncertainty in the original measurement is unresolved.
- **Intentional overlaps**: preserve all labels if multilabel output is authorized; retain the reference's ambiguous diagnostic to show multiplicity, and document any renamed downstream status.

## Test case
**Input:**
> Fictional ranges A=(0,2), B=(2,4] and C=[4,6]. Observations x=2, y=4 and z=null. Assign categories and explain the boundary behavior without choosing a preferred range.

**Assertions:**
1. x remains unmatched because both adjacent intervals exclude 2.
2. y retains B and C and is marked ambiguous.
3. z remains missing rather than becoming zero or unmatched.
4. All three observation identities remain in the diagnostic output.
