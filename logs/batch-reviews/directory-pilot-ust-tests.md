# Independent execution of UST pilot requests

Reviewer: directory_spatial agent, not the UST author. Date: 2026-10-31. This is an assertion-guided independent review, not a blind evaluation: coordinator assertions were visible to the reviewer.
Inputs: coordinator requests in plans/directory-pilot-tests.md and the two UST skill files. These are fresh text-artifact executions, not live application tests. No dashboard, configurator, sensor, inventory system, or transaction was operated. The outputs below are the reviewer's actual responses using the skills, followed by assertion decisions. No claim of cross-model portability is made.

## UST-001 ordinary request

```text
Scope: Specify a depot temperature card that distinguishes a last known observation from currently arriving data.
Evidence: A valid sample and subsequent connection loss are supplied. Measurement timestamp, clock comparability, unit, and freshness cutoff are not supplied. Transport state is independent evidence.
State contract:
Unknown freshness | sample exists but age/policy is unresolved | retain with qualifications | Last known observation; freshness unknown | request timestamp and policy details
Disconnected | transport reports loss | retain last known value as historical, not live | Disconnected; displaying last known observation | retry if authorized action exists
Unavailable | no sample exists | show no numeric substitute | No observation available | inspect source
Invalid | quality check rejects sample | do not show as trusted reading | Invalid observation | inspect quality evidence
Stale | comparable age exceeds supplied future policy | retain as historical | Observation exceeds age policy | request update if available
Fresh | valid sample satisfies confirmed clock and age policy | show value and observation time | Current under configured policy | none required
Transition walkthrough:
Valid sample received | last known value; freshness unresolved | validity alone does not establish recency
Connection lost | historical value plus disconnected | transport changed, not the observation timestamp
Refresh requested | request pending; historical status retained | requested recovery is not successful recovery
Reconnect with old sample | connected plus historical value | delivery does not refresh observation time
Qualifying new sample arrives | freshness evaluated against confirmed policy | fresh state remains unavailable until the policy is supplied
Open dependencies: What observation timestamp and clock semantics are supplied? What age policy and boundary does the depot owner require? What unit and refresh actions apply?
Delivery status: Specification only; no interface implementation, rendering, or device checks performed.
```

Assertions: PASS — transport and age are separate; old value is historical; no numeric freshness cutoff invented. Skill handles the missing policy without calling a valid sample fresh.

## UST-001 missing-input request

```text
Scope: Specify how an arrival-only temperature feed displays uncertainty about measurement age and quality.
Evidence: Arrival time exists. Measurement time, source clock, validity/quality evidence, and freshness policy are absent. Arrival time records receipt, not measurement.
State contract:
Unknown provenance | only arrival evidence exists | show only as unverified received value if available | Measurement time and quality unknown | obtain source contract
Unavailable | no observation value exists | no number | No observation received | inspect delivery
Invalid | a future quality check rejects sample | suppress trusted presentation | Observation invalid | inspect quality evidence
Stale | confirmed observation age exceeds confirmed policy | show historical value | Observation old | request update if available
Fresh | confirmed valid observation satisfies confirmed policy | show value with observation time | Current under policy | no recovery action needed
Transition walkthrough:
First arrival | unverified received value | receipt establishes delivery only
Later arrival | still unknown freshness | later receipt does not prove later measurement
Connection becomes available | transport status changes only | no age or quality evidence added
Measurement metadata supplied | evaluate clock comparability and quality | do not assume metadata is comparable merely because present
Applicable age policy supplied | classify eligible samples | exact boundary follows owner policy
Open dependencies: What measurement timestamp and clock source should accompany arrivals? What source identity and quality flags establish provenance and validity? What freshness policy and boundary should apply?
Delivery status: Specification only; no live feed, implementation, or interface validation performed.
```

Assertions: PASS — arrival and measurement times remain distinct; unknown provenance and quality are visible; consolidated contract questions are included.

## UST-001 late-buffered-sample request

```text
Scope: Prevent an older buffered temperature sample from silently replacing a newer measurement after reconnect.
Evidence: The scenario establishes measurement ordering: buffered sample is older than the current sample. Actual timestamps, tie rules, quality evidence, and freshness cutoff remain unspecified. Receipt order differs from measurement order.
State contract:
Latest eligible observation | greatest confirmed measurement order among accepted samples | preserve latest value | Latest known measurement; freshness separately evaluated | inspect age policy
Historical backfill | confirmed measurement order precedes current sample | retain in historical chart if supported | Historical observation | none required
Ordering conflict | timestamps or ordering identifiers cannot be compared | retain current value with conflict notice | Observation order unresolved | obtain ordering contract
Unavailable | no eligible observation | no fabricated zero | No eligible observation | inspect source
Invalid | sample rejected by quality contract | exclude from trusted latest card | Invalid observation | inspect quality evidence
Transition walkthrough:
Newer measurement already displayed | retain current observation | established measurement ordering
Connection reconnects | connected transport; value unchanged | reconnect is not a new observation
Older buffered sample arrives later | historical backfill; latest card unchanged | receipt order cannot override known measurement order
Equal or incomparable order arrives | ordering conflict notice | no tie-breaking evidence supplied
New qualifying observation arrives | replace according to confirmed ordering and validity policy | freshness still evaluated independently
Open dependencies: Timestamp/ordering contract and tie handling; quality contract; freshness cutoff and boundary; historical chart support.
Delivery status: Specification only; no actual stream ordering, rendering, or recovery implementation tested.
```

