---
name: demo-architect
description: Use to design the 2–3 minute live demo story (hook, problem, wow, proof, impact) and run the demo-safety checklist before judging.
---

# demo-architect

## Top rules
1. Design the demo before the code is finished. The demo decides what's worth building.
2. Every second on screen must earn a rubric point. Login screens, loading spinners and settings pages earn zero.
3. One wow moment, placed at 40–60% of the demo. Everything before builds to it; everything after proves it.
4. The demo must survive: no Wi-Fi, a dead API, a nervous presenter. Assume all three happen.
5. Rehearse with a timer. Out loud. Three times minimum.

## When to use
- Pitcher at H0–H4 to draft the demo story from the scope card.
- At feature freeze to lock the final demo script.
- 1 hour before judging to run the safety checklist.

## Inputs needed
- SCOPE CARD (demo path, REAL vs MOCKED).
- RECON BRIEF (scoring map, judging format and time per team).
- Who will present and who will drive the laptop.

## Steps

### 1. Story spine (2–3 min total)
| Beat | Time | Content |
|---|---|---|
| Hook | 0:00–0:15 | A specific person, a specific painful moment, or a striking number. No "Hi, we're team X". |
| Problem | 0:15–0:35 | Why it's bad today, one stat or one quote from a real user. |
| Demo setup | 0:35–0:50 | "Meet Priya, she has her exam tomorrow" — then straight into the product. |
| Wow moment | 0:50–1:30 | The thing nobody has seen. Pause after it lands. |
| Proof | 1:30–2:10 | Try it on a fresh input / show it's real / show the tech trail briefly. |
| Impact + ask | 2:10–2:40 | Who benefits, a number, what's next. Name the sponsor tech once, naturally. |

### 2. Map beats to rubric
Next to each beat, write which criterion it scores. If a high-weight criterion has no beat, add one. If a beat scores nothing, cut it.

### 3. Write the click script
Exact clicks, exact inputs, exact lines spoken. Example:
```
[0:50] Click "Start viva". Say: "Priya explains photosynthesis — badly, on purpose."
[0:55] Speak: "Plants take sunlight and make food, and oxygen comes out."
[1:05] App interrupts: "You skipped where the energy is stored. Your notes, page 4, say..." → PAUSE 2s.
[1:15] Gap card appears with page citation. Hover the citation.
```

### 4. Plan the proof
Pick one: a judge's own input, a second unseen document, or a 10-second look at the architecture or retrieval trail. Proof converts "nice video" into "this is real".

### 5. Run the demo-safety checklist
Use `references/demo-safety-checklist.md` in full, 60 minutes before judging and again 10 minutes before.

### 6. Rehearse
- Run 1: read the script. Run 2: from memory. Run 3: with someone interrupting with a question at the wow moment.
- Time each run. If over by 15 s, cut a beat, don't speed up talking.

## Outputs
```
DEMO SCRIPT — <project>   Total: <m:ss>
Presenter: <name>  Driver: <name>
Beats with times, rubric mapping, spoken lines, clicks
Wow moment: <timestamp + line>
Proof: <type>
Fallbacks: <what happens if X fails>
```

## Worked example
VoiceViva, 2:30 slot, rubric Innovation/Technical/Impact/Presentation.
- Hook: "Last night 40 lakh students revised by rereading notes. Rereading is the least effective way to study." (Impact)
- Wow at 1:05: the app interrupts mid-sentence with a page-cited gap. (Innovation)
- Proof at 1:40: a judge says one sentence about any topic in a pre-indexed sample chapter; app finds the gap live. (Technical)
- Impact: "Retrieval practice beats rereading; we turn it into a 5-minute daily habit." Sponsor line: "Every note is embedded and searched in <vector DB>."
- Fallback: if mic fails, type mode; if API fails, cached responses for the scripted lines; if everything fails, play the backup video from 0:50.

## Failure modes
- Opening with the team intro and the tech stack.
- Demoing every feature. Judges remember one.
- Typing slowly on stage. Pre-fill inputs or paste them.
- Wow moment buried at 2:45 after the judge stopped listening.
- No backup video when the venue Wi-Fi dies.

## Hand-off
Script → `pitch-builder` (slides wrap the demo) and `demo-video` (video follows the same spine).
