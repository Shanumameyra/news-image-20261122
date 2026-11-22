# Build record — news-image-20261122

## Bounty (verified from the make.fun API, 22 Nov 2026)
- Bounty: `news-image-20261122` — "Sum up 22 November's world news in one image"
- Page: https://make.fun/bounty/news-image-20261122
- Status: open, acceptingSubmissions: true
- Opens: 2026-11-22T00:00:00Z (22 Nov 2026 07:00 WIB)
- Deadline: 2026-11-24T00:00:00Z (Tue 24 Nov 2026 07:00 WIB)
- Prize: $100 total, top 50 — 1st $20, 2nd $12, 3rd $6, 4–10 $2, 11–50 $1.20
- Entry fee: none (entryFeeUsd null) — no payment, key or deposit needed
- Baseline: none (AI-judge pairwise contest; house images are from 13 Nov 2026)
- Account: make.fun @rapid-pika-70 (never @romi-prayoga)
- GitHub: Shanumameyra
- Quota endpoint requires sign-in; checked at build time via the public API
  (status open, submissionCount ~10,430 at build time).

## Session
- Builder session started: 22 Nov 2026 ~20:49 WIB — after the competition
  opened (07:00 WIB). All work in this session falls inside the window.
- Previous days' entry folders (news-image-20261118/19/20/21) were NOT read
  or copied; this entry was built fresh from the bounty spec + news research.

## News research (22 Nov 2026, web search, news vertical)
Sources: OneTurn world-news roundup 22 Nov; TFI Online 22 Nov roundup;
WPXI/AP world list 22 Nov; Seven Lights (Indonesia factory fire, 22 Nov);
EIN Presswire live feed 22 Nov; Cognoscere brief 22 Nov; Daily Perspective
22 Nov; WSJ/AP/NY Post (trilateral date check); Al Jazeera + INDECI reports
(Peru quake date check).
- 10 stories selected, all events happened or first reported 22 Nov 2026.
- Date-check exclusions: Trump–Xi–Putin trilateral summit was 19 Nov 2026
  (WSJ/AP/NY Post); Peru M6.7 quake struck 20 Nov 2026 (IGP/INDECI) — both
  left out even though 22 Nov roundups mentioned them.

## Image build
- Tool: Python 3 + PIL 10.2.0, DejaVu fonts; script `draw_image.py`
  (included in the repo) draws the 1024×1024 front page in code.
- Layout: navy masthead with date, lead story card, 3×3 story grid with
  flat icon glyphs, navy footer repeating the date.
- Layout assertions in the script (no text overflows a card; footer fits)
  pass. Image verified visually at full size and at 300 px (still legible:
  title, date, lead headline and tile headlines read clearly).
- entry.png: 1024×1024, RGB, 153,741 bytes (limit 1,048,576).

## Program
- `main.ts` (Node 22, stdlib only): copies entry.png to
  `$MAKEFUN_OUTPUT_DIR` (default /output). No network. Deterministic
  (pure copy).

## Checks (run 22 Nov 2026 ~20:55 WIB — ALL PASS)
- [x] PNG signature valid + whole-file validity (PIL verify passed)
- [x] Dimensions 1024×1024 (limit 1024×1024)
- [x] Size 153,741 bytes (limit 1,048,576)
- [x] Determinism: main.ts run twice → identical sha256
      `653487bd6ff1f680d0c0950bea479f4687d7c0bff54f328b26d7ebcccdfd8768`
      (also matches repo entry.png)
- [x] No network use in main.ts (pure file copy)
- [x] Repo pushed: https://github.com/Shanumameyra/news-image-20261122
      commit `1659d7617b27ee46307ce48a0cca94eb396c8983` (main)
- [ ] Submit — NOT done by this builder; parent handles submission.

## Submit command (for the parent)
From the kit directory (`~/workspace/makefun/news-image-20261122-work/news-image-20261122-kit`):
1. Bundle transcripts first (see kit RULES.txt, Enter step 3).
2. `node cli/makefun.mjs check --kit . --repo Shanumameyra/news-image-20261122 --transcripts transcripts.tar.gz`
3. Submit via the CLI per kit RULES.txt (Enter step 4/5) with the
   @rapid-pika-70 API key.
