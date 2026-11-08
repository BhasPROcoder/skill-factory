---
id: TBX-002
name: paired-list-positional-expansion
domain: Table Transformation Contracts
subdomain: Nested row expansion
version: 1.0
description: Expand paired list columns by their shared position when nested table values represent aligned observations rather than independent combinations.
triggers: ["expand paired list columns", "explode lists without a Cartesian product", "keep nested observations aligned", "reject unequal paired arrays", "trace expanded rows to list positions"]
not_for: ["join multiplication diagnosis [TDQ-008]", "matching unordered arrays by inferred meaning", "expanding independent combinations"]
requires: []
risk_level: medium
---

# Paired List Positional Expansion

## Purpose
Produce child rows from explicitly aligned lists while preserving parent identity and original list position. Keep empty lists, missing lists and mismatched lengths visible instead of generating false combinations or silently dropping unmatched values.

## Inputs to collect
1. **Parent rows** — obtain the selected source snapshot and unique parent identifiers. They establish provenance for every child. Default: none; a display name alone is insufficient if it repeats.
2. **Paired columns** — identify which list columns share a positional contract and why. This determines whether position connects their values. Default: do not assume alignment merely because lengths match.
3. **Element semantics** — establish whether an element can be null and whether null means an unknown value at a real position. Default: preserve explicit elements without filtering.
4. **Empty-parent policy** — obtain how parents with empty lists must appear in the result. Default: emit no invented child, but retain the parent in a separate empty-parent ledger.
5. **Scalar fields** — identify parent attributes to retain separately or repeat deliberately. Default: preserve parent records unchanged and reference them by key; avoid multiplying amounts accidentally.
6. **Output destination** — identify a child table schema and any ordering requirement. Default: in-memory tuples ordered by parent input order and then list position; no external table mutation.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Ask for the positional meaning before producing output rows.

## Procedure
1. Freeze the parent snapshot and confirm unique parent identities. Preserve original arrays so the output can be traced without depending on displayed text.
2. Record the supplied evidence that list position denotes the same observation across paired columns. If values are keyed independently, route to an explicit key-matching procedure rather than sorting them into guessed alignment.
3. Validate the type and presence of every paired list. ⚠️ A missing list is not an empty list, and a scalar is not a one-element list unless an explicit conversion rule authorizes that interpretation.
4. Compare list lengths within each parent. Reject a mismatched parent before returning the batch under this all-or-nothing reference contract; do not use a truncating pair operation or pad missing elements silently.
5. Emit one child for each valid position, carrying parent identity, zero-based position and all paired element values. Preserve an explicit null element as a real position.
6. Record parents whose lists are all empty in the empty-parent ledger. This retains parent coverage without inventing a child that never existed.
7. Reconcile child count against the sum of validated list lengths. Check that positions within each parent are complete and unique, not merely that the grand total agrees.
8. Reconstruct selected list columns from the children and empty ledger as a verification step. Preserve parent-level fields separately; their repeated appearance in child output does not make them additive child measures.

The Python 3 reference below models two paired columns named names and values. Parent identifiers are unique strings; both columns must be lists and elements are treated as opaque fixture values. The procedure establishes alignment meaning outside the function. Run the complete snippet with the installed Python 3 interpreter and record the environment; it does not decode serialized list strings or infer array relationships.

```python
def expand(rows):
    seen, children, empty = set(), [], []
    for row in rows:
        key = row["id"]
        if key in seen:
            raise ValueError("duplicate parent identity")
        seen.add(key)
        names, values = row["names"], row["values"]
        if not isinstance(names, list) or not isinstance(values, list):
            raise ValueError("paired columns must be lists")
        if len(names) != len(values):
            raise ValueError("unequal paired lengths")
        if not names:
            empty.append(key)
        for position in range(len(names)):
            children.append((key, position, names[position], values[position]))
    return children, empty

rows = [{"id": "A", "names": ["red", "blue"], "values": [4, None]},
        {"id": "B", "names": [], "values": []}]
children, empty = expand(rows)
assert children == [("A", 0, "red", 4), ("A", 1, "blue", None)]
assert empty == ["B"] and len(children) == 2
assert [c[2] for c in children if c[0] == "A"] == rows[0]["names"]
assert [c[3] for c in children if c[0] == "A"] == rows[0]["values"]
try:
    expand([{"id": "C", "names": ["x", "y"], "values": [9]}])
except ValueError:
    pass
else:
    raise AssertionError("truncated pair accepted")
print("paired expansion checks passed")
```

