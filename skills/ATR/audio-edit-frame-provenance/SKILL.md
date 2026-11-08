---
id: ATR-001
name: audio-edit-frame-provenance
domain: Audio Timeline Reconstruction
subdomain: Edit provenance
version: 1.0
description: Build an edited audio sequence with exact source-frame correspondence when cuts or repetitions must remain traceable to original recordings.
triggers: ["trace edited audio to source frames", "build a reversible audio cut sequence", "check sample boundaries in an edit", "map repeated audio segments", "reconstruct audio from an edit list"]
not_for: ["choosing dialogue meaning or pacing [TAM-004]", "resampling or time stretching", "mixing overlapping clips", "decoding arbitrary audio formats"]
requires: []
risk_level: medium
---

# Audio Edit Frame Provenance

## Purpose
Construct a sequence from explicit source intervals and produce a ledger connecting every output interval to its source frames. This procedure makes cuts and repeated material inspectable without claiming that the resulting boundaries sound natural or preserve an intended spoken meaning.

## Inputs to collect
1. **Decoded source frames** — obtain immutable source identifiers, equal-width channel frames and their common sampling rate. These establish what each frame represents. Default: none; source data and rate agreement are required for construction.
2. **Edit decisions** — collect ordered source identifiers with start-inclusive and end-exclusive frame indices. This determines selection without timecode rounding. Default: no inferred cut points; ask for the intended intervals.
3. **Channel convention** — obtain channel ordering and confirm that each selected source uses that order. This avoids substituting one channel role for another. Default: unknown, so mixed-source construction waits.
4. **Output scope** — identify whether the request is for in-memory frames, a preview file or an editor handoff. Default: frames and a ledger only; encoding requirements remain a separate input.
5. **Permitted transformations** — establish whether cuts alone are allowed or fades and other processing are authorized. Default: exact concatenation, with potentially abrupt joins reported for later audition.

If a required input has no safe default, ask in one message with at most three questions. Group source format, rate and channel questions together rather than guessing from a filename extension.

## Procedure
1. Freeze the source revisions and label each input with a stable identifier. Keep a new output container so edits do not overwrite the recordings used as evidence.
2. Confirm that rates and channel roles agree across selected sources. A frame contains the simultaneous values for the channels; an index into a flattened interleaved buffer is not automatically a frame index.
3. Normalize edit boundaries into integer frame indices using an explicitly supplied conversion rule if the input uses time units. Retain the original times and conversion rule beside the normalized decisions.
4. ⚠️ Reject negative, reversed, empty or out-of-range intervals instead of letting permissive slicing silently shorten them. An empty requested edit list is different from a malformed individual selection.
5. Append the selected frame ranges in edit-list order. Preserve repetitions as separate selections with separate output locations; duplicate source references can be intentional musical or editorial decisions.
6. Record output start and end indices as each range is appended. Verify that interval lengths match and that output intervals meet without unintended gaps or overlaps.
7. Compare each constructed output interval with its referenced source slice. This verifies exact sample selection, but not playback quality, channel semantics or the appropriateness of the editorial decision.
8. Audition permitted previews around each join using the supplied listening environment, or state that listening remains pending. Describe any proposed fade separately because processing would change exact source sample equality.

The following executable Python 3 reference uses decoded finite numeric samples, a common rate and already-confirmed channel order as preconditions. It does not decode files or perform rate conversion. Run it unchanged to check the fictional fixture, then substitute the user's validated arrays and decisions. Save the snippet as a local script and run it with the installed Python 3 interpreter; record the actual interpreter version in the test evidence rather than calling any version current.

```python
def assemble(sources, edits):
    output, ledger = [], []
    width = None
    for sid, start, end in edits:
        frames = sources[sid]
        if type(start) is not int or type(end) is not int:
            raise ValueError("frame indices must be integers")
        if not 0 <= start < end <= len(frames):
            raise ValueError("invalid interval")
        block = [tuple(frame) for frame in frames[start:end]]
        for frame in block:
            if not frame or (width is not None and len(frame) != width):
                raise ValueError("channel width mismatch")
            width = len(frame)
        out_start = len(output)
        output.extend(block)
        ledger.append((sid, start, end, out_start, len(output)))
    return output, ledger

src = {"A": [(0,), (1,), (2,), (3,), (4,), (5,)]}
out, log = assemble(src, [("A", 1, 4), ("A", 1, 3)])
assert out == [(1,), (2,), (3,), (1,), (2,)]
assert log == [("A", 1, 4, 0, 3), ("A", 1, 3, 3, 5)]
assert assemble(src, []) == ([], [])
try:
    assemble(src, [("A", 4, 7)])
except ValueError:
    pass
else:
    raise AssertionError("out-of-range selection accepted")
print("frame provenance checks passed")
```

