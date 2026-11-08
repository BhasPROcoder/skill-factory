---
id: TBX-001
name: reversible-wide-long-cell-mapping
domain: Table Transformation Contracts
subdomain: Reshape provenance
version: 1.0
description: Construct and reverse a wide-to-long table mapping when every original cell must retain its row identity and explicit column identity.
triggers: ["reshape without losing cells", "make wide long conversion reversible", "retain row identity during melting", "reconstruct a wide table", "check duplicate pivot coordinates"]
not_for: ["aggregating duplicate observations", "join multiplication diagnosis [TDQ-008]", "inferring units from column names"]
requires: []
risk_level: medium
---

# Reversible Wide Long Cell Mapping

## Purpose
Transform a rectangular table into identified cell records and reconstruct the original arrangement without aggregation. Preserve row order, column order and explicit null values so a successful reshape means more than matching the number of nonempty values.

## Inputs to collect
1. **Source rectangle** — obtain the exact selected columns, rows and snapshot identity. This establishes the cells being transformed. Default: none; do not expand the selection silently.
2. **Row identities** — obtain unique stable row keys independent of possibly duplicated business labels. This prevents two distinct observations collapsing into one. Default: assign snapshot-local positional keys only when the requester accepts their limited lifetime.
3. **Column identities** — obtain distinct selected column identifiers and their order. This preserves columns with similar displayed headings. Default: no interpretation of suffixes, dates or units from spelling alone.
4. **Cell values** — establish how explicit null, empty text and absent columns differ. Default: retain supplied values exactly; absent cells violate this rectangular contract.
5. **Return contract** — specify whether original ordering and metadata must be reconstructed. Default: retain ordered row and column sidecars and compare exact cells; no type conversion or aggregation.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Combine snapshot and identity questions so the requester can supply one coherent rectangle.

## Procedure
1. Freeze the source selection and preserve an unmodified copy or stable artifact reference. A reshape cannot prove reversibility against a changing source.
2. Validate that row and column identifiers are individually unique. Distinguish duplicate business labels from duplicate technical row identities; retain the former as data when legitimate.
3. Verify that every selected row contains exactly the selected columns. ⚠️ Do not turn an absent column into null, because that would hide a schema discrepancy rather than preserve a supplied value.
4. Emit one long record per row-and-column coordinate, carrying both identities and the untouched value. Keep coordinates separate from interpreted variable metadata.
5. Preserve ordered row and column manifests alongside the cell records. Long-record order alone is not a reliable replacement for these manifests if later steps may sort or filter.
6. Reconstruct by accepting each coordinate exactly once. Reject duplicates even when their values agree; duplicate coordinates indicate a broken one-cell-per-coordinate contract.
7. Require the full expected coordinate set before returning the reconstructed table. ⚠️ A missing cell record is not an explicit null cell; fail the reconstruction instead of filling the gap automatically. For a complete defect report, tally all received coordinates separately: report repeated coordinates and the expected-minus-received coordinate set together, even if the fail-fast constructor raises at the first defect.
8. Compare reconstructed rows, values and order against the frozen input. Report the exact tested type and serialization scope; equality in memory does not prove that a later spreadsheet or file writer preserves types.

The Python 3 reference below operates on ordered row pairs and dictionaries with string column keys. Row identifiers are unique strings; values are opaque scalar fixture values, including None. It produces in-memory records and sidecars, not an exported spreadsheet. Save and run the entire snippet with the installed Python 3 interpreter and record the actual environment.

```python
def melt(rows, columns):
    ids = [key for key, _ in rows]
    if len(ids) != len(set(ids)) or len(columns) != len(set(columns)):
        raise ValueError("duplicate identity")
    if any(set(values) != set(columns) for _, values in rows):
        raise ValueError("nonrectangular source")
    cells = [(key, col, values[col])
             for key, values in rows for col in columns]
    return ids, list(columns), cells

def rebuild(ids, columns, cells):
    if len(ids) != len(set(ids)) or len(columns) != len(set(columns)):
        raise ValueError("duplicate identity")
    expected = {(key, col) for key in ids for col in columns}
    values = {}
    for key, col, value in cells:
        coordinate = (key, col)
        if coordinate not in expected or coordinate in values:
            raise ValueError("unexpected or duplicate coordinate")
        values[coordinate] = value
    if set(values) != expected:
        raise ValueError("missing coordinate")
    return [(key, {col: values[key, col] for col in columns}) for key in ids]

rows = [("rB", {"east": 4, "west": None}),
        ("rA", {"east": 0, "west": ""})]
ids, columns, cells = melt(rows, ["west", "east"])
assert len(cells) == 4
assert rebuild(ids, columns, list(reversed(cells))) == rows
assert list(rebuild(ids, columns, cells)[0][1]) == ["west", "east"]
for bad in (cells[:-1], cells + [cells[0]]):
    try:
        rebuild(ids, columns, bad)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid cell set accepted")
print("reshape coordinate checks passed")
```

