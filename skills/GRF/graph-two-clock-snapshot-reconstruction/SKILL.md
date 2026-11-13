---
id: GRF-005
name: graph-two-clock-snapshot-reconstruction
domain: Graph Engineering Foundations
subdomain: Temporal graph reconstruction
version: 1.0
description: Reconstruct an evidence-linked graph edge view at an effective-time point and a recorded-time cutoff when late corrections or retractions change historical answers.
triggers: ["reconstruct a graph as known then", "separate effective time from recorded time", "query graph history after late corrections", "preserve retracted graph assertions", "explain different historical graph snapshots"]
not_for: ["general dataset lineage mapping [TDS-002]", "authorized dataset withdrawal planning [TDS-012]", "scalar interval category assignment [TBX-003]", "temporal path planning or live database migration"]
requires: []
risk_level: medium
---

# Graph Two Clock Snapshot Reconstruction

## Purpose
Produce a graph edge view answering what relationships were asserted for one effective-time point according to records available at another time. Preserve corrections and explicit retractions so later knowledge does not silently rewrite an earlier answer. This reconstructs supplied assertions, not independently established historical truth.

## Inputs to collect
1. **Question and two clock values** — collect the effective-time point and recorded-time cutoff separately; why: a late report can describe an earlier relationship. Default: none; do not substitute the present for either clock.
2. **Versioned assertion ledger** — collect stable edge identity, unique revision identity, endpoints, assertion state, both intervals and source references; why: overwriting revisions makes earlier views unrecoverable. Default: supplied history only; missing revisions remain a coverage limitation.
3. **Time contract** — obtain units, timezone/precision where applicable, interval endpoint inclusion and the meaning of an open end; why: boundary selection must be reproducible. Default: no inferred convention; the reference fixture explicitly uses integer ticks and half-open intervals.
4. **Correction policy** — obtain which source establishes each recorded interval and how correction/retraction versions replace earlier assertions; why: arrival order alone cannot resolve conflicting claims. Default: retain conflicting evidence and block an accepted view for that edge.
5. **Node scope** — obtain the node inventory and any node lifetime rules; why: an edge snapshot cannot prove endpoint existence from an ID alone. Default: require endpoints in the supplied inventory, disclose unverified lifetimes; use the reference only when inventory membership is fixed across the requested window.
6. **Coverage and destination** — identify retained-history limits, expected edge population and intended consumer; why: missing history can resemble absence. Default: offline view of supplied records with no complete-world or database claim.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the ledger and record the exact effective-time question and recorded-time cutoff in the output.
2. Declare both clock meanings and interval conventions before converting timestamps; retain original values and source references beside any approved normalized representation.
3. Validate revision uniqueness, endpoint identity, interval ordering and allowed assertion states; reject malformed records with their locators instead of silently repairing them.
4. Establish the revision sequence from source evidence. A corrected historical statement must retain its earlier recorded interval; do not backdate when the system learned the correction merely because its effective interval starts earlier.
5. Select revisions whose recorded interval contains the cutoff. Keep excluded revisions in the frozen ledger for explaining earlier answers.
6. Select from those revisions the ones whose effective interval contains the requested point; retain both selection predicates in the evidence table.
7. ⚠️ Group selected revisions by stable edge identity. If several compete, report a conflict and emit no accepted assertion for that edge; sorting by revision name or ingestion position is not a resolution policy.
8. Separate active assertions from explicit retractions. Preserve the selected retraction as evidence while excluding its relationship from the active edge view; distinguish this from no matching revision.
9. Check selected active endpoints against the node inventory and any supplied lifetime rules. Hold edges with unresolved endpoint eligibility rather than inventing nodes or silently dropping them.
10. Test the exact correction boundaries and rerun the same effective-time question at earlier and later recorded cutoffs. Explain changed edge membership with revision IDs, not just counts.
11. Deliver the active view, retraction/conflict evidence and coverage limits. Label a conflict-free result accepted only for the declared ledger scope and node policy; no match alone does not prove a relationship never existed.

