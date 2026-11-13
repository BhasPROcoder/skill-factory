---
id: ATR-002
name: audio-loop-edge-taper-comparison
domain: Audio Timeline Reconstruction
subdomain: Loop boundary editing
version: 1.0
description: Construct and compare a duration-preserving edge-taper candidate when a loop boundary needs an inspectable edit without treating a sample metric as an audibility verdict.
triggers: ["compare a loop edge fade", "repair a loop boundary reversibly", "inspect repeated audio seam", "keep loop length while testing a fade", "measure changes made by a loop taper"]
not_for: ["finding a musical loop automatically", "choosing universal fade durations", "time stretching or beat alignment", "noise reduction audition planning [TAM-005]"]
requires: []
risk_level: medium
---

# Audio Loop Edge Taper Comparison

## Purpose
Produce a reversible loop candidate that tapers both edges while retaining the original frame count and channel relationships. Compare measured boundary changes with the material altered, then leave audible and musical acceptance to an actual repeated-playback review.

## Inputs to collect
1. **Loop frames** — obtain decoded finite numeric channel frames, sampling rate and loop boundaries. These identify the actual repeated segment. Default: none; a verbal description cannot support an executed waveform edit.
2. **Editable regions** — obtain permission to alter the beginning and end, including any protected transient or phrase. This bounds the candidate transformation. Default: no modification until the permitted extent is known.
3. **Taper length** — obtain an integer frame count for each symmetric edge in this reference method. This defines the actual altered samples. Default: no universal length; request a trial value within the editable regions.
4. **Listening target** — identify playback context and the desired observable result, such as avoiding a conspicuous join without softening a named attack. Default: numerical comparison only, listening acceptance pending.
5. **Output format** — identify whether decoded arrays or an encoded audition file are required. Default: decoded candidate and report, preserving the original; encoding settings are not invented.

If required inputs lack safe defaults, ask in one message with at most three questions. Request frame data and format together, then editable extent and trial length, then the listening target.

## Procedure
1. Preserve the original loop as the baseline and record its exact frame count, channel order and rate. A candidate that changes duration is a different timing experiment and must be labeled separately.
2. Measure the last-to-first value difference for each channel in the supplied decoded data. Record this as a boundary value difference, not a predicted click loudness or a perceptual quality score.
3. Confirm that both taper windows lie inside authorized editable regions and do not overlap. If they overlap, choose another explicitly approved length or another method; do not let two independently applied gains interact accidentally.
4. Apply the same linear gain sequence to all channels at each edge. The supplied reference starts at zero at each outer endpoint and reaches unity at the inner endpoint; it leaves the center untouched.
5. Compare candidate and baseline frame counts, channel widths and changed sample locations. ⚠️ A smaller boundary difference does not justify changing protected content; identify every changed region before evaluating the metric.
6. Assemble repeated baseline and candidate arrays for audition without overwriting either version. Keep comparison playback conditions consistent; disclose any gain normalization or export processing that could alter the comparison.
7. Listen across multiple repetitions if audio playback is available. Check the join, rhythmic energy near the seam, transient shape and any perceived dip; describe observations rather than declaring an edit transparent from endpoint equality.
8. Report whether the candidate satisfies the supplied constraints and what listening remains pending. Retain a rejected candidate with its reason when that helps distinguish an unsuitable fade from an incorrectly implemented one.

Run this Python 3 reference as a local script to generate the fictional decoded candidate and verify its invariants. Arrays use arbitrary amplitude units; the example is not normalized production audio. The code assumes finite numeric frame values and does not decode, encode or play audio. Record the installed interpreter version with the actual test result.

```python
def edge_taper(frames, n):
    if type(n) is not int or n < 2 or 2 * n > len(frames):
        raise ValueError("nonoverlapping edge length required")
    original = [tuple(row) for row in frames]
    width = len(original[0])
    if width == 0 or any(len(row) != width for row in original):
        raise ValueError("inconsistent channel frames")
    out = list(original)
    for i in range(n):
        gain = i / (n - 1)
        out[i] = tuple(v * gain for v in original[i])
        out[-1-i] = tuple(v * gain for v in original[-1-i])
    return out

def seam_difference(frames):
    return tuple(abs(a-b) for a, b in zip(frames[-1], frames[0]))

baseline = [(v,) for v in [2, 2, 2, 2, -2, -2, -2, -2]]
candidate = edge_taper(baseline, 3)
assert candidate == [(0,), (1,), (2,), (2,), (-2,), (-2,), (-1,), (0,)]
assert len(candidate) == len(baseline) == 8
assert seam_difference(baseline) == (4,)
assert seam_difference(candidate) == (0,)
assert candidate[3:5] == baseline[3:5]
assert baseline[0] == (2,)
audition_frames = candidate * 3
assert len(audition_frames) == 24
try:
    edge_taper(baseline, 5)
except ValueError:
    pass
else:
    raise AssertionError("overlapping windows accepted")
print("loop taper checks passed")
```

