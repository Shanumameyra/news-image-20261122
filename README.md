# news-image-20261122

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Shanumameyra/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Shanumameyra/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

make.fun bounty entry: **Sum up 22 November's world news in one image**
(Sunday 22 November 2026). Prize pool $100, top 50 entries share it.

## The image

`entry.png` (1024×1024, ~150 KB) is a one-page front page drawn in code
with Python/PIL (`draw_image.py`, included): a navy masthead naming the day
— **WORLD NEWS, SUNDAY 22 NOVEMBER 2026** — a lead story, and nine more
tiles covering the day's most consequential stories across regions and
fields: the Middle East, Mexico, climate, markets, cyber, Ukraine,
international justice, Nigeria, Indonesia and South Korea.

## The day's stories (all verified against 22 Nov 2026 reporting)

1. **Iran strikes Bahrain; tankers hit in the Strait of Hormuz** — Bahrain
   said a civilian site was struck; two tankers hit near the strait.
2. **Mexico captures 'El Chapo Isidro'** — cartel boss Fausto Isidro Meza
   Flores held in a Sinaloa raid; 11 killed.
3. **COP31 deadlocked over fossil fuels** — climate summit in Antalya runs
   into overtime.
4. **AI sell-off pushes US stocks into correction** — S&P 500 −3.7%,
   Nikkei −5.1%.
5. **FBI crime database hacked** — bureau probes a breach of its national
   criminal records (NCIC).
6. **Russia hits Zelenskyy's hometown** — Kryvyi Rih strike kills 2,
   wounds dozens.
7. **UN court: Myanmar committed genocide** — judges rule on the Rohingya;
   sanctions urged.
8. **Nigeria boat capsizes; 24 dead** — boat carrying funeral mourners
   sinks in the south.
9. **Indonesia factory fire; 36 missing** — candy plant blaze in Banten
   kills 3.
10. **South Korea education minister resigns** — quits over an
    exam-cheating scandal.

Two widely repeated items were deliberately left out after date checks:
the Trump–Xi–Putin trilateral summit in Shenzhen happened on **19 Nov**,
and the magnitude 6.7 Peru earthquake struck on **20 Nov** — neither is
22 November news.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`). No network at runtime;
two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
