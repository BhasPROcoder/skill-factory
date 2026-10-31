---
name: demo-video
description: Use to plan, script, record and edit the 2–3 minute hackathon submission video: shot list, narration, timing, and export settings.
---

# demo-video

## Top rules
1. The video is often the only thing async judges and sponsors see. It's the asset the sponsor shares in the winners post. Treat it as a deliverable, not a chore.
2. Respect the max length to the second. Over-length can mean disqualification or the judge stopping early.
3. Product on screen within 15 seconds.
4. Clear audio beats pretty visuals. A bad mic ruins a great project.
5. Record a backup cut at feature freeze. Record the final cut by 3 hours before deadline. Upload takes longer than you think.

## When to use
- Feature freeze reached, or a backup recording is needed.
- Submission requires a video (most Devpost events do).

## Inputs needed
- DEMO SCRIPT (spine and wow moment).
- Max length and platform rules (YouTube / Vimeo / direct upload, public or unlisted).
- Recording tools available (OBS, Loom, QuickTime, phone).
- Whether faces on camera are wanted (optional; a short face intro adds trust).

## Steps

### 1. Shot list (15 min)
| # | Time | Visual | Audio |
|---|---|---|---|
| 1 | 0:00–0:10 | Title card or hook visual (bold text, 1 line) | Hook line |
| 2 | 0:10–0:25 | Problem: user photo/stock-free illustration or stat card | Problem + stat |
| 3 | 0:25–0:40 | App landing, one click into the flow | "Meet <user>…" |
| 4 | 0:40–1:20 | Screen recording of wow moment, zoom on key area | Narration, 1 pause |
| 5 | 1:20–1:50 | Proof: second input or reasoning panel | "It's live on any document…" |
| 6 | 1:50–2:15 | Architecture diagram, sponsor tech highlighted | 2 sentences on how |
| 7 | 2:15–2:30 | Impact number + what's next | Close line |
| 8 | 2:30–2:40 | End card: name, live URL, repo, team | Silence or short music sting |

### 2. Narration script
- Reuse the pitch script; tighten to fit the shot timings.
- 140–150 words per minute. A 2:30 video ≈ 350 words max.
- Record voice separately from screen if possible, so retakes are cheap.

### 3. Record
- Screen: 1920×1080, browser at 110–125% zoom, hide bookmarks bar, close notifications, use a clean demo account.
- Cursor: enable highlight if available; move slowly; no frantic scrolling.
- Audio: closest decent mic (phone earbuds beat laptop mic), quiet room or a hoodie-covered corner; record 5 s of silence for noise reduction.
- Do each shot as a separate clip.

### 4. Edit (45–60 min)
- Tools: DaVinci Resolve, CapCut desktop, iMovie, or Descript for text-based editing.
- Cut dead air and loading time. Speed up waits 2–4× with a small "⏩" label.
- Zoom (Ken Burns / scale keyframes) on the exact UI area during the wow moment.
- Captions on. Many judges watch muted.
- Background music at −25 to −30 dB under voice, royalty-free only.
- Export H.264 MP4, 1080p, 30 fps.

### 5. Upload and verify
- Upload as unlisted or public per rules. Open the link in an incognito window to confirm it plays.
- Paste the link into the submission draft immediately.

## Checklist
- [ ] Under max length
- [ ] Product visible by 0:15
- [ ] Wow moment zoomed and paused
- [ ] Captions present
- [ ] Sponsor tech named on screen and in audio
- [ ] Live URL and repo on end card
- [ ] Plays in incognito
- [ ] No API keys, emails or private data visible in any frame

## Outputs
- `video-script.md` (shot list + narration).
- Final MP4 and uploaded link.
- Backup cut from freeze time.

## Worked example
VoiceViva, 2:00 max. Cut shot 6 to 10 s (diagram only), merged 2 and 3. Final 1:56. Wow moment: the interruption with a 2× zoom on the citation chip and a 1.5 s silent pause. Captions burned in. Uploaded unlisted on YouTube at H33; incognito check passed.

## Failure modes
- Recording the full 3 minutes in one take at H47 and running out of time.
- Laptop mic in a noisy hall.
- Showing the code editor for 40 seconds.
- Exceeding the limit by 20 seconds.
- Leaking an API key in a terminal shot.

## Hand-off
Link → `submission-writer`.
