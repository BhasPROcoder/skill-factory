# Independent ATR execution review

Reviewer: review_atr, independent of author recover_atr. All cases are new fictional fixtures. The script executes the actual embedded snippets, asserts new results and records outputs. Narrative responses below are the reviewer’s application of the full skill; permission, missing-input and perceptual judgments are not claimed as automated by the snippets.

Observed Python interpreter: 3.14.6

## Reviewed source fingerprints

- ATR-001: SHA256 `79c3a9ffa16fb2e706f1b66f8d1550f5f7741658bbf8969ec5a2ad1cdc0f808c`; embedded output: `frame provenance checks passed`
- ATR-002: SHA256 `aa6dba2faac77b3a55505458c85ba655f0a5cc93c711ec569600b1e216e6dc6a`; embedded output: `loop taper checks passed`
- ATR-003: SHA256 `24e96fd371109fbeac54ebb11a1d7a972ab7015404baccb660d3d0cccb047064`; embedded output: `stem offset checks passed`

## ATR-001 ordinary

Request: Fictional Cedar supplies P/Q stereo arrays as recorded below on one confirmed common rate and channel order. Assemble P[0,2), Q[1,2), P[1,3); exact decoded arrays only.

Actual numerical result:
```json
{
  "sources": {
    "P": [
      [
        3,
        30
      ],
      [
        4,
        40
      ],
      [
        5,
        50
      ]
    ],
    "Q": [
      [
        6,
        60
      ],
      [
        7,
        70
      ]
    ]
  },
  "edits": [
    [
      "P",
      0,
      2
    ],
    [
      "Q",
      1,
      2
    ],
    [
      "P",
      1,
      3
    ]
  ],
  "output": [
    [
      3,
      30
    ],
    [
      4,
      40
    ],
    [
      7,
      70
    ],
    [
      4,
      40
    ],
    [
      5,
      50
    ]
  ],
  "ledger": [
    [
      "P",
      0,
      2,
      0,
      2
    ],
    [
      "Q",
      1,
      2,
      2,
      3
    ],
    [
      "P",
      1,
      3,
      3,
      5
    ]
  ]
}
```

Reviewer response:
```text
Construction: Cedar P/Q, confirmed common rate and stereo order. Edit ledger uses the exact source/output intervals below. Output: constructed array below. Checks: interval equality, total length and source preservation passed. Join review: not listened. Processing boundary: exact copies only, no encoding or fades.
```

Checks passed: five output frames; each output interval equals source slice; repeated P region retained; inputs unchanged.

## ATR-001 missing

Request: Fictional Cedar requests Absent[0,1), but provides only source P. Do not substitute another recording.

Actual numerical result:
```json
{
  "exception": "KeyError",
  "message": "'Absent'"
}
```

Reviewer response:
```text
Construction: unresolved source Absent. Edit ledger: retain requested Absent[0,1) as pending. Output: none. Checks: code rejected the missing key. Join review: not performed. Processing boundary: no replacement or edit delivered. Please supply Absent with its frame basis and channel identity, or explicitly revise the edit decision.
```

Checks passed: missing source rejected; no returned constructed output.

## ATR-001 edge

Request: Fictional Cedar asks to accept negative, empty, reversed, oversized and boolean frame bounds by permissive slicing. P has three frames.

Actual numerical result:
```json
[
  {
    "bounds": [
      -1,
      1
    ],
    "result": {
      "exception": "ValueError",
      "message": "invalid interval"
    }
  },
  {
    "bounds": [
      1,
      1
    ],
    "result": {
      "exception": "ValueError",
      "message": "invalid interval"
    }
  },
  {
    "bounds": [
      2,
      1
    ],
    "result": {
      "exception": "ValueError",
      "message": "invalid interval"
    }
  },
  {
    "bounds": [
      0,
      4
    ],
    "result": {
      "exception": "ValueError",
      "message": "invalid interval"
    }
  },
  {
    "bounds": [
      false,
      1
    ],
    "result": {
      "exception": "ValueError",
      "message": "frame indices must be integers"
    }
  }
]
```