The Python 3 reference uses fixed string node IDs and integer clock ticks. Every tuple contains revision ID, edge ID, source, target, effective start/end, recorded start/end and state. Ends are exclusive; None is an explicitly open upper end. Revisions carry source-record identity in their revision ID. Execute the entire snippet and record the installed interpreter version. It checks this in-memory contract, not timestamp conversion, history completeness, node lifetimes or storage behavior.

```python
def contains(start, end, point):
    return start <= point and (end is None or point < end)

def snapshot(nodes, rows, effective, recorded):
    if type(effective) is not int or type(recorded) is not int:
        raise ValueError("integer query clocks required")
    if any(not isinstance(n, str) or not n for n in nodes):
        raise ValueError("nonempty node IDs required")
    if len(nodes) != len(set(nodes)):
        raise ValueError("duplicate node ID")
    seen, candidates = set(), {}
    for row in rows:
        rev, edge, src, dst, vs, ve, rs, re, state = row
        if any(not isinstance(x, str) or not x
               for x in (rev, edge, src, dst)):
            raise ValueError("nonempty identities required")
        if rev in seen:
            raise ValueError("duplicate revision")
        seen.add(rev)
        if src not in nodes or dst not in nodes:
            raise ValueError("endpoint outside fixed inventory")
        if state not in ("active", "retracted"):
            raise ValueError("unknown assertion state")
        for start, end in ((vs, ve), (rs, re)):
            if (type(start) is not int or
                (end is not None and
                 (type(end) is not int or end <= start))):
                raise ValueError("invalid half-open interval")
        candidates.setdefault(edge, [])
        if contains(rs, re, recorded) and contains(vs, ve, effective):
            candidates[edge].append(row)
    active, evidence = [], {}
    for edge, matches in candidates.items():
        status = ("no-match" if not matches else "conflict"
                  if len(matches) > 1 else matches[0][-1])
        evidence[edge] = (status, [r[0] for r in matches])
        if status == "active":
            r = matches[0]
            active.append((edge, r[2], r[3], r[0]))
    return active, evidence

nodes = ["A", "B"]
rows = [("r1", "e", "A", "B", 1, 9, 2, 6, "active"),
        ("r2", "e", "A", "B", 1, 5, 6, None, "active"),
        ("r3", "e", "A", "B", 5, 9, 6, None, "retracted")]
assert snapshot(nodes, rows, 7, 4)[0] == [("e", "A", "B", "r1")]
assert snapshot(nodes, rows, 7, 6) == ([], {"e": ("retracted", ["r3"])})
assert snapshot(nodes, rows, 3, 6)[0][0][-1] == "r2"
assert snapshot(nodes, rows, 9, 6)[1]["e"] == ("no-match", [])
extra = ("r4", "e", "A", "B", 1, 9, 6, None, "active")
assert snapshot(nodes, rows + [extra], 7, 6)[1]["e"][0] == "conflict"
print("two-clock, correction-boundary, retraction and conflict checks passed")
```

## Decision rules
- IF a correction is recorded after the requested cutoff THEN exclude it from that historical view BECAUSE later knowledge was unavailable at the earlier cutoff.
- IF two revisions compete for the same edge at both query coordinates THEN report conflict BECAUSE revision order alone does not authorize a winner.
- IF the selected revision retracts an assertion THEN retain its evidence separately from active edges BECAUSE retraction and an unobserved relationship are different states.
- IF retained history does not cover the cutoff THEN qualify or block the answer BECAUSE current records cannot reconstruct missing historical knowledge.
- IF endpoint lifetimes are required but unavailable THEN hold the affected graph claim BECAUSE edge timing alone cannot establish node eligibility.

