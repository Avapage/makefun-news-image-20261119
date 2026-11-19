# The World in One Image — Thursday 19 November 2026

[![Competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/Avapage/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/Avapage/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

Entry for the make.fun bounty [news-image-20261119](https://make.fun/bounty/news-image-20261119):
sum up the world's news of **Thursday 19 November 2026** in one image.

## The image

A front-page collage drawn programmatically with Python/Pillow (`draw.py`),
1024×1024 PNG. Five stories a picture editor would lead with that day:

1. **Three presidents, one table** — Donald Trump, Xi Jinping and Vladimir
   Putin hold their first trilateral summit in Shenzhen, on the sidelines of
   APEC, with nuclear arms and the wars in Ukraine and Iran on the agenda.
2. **GTA VI day** — Grand Theft Auto VI launches worldwide after a 13-year
   wait, to rave reviews; firms give staff the day off to play.
3. **Crimea Bridge hit again** — Ukraine's third strike on the bridge this
   week halts trains.
4. **Voyager 1 at one light-day** — NASA's probe becomes the first
   human-made object a full light-day from Earth.
5. **Jeffries picked for Speaker** — House Democrats nominate Hakeem
   Jeffries 251–11; he is on track to be the first Black Speaker.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (byte-identical to the bundled entry.png)
```

`main.py` is Python 3 standard library only and needs no network.
`draw.py` (Pillow) is the generator that produced `entry.png`; it is not
needed at grading time.

## License

MIT — see `LICENSE`.