## Decision rules
- IF source rates differ THEN stop exact concatenation and request an approved conversion step BECAUSE equal frame counts would represent different durations.
- IF the same source interval appears twice THEN retain two ledger entries BECAUSE output position, not source uniqueness, defines the edit sequence.
- IF a fade is applied after construction THEN keep a processing annotation alongside provenance BECAUSE processed values no longer equal their unmodified source samples.
- IF a user supplies seconds without a rounding convention THEN request that convention before frame conversion BECAUSE ambiguous boundaries can select different samples.

## Output template
```text
Construction: <source revisions, rate and channel convention; up to three lines>
Edit ledger:
Source | Source [start,end) | Output [start,end) | Frame count
<one row per edit; first twelve rows with a full ledger attachment if longer>
Output: <actual array, local artifact reference or explicit construction limitation>
Checks: <up to five executed comparisons and outcomes>
Join review: <up to five observed or pending listening findings>
Processing boundary: <up to two sentences identifying exact-copy and processed regions>
```

## Quality checklist
- [ ] Every selection identifies its actual source revision.
- [ ] Rate and channel-order agreement are established before construction.
- [ ] Frame indices use the stated inclusive/exclusive convention.
- [ ] Invalid intervals are rejected rather than clipped silently.
- [ ] Output interval lengths equal selected source lengths.
- [ ] Intentional repeated selections have distinct output locations.
- [ ] Source data remain unchanged after output construction.
- [ ] Listening and encoding claims match work actually performed.

## Anti-patterns
- **Silent slice clipping**: an oversized end index yields a shorter edit unnoticed. Fix: validate both bounds before slicing.
- **Interleaved index confusion**: one channel sample is treated as a whole frame. Fix: establish frame shape and channel order first.
- **Deduplicated refrain**: repeated source selections are collapsed. Fix: retain ordered edit occurrences.
- **Provenance as approval**: exact copying is called an acceptable dialogue edit. Fix: review meaning and audible joins separately.

## Worked example
**Input:**
> Fictional studio Reed supplies mono source A with frames 0, 1, 2, 3, 4, 5. All selections use the source's unchanged sampling rate. Select A frames [1,4), then A [1,3). Produce exact decoded frames only; no listening or processing is requested.

**Output:**
```text
Construction: Reed source A; unchanged supplied common rate; one mono value per frame.
Edit ledger:
Source | Source [start,end) | Output [start,end) | Frame count
A | [1,4) | [0,3) | 3
A | [1,3) | [3,5) | 2
Output: [(1,), (2,), (3,), (1,), (2,)]
Checks: Exact array matches both source slices; 3+2=5 output frames; source remains unchanged; reference assertions pass when executed.
Join review: No listening performed; the join from source value 3 to 1 remains unassessed audibly.
Processing boundary: Both regions are exact copies. No fades, resampling or file encoding performed.
```

**Bad output:**
> Remove the repeated segment because source A is already present; output frames 1, 2, 3.

This discards an intentional edit occurrence and changes the requested sequence.

## Edge cases
- **No selections**: return an explicitly empty output and ledger; do not invent silence of an unspecified duration.
- **Channel count changes**: reject construction until an approved channel mapping is supplied; padding channels is a separate transformation.
- **Time-stretched region**: retain its separate transformation map instead of claiming a one-to-one unmodified frame interval.
- **Missing source**: identify the unresolved source identifier and preserve the edit decision without substituting a similarly named file.

## Test case
**Input:**
> Fictional source B has four mono frames. Request [0,2), [2,4), and then [3,6). The requester says to accept whatever slicing returns.

**Assertions:**
1. Rejects the final interval because its end exceeds the source extent.
2. Does not silently produce a shortened final selection.
3. Preserves the requested intervals as the correction basis and asks for a valid final boundary.
4. Makes no listening or file-encoding claim from array construction alone.