Reviewer response:
```text
Construction: Cedar P supplied; requested bounds are invalid. Edit ledger: each rejected interval retained in the results below. Output: no shortened substitute. Checks: every malformed selection rejected. Join review: not performed. Processing boundary: ask the edit owner for valid integer boundaries rather than silently clipping.
```

Checks passed: all five malformed selections rejected; source unchanged.

## ATR-002 ordinary

Request: Fictional studio Hazel permits editing both outer three-frame windows of the stereo fixture below. Use the same taper in both channels and return decoded arrays only.

Actual numerical result:
```json
{
  "baseline": [
    [
      6,
      12
    ],
    [
      6,
      12
    ],
    [
      6,
      12
    ],
    [
      8,
      16
    ],
    [
      -8,
      -16
    ],
    [
      -6,
      -12
    ],
    [
      -6,
      -12
    ],
    [
      -6,
      -12
    ]
  ],
  "candidate": [
    [
      0.0,
      0.0
    ],
    [
      3.0,
      6.0
    ],
    [
      6.0,
      12.0
    ],
    [
      8,
      16
    ],
    [
      -8,
      -16
    ],
    [
      -6.0,
      -12.0
    ],
    [
      -3.0,
      -6.0
    ],
    [
      -0.0,
      -0.0
    ]
  ],
  "baseline_seam": [
    12,
    24
  ],
  "candidate_seam": [
    0.0,
    0.0
  ]
}
```

Reviewer response:
```text
Baseline: Hazel eight stereo frames, supplied unchanged rate. Candidate: three-frame linear edge taper shown below. Comparison: endpoint differences become zero, center remains unchanged and duration is preserved. Listening: not performed. Disposition: keep for audition, not audibly approved. Remaining: actual playback review if perceptual acceptance is required.
```

Checks passed: eight frames retained; stereo gain relation preserved; center unchanged; source unchanged.

## ATR-002 missing

Request: Fictional Hazel supplies valid arrays but no taper length or editable-region permission; requester asks to use a typical fade.

Actual numerical result:
```json
{
  "exception": "ValueError",
  "message": "nonoverlapping edge length required"
}
```

Reviewer response:
```text
Baseline: supplied arrays retained. Candidate: not constructed. Comparison: no authorized trial extent. Listening: not performed. Disposition: retain original pending scope. Remaining: please specify editable edge regions and a trial frame count; identify any protected attack and listening target. No typical duration is inferred.
```

Checks passed: missing trial length rejected; no universal duration selected.

## ATR-002 edge

Request: Fictional Hazel expressly permits two-frame edge windows on a four-frame stereo loop. Compare the touching nonoverlapping windows, then try an unapproved three-frame window. No playback requested.

Actual numerical result:
```json
{
  "baseline": [
    [
      2,
      4
    ],
    [
      3,
      6
    ],
    [
      4,
      8
    ],
    [
      5,
      10
    ]
  ],
  "two_frame_candidate": [
    [
      0.0,
      0.0
    ],
    [
      3.0,
      6.0
    ],
    [
      4.0,
      8.0
    ],
    [
      0.0,
      0.0
    ]
  ],
  "overlap_attempt": {
    "exception": "ValueError",
    "message": "nonoverlapping edge length required"
  }
}
```

Reviewer response:
```text
Baseline: four-frame stereo fixture. Candidate: authorized two-frame windows produce the array below; no unedited center interval exists. Comparison: inner endpoints retain unity and outer endpoints zero. Listening: not performed. Disposition: numeric candidate only. Remaining: larger overlapping windows require another approved method; endpoint equality does not establish an inaudible join.
```

Checks passed: touching windows do not overlap; four frames retained; overlapping windows rejected.

## ATR-003 ordinary

Request: Fictional Juniper uses supplied stereo source on one agreed frame basis. Construct separate +2 and -1 candidates of length five. Owner permits last-frame crop in +2 and first-frame crop in -1. No marker identity or listening claim requested.

