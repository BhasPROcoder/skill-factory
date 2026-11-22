Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-046
name: typed-graph-property-interchange
domain: Graph Engineering Foundations
subdomain: Typed property interchange
version: 1.0
description: Design and verify a neutral tagged graph export that preserves absent, null, Boolean, integer, decimal-text and string property meanings across a roundtrip.
triggers: ["preserve graph property types across export", "distinguish missing and null graph fields", "roundtrip graph properties", "avoid decimal precision loss in graph interchange", "tag graph property values", "verify parallel-edge properties after import"]
not_for: ["edge-list intake reconciliation [GRF-003]", "relational graph schema implementation [GRF-014]", "identity migration and cutover [GRF-017]", "choosing a vendor interchange format", "inferring missing property meanings"]
requires: []
risk_level: medium
---

# Typed Graph Property Interchange

## Purpose
Preserve graph identities and scalar property meanings through a neutral export. Distinguish absent, null, Boolean, integer, decimal text and string values. Report exact roundtrip mismatches; test external adapters separately.

## Inputs to collect
1. **Source snapshot** — identified nodes, directed edges and property maps. Why: identity and presence must survive. Default: none, required.
2. **Type contract** — permitted scalar kinds and field meanings. Why: numeric-looking strings must stay strings. Default: the five listed kinds; extend explicitly.
3. **Decimal policy** — accepted decimal text and scale meaning. Why: floating conversion may lose precision. Default: preserve validated text exactly.
4. **Missing/null rule** — representation of absence and null. Why: meanings differ. Default: omitted key versus present null tag.
5. **Edge identity** — endpoints, parallel edges and loops. Why: property parity cannot prove graph parity. Default: retain direction and IDs.
6. **Target adapter** — actual importer/exporter. Why: offline success cannot prove target behavior. Default: neutral artifact only.

If a required input is missing without a safe default, ask in one message with at most three questions. Freeze the snapshot before encoding.

## Procedure
1. Record source version, field meanings, decimal policy and inventories.
2. Validate unique nonempty IDs, endpoints and property keys; reject malformed records.
3. Encode each present property with a tagged object. Omit an absent key; encode explicit null as a null tag with no value field.
4. Encode Boolean before integer so language-specific Boolean subtyping cannot silently turn `true` into numeric one.
5. Encode integers as signed decimal text rather than a transport number; parse them only with exact integer conversion on decode. Keep decimal text under its own tag and validate its declared grammar without floating conversion.
6. Encode ordinary strings under a string tag even when their content looks like `1`, `true`, `null` or a decimal.
7. Serialize and parse the artifact; an in-memory copy is not a wire roundtrip.
8. Decode with exact tag and field-shape checks. Reject unknown tags, missing value fields for value-bearing kinds, extra fields, malformed numeric text and duplicate graph identities.
9. Compare identities, direction, parallels, loops, key presence and typed values record by record.
10. ⚠️ If the real target has different null, numeric or Boolean behavior, write an adapter transformation with an inverse and test its actual exported values. Keep unsupported kinds as explicit exceptions rather than silently coercing them.
11. Deliver the contract, roundtrip ledger, mismatches and untested adapter boundary.

This Python 3 reference uses standard JSON and an explicit `DecimalText` wrapper. Its decimal grammar accepts an optional minus sign, integer digits without leading zero except zero itself, and an optional fractional part; it preserves the accepted text exactly. It supports finite in-memory node/edge lists and scalar properties only. Run the whole snippet on the available interpreter and record its version.

