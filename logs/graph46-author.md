# GRF-046 author evidence

Read AGENTS.md and SPEC, queried sf.py for typed property and null/missing, and inspected actual GRF-003, GRF-014 and GRF-017 procedures. GRF-003 reconciles identities during import and says to roundtrip representative properties, without defining a scalar encoding. GRF-014 implements a database schema with property type checks. GRF-017 copies caller-validated property dictionaries through an identity migration. GRF-046 specifically defines a neutral tag grammar and tests absence versus null, exact integer text, decimal text and Boolean/string distinctions through JSON parsing. This is a scoped distinction, not whole-library uniqueness proof. No registry mutation or push.

Draft: `skills/GRF/typed-graph-property-interchange/SKILL.md`; manifest `staging/graph_g46.json`. Final `sf.validate_text(text, path)` returned zero errors/warnings. Complete embedded Python 3 snippet executed and printed `typed properties, absent key, parallel edges and loop roundtrip checked`. Additional direct encode/decode calls returned equal values for Boolean `True`, integer `1`, string `"1"`, null, and `DecimalText("1.2300")`, retaining their distinct types. External import tests:

```text
unknown tag: REJECT unknown tag or invalid tagged value
duplicate JSON property key: REJECT duplicate JSON key
malformed integer text 01: REJECT unknown tag or invalid tagged value
malformed decimal text 1e3: REJECT unknown tag or invalid tagged value
```

Ordinary scenario:
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

Missing-input scenario:
```text
Scope: A graph export request supplies edge counts but no property type contract or complete identified inventory.
Contract: Unresolved; absent/null and decimal meaning not supplied.
Roundtrip: Not executed.
Type checks: Pending source property map and declared types.
Graph checks: Pending node/edge IDs and directed endpoints.
Decision: Unresolved.
Limits: Counts do not establish identity or value preservation.
Next action: Request the source snapshot, property meanings and target adapter together.
```

Edge scenario:
```text
Scope: Fictional A/B; e1 and e2 both A→B, loop B→B, A has flag=true, count=1, text="1", rate decimal text "1.2300", null key present and missing key absent.
Contract: Tagged Boolean, integer text, string, decimal text and null; absent omitted.
Roundtrip: Serialized and parsed; 2 nodes and 3 edges compared by ID.
Type checks: True remains Boolean; 1 remains integer; "1" remains string; 1.2300 retains decimal text; null present, missing absent.
Graph checks: e1/e2 remain separate A→B IDs; loop remains B→B.
Decision: Neutral roundtrip passed.
Limits: Unknown tags and duplicate JSON property keys reject; external adapter untested.
Next action: Probe the target adapter with the same distinct values before cutover.
```

Claim audit: examples are fictional and counts agree with their listed records. The only specific grammar is defined by the skill itself, rather than asserted as an external standard. No current platform rule, price, version, source or study is claimed. External adapters are explicitly unverified. Independent review required before acceptance.