Actual numerical result:
```json
{
  "source": [
    [
      11,
      21
    ],
    [
      12,
      22
    ],
    [
      13,
      23
    ],
    [
      14,
      24
    ]
  ],
  "delayed": [
    [
      0,
      0
    ],
    [
      0,
      0
    ],
    [
      11,
      21
    ],
    [
      12,
      22
    ],
    [
      13,
      23
    ]
  ],
  "delay_ledger": [
    0,
    3,
    2,
    5,
    0,
    1
  ],
  "advanced": [
    [
      12,
      22
    ],
    [
      13,
      23
    ],
    [
      14,
      24
    ],
    [
      0,
      0
    ],
    [
      0,
      0
    ]
  ],
  "advance_ledger": [
    1,
    4,
    0,
    3,
    1,
    0
  ]
}
```

Reviewer response:
```text
Grid: supplied common basis, five frames. Alignment ledger: +2 retains [0,3) to [2,5), tail crop one; -1 retains [1,4) to [0,3), head crop one. Constructed arrays: below. Marker check: not requested or inferred. Content decision: both stated crops permitted; listening not performed. Verification: exact retained frame placement and unchanged source passed; no phase or encoding conclusion.
```

Checks passed: five frames per candidate; positive offset delays; negative offset advances; tail/head crops explicit; inputs unchanged.

## ATR-003 missing

Request: Fictional Juniper asks for an aligned result but supplies neither approved offset nor confirmed corresponding marker. A suggested half-frame approximation is not authorized.

Actual numerical result:
```json
{
  "missing_offset": {
    "exception": "ValueError",
    "message": "integer offset and positive length required"
  },
  "fractional_offset": {
    "exception": "ValueError",
    "message": "integer offset and positive length required"
  }
}
```

Reviewer response:
```text
Grid: output request known, offset unresolved. Alignment ledger: pending. Constructed arrays: none. Marker check: identity and desired location required if deriving offset. Content decision: no crop accepted. Verification: reference rejects missing/fractional offsets. Please provide approved integer offset or confirmed marker indices and an approved alternative method for fractional placement.
```

Checks passed: missing and fractional offsets rejected; no silent rounding.

## ATR-003 edge

Request: Fictional Juniper proposes -3 on a four-frame grid. The first three source frames are protected speech and no crop is authorized. Also test +4, which would place all material outside the grid.

Actual numerical result:
```json
{
  "proposed_candidate": [
    [
      14,
      24
    ],
    [
      0,
      0
    ],
    [
      0,
      0
    ],
    [
      0,
      0
    ]
  ],
  "crop_ledger": [
    3,
    4,
    0,
    1,
    3,
    0
  ],
  "no_overlap": {
    "exception": "ValueError",
    "message": "source has no retained overlap"
  }
}
```

Reviewer response:
```text
Grid: four frames. Alignment ledger: proposed -3 retains [3,4) at [0,1), crops three protected head frames and pads three trailing frames. Constructed arrays: diagnostic candidate only below. Marker check: arithmetic cannot authorize removal. Content decision: reject delivery under supplied protection; request grid or offset revision. Verification: source placement passed, zero-overlap alternative rejected; no phase or listening acceptance.
```

Checks passed: three head frames would be removed; only final frame retained; zero-overlap rejected.

## Scope, claims and uniqueness

Nine fresh cases passed their executed assertions; no blocker found in these paths. Finite numeric arrays, rate agreement and channel order remain preconditions as stated by the skills. These checks are not production decoders, listening tests or proof of perceptual quality. The missing/protected-input responses apply the written workflow rather than claiming the functions enforce approval.

Routing and selected procedures compared through sf.py: TAM-004 chooses dialogue meaning and pacing; ATR-001 constructs exact source-frame correspondence. TAM-005 is a noise-reduction audition plan; ATR-002 constructs a bounded edge-taper candidate and reports its numerical alteration. TAM-009 defines stem delivery requirements and reimport checks; ATR-003 implements integer placement with explicit crops and padding. The new artifacts and decision rules are distinct from those neighbors; this is a substantive comparison, not a universal uniqueness proof.

Arithmetic in fixtures is asserted against literal expected arrays, interval lengths and crop ledgers. Names and numeric inputs are explicitly fictional. No rate, production threshold, legal rule, current software API, source citation or audibility statistic is invented. Review covers decoded arrays and procedural decisions only.
