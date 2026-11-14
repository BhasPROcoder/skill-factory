---
name: pitch-builder
description: Use to write the hackathon pitch script and a 5–7 slide outline weighted to the judging rubric, plus hook line variants, wrapped around the live demo.
---

# pitch-builder

## Top rules
1. The demo is the pitch. Slides are the frame around it, not the content.
2. Spend slide time in proportion to rubric weight.
3. One idea per slide. Under 15 words of text per slide. Big visuals.
4. Say the number. "Saves time" is noise; "cuts 40 min of revision to 8" is a score.
5. End with what's next and the ask, never with "any questions?" alone.

## When to use
- Demo script exists (from `demo-architect`).
- Judging includes a stage or table pitch, or slides are a submission requirement.

## Inputs needed
- DEMO SCRIPT and RECON BRIEF (scoring map with weights, time per team).
- One real user quote or stat (collect at the venue if needed).
- Team names and roles (one line on the last slide only).

## Steps

### 1. Allocate time by rubric
Example for a 3-minute slot with Innovation 30 / Technical 25 / Impact 25 / Presentation 20:
- Hook + problem (Impact): 35 s
- Live demo incl. wow (Innovation): 80 s
- How it works (Technical): 30 s
- Impact + next + ask: 35 s
Presentation is scored across all of it.

### 2. Slide outline (5–7 slides)
Use `references/pitch-template.md`.
1. **Hook** — one image + one sentence or number.
2. **Problem** — the user, the pain, one stat or quote.
3. **Demo** — title only; switch to the live app.
4. **How it works** — one architecture diagram, max 6 boxes, sponsor tech labelled.
5. **Impact** — who, how many, one metric from testing at the venue if possible.
6. **What's next** — 3 bullets max, realistic.
7. **Team + ask** — names, roles, one ask (try it, intro, prize-specific line).

### 3. Write hook variants (pick the best after saying each aloud)
Formulas:
- **Number shock**: "<huge number> <people> <do painful thing> every <time>."
- **Person moment**: "<Name> is <age>, <situation>. Last <time>, <painful specific event>."
- **Contrast**: "<Common belief>. Research says <opposite>."
- **Question that stings**: "When did you last <universal annoying thing>?"
- **Live**: Start the demo cold with no intro; explain after the wow.

### 4. Write the script
Plain spoken language, short sentences, written to be said, not read. Mark pauses with `/`. Mark the slide/demo switch.

### 5. Rehearse and cut
Time it. Over by 10%+ → cut a whole sentence block, not words.

## Outputs
```
PITCH PACK — <project>
Time budget by beat
Slide outline (5–7) with on-slide text and visual
Full spoken script with switch markers
Hook: chosen + 2 alternates
Ask line
```

## Worked example
VoiceViva hooks:
- Number: "Tonight, about 40 lakh JEE and NEET aspirants will revise by rereading notes. It's the weakest way to learn."
- Person: "Riya has a bio test at 9 AM. She's read chapter 6 four times. She still can't explain it."
- Contrast: "Students think rereading works. Decades of memory research say testing yourself works better."
Chosen: Person (strongest in a room of students), then number on slide 2.
Ask: "We'd love the vector-DB team's take on scaling per-student indexes — and if you've ever reread a chapter four times, try it at our table."

## Failure modes
- 12 slides, 4 minutes of slides, 30 seconds of demo.
- Architecture slide with 20 boxes and tiny text.
- "We used React, Node, MongoDB..." as a slide. Stack lists score nothing.
- Unrehearsed handoffs between speakers.

## Hand-off
Script → `demo-video` narration. Likely questions → `judge-qa-prep`.
