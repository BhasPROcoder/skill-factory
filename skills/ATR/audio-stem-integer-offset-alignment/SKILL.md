---
id: ATR-003
name: audio-stem-integer-offset-alignment
domain: Audio Timeline Reconstruction
subdomain: Stem alignment
version: 1.0
description: Construct aligned multichannel stem arrays from approved integer frame offsets while making padding, cropped content and reference-marker correspondence explicit.
triggers: ["align stems by sample offsets", "apply a declared audio delay", "verify stereo stem timing after edits", "reconcile cropped stem beginnings", "build aligned arrays from sync markers"]
not_for: ["estimating delay automatically from similar waveforms", "fractional-delay filters or rate conversion", "stem export requirements [TAM-009]", "phase-coherence certification"]
requires: []
risk_level: medium
---

# Audio Stem Integer Offset Alignment

## Purpose
Build new stem arrays on one explicit output frame grid using supplied integer offsets. Preserve each stem's channel grouping and show any removed or padded regions so a numerically aligned marker cannot hide discarded audio or an unsupported timing assumption.

## Inputs to collect
1. **Stem arrays** — obtain finite numeric decoded channel frames, stable source revisions and channel ordering. This defines the material being moved. Default: none; source audio is required for construction.
2. **Common frame basis** — confirm a common sampling rate and the intended output origin. This makes equal index changes comparable. Default: unknown; do not infer agreement from matching file lengths.
3. **Offsets or reference markers** — obtain an approved integer offset for each stem, or a confirmed marker index and desired output index from which to derive it. This prevents guessing alignment from the largest waveform peak. Default: no automatic offset estimation.
4. **Output extent** — obtain the required positive integer frame count. This defines which source regions fit. Default: ask; do not trim to the shortest stem or extend indefinitely without an agreed boundary.
5. **Crop permission** — identify any content permitted to fall outside the output extent. This controls otherwise silent deletion at either edge. Default: produce a proposed crop ledger for approval before accepting the aligned output.
6. **Verification target** — identify whether marker coincidence, reconstructed mix listening or another check is required. Default: sample-placement verification only; musical and phase judgments remain untested.

If a required input has no safe default, ask in one message with at most three questions. Combine the frame basis and output extent, then collect the offsets and crop permission.

## Procedure
1. Freeze the stem revisions and rate/channel metadata. Keep the decoded input arrays untouched and create new arrays for every alignment candidate.
2. Declare the offset sign convention: output index equals source index plus offset. A positive offset delays the source by inserting leading silence; a negative offset advances it and may crop its beginning on a fixed output grid.
3. Derive each offset from a confirmed marker only when requested: desired output index minus source marker index. Preserve both operands and the marker's evidence; do not substitute a similar-looking transient without confirmation.
4. Calculate the intersection of each shifted source interval with the agreed output interval. ⚠️ List cropped head and tail frames before treating the candidate as deliverable, because correct marker placement can coexist with lost phrase content.
5. Apply each stem's offset to all of its channels together. Keep the existing channel order; an offset belongs to the grouped stem unless a separate channel-level correction is explicitly authorized.
6. Fill uncovered output frames with numeric zero and retain an explicit padding ledger. This creates silence in the reference decoded representation; it does not establish the properties of an encoded file.
7. Verify every retained frame against its source position using the declared offset equation. Confirm output lengths and any marker positions independently of audible similarity.
8. Review crop permission and the actual listening target. Preserve the candidate as a proposal if removed regions are unapproved or if a required listening comparison has not occurred.

The Python 3 reference below operates on finite numeric frame tuples already decoded at one common rate. Run the complete snippet as a local script for its fictional fixture, then substitute validated arrays and approved parameters. It does not load audio files, estimate offsets, resample or assess phase; record the actual interpreter version when testing.

```python
def shift_stem(frames, offset, length):
    if type(offset) is not int or type(length) is not int or length < 1:
        raise ValueError("integer offset and positive length required")
    source = [tuple(frame) for frame in frames]
    if not source or not source[0]:
        raise ValueError("nonempty channel frames required")
    width = len(source[0])
    if any(len(frame) != width for frame in source):
        raise ValueError("channel width mismatch")
    start = max(0, -offset)
    end = min(len(source), length-offset)
    if start >= end:
        raise ValueError("source has no retained overlap")
    output = [(0,) * width for _ in range(length)]
    for index in range(start, end):
        output[index+offset] = source[index]
    ledger = (start, end, start+offset, end+offset,
              start, len(source)-end)
    return output, ledger

a = [(1, 10), (2, 20), (3, 30)]
b = [(-1, -10), (4, 40), (5, 50), (6, 60)]
ao, al = shift_stem(a, 1, 4)
bo, bl = shift_stem(b, -1, 4)
assert ao == [(0, 0), (1, 10), (2, 20), (3, 30)]
assert bo == [(4, 40), (5, 50), (6, 60), (0, 0)]
assert al == (0, 3, 1, 4, 0, 0)
assert bl == (1, 4, 0, 3, 1, 0)
assert 1+1 == 3-1 == 2  # supplied marker indices
assert a[0] == (1, 10) and b[0] == (-1, -10)
try:
    shift_stem(a, 10, 4)
except ValueError:
    pass
else:
    raise AssertionError("empty retained overlap accepted")
print("stem offset checks passed")
```

