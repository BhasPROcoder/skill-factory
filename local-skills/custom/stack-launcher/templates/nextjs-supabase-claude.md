# Template: Next.js + Supabase + Claude (default stack)

## Scaffold
```bash
npx create-next-app@latest app --ts --tailwind --eslint --app --src-dir --use-npm --no-import-alias
cd app
npm i @supabase/supabase-js @anthropic-ai/sdk zod
npx shadcn@latest init -d
npx shadcn@latest add button card input textarea badge skeleton sonner
```

## Env
`.env.local`
```
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
ANTHROPIC_API_KEY=
DEMO_MODE=false
```
Copy key names (no values) into `.env.example`.

## Supabase client
`src/lib/supabase.ts`
```ts
import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

export const supabaseAdmin = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);
```

## Claude route
`src/app/api/ai/route.ts`
```ts
import Anthropic from "@anthropic-ai/sdk";
import { NextResponse } from "next/server";

const client = new Anthropic();

export async function POST(req: Request) {
  const { prompt } = await req.json();
  const msg = await client.messages.create({
    model: process.env.CLAUDE_MODEL ?? "claude-sonnet-4-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: prompt }],
  });
  const text = msg.content.map((b) => (b.type === "text" ? b.text : "")).join("");
  return NextResponse.json({ text });
}
```
Set `CLAUDE_MODEL` to whatever current model your account has; check the Anthropic docs at the event.

## First migration
`supabase/migrations/0001_init.sql`
```sql
create table if not exists items (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz default now(),
  user_id text not null default 'demo',
  data jsonb not null
);
```

## Seed script
`scripts/seed.ts`
```ts
import { supabaseAdmin } from "../src/lib/supabase";

const rows = [
  { data: { title: "Sample 1" } },
  { data: { title: "Sample 2" } },
];

async function main() {
  await supabaseAdmin.from("items").delete().eq("user_id", "demo");
  const { error } = await supabaseAdmin.from("items").insert(rows);
  if (error) throw error;
  console.log("seeded", rows.length);
}

main();
```
Run: `npx tsx scripts/seed.ts` (install `tsx` and `dotenv` if needed; load `.env.local`).

## Deploy
```bash
git init && git add -A && git commit -m "init"
gh repo create <name> --public --source=. --push
```
Import the repo in Vercel, paste env vars, deploy. Hit `/api/ai` from the live URL with a test POST before writing features.