## Decision rules
- IF business labels repeat THEN retain independent row identities BECAUSE repeated labels do not establish duplicate observations.
- IF a cell value is explicitly null THEN emit its coordinate with null BECAUSE omitting it would erase the distinction between null and absent data.
- IF reconstruction sees two records for one coordinate THEN reject the input BECAUSE choosing either or aggregating them changes this reversible contract.
- IF the requested transformation interprets column names as dates or units THEN obtain a separate explicit mapping BECAUSE coordinate preservation does not establish semantic parsing.

## Output template
```text
Boundary: <source snapshot, selected rectangle and value scope; three lines maximum>
Identity manifests: <ordered row keys and ordered column keys or artifact references>
Long records: <actual records; first twelve with full artifact when longer>
Reconstruction: <actual rows or failure with exact coordinates>
Checks: <up to six observed invariants and outcomes>
Limits: <two sentences on serialization, typing and semantic interpretation>
```

## Quality checklist
- [ ] Row and column identities are unique within the frozen selection.
- [ ] Every input row contains the selected columns exactly.
- [ ] Explicit null and empty text remain distinguishable.
- [ ] Ordered identity manifests accompany the long records.
- [ ] Duplicate coordinates fail rather than aggregate.
- [ ] Missing coordinates fail rather than become null.
- [ ] Reconstruction checks both values and required ordering.
- [ ] File-format or semantic claims match work actually performed.

## Anti-patterns
- **Null evaporation**: null cells disappear during the reshape. Fix: retain an explicit coordinate and value.
- **Label collapse**: repeated names become one row. Fix: identify source rows independently of business labels.
- **Helpful aggregation**: duplicate coordinates are summed to make a pivot succeed. Fix: reject or switch to a separately approved aggregation task.
- **Order by accident**: sorted long records redefine original order. Fix: use the preserved identity manifests.
- **Schema repair disguised as reshape**: missing keys become empty cells. Fix: report the source rectangle discrepancy before construction.

## Worked example
**Input:**
> Fictional table Cedar snapshot S has rows rB and rA in that order. rB contains east=4, west=null; rA contains east=0, west=empty text. Requested column order is west then east. Produce long cells and reconstruct without aggregation.

**Output:**
```text
Boundary: Cedar S, two rows and two selected columns; scalar values preserved in memory.
Identity manifests: rows=[rB,rA]; columns=[west,east].
Long records: [(rB,west,null),(rB,east,4),(rA,west,empty text),(rA,east,0)].
Reconstruction: rB={west:null,east:4}; rA={west:empty text,east:0}, retaining the stated row and column order.
Checks: Four coordinates for two rows by two columns; null, empty text and zero remain distinct; reversing cell-record order does not change reconstruction; missing or repeated coordinates rejected by reference assertions.
Limits: In-memory reconstruction only. No exported file or interpretation of east/west as measurement metadata was tested.
```

**Bad output:** “Drop the null row, group by displayed label and sum duplicated cells.”
This changes the observation set and adds aggregation rather than reversing a cell mapping.

## Edge cases
- **Empty rectangle**: retain both identity manifests even if there are no cells, so zero selected columns can still reconstruct the known empty rows.
- **Duplicate displayed headings**: assign distinct technical column keys with a supplied display-label sidecar before reshaping; do not merge them.
- **Filtered long records**: label the result partial and do not claim round-trip reconstruction until omitted coordinates are restored.
- **Mutable nested values**: use a documented independent-copy or serialization contract before extending this scalar reference; shared objects are outside its guarantee.

## Test case
**Input:**
> Fictional source has unique rows A and B, each with selected columns p and q. Its long export contains A/p twice with equal values, A/q and B/p once, and no B/q. Total record count is four. Reconstruct it.

**Assertions:**
1. Rejects duplicate A/p instead of treating equal values as permission to collapse it.
2. Identifies that B/q is missing rather than converting it to null.
3. Does not accept total count alone as a coordinate completeness check.
4. Preserves the original records as evidence while requesting a corrected export.
