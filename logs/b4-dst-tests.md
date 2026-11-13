# Independent design-system text executions

Reviewer: coordinator, not the author of DST. Fresh fictional requests below are executed as text tasks. Actual responses follow the skill templates. No live UI, deployment, cross-model equivalence or external consumer verification is claimed.

## DST-001 case 1

Request: Fictional Dawn graph a->b, b->c, c->b; owner says c should point to literal d=blue. Only a is a known consumer.

```text
Context: Dawn graph, single supplied mode; revision unspecified.
Trace: a -> b -> c -> b; b repeats.
Affected set: Loop b/c; upstream a; other consumers unknown.
Repair proposal: On a copy, set c -> d following supplied owner intent.
Checks: Proposed a -> b -> c -> d reaches blue; consumer/render checks pending.
Disposition: Proposal, not a changed export.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-001 case 2

Request: Fictional team supplies only a screenshot and asks which alias cycles.

```text
Context: Screenshot only; mode and definitions absent.
Trace: Cannot derive edges from appearance.
Affected set: Unknown.
Repair proposal: Obtain definitions, active mode/precedence and failing consumer.
Checks: No graph check possible; no repair performed.
Disposition: Blocked on source evidence.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-001 case 3

Request: Fictional Day has a->base with base literal; Night has a->a. Diagnose both.

```text
Context: Separate supplied Day and Night graphs.
Trace: Day a -> base terminates; Night a -> a repeats.
Affected set: Night loop a; consumers not supplied.
Repair proposal: Ask token owner for intended Night target; preserve Day.
Checks: Graph reasoning only; verify actual overrides and visual result after any edit.
Disposition: Night blocked; no universal cycle or arbitrary replacement claimed.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-002 case 1

Request: Fictional Panel has small/large size and closed/open phase; contract supports all except small/open; no runtime supplied.

```text
Component: Fictional Panel static contract.
Space: Two sizes × two phases = four explicit combinations; defaults unknown.
Matrix:
Combination | Support status | Expected behavior | Evidence or question
small,closed | supported | closed content | supplied contract; interaction unknown
large,closed | supported | closed content | supplied contract; interaction unknown
large,open | supported | open content | supplied contract; interaction unknown
small,open | prohibited | rejection or normalization undecided | owner decision
Coverage: Four static cases plus transitions proposed; no executions.
Owner decisions: Define defaults, interaction and prohibited-request behavior.
Verification: Text matrix only; rendering and input behavior untested.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-002 case 2

Request: Fictional component is described only as flexible. Produce complete coverage.

```text
Component: Unspecified flexible component.
Space: Properties and allowed values unknown; no finite count justified.
Matrix:
Combination | Support status | Expected behavior | Evidence or question
unknown | unresolved | unknown | require property and behavior contract
Coverage: No exhaustive claim; collect actual revision and independently settable dimensions.
Owner decisions: Supply properties/defaults, constraints and behavior examples.
Verification: No component tested.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-002 case 3

Request: Fictional button gallery shows active+disabled but owner contract prohibits it.

```text
Component: Button, conflicting supplied sources.
Space: Complete domains absent; total count unresolved.
Matrix:
Combination | Support status | Expected behavior | Evidence or question
active,disabled | disputed | unknown intended rejection/normalization | gallery contradicts rule
Coverage: Test this conflict and transition after owner resolves contract; other rows unknown.
Owner decisions: Which revision and policy apply? What should activation do?
Verification: Conflict documented; screenshot is not proof of supported interaction.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-003 case 1

Request: Fictional pad.old=8 is renamed pad.new with same role; owner permits old->new alias; Widget direct reference known, external users unknown.

