# Table Transformation Contracts (TBX)

Preserve observation identity through reversible cell reshaping, positional nested expansion and explicit numeric interval membership.

Macro-area: AI/ML & Data Science

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| TBX-003 | [numeric-interval-membership-assignment](numeric-interval-membership-assignment/SKILL.md) | Assign supplied numeric observations to explicit intervals when endpoint inclusion, gaps or overlapping ranges can make category membership ambiguous. | assign values to interval labels; check open and closed bin edges; find ambiguous numeric categories | validated |
| TBX-002 | [paired-list-positional-expansion](paired-list-positional-expansion/SKILL.md) | Expand paired list columns by their shared position when nested table values represent aligned observations rather than independent combinations. | expand paired list columns; explode lists without a Cartesian product; keep nested observations aligned | validated |
| TBX-001 | [reversible-wide-long-cell-mapping](reversible-wide-long-cell-mapping/SKILL.md) | Construct and reverse a wide-to-long table mapping when every original cell must retain its row identity and explicit column identity. | reshape without losing cells; make wide long conversion reversible; retain row identity during melting | validated |