The ledger tuple means source start, source end, output start, output end, cropped head count, cropped tail count. Every interval is start-inclusive and end-exclusive. The function constructs a candidate even when cropping occurs; its caller must apply the supplied crop-permission decision before accepting that candidate.

## Decision rules
- IF rates differ THEN request an approved common-rate conversion before integer alignment BECAUSE one frame shift would otherwise represent different elapsed times.
- IF a shifted source has no retained overlap THEN reject that configuration BECAUSE an all-silent replacement would conceal the absence of the requested stem.
- IF alignment crops unapproved material THEN leave delivery pending BECAUSE marker coincidence does not authorize removal of other audio.
- IF the source is a linked multichannel stem THEN shift its channels together BECAUSE independent offsets would change the recorded interchannel timing.
- IF a marker's identity is uncertain THEN retain the proposed offset as unverified BECAUSE numerical arithmetic cannot establish that two events represent the intended same moment.

## Output template
```text
Grid: <common rate, origin and output frame count; up to three lines>
Alignment ledger:
Stem | Offset | Retained source [start,end) | Placed output [start,end) | Head/tail crop | Padding
<one row per stem; first twelve rows plus full attachment when longer>
Constructed arrays: <actual values or local artifact references>
Marker check: <up to six source-index plus offset calculations>
Content decision: <crop authorization and pending listening; up to three sentences>
Verification: <up to five executed invariants and limitations>
```

## Quality checklist
- [ ] The output grid has an agreed origin, rate and frame count.
- [ ] Every offset uses the declared sign convention.
- [ ] Marker-derived offsets retain their source and target indices.
- [ ] Head and tail crops are explicitly counted and permission is checked.
- [ ] Each grouped stem receives one timing transformation across its channels.
- [ ] Output frame count and retained sample placement are verified.
- [ ] Original arrays remain unchanged.
- [ ] No phase, listening or encoding claim follows solely from marker arithmetic.

## Anti-patterns
- **Peak guessing**: the largest peaks are assumed to be the same event. Fix: confirm marker identity or label the offset unverified.
- **Sign reversal**: a delay is applied as an advance. Fix: calculate a known marker's output index before construction.
- **Silent head loss**: negative offset removes content without notice. Fix: publish the retained interval and crop count before accepting output.
- **Shortest-stem trimming**: all stems are cut to an arbitrary common minimum. Fix: use the agreed output extent and review each boundary separately.
- **Phase overclaim**: coincident markers are described as perfect phase alignment. Fix: state exactly which timing relationship was tested.

## Worked example
**Input:**
> Fictional studio Moss supplies stereo A=[(1,10),(2,20),(3,30)] and B=[(-1,-10),(4,40),(5,50),(6,60)] on one confirmed frame basis. Confirmed markers are A index 1 and B index 3; both should land at output index 2. Output length is 4. Removing B's first frame is expressly permitted. No playback requested.

**Output:**
```text
Grid: Moss common supplied rate and origin; 4 output frames, stereo order unchanged.
Alignment ledger:
Stem | Offset | Retained source [start,end) | Placed output [start,end) | Head/tail crop | Padding
A | +1 | [0,3) | [1,4) | 0/0 | one leading frame
B | -1 | [1,4) | [0,3) | 1/0 | one trailing frame
Constructed arrays: A=[(0,0),(1,10),(2,20),(3,30)]; B=[(4,40),(5,50),(6,60),(0,0)].
Marker check: A: 1+1=2. B: 3-1=2.
Content decision: B's one-frame head crop is permitted; no other source frames cropped. No playback acceptance requested or claimed.
Verification: Four stereo frames per output; retained values match source positions; original arrays unchanged; no encoding, phase assessment or listening performed.
```

**Bad output:**
> Both markers align, so discard the leading audio and call the mix phase-perfect.

This omits crop permission and claims a property that marker placement alone does not establish.

## Edge cases
- **Different channel counts between stems**: retain each stem's own channel grouping; mixing them requires a separate explicit channel-routing plan.
- **Fractional offset requested**: do not round silently; obtain an approved integer approximation or a separate fractional-delay method.
- **Uncertain source duration**: obtain the actual decoded frame extent before calculating crops; metadata alone is insufficient when it disagrees with the material.
- **Late marker beyond output end**: report that the requested event cannot appear on the selected grid and request an extent or offset decision.

## Test case
**Input:**
> Fictional three-frame stem C must be advanced by two frames on a three-frame output grid. Its first two frames contain protected speech. No crop is authorized, but the final marker would align correctly.

**Assertions:**
1. Calculates that only source frame [2,3) would remain under the proposed offset.
2. Reports two cropped head frames and refuses to treat the candidate as an accepted delivery.
3. Requests an approved grid or alignment revision instead of erasing protected speech.
4. Does not infer listening or phase quality from the surviving marker.
