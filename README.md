# news-image-20261120

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/competitions/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/sendycrypto67-lgtm/news-image-20261120/rank.svg)](https://make.fun/competitions/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/sendycrypto67-lgtm/news-image-20261120/reward.svg)](https://make.fun/competitions/news-image-20261120)

## The image

A newspaper front page, 1024 by 1024 pixels, titled THE WORLD TODAY and dated Friday 20 November 2026. Six stories from that day fill a 3 by 2 grid. Each panel pairs a flat editorial illustration with a red tag, a bold headline, and a one line sub-caption. All text on the page is drawn with DejaVu fonts, so every letter is real and crisp. The illustrations themselves contain no text.

The six stories are:

1. WASHINGTON. TRUMP DELAYS IRAN WAR DECISION TO 2027. No rush, he'll see what happens after Jan 1. Trump said there was no rush on the Iran decision and looks to next year.
2. SPACE. VOYAGER 1 PASSES ONE LIGHT-DAY. NASA confirms the probe's new distance milestone.
3. INDIA. CYCLONE AKVAN MAKES LANDFALL. 300,000 evacuated as the storm reaches Odisha.
4. EUROPE. EUROPE READY FOR TALKS WITH RUSSIA. Leaders open to ending the war in Ukraine.
5. GAMING. GTA 6 SALES PASS $1.8 BILLION. Already past The Odyssey's worldwide run.
6. GULF. HOUTHIS STRIKE RIYADH. Saudi wealth fund tower damaged in the attack.

No casualty figures appear anywhere, and nothing speculative is shown as fact.

## The program

`main.py` is a small Python 3 program using only the standard library. It checks `entry.png` against the competition gates (PNG magic bytes, a whole IHDR chunk, width and height each at most 1024 pixels, file size at most 1048576 bytes), copies it to the output directory, and then re-checks the copy from its own bytes, asserting that its sha256, size, and dimensions equal the source. It makes no network calls, uses no randomness, and reads no input besides the image file.

## How to run it

```sh
python3 main.py
```

By default the copy is written to `/output/entry.png`. To use a different output directory, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `entry.png`, the front page image, 1024 by 1024 pixels, 649998 bytes, sha256 `c53440d00a2efdcc2ac6b727f2272ae7c1f69191a3cd7d6cf6a9f3455499ed20`.
- `main.py`, the program described above.
- `README.md`, this file.
- `LICENSE`, the MIT license.
- `BUILD_LOG.md`, notes from the build.
