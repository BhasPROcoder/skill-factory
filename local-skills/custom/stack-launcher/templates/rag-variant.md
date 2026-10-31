# Template: AI / RAG variant

Use when the wow moment depends on answering from a specific document set.

## Choice of vector store
| Option | When |
|---|---|
| Supabase pgvector | Already using Supabase, < 100k chunks. Default. |
| Qdrant Cloud free tier | Need hybrid search filters, sponsor is Qdrant, or > 100k chunks. |

Embeddings: call an embedding API, or run BGE-M3 locally only for the one-time seed job (6GB VRAM is enough for batch encoding at small batch size). Never run the embedding model live during the demo on a laptop.

## pgvector setup
`supabase/migrations/0002_rag.sql`
```sql
create extension if not exists vector;

create table if not exists chunks (
  id bigserial primary key,
  doc_id text not null,
  page int,
  content text not null,
  embedding vector(1024)
);

create index if not exists chunks_embedding_idx
  on chunks using hnsw (embedding vector_cosine_ops);

create or replace function match_chunks(q vector(1024), k int)
returns table (id bigint, doc_id text, page int, content text, score float)
language sql stable as $$
  select id, doc_id, page, content, 1 - (embedding <=> q) as score
  from chunks
  order by embedding <=> q
  limit k;
$$;
```
Set the vector dimension to match your embedding model.

## Ingest (Python, one-time)
`scripts/ingest.py`
```python
import os, sys, json
from pypdf import PdfReader
from supabase import create_client

sb = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"])

def chunks(path, size=800, overlap=150):
    r = PdfReader(path)
    for i, p in enumerate(r.pages):
        t = (p.extract_text() or "").strip()
        s = 0
        while s < len(t):
            yield i + 1, t[s:s + size]
            s += size - overlap

def embed(texts):
    from sentence_transformers import SentenceTransformer
    m = embed.m if hasattr(embed, "m") else SentenceTransformer("BAAI/bge-m3", device="cuda")
    embed.m = m
    return m.encode(texts, batch_size=8, normalize_embeddings=True).tolist()

for path in sys.argv[1:]:
    doc = os.path.basename(path)
    rows = list(chunks(path))
    vecs = embed([c for _, c in rows])
    sb.table("chunks").insert([
        {"doc_id": doc, "page": p, "content": c, "embedding": v}
        for (p, c), v in zip(rows, vecs)
    ]).execute()
    print(doc, len(rows))
```
For live user uploads during the demo, use an embedding API instead of the local model so the deployed app works without your laptop.

## Retrieval + answer route
`src/app/api/ask/route.ts`
```ts
import Anthropic from "@anthropic-ai/sdk";
import { supabaseAdmin } from "@/lib/supabase";
import { embedQuery } from "@/lib/embed";

const client = new Anthropic();

export async function POST(req: Request) {
  const { question } = await req.json();
  const q = await embedQuery(question);
  const { data: hits } = await supabaseAdmin.rpc("match_chunks", { q, k: 6 });
  const context = (hits ?? [])
    .map((h: any, i: number) => `[${i + 1}] (${h.doc_id} p.${h.page}) ${h.content}`)
    .join("\n\n");
  const msg = await client.messages.create({
    model: process.env.CLAUDE_MODEL ?? "claude-sonnet-4-5",
    max_tokens: 800,
    system: "Answer only from the numbered sources. Cite like [2]. If the sources don't cover it, say so.",
    messages: [{ role: "user", content: `Sources:\n${context}\n\nQuestion: ${question}` }],
  });
  const text = msg.content.map((b) => (b.type === "text" ? b.text : "")).join("");
  return Response.json({ text, sources: hits });
}
```

## Demo-visible RAG polish
- Show citations as clickable chips that open the source page. Judges trust what they can verify.
- Show retrieved chunks in a collapsible "Why this answer" panel. This scores technical points cheaply.
- Pre-index the demo documents. Live-upload one small file to prove it's real.
