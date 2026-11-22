# GRF-046 independent review

Reviewer g33_reviewer. Read SPEC, complete draft and author evidence, and actual procedures of GRF-003, GRF-014 and GRF-017. G03 reconciles source edge-list identities, G14 enforces relational schema constraints, and G17 maps identities across a migration. G46 defines an explicit neutral tagged scalar grammar and verifies exact type/presence preservation after JSON serialization and parsing. This is a scoped distinction, not a whole-library uniqueness proof. Registry untouched.

## Execution evidence

Executed the embedded Python under Python 3.14.6; it printed `typed properties, absent key, parallel edges and loop roundtrip checked`. Independent fixture encoded and parsed two nodes, two parallel A→B edges and a B→B loop. A property map contained absent `missing`, present null, Boolean true, integer one, decimal text `1.2300`, ordinary string `"1"`, and a 61-digit integer. The parsed graph equaled the original, Boolean and integer retained distinct exact types, the decimal text retained trailing zeros, the huge integer appeared as decimal digits inside a tagged JSON string, and all three edge IDs/endpoints survived.

Additional rejection checks:

```text
unknown tag: REJECT unknown tag or invalid tagged value
missing value on integer tag: REJECT invalid tag fields
extra value on null tag: REJECT invalid null fields
malformed integer text 01: REJECT unknown tag or invalid tagged value
malformed decimal exponent 1e3: REJECT unknown tag or invalid tagged value
duplicate JSON property key: REJECT duplicate JSON key
duplicate edge identity: REJECT duplicate identity
unknown tampered endpoint: REJECT unknown endpoint
unsupported array property: REJECT unsupported property kind
valid but direction-tampered A→B to B→A wire: importer accepts valid graph, but full imported-versus-source record comparison rejects equality despite equal edge counts
```

The final tampering case confirms why Procedure step 9 compares complete source and imported records: an importer alone can validate a changed but well-formed graph. The contract's decimal grammar is expressly internal to this skill; no external interchange standard or adapter compatibility is claimed. Actual target adapters require separate tests.

## Ordinary scenario

```text
Scope: Fictional Elm S1; nodes A,B and directed e1,e2 A→B; supported null, Boolean, integer, decimal text and string.
Contract: Missing key omitted; note null tagged; flag Boolean; count integer text; rate decimal text; label string.
Roundtrip: Serialized and parsed; 2 nodes and 2 identified edges compared.
Type checks: missing absent; note=null; flag=true Boolean; count=1 integer; rate="1.2300" decimal text; label="1" string; pass.
Graph checks: A/B identities and both directed parallel IDs preserved; no loops in S1.
Decision: Neutral roundtrip passed.
Limits: External importer untested; complex property kinds unsupported.
Next action: Run these tagged fixtures through the chosen adapter before migration.
```

## Missing-input scenario

```text
Scope: Export request supplies counts but no full identified graph or property type contract.
Contract: Unresolved; absence, null and decimal meanings unavailable.
Roundtrip: Not executed.
Type checks: Pending source property map and declared kinds.
Graph checks: Pending node/edge IDs and directed endpoints.
Decision: Unresolved.
Limits: Counts cannot establish identity or typed-value preservation.
Next action: Request source snapshot, field meanings and intended target adapter together.
```

## Edge/Test scenario

```text
Scope: Fictional A/B; e1,e2 A→B plus loop B→B; A has true, integer 1, text "1", decimal text "1.2300", present null and absent missing.
Contract: Explicit bool/int/string/decimal/null tags; missing omitted.
Roundtrip: Serialized and parsed; 2 nodes and 3 edge records compared by ID.
Type checks: True remains Boolean, 1 integer, "1" string, 1.2300 exact decimal text, null present, missing absent.
Graph checks: e1/e2 remain separate directed A→B records; loop remains B→B.
Decision: Neutral roundtrip passed.
Limits: Unknown tags and duplicate JSON keys reject; external adapter untested.
Next action: Probe the actual target adapter with the same values and identities.
```

## Verdict

Recommend acceptance for the skill's declared neutral tagged format. The worked example and Test case assertions are consistent with executed checks. No unstable external-format/API claim, invented source or current value appears. Source completeness and adapter behavior remain explicit boundaries.
