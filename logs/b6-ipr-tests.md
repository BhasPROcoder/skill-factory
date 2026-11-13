# Independent IPR executable review

Reviewer: recover_lre, separate from IPR author. Fresh fictional traces execute the actual fenced Python blocks. Interpreter observed: 3.14.6.

Initial review identified an acceptance-time identity gap in IPR-001. The original revision-only guard is reproduced separately below; the coordinator repaired the actual skill to bind identity and revision. Tests below run the repaired skill and reject form, record and schema switches even when revision remains equal.

## Embedded assertions: interrupted-form-draft-restoration

```json
"draft transition checks passed"
```

PASS

## IPR-001 ordinary: allowlisted title and no submission

```json
[
  {
    "form": "Notebook",
    "record": "Cedar",
    "schema": "S2",
    "revision": 8,
    "values": {
      "title": "Aster"
    },
    "submitted": false
  },
  "restored-for-review"
]
```

PASS

## IPR-001 missing: no eligible offer

```json
[
  {
    "form": "Notebook",
    "record": "Cedar",
    "schema": "S2",
    "revision": 7,
    "values": {},
    "submitted": false
  },
  "review-required"
]
```

PASS

## IPR-001 edge: same-revision identity switches and later edit

```json
{
  "form": [
    {
      "form": "different",
      "record": "Cedar",
      "schema": "S2",
      "revision": 7,
      "values": {},
      "submitted": false
    },
    "review-required"
  ],
  "record": [
    {
      "form": "Notebook",
      "record": "different",
      "schema": "S2",
      "revision": 7,
      "values": {},
      "submitted": false
    },
    "review-required"
  ],
  "schema": [
    {
      "form": "Notebook",
      "record": "Cedar",
      "schema": "different",
      "revision": 7,
      "values": {},
      "submitted": false
    },
    "review-required"
  ]
}
```

PASS

## Reproduction of original defect: Cedar values applied to Maple by old acceptance guard

```json
[
  {
    "form": "Notebook",
    "record": "Maple",
    "schema": "S2",
    "revision": 8,
    "values": {
      "title": "Aster"
    },
    "submitted": false
  },
  "restored-for-review"
]
```

PASS

## Embedded assertions: asynchronous-result-generation-ownership

```json
"generation ownership checks passed"
```

PASS

## IPR-002 ordinary: owning response settles once

```json
[
  {
    "generation": 1,
    "query": "violet",
    "status": "success",
    "items": [
      "v1",
      "v2"
    ],
    "error": null
  },
  "accepted"
]
```

PASS

## IPR-002 missing: response has no request token

```json
[
  {
    "generation": 1,
    "query": "pending",
    "status": "pending",
    "items": [],
    "error": null
  },
  "ignored"
]
```

PASS

## IPR-002 edge: repeated text then clear rejects stale success and errors

```json
[
  {
    "generation": 4,
    "query": "",
    "status": "idle",
    "items": [],
    "error": null
  },
  "ignored"
]
```

PASS

## Embedded assertions: transactional-edit-history-branching

```json
"edit history checks passed"
```

PASS

## IPR-003 ordinary: complete undo-redo round trip

```json
[
  [
    "Cedar",
    "Maple"
  ],
  "Aster",
  []
]
```

PASS

## IPR-003 missing: no string snapshot supplied

```json
"reference snapshots must be strings"
```

PASS

## IPR-003 edge: canceled preview/no-op retain redo; real edit clears it

```json
[
  [
    "Cedar",
    "Maple"
  ],
  "Juniper",
  []
]
```

PASS

## Judgment and boundaries

IPR-001: Fresh normal, missing-offer and switched-context cases retain allowlist, identity and edit-version constraints. The original failure is a regression reproduction, not a current failure. Follow-up assertions reject offers after submission or policy changes when the caller advances revision as required. The inspected post-snippet contract limits the model to one editing lifetime and fixed allowlist; reopened records must discard old offers before revision reset or add a lifetime identity. This boundary is explicit, not implemented by the snippet. If the user provides no form identity or field policy, request form/record/schema and allowed fields before offering recovery; no browser persistence is inferred.

IPR-002: Fresh response traces reject missing ownership, duplicate callbacks, repeated-text older generations and errors after clearing. A request whose non-query context is unspecified requires the actual context contract before integration; the sample only implements one query-owned view.

IPR-003: Fresh traces preserve history through canceled preview and no-op commit, reject missing string content and invalidate the old future on a genuine branch edit. Grouped previews are modeled outside committed history as instructed, not inferred from timings.

These are executable transition-model tests, not rendered UI, framework lifecycle, persistent storage, service, security or cross-model validation. No current external APIs, empirical claims or mutable policies were assumed. Fixture labels are fictional; arithmetic consists only of deterministic revision increments.

No remaining blocker found in these tested paths after the identity repair. Usability of a production adaptation still requires its actual state schema and integration checks.