Assertions: PASS — late delivery does not imply latest measurement; ordering and conflict behavior are explicit; reconnection does not certify freshness.

## UST-002 ordinary request

```text
Configuration: shade=large; base=short; prior base choice retained; no pins specified.
Conflict: The supplied lamp rule excludes large shade with short base. The new shade selection conflicts with the retained base choice.
Repair options:
A | base becomes tall | large shade | price and availability unknown; recheck full applicable rules
B | shade becomes small | short base | price and availability unknown; recheck full applicable rules
Interaction contract: Explain that large shade cannot be paired with short base under the supplied rule.
Keep the user's draft while showing A and B as proposals.
Show the precise changed choice before confirmation.
Apply only the selected confirmed repair; provide undo that restores the draft and its conflict notice.
Walkthrough: Select large shade after short base -> display the conflict without substitution.
Preview A -> tall base shown as a proposed change, not an applied choice.
Confirm A -> compatible under the supplied rule; retain unknown commercial state.
Undo -> restore large plus short with its incompatibility notice.
Commit gate: Confirm applicable compatibility rules, availability, and current price before order readiness.
Delivery status: Design only; no live selection change, quote, inventory lookup, or purchase performed.
```

Assertions: PASS — exact conflict named; original intent retained; no silent substitution; two alternatives supported by supplied allowed values and rule.

## UST-002 missing-rule request

```text
Configuration: finish=unspecified; size=unspecified; authoritative allowed-value list absent.
Conflict: Compatibility is unknown, not established invalid. The statement that some finishes do not work with some sizes identifies a missing rule table, not a specific prohibited combination.
Repair options:
No supported repair; allowed values and constraints have not been supplied.
Interaction contract: Show Compatibility pending rule verification rather than Invalid selection.
Retain any user-entered draft without inventing substitutions.
Request authoritative rules before offering validated repair choices.
Walkthrough: User enters draft -> preserve entries and mark compatibility unknown.
Rule table requested -> keep pending state rather than guessing valid combinations.
Authoritative rules arrive -> compare actual draft against all applicable constraints.
Conflict established, if any -> show only supported repairs and require deliberate confirmation.
Commit gate: Obtain allowed values, compatibility rules with owner/revision, and the user's actual draft; subsequently recheck price and availability before commitment.
Delivery status: Design only; no configuration was validated or changed. Questions: What are the allowed finishes and sizes? What authoritative rule table and revision apply? What selections and pinned preferences should be preserved?
```

Assertions: PASS — no combinations invented; authoritative constraints requested; unknown compatibility separated from known invalidity. No substantive skill repair needed.

## UST-002 saved-configuration edge request

```text
Configuration: saved selections preserved as historical draft; exact values unspecified; separate option has unavailable stock.
Conflict: Today's supplied rule disallows the saved configuration that was valid under yesterday's context. This is current incompatibility, separate from the stock issue for another option.
Repair options:
No supported repair until the affected dimensions, allowed alternatives, and current rule details are supplied.
Interaction contract: Preserve the saved selection and identify its prior validation context as historical.
Display current rule conflict separately from the unrelated stock-unavailable notice.
Show any eventual repair as an explicit changed-dimension comparison before confirmation.
Do not purchase or replace options automatically; preserve an undo path to the saved draft with current warnings.
Walkthrough: Restore saved draft -> prior validation retained as historical, not current approval.
Apply today's rule evidence -> current incompatibility shown without deleting choices.
Inspect separate option -> stock unavailable shown as availability evidence, not proof of incompatibility.
Obtain permitted alternatives -> explain exactly which values each repair would change.
Confirm chosen repair -> revalidate rules, inventory, and price before any separate commitment.
Commit gate: Resolve the supplied rule conflict with supported values; check availability independently; refresh price/quote evidence. No order authority is assumed.
Delivery status: Design only; exact repair values cannot be invented from the sparse request; no live update or purchase performed.
```

Assertions: PASS — historical validity, current rule incompatibility, and stock unavailability are distinct; no automatic purchase; recovery requires a disclosed change set rather than fabricated option names.

## Review disposition

All six text-artifact executions satisfy their coordinator assertions. The procedures produce meaningfully different contracts: temporal evidence and stream ordering versus option-constraint recovery and preserved intent. No blocking substantive issue found in this bounded review. This does not establish correctness of future implementations or replace broader testing.
