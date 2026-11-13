# Audio Timeline Reconstruction (ATR)

Construct decoded audio frame edits, loop taper candidates and declared-offset stem arrays with explicit provenance and bounded verification.

Macro-area: Music & Audio Production

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| ATR-001 | [audio-edit-frame-provenance](audio-edit-frame-provenance/SKILL.md) | Build an edited audio sequence with exact source-frame correspondence when cuts or repetitions must remain traceable to original recordings. | trace edited audio to source frames; build a reversible audio cut sequence; check sample boundaries in an edit | validated |
| ATR-002 | [audio-loop-edge-taper-comparison](audio-loop-edge-taper-comparison/SKILL.md) | Construct and compare a duration-preserving edge-taper candidate when a loop boundary needs an inspectable edit without treating a sample metric as an audibility verdict. | compare a loop edge fade; repair a loop boundary reversibly; inspect repeated audio seam | validated |
| ATR-003 | [audio-stem-integer-offset-alignment](audio-stem-integer-offset-alignment/SKILL.md) | Construct aligned multichannel stem arrays from approved integer frame offsets while making padding, cropped content and reference-marker correspondence explicit. | align stems by sample offsets; apply a declared audio delay; verify stereo stem timing after edits | validated |
