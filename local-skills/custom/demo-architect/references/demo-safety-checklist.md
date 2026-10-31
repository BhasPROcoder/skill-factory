# Demo Safety Checklist

Run 60 minutes before judging. Run sections D and E again 10 minutes before.

## A. Environment
- [ ] Demo runs on the deployed URL, not localhost (unless judging requires local).
- [ ] Phone hotspot tested with the demo laptop; data balance enough for 1 h.
- [ ] Laptop charged > 80%, charger and adapter (HDMI/USB-C) in the bag.
- [ ] Display mirroring tested on an external screen or projector if one is available.
- [ ] Browser: fresh profile or guest window, bookmarks bar hidden, extensions off, zoom 110–125%.
- [ ] Notifications off (OS do-not-disturb, Slack/Discord/WhatsApp quit).
- [ ] Only demo tabs open, in click order.

## B. Data and accounts
- [ ] Demo account pre-logged-in; session won't expire in the next 2 hours.
- [ ] `npm run seed` (or equivalent) run; demo state is the "before" state.
- [ ] Demo inputs saved in a text file for paste, not typed live.
- [ ] Judge-try inputs written on a card (2–3 safe ones).
- [ ] No personal data, emails or API keys visible anywhere on screen.

## C. Reliability
- [ ] Demo path run 3× in a row on the deployed URL without touching code.
- [ ] AI cache warmed for every scripted input; cache persists across restarts.
- [ ] Every external call has a timeout + fallback; tested by turning Wi-Fi off once.
- [ ] Sponsor API status page checked.
- [ ] Rate limits: enough credits/quota left for 20+ runs.
- [ ] Last good build tagged; rollback command written down.

## D. Fallback ladder (know who does what)
1. Live call slow → keep talking, cache returns at timeout.
2. Feature fails → switch to the typed/simpler path for that step.
3. Deploy down → run localhost build (already started in a background terminal).
4. Laptop or network dead → play backup video from the wow moment timestamp (file on desktop AND phone).
5. Everything dead → slides + screenshots, presenter narrates the flow. Still finish the story and the ask.

## E. People
- [ ] Presenter and driver decided; driver knows every click.
- [ ] Timer running on a phone visible to the presenter.
- [ ] Q&A owners assigned by topic.
- [ ] Everyone knows the one sentence answer to "what's mocked?".
- [ ] Water nearby. Speak slower than feels natural.