```python
import json
import re
from dataclasses import dataclass

@dataclass(frozen=True)
class DecimalText:
    text: str

INTEGER = re.compile(r"-?(0|[1-9][0-9]*)\Z")
DECIMAL = re.compile(r"-?(0|[1-9][0-9]*)(\.[0-9]+)?\Z")

def encode_value(value):
    if value is None:
        return {"t": "null"}
    if type(value) is bool:
        return {"t": "bool", "v": value}
    if type(value) is int:
        return {"t": "int", "v": str(value)}
    if type(value) is DecimalText:
        if not DECIMAL.fullmatch(value.text):
            raise ValueError("invalid decimal text")
        return {"t": "decimal", "v": value.text}
    if type(value) is str:
        return {"t": "string", "v": value}
    raise ValueError("unsupported property kind")

def decode_value(tagged):
    if type(tagged) is not dict or "t" not in tagged:
        raise ValueError("missing type tag")
    kind = tagged["t"]
    if kind == "null":
        if set(tagged) != {"t"}:
            raise ValueError("invalid null fields")
        return None
    if set(tagged) != {"t", "v"}:
        raise ValueError("invalid tag fields")
    value = tagged["v"]
    if kind == "bool" and type(value) is bool:
        return value
    if kind == "int" and type(value) is str and INTEGER.fullmatch(value):
        return int(value)
    if kind == "decimal" and type(value) is str and DECIMAL.fullmatch(value):
        return DecimalText(value)
    if kind == "string" and type(value) is str:
        return value
    raise ValueError("unknown tag or invalid tagged value")

def check_graph(nodes, edges):
    if any(type(n) not in (tuple, list) or len(n) != 2 for n in nodes):
        raise ValueError("invalid node record")
    if any(type(e) not in (tuple, list) or len(e) != 4 for e in edges):
        raise ValueError("invalid edge record")
    ids = [n for n, _ in nodes]
    eids = [e for e, _, _, _ in edges]
    if any(type(x) is not str or not x for x in ids + eids):
        raise ValueError("invalid identity")
    if len(set(ids)) != len(ids) or len(set(eids)) != len(eids):
        raise ValueError("duplicate identity")
    if any(a not in ids or b not in ids for _, a, b, _ in edges):
        raise ValueError("unknown endpoint")
    for props in [p for _, p in nodes] + [p for _, _, _, p in edges]:
        if type(props) is not dict or any(type(k) is not str or not k for k in props):
            raise ValueError("invalid property map")

def export_graph(nodes, edges):
    check_graph(nodes, edges)
    encode = lambda p: {k: encode_value(v) for k, v in sorted(p.items())}
    payload = {"nodes": [[n, encode(p)] for n, p in nodes],
               "edges": [[e, a, b, encode(p)] for e, a, b, p in edges]}
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))

def import_graph(wire):
    def unique_object(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out
    payload = json.loads(wire, object_pairs_hook=unique_object)
    if type(payload) is not dict or set(payload) != {"nodes", "edges"}:
        raise ValueError("invalid graph fields")
    if type(payload["nodes"]) is not list or type(payload["edges"]) is not list:
        raise ValueError("invalid graph arrays")
    def unpack(p):
        if type(p) is not dict or any(type(k) is not str or not k for k in p):
            raise ValueError("invalid tagged property map")
        return {k: decode_value(v) for k, v in p.items()}
    nodes = [(n, unpack(p)) for n, p in payload["nodes"]]
    edges = [(e, a, b, unpack(p)) for e, a, b, p in payload["edges"]]
    check_graph(nodes, edges)
    return nodes, edges

nodes = [("A", {"absent_neighbor": "1", "null": None,
                "flag": True, "count": 1, "rate": DecimalText("1.2300")}),
         ("B", {})]
edges = [("e1", "A", "B", {"text": "true"}),
         ("e2", "A", "B", {"text": "null"}),
         ("loop", "B", "B", {})]
wire = export_graph(nodes, edges)
assert import_graph(wire) == (nodes, edges)
assert "missing" not in import_graph(wire)[0][0][1]
assert type(import_graph(wire)[0][0][1]["flag"]) is bool
assert import_graph(wire)[0][0][1]["rate"].text == "1.2300"
print("typed properties, absent key, parallel edges and loop roundtrip checked")
```

## Decision rules
- IF a key is absent THEN keep it absent BECAUSE absence is distinct from a present null tag.
- IF a Boolean appears THEN encode it as Boolean before integer BECAUSE otherwise it can be mistaken for one or zero in some language runtimes.
- IF decimal scale or spelling matters THEN preserve validated text under its own tag BECAUSE floating conversion can change the representation.
- IF an unknown tag or malformed field shape appears THEN reject decode BECAUSE guessing a type would break roundtrip fidelity.
- IF node or edge identities or endpoint direction change THEN reject the interchange BECAUSE property equality alone is insufficient.
- IF an external adapter has not been exercised THEN describe only offline neutral-artifact behavior BECAUSE target behavior remains unverified.