## Decision rules
- IF paired lengths disagree THEN reject the parent and request corrected alignment evidence BECAUSE truncation hides an unmatched observation.
- IF both lists are empty THEN retain the parent in the empty ledger BECAUSE absence of children does not imply absence of the parent.
- IF a list contains an explicit null element THEN retain that position BECAUSE filtering it would shift later pair relationships.
- IF the lists represent independent choices THEN do not apply positional expansion BECAUSE a different combination contract is required.
- IF a parent measure is repeated on children THEN label it nonadditive across those rows BECAUSE repeated context is not newly observed quantity.

## Output template
```text
Pairing contract: <source snapshot, parent key and evidence for positional alignment; three lines>
Children: <parent, position, paired values; first twelve rows plus full artifact if longer>
Empty parents: <actual identities or None>
Rejected parents: <identity, exact discrepancy and correction needed; up to six rows>
Reconciliation: <expected versus actual child count and positional checks; four lines>
Limits: <two sentences on scalar context, missing inputs and external writes>
```

## Quality checklist
- [ ] Parent identities are unique before expansion.
- [ ] The positional relationship is supplied rather than inferred from equal lengths.
- [ ] Missing, null and empty list states are distinguished.
- [ ] Unequal lengths fail without truncation or invented padding.
- [ ] Each child retains its original parent and position.
- [ ] Explicit null elements retain their positions.
- [ ] Empty parents remain represented outside the child table.
- [ ] Repeated parent attributes are not counted as additive child measures.

## Anti-patterns
- **Cartesian surprise**: every name is combined with every value. Fix: use one child per shared position when the supplied contract is positional.
- **Truncating pair**: excess elements disappear during pairing. Fix: compare lengths before producing accepted output.
- **Null shift**: null elements are removed before expansion. Fix: retain their coordinates and meanings.
- **Empty-parent loss**: a parent vanishes when it has no children. Fix: preserve an explicit empty-parent ledger.
- **Scalar duplication inflation**: a parent total is summed once per child. Fix: retain the parent grain or mark repeated context as nonadditive.

## Worked example
**Input:**
> Fictional survey snapshot Grove declares positional pairs. Parent A has names [red,blue] and values [4,null]. Parent B has two empty lists. Retain empty parents separately and preserve null elements. No parent amounts are present.

**Output:**
```text
Pairing contract: Grove, unique parent id; supplied names and values share positions.
Children: (A,0,red,4); (A,1,blue,null).
Empty parents: B.
Rejected parents: None.
Reconciliation: Expected 2+0=2 children; actual 2. A positions 0 and 1 are complete, and both selected lists reconstruct exactly; B remains explicitly empty.
Limits: In-memory expansion only, with no scalar amount duplication. No external table was written and no relationship was inferred from the value spelling.
```

**Bad output:** “Produce red/4, red/null, blue/4 and blue/null, then remove B.”
This invents independent combinations and loses the empty parent's existence.

## Edge cases
- **Repeated elements**: retain separate positions even if the values agree; equality is not permission to deduplicate observations.
- **Serialized list text**: request the applicable parser and schema before expansion; commas inside text do not establish element boundaries.
- **Several paired lists**: validate all lengths against one shared position contract before extending the reference schema.
- **Parent order changes later**: use stable parent identities and explicit positions for reconstruction instead of the sorted output's row order.

## Test case
**Input:**
> Fictional parent Q has names [oak,elm,ash] and values [2,5]. The requester suggests pairing only the shorter length. Parent R has names [] and values [], while S has no values field.

**Assertions:**
1. Rejects Q's mismatch rather than losing ash.
2. Distinguishes R's empty lists from S's missing field.
3. Preserves Q's original lists as correction evidence.
4. Does not return a supposedly complete accepted child table for the invalid batch.
