---
name: stack-launcher
description: Use when a hackathon project needs a stack chosen and scaffolded, with auth, database and a live deploy running within 45 minutes.
---

# stack-launcher

## Top rules
1. Use the stack the team already ships fastest in. A hackathon is not the place to learn a framework, unless a sponsor prize requires it.
2. Deploy hello world in the first 30 minutes. Deploy pain discovered at H40 kills demos.
3. One repo, one deploy target, one database. Microservices are a pitch slide, not a hackathon architecture.
4. Secrets go in env vars from minute one. A leaked key in a public repo can get you disqualified and billed.
5. Pre-existing boilerplate is allowed only if the rules allow it. Check the recon brief.

## When to use
- Scope card exists and no repo is set up.
- The chosen stack is fighting the team at H4+ and a reset is on the table.

## Inputs needed
- SCOPE CARD (what is REAL determines what infra is needed).
- Rules on pre-existing code.
- Required sponsor SDKs.
- Whether a Python ML backend is needed or JS alone is enough.

## Decision table

| Project shape | Stack | Deploy |
|---|---|---|
| Web app + LLM calls, no heavy ML | Next.js + TypeScript + Supabase + Claude API | Vercel |
| Web app + RAG over documents | Next.js front + Supabase (pgvector) or Qdrant Cloud; embeddings via API | Vercel |
| Python-heavy ML / custom models | FastAPI backend + Next.js or Streamlit front | Render/Railway (API) + Vercel (front) |
| Data demo, judges just need to see output | Streamlit or Gradio | Streamlit Cloud / HF Spaces |
| Mobile-first | Expo (React Native) + Supabase | Expo Go QR for demo |
| Chat-surface product | WhatsApp/Telegram bot + FastAPI | Render/Railway |
| Browser extension | Plasmo or plain MV3 + small API | Load unpacked for demo |

Constraint: local GPU is 6GB VRAM. Run embeddings and LLMs via API. Local models only for small embedding jobs done before the demo.

## Steps

### 1. Scaffold (15 min)
Default stack: see `templates/nextjs-supabase-claude.md`.
AI/RAG variant: see `templates/rag-variant.md`.

### 2. Deploy hello world (10 min)
- Push to GitHub, import into Vercel, set env vars, get the live URL.
- Paste the URL in the team channel. This URL is the demo URL from now on.

### 3. Wire the three services (15 min)
- DB: one table that the demo path needs, created via SQL migration file in the repo.
- Auth: skip unless REAL. Default is a hardcoded demo user.
- LLM: one server route that calls the model with a test prompt and returns text. Hit it from the deployed URL.

### 4. Add repo hygiene (5 min)
- `.env.example` with every key name, no values.
- README stub: one-line pitch, live URL, how to run.
- `seed` script stub.
- Branch rule: main always deploys and always works.

## Outputs
```
STACK READY — <project>
Repo: <url>   Live: <url>
Stack: <list>
Env keys: <names only>
Smoke test: DB read ✓ / LLM call ✓ / deploy ✓
Known gaps: <...>
```

## Worked example
VoiceViva → RAG variant. 40 minutes:
- `create-next-app`, Supabase project with pgvector, Claude API route, Deepgram/Web Speech for STT.
- Deployed at H0:50. Smoke test passed. Embeddings computed via API for two seed PDFs and stored with a seed script.

## Failure modes
- Local-only dev until H30, then Vercel build fails on a type error.
- Self-hosting a vector DB in Docker on a laptop. Use a managed free tier.
- Committing `.env`. Rotate the key immediately if it happens.
- Picking a new framework "because it's fast". It is fast for people who know it.

## Hand-off
Builders move to `build-sprint`. AI-heavy features go through `ai-feature-kit`.