## Decision rules
- IF the initial transient is protected THEN reject a taper that alters it BECAUSE a seam metric cannot overrule the permitted edit boundary.
- IF endpoint values agree after tapering THEN report that numerical result only BECAUSE other waveform changes and musical effects still need listening.
- IF channels belong to one synchronized recording THEN apply the same edge timing and gain law BECAUSE independently chosen edge edits would change their relative behavior.
- IF the requested taper windows overlap THEN reject this reference configuration BECAUSE its unchanged-center construction no longer applies.

## Output template
```text
Baseline: <source, frame extent, rate and channels; up to three lines>
Candidate: <actual decoded array or artifact reference; taper length and gain law>
Comparison:
Measure | Baseline | Candidate | Scope
<up to six rows covering length, seam difference and altered regions>
Listening: <up to four actual observations, or explicitly pending>
Disposition: <keep for audition / reject / accepted by named review; one sentence>
Remaining: <up to three required inputs or checks>
```

## Quality checklist
- [ ] Baseline frames remain unchanged.
- [ ] Taper length is supplied or explicitly approved for the trial.
- [ ] Both edited regions fit the permitted extent without overlap.
- [ ] Candidate frame count equals baseline frame count.
- [ ] Channels use the same edge gain at corresponding frames.
- [ ] Measured value differences are labeled in source amplitude units.
- [ ] Protected attacks and phrase content are checked separately from endpoint metrics.
- [ ] Playback, encoding and perceptual acceptance are claimed only when performed.

## Anti-patterns
- **Zero-difference victory**: equal endpoints are called an inaudible loop. Fix: separate numerical continuity from actual repeated listening.
- **Fixed fade folklore**: a remembered fade duration becomes mandatory. Fix: use the supplied editable window and trial value.
- **Hidden duration change**: an overlap operation silently shortens the loop. Fix: compare frame counts and declare a different timing experiment if necessary.
- **Channel-specific repair**: one channel receives a different taper without approval. Fix: preserve linked timing and gain behavior for synchronized channels.

## Worked example
**Input:**
> Fictional producer Fern supplies mono values [2,2,2,2,-2,-2,-2,-2], at an unchanged supplied rate. Both outer three-frame regions may be edited; no protected attack is specified. Compare the reference three-frame edge taper. No playback or encoded file is requested.

**Output:**
```text
Baseline: Fern supplied mono loop, frames [0,8), unchanged supplied rate.
Candidate: [0,1,2,2,-2,-2,-1,0]; three-frame linear edge taper with outer gain zero and inner gain one.
Comparison:
Measure | Baseline | Candidate | Scope
Frame count | 8 | 8 | timing extent preserved
Last-to-first absolute difference | 4 | 0 | mono source amplitude units
Changed frame indices | none | 0,1,6,7 | within approved edge regions
Center frames [3,5) | [2,-2] | [2,-2] | unchanged
Listening: Not performed; no claim that the join or energy dip is inaudible.
Disposition: Keep for audition; numeric constraints pass but perceptual acceptance is pending.
Remaining: Audition repetitions under the intended playback conditions if acceptance is required.
```

**Bad output:**
> Boundary difference is zero, so the loop is seamless and approved.

This promotes one measured property into an unsupported listening and approval claim.

## Edge cases
- **One-frame requested taper**: reject this reference because its denominator and inner/outer endpoint definition require at least two frames; ask for another permitted method.
- **Very short loop**: if authorized windows cannot fit, retain the baseline and report the constraint rather than altering the whole phrase silently.
- **Already matching endpoints**: do not apply a fade automatically; compare whether any requested problem remains and preserve the original when no edit is justified.
- **Nonfinite or malformed data**: stop before metric calculation and obtain valid decoded frames; do not turn invalid numbers into zeros.

## Test case
**Input:**
> Fictional loop has matching endpoints but its first attack is explicitly protected. The requester asks to apply the reference taper only because it usually fixes loops. No audible seam problem is supplied.

**Assertions:**
1. Does not alter the protected attack under the proposed taper.
2. Distinguishes already matching endpoints from broader listening quality.
3. Requests an actual problem or an approved alternative edit boundary before constructing a replacement.
4. Does not claim that unchanged data have been audibly approved.
