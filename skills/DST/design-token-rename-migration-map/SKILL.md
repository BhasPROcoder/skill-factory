---
id: DST-003
name: design-token-rename-migration-map
domain: Design System Maintenance
subdomain: Token migration
version: 1.0
description: Map a proposed design-token rename through aliases, generated outputs and consumer references when preserving a value alone may not preserve compatibility.
triggers: ["rename a design token safely", "map token rename consumers", "plan a semantic token migration", "find references affected by token renaming", "retire an old token name"]
not_for: ["alias cycle diagnosis [DST-001]", "general release-note wording [MPU-009]", "component retirement [DST-004]"]
requires: []
risk_level: medium
---

# Design token rename migration map

## Purpose
Produce an evidence-backed migration map from an existing token identifier to a proposed identifier. Distinguish a spelling change from a change in semantic role, and preserve consumer behavior through explicit compatibility decisions rather than broad text replacement.

## Inputs to collect
1. **Rename proposal:** Obtain the old and new fully qualified identifiers and the stated reason. Required; do not infer intended names from similar labels.
2. **Definition inventory:** Obtain token types, values, aliases, modes and precedence for the relevant revision. Required for claiming equivalence; otherwise leave equivalence unverified.
3. **Consumer evidence:** Collect source references, generated exports, documentation examples and external consumer declarations. Default: inventory coverage limited to supplied material.
4. **Compatibility policy:** Ask whether the project supports transitional aliases, warnings, removal windows or parallel identifiers. Default: no removal schedule or release severity assumed.
5. **Execution scope:** Identify whether edits, generation and consumer tests are authorized and available. Default: migration specification only.
6. **Acceptance owner:** Identify who can approve semantic equivalence and consumer migration completion. Default: owner decision pending; do not invent approval.

If a required input has no safe default, ask in one message with at most three questions.

## Procedure
1. Establish a baseline revision and list the exact old identifier in each active mode. Preserve namespaced identity so equally spelled tokens from another package are not swept into the migration.
2. Compare the old role with the proposed role. If the proposal changes meaning, scope the work as a behavior change as well as a rename; equal present values do not establish semantic equivalence.
3. Trace incoming aliases and direct consumer references separately. Record generated references with their source generator, so the plan changes the source of truth rather than only an output that will be overwritten.
4. Classify every occurrence as a definition, dependency, consumer use, explanatory example or unrelated text. ⚠️ A substring match is a candidate occurrence, not proof that it refers to the token.
5. Define the migration relationship: direct replacement, temporary old-to-new compatibility alias, or parallel definitions pending a decision. Use the supplied project policy and actual tool capabilities; never assume every system supports aliases.
6. Check for collisions at the destination identifier and for cycles introduced by compatibility aliases. Keep old-to-new direction explicit and do not preserve both opposing references.
7. Order changes so a consumer does not require a new name before that name exists in its installed dependency. Identify release or deployment coordination needs without inventing dates or version numbers.
8. Write a row for each affected consumer group with its required action, compatibility state and evidence needed for completion. A search returning no local matches is not evidence that external consumers migrated.
9. On an authorized copy, compare resolved type and value before and after for each supplied mode, then run actual consumer checks. ⚠️ Treat unchanged color output as only one check; source imports, generated names and documented examples can still be broken.
10. Propose removal of the old name only after the agreed gate is satisfied. Preserve a rollback mapping and unresolved consumer inventory so the owner can defer removal without losing the new naming work.

