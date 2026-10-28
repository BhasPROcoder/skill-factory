Read AGENTS.md and SPEC.md.

TASK: Plan the taxonomy for the next 2 macro-areas. Write registry rows only — no skill files.

1. Run `python3 tools/sf.py macros`. Take the first 2 lines marked TODO.
2. Run `python3 tools/sf.py codes` to see codes already used.
3. For each macro-area, design 3–6 domains. Each domain needs:
   - a unique 2–4 letter uppercase `code`
   - `name`, `macro` (exact string from macros.json), `scope` (one sentence, under 25 words), `subdomains` (3–8 strings)
4. For each domain, plan 5–10 skills. Each skill is ONE concrete, repeatable task a user would ask for (e.g. "review an NDA for one-sided clauses"), not a topic ("NDAs"). Cover beginner to expert tasks. Include India- and US-specific variants where the rules differ.
5. Append one JSON line per domain to `registry/domains.jsonl`:
   `{"code":"LAW","name":"Contract Law","macro":"Law & Compliance","scope":"...","subdomains":["..."]}`
6. Append one JSON line per skill to `registry/skills.jsonl`:
   `{"id":"LAW-001","name":"nda-one-sided-clause-review","domain_code":"LAW","subdomain":"...","description":"<what it does>; use when <situation>.","risk_level":"high","requires":[],"status":"planned"}`
   - IDs numbered 001 upward per domain. Names kebab-case and globally unique (prefix with the country code if country-specific).
   - `requires` only lists IDs that exist or that you are adding in this session.
   Append with a small script or `>>`; never rewrite the files.
7. Run `python3 tools/sf.py check-registry`. Fix every error it prints, then run it again until it prints OK.
8. Append to `logs/progress.md`: `- taxonomy: <macro 1>, <macro 2> — <N> domains, <M> skills`.
9. Reply with that same line and stop.