```text
Boundary: Fictional same-role rename; one supplied mode.
Migration map:
Occurrence | Role | Proposed action | Compatibility evidence | Status
pad.old=8 | definition | introduce pad.new=8, retain old->new | owner permits alias | proposed
Widget | consumer | update after new name available | build/interaction pending | proposed
external | consumers | obtain adoption evidence | inventory missing | unresolved
Sequence: Introduce new; retain alias; migrate Widget; check generated output; verify; review removal.
Verification: Compare type/value and Widget; no build run.
Removal gate: Unknown external adoption blocks removal; policy required.
Rollback: Preserve baseline and revert dependency/consumer changes together if verified regression occurs.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-003 case 2

Request: Fictional request says rename main to primary without namespace, roles or references.

```text
Boundary: Ambiguous old/new identifiers; source revision absent.
Migration map:
Occurrence | Role | Proposed action | Compatibility evidence | Status
main/primary | unknown | obtain qualified identities and roles | absent | blocked
Sequence: Confirm identities; inspect occurrences; decide compatibility; then plan edits.
Verification: No source or consumer checks possible.
Removal gate: Cannot remove unknown public identifier; require policy and inventory.
Rollback: Retain original definitions; no changes made.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-003 case 3

Request: Fictional old token=12 in both modes; new identifier already exists with value6 in Night. Both roles unspecified.

```text
Boundary: Proposed rename has Night collision; semantic intent unknown.
Migration map:
Occurrence | Role | Proposed action | Compatibility evidence | Status
new in Night | existing definition=6 | preserve pending owner decision | collides with old=12 | blocked
old | existing definition | retain while scope clarified | equal-role evidence absent | unchanged
Sequence: Establish roles; resolve collision; inspect consumers; plan context-specific migration.
Verification: Different Night values prevent an equivalence claim; actual files untested.
Removal gate: Collision, inventory and policy unresolved.
Rollback: Preserve both baseline identifiers; no overwrite performed.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-004 case 1

Request: Fictional OldChoice supports multiple selections, replacement only single. Consumer Filters needs multiple.

```text
Retirement boundary: Proposed replacement; revisions and approval unspecified.
Consumer handoff:
Consumer | Required behavior | Successor evidence | Migration action | Acceptance status
Filters | multiple selections | replacement single-only | retain old pending supported alternative | blocked
Sequence: Confirm versions; inventory consumers; resolve parity gap; test migration; review removal.
Blockers: Owner must resolve multiple-selection gap and retirement policy.
Removal gate: Not met; code replacement alone fails required behavior.
Recovery: Preserve old consumer implementation and behavior baseline.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-004 case 2

Request: Fictional team asks to retire a component but supplies neither successor nor consumer list.

```text
Retirement boundary: Unspecified component and unapproved retirement proposal.
Consumer handoff:
Consumer | Required behavior | Successor evidence | Migration action | Acceptance status
unknown | unknown | no successor | obtain inventory and requirements | blocked
Sequence: Identify component; discover consumers; assess replacement; plan tests; obtain decision.
Blockers: Identity/revisions, inventory, successor and owner policy missing.
Removal gate: No evidence supports removal.
Recovery: Preserve baseline package and references; no changes made.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

## DST-004 case 3

Request: Fictional local search finds no imports; published wrapper exposes old component and unknown external customers remain.

```text
Retirement boundary: Local code-search result only; wrapper remains public.
Consumer handoff:
Consumer | Required behavior | Successor evidence | Migration action | Acceptance status
published wrapper | public contract unresolved | not supplied | inspect wrapper behavior and downstream compatibility | blocked
external users | unknown | absent | obtain migration/compatibility evidence | unresolved
Sequence: Trace wrapper; establish successor parity; communicate via authorized process; test; review removal.
Blockers: External inventory, wrapper contract and retirement policy unknown.
Removal gate: Zero local imports is insufficient.
Recovery: Retain old distribution and wrapper mapping until verified migration permits retirement.
```

Result: Response preserves supplied evidence, names unresolved dependencies and makes no unperformed execution claim. No blocking finding in this bounded case.

Review limits: Four methods retain different artifacts and decisions: graph trace, supported variant matrix, token-reference migration, and behavioral consumer retirement. Nominal four-row enumeration is not a completed runtime test. Twelve text cases do not prove universal reliability.