## Output template
```text
Scope: <snapshot, node/edge identities, direction and supported kinds; max 3 lines>
Contract: <absent/null rule, scalar tags, integer and decimal-text policy>
Roundtrip: <serialized and parsed; record counts and identity comparison>
Type checks: <key presence and each tag/value comparison; pass or mismatches>
Graph checks: <node IDs, edge IDs, endpoints, parallel edges and loops>
Decision: <neutral roundtrip passed | rejected | unresolved>
Limits: <unsupported kinds and untested external adapter; max 2 lines>
Next action: <one concrete step>
```

## Quality checklist
- [ ] Source snapshot and supported scalar kinds are declared.
- [ ] Missing property keys remain omitted and null keys remain present.
- [ ] Boolean and integer tags are distinct after parsing.
- [ ] Integer text passes exact grammar before conversion.
- [ ] Decimal text retains its exact accepted spelling and scale.
- [ ] Numeric-looking ordinary strings stay strings.
- [ ] Unknown tags, extra fields and malformed values are rejected.
- [ ] Node and edge IDs, direction, parallel edges and loops roundtrip.
- [ ] External adapter claims are limited to actual adapter tests.

## Anti-patterns
- **Null padding**: adding null for every missing key. Fix: omit absent keys and preserve explicit null tags.
- **Boolean as one**: testing integer type before Boolean. Fix: tag Boolean first and check exact types.
- **Floating conversion**: converting decimal text to a binary float. Fix: validate and preserve the text representation.
- **String guessing**: turning `"1"` into an integer. Fix: use the source's declared type tag.
- **Count-only roundtrip**: equal totals conceal swapped IDs or endpoints. Fix: compare full records by identity.
- **Adapter assumption**: treating neutral JSON success as proof of a database importer. Fix: test a real adapter separately.

## Worked example
**Input:**
> Fictional Elm snapshot S1 has nodes A and B. A has null `note`, Boolean `flag=true`, integer `count=1`, decimal text `rate=1.2300`, and ordinary string `label="1"`; `missing` is absent. Edges e1 and e2 both go A→B with separate IDs. Export and import through the neutral tagged form.

**Output:**
```text
Scope: Fictional Elm S1; nodes A,B; directed e1,e2 A→B; null, Boolean, integer, decimal text and string.
Contract: Omitted missing key stays absent; note has null tag; flag bool; count int text; rate decimal text; label string.
Roundtrip: Serialized and parsed; 2 nodes and 2 edges compared by ID.
Type checks: missing absent; note=null; flag=true Boolean; count=1 integer; rate="1.2300" decimal text; label="1" string; pass.
Graph checks: A/B identities and both A→B edge IDs preserved; no loops in S1.
Decision: Neutral roundtrip passed.
Limits: External importer behavior untested; complex property types outside this contract.
Next action: Run the same tagged fixtures through the chosen target adapter before migration.
```

**Bad output:** "All present values became strings, so the export succeeded." This fails because Boolean, integer, decimal text and ordinary string were required to remain distinguishable.

## Edge cases
- **Absent versus null**: omit absent key, retain a present null-tagged key.
- **Huge integer**: keep exact integer digits in the wire form; do not pass through a floating numeric field.
- **Decimal precision**: preserve accepted text and scale, including trailing zeros.
- **Parallel edges and loop**: retain each edge ID and original directed endpoints independently.
- **Malformed tag or extra field**: reject rather than coercing to string or null.
- **Unsupported array/object property**: reject pending an explicit versioned extension.

## Test case
**Input:**
> Fictional Elm S1 has A and B; A has absent `missing`, explicit-null `note`, Boolean `flag=true`, integer `count=1`, decimal text `rate=1.2300`, and string `label="1"`. Edges e1 and e2 both run A→B. Show the neutral roundtrip and what happens to a bogus type tag.

**Assertions:**
1. The result preserves absence separately from explicit null.
2. It keeps Boolean, integer, decimal text and string types distinct, with rate text `1.2300` unchanged.
3. Both parallel directed edge IDs and endpoints remain intact.
4. An unknown tag is rejected and no external adapter success is claimed.
</skill>

<user_request>
Fictional Elm S1 has A and B; A has absent `missing`, explicit-null `note`, Boolean `flag=true`, integer `count=1`, decimal text `rate=1.2300`, and string `label="1"`. Edges e1 and e2 both run A→B. Show the neutral roundtrip and what happens to a bogus type tag.
</user_request>