## Output template
```text
Query: <ledger snapshot, effective point, recorded cutoff; two lines>
Clock contract: <units, inclusion, open ends, node scope; maximum 80 words>
Active edges: <edge | source | target | selected revision; full table or attachment>
Evidence: <edge | active/retracted/no-match/conflict | selected revision IDs>
Boundary checks: <query pair | selected IDs | observed or pending; up to six rows>
Disposition: <accepted scoped view / blocked / incomplete; reason, maximum 80 words>
Limits: <history coverage, endpoint lifetime and destination checks; maximum 80 words>
```

## Quality checklist
- [ ] Both query clocks are named and separately supplied.
- [ ] Interval inclusion and open-end meaning are explicit.
- [ ] Revision IDs and source evidence remain traceable.
- [ ] Late corrections are excluded from earlier recorded cutoffs.
- [ ] Conflicting selected revisions receive no arbitrary winner.
- [ ] Retractions, active edges and no-match states remain distinct.
- [ ] Endpoint scope and history coverage are disclosed.
- [ ] Boundary tests report actual checks separately from pending execution.

## Anti-patterns
- **Latest-row shortcut**: use today's revision for every past query. Fix: evaluate the recorded interval first.
- **Clock conflation**: copy effective start into recorded start. Fix: preserve the evidenced availability time independently.
- **Retraction erasure**: delete all traces of a withdrawn assertion. Fix: retain its revision and applicable intervals.
- **Boundary overlap**: include both ends by habit. Fix: apply the supplied inclusion contract at equality.
- **Absence certainty**: treat a ledger gap as proof of no relationship. Fix: state the retained-history scope and no-match status.

## Worked example
**Input:** Fictional project Alder supplies the snippet ledger and fixed nodes A/B. r1 asserted e for effective ticks [1,9), known during recorded ticks [2,6). At recorded tick 6, r2 corrects active validity to [1,5), and r3 explicitly retracts [5,9). Ask about effective tick 7 as recorded at tick 6, comparing tick 4.

**Output:**
```text
Query: Alder supplied ledger; effective=7, recorded=6; comparison recorded=4.
Clock contract: Integer ticks; start included, end excluded; None is open upper end. Fixed node inventory A/B for this fixture.
Active edges: none.
Evidence: e | retracted | r3. Earlier comparison: e | active | r1.
Boundary checks: (7,4) selects r1; (7,6) selects r3; (3,6) selects r2; (9,6) has no match. Reference assertions verify these when executed.
Disposition: Accepted scoped view; e is not active at (7,6), and the earlier answer remains reconstructible.
Limits: Supplied fictional history only; fixed-node assumption. No database or timestamp conversion tested; no independent historical-truth claim.
```

**Bad output:** “e was never active at tick 7 because its latest active revision ends at 5.”
This retroactively applies a correction to an earlier knowledge state and loses r1's historical answer.

## Edge cases
- **No recorded history retained**: return the current assertion only if requested; mark the historical query unreconstructible rather than backfilling recorded intervals.
- **Unknown timezone or precision**: retain raw timestamps and request normalization rules before equality/boundary decisions.
- **Simultaneous conflicting sources**: preserve separate revision identities and show conflict; apply precedence only when supplied and evidenced.
- **Changing node lifetimes**: evaluate their own eligibility at the same query coordinates before accepting edges; the fixed-node snippet is insufficient.
- **Open end versus missing end**: accept None only under an explicit open-end convention; an unknown end remains a data-quality question.

## Test case
**Input:**
> Fictional edge k has revision a: effective [0,10), recorded [1,8), active. Correction b: effective [0,4), recorded [8,open), active; c: effective [4,10), recorded [8,open), retracted. Nodes are fixed and history complete for this fixture. Compare effective=6 at recorded=7 and recorded=8.

**Assertions:**
1. The earlier view includes k with revision a.
2. At recorded=8 the view excludes k and retains retraction c as evidence.
3. It excludes a at its recorded upper boundary and does not select b outside its effective interval.
4. It distinguishes the two clock meanings and makes no live-database claim.