For changing implementation details use [VERIFY: token-reference syntax, export naming and compatibility-alias support in the installed tool's official documentation]. Record the environment used for actual verification.

This Python 3 fixture checks a fictional rename ledger's direct mapping and collision gate. It does not edit files or resolve real token formats. Run it with an available Python 3 interpreter and record that interpreter version.

```python
old = "space.panel"
new = "space.container"
definitions = {old: 12, "space.inline": 4}
assert new not in definitions
migrated = {new if k == old else k: v for k, v in definitions.items()}
assert migrated[new] == definitions[old]
assert old not in migrated
assert migrated["space.inline"] == 4
```

## Decision rules
- IF the destination already exists with a different role THEN hold the rename BECAUSE overwriting it would merge distinct contracts.
- IF old and new names have equal values but different meanings THEN require semantic review BECAUSE future mode changes can expose the difference.
- IF an export is generated THEN change the generator input and regenerate BECAUSE patching only the output leaves the next build inconsistent.
- IF external consumer coverage is unknown THEN keep removal readiness unresolved BECAUSE local search cannot certify remote adoption.
- IF the project lacks a compatibility mechanism THEN coordinate consumer and definition changes explicitly BECAUSE a temporary alias cannot be assumed.

## Output template
```text
Boundary: <baseline, old/new identifiers and semantic intent; up to three lines>
Migration map: <up to eight rows; attach remaining occurrences>
Occurrence | Role | Proposed action | Compatibility evidence | Status
Sequence: <up to six ordered stages>
Verification: <mode, type/value and consumer checks; up to six lines>
Removal gate: <supplied policy and missing evidence; up to three lines>
Rollback: <old/new mapping and recovery condition; up to three lines>
```

## Quality checklist
- [ ] Old and new identifiers are fully qualified and unambiguous.
- [ ] Semantic equivalence is established or explicitly unresolved.
- [ ] Definitions, aliases, generated outputs and consumer references are distinguished.
- [ ] Destination collisions and introduced cycles are checked.
- [ ] Compatibility behavior follows supplied policy and verified capabilities.
- [ ] Consumer ordering does not require unavailable identifiers.
- [ ] Actual verification is separated from proposed checks.
- [ ] Removal readiness accounts for unknown consumers.

## Anti-patterns
- **Replace everywhere:** a substring replacement edits unrelated names. Fix: classify each occurrence and match exact identity.
- **Value-only equivalence:** matching pixels are treated as compatibility proof. Fix: check reference paths, types, modes and consumer behavior separately.
- **Generated-file patch:** the export changes without generator inputs. Fix: identify the source of truth and verify regenerated output.
- **Invented sunset:** an arbitrary removal date is imposed. Fix: collect the project's approved compatibility and communication policy.
- **Local certainty:** no repository matches becomes universal migration completion. Fix: state which consumer inventories were actually inspected.

## Worked example
**Input:** Fictional team Slate wants to rename space.panel to space.container without changing its spacing role. Its supplied single-mode ledger uses value 12, and Card refers directly to space.panel. The project permits an old-to-new alias during transition. External consumers exist but their migration is unknown. No files or UI can be edited.

**Output:**
```text
Boundary: Slate's supplied single-mode ledger; space.panel becomes space.container, same stated spacing role.
Migration map:
Occurrence | Role | Proposed action | Compatibility evidence | Status
space.panel=12 | definition | introduce space.container=12 | project permits transitional alias | proposed
space.panel | old public identifier | retain alias to space.container temporarily | old-to-new direction; no opposing alias | proposed
Card reference | direct consumer | move to space.container after its dependency exposes that name | consumer check pending | proposed
External users | unknown references | obtain adoption evidence before removal | coverage incomplete | unresolved
Sequence: Introduce new name; retain old alias; update Card; regenerate outputs; check consumers; review removal gate.
Verification: Confirm equivalent resolved type and value in the supplied mode and test Card. No actual file, build or UI check performed.
Removal gate: External adoption and owner approval unresolved; no removal date invented.
Rollback: Preserve baseline mapping and revert affected consumers/definitions together if verified regression requires it.
```

**Bad output:** “Both names currently equal 12, so delete the old one immediately.”
This ignores references and the supplied transitional policy.

## Edge cases
- The old token is used only through aliases: migrate the dependency chain deliberately rather than expecting a direct consumer search to find all impact.
- The new spelling conflicts in one theme: keep that theme blocked even if other modes pass.
- A runtime constructs names dynamically: request construction rules and representative traces; literal search alone is incomplete.
- A consumer cannot upgrade yet: document its supported compatibility path or keep removal pending instead of marking it migrated.

## Test case
**Input:**
> Fictional token color.alert is being renamed color.warning, but color.warning already exists for a different meaning. Both currently resolve to amber. No owner decision is supplied.

**Assertions:**
1. Identifies the destination collision and semantic difference.
2. Does not overwrite the existing warning token merely because values match.
3. Requests the owner's mapping decision before defining a migration.
4. Does not claim any consumer was changed.
