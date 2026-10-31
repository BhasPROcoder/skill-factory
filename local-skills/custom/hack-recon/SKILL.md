---
name: hack-recon
description: Use at the very start of a hackathon, before any ideation, to parse rules, rubric, tracks, sponsors and prizes into a weighted scoring map and prize-stacking plan.
---

# hack-recon

## Top rules (read at 3 AM)
1. Rubric first, problem statement second. The rubric is what gets rewarded; the problem statement is what they hope gets built.
2. Rules are a filter, not a sort. Violating one disqualifies you. Meeting them earns nothing extra.
3. Every sponsor prize is a separate lottery ticket. One project should qualify for 2–4 of them.
4. Ask of every sponsor: "If they reward this, do they look good in the winners post?"
5. Finish recon in 30 minutes max. Recon that eats the build is failure.

## When to use
- Hackathon has just been announced or kicked off.
- Team is about to brainstorm and nobody has read the judging section.
- A new track or sponsor prize was announced mid-event (re-run step 4 only).

## Inputs needed
Ask for anything missing. Do not guess.
- Hackathon page URL or pasted text (overview, rules, judging, prizes, FAQ).
- Format and duration (24h / 36h / 48h / multi-week online).
- Team size and skills.
- Submission requirements (Devpost, video length, repo, live demo, slides).
- Judging format: science fair, stage pitch, async video only, or mixed.

## Steps

### 1. Extract hard constraints (5 min)
Fill this table. Any "unknown" becomes a question for organizers or the Discord.

| Constraint | Value | Source line |
|---|---|---|
| Submission deadline (local time) | | |
| Code must be written during event? | | |
| Pre-existing code / templates allowed? | | |
| Required tech / sponsor API? | | |
| Team size limit | | |
| Video required? max length? | | |
| Live demo or video-only judging? | | |
| Open source license required? | | |
| Eligibility (student, region, age) | | |

### 2. Build the weighted scoring map (10 min)
Use `references/rubric-scoring-sheet.md`.
- List every criterion with its weight. If weights are not published, assume equal and note it.
- Translate each criterion into "what a judge must SEE in 3 minutes to give full marks".
- Mark the top-weighted criterion as the **anchor**. The idea and demo get designed around it.

Translation rules:
- "Innovation / Creativity" → a moment in the demo nobody has seen before.
- "Technical complexity" → one hard thing visibly working, plus an architecture diagram.
- "Impact / Usefulness" → a named user, a number (time saved, people affected), and a real quote or stat.
- "Design / UX" → a polished happy path; zero raw JSON or console on screen.
- "Completeness / Functionality" → a live end-to-end flow, not screenshots.
- "Use of sponsor tech" → the sponsor API visibly central, not a side call.
- "Presentation" → a rehearsed 2–3 min story with a hook.

### 3. Read judges and sponsors (5 min)
For each judge and sponsor: role, company, what they ship, what they would brag about.
Output one line each: "Sponsor X wins if a project shows their API doing Y for audience Z."

### 4. Prize-stacking plan (10 min)
List every prize and track. For each: requirement, effort to qualify, competition estimate, value.

Decision rules:
- Qualify for the main prize plus every sponsor prize that costs under 1 hour of extra work.
- Prefer niche sponsor prizes with low competition over the crowded "Best AI" track.
- Never bolt on a sponsor API that is not on the demo path. Judges spot it.
- Max 4 prizes. Beyond that the story fragments.

## Outputs
A single recon brief in this exact format:

```
RECON BRIEF — <hackathon name>
Deadline: <local time>   Judging: <format>   Video: <yes/no, length>
Hard rules: <bullets>
Scoring map:
  1. <criterion> (<weight>) — judge must see: <...>  [ANCHOR]
  2. ...
Sponsor angles:
  - <sponsor>: wins if <...>
Prize stack (target): <main> + <sponsor A> + <sponsor B>
Open questions for organizers: <bullets>
```

## Worked example
Input: 36h college AI hackathon. Rubric: Innovation 30%, Technical 25%, Impact 25%, Presentation 20%. Sponsors: a vector DB company (best use of vector search, ₹25k), a voice API company (best voice app, ₹20k). Video 2 min required.

Output excerpt:
```
Scoring map:
  1. Innovation (30%) — judge must see: an interaction no student project usually has  [ANCHOR]
  2. Technical (25%) — judge must see: retrieval + reasoning visibly working on real data
  3. Impact (25%) — judge must see: named user group + a hard number
  4. Presentation (20%) — rehearsed 2 min story, hook in first 10 s
Sponsor angles:
  - Vector DB: wins if their DB is the memory of a product students would actually use
  - Voice API: wins if voice is the primary interface, not a toggle
Prize stack: Main + Vector DB + Voice API (voice-first RAG tutor fits all three)
```

## Failure modes
- Skimming the rubric once, then never looking again. Print the scoring map and pin it.
- Chasing every sponsor prize. Four half-integrations lose to one deep one.
- Missing "must be built during event" and getting disqualified for using an old repo.

## Hand-off
Pass the RECON BRIEF to `idea-forge`.
