# Build log, news-image-20261120

Built 20 November 2026. A newspaper front page summing up the world news of Friday 20 November 2026 in six panels.

## Brief

Competition news-image-20261120, "Sum up 20 November's world news in one image". One 1024 by 1024 PNG, at most 1 MiB, six panels in a 3 by 2 grid. The program is main.py, Python standard library only, and copies entry.png to the output directory. No network, no randomness, both grader runs byte-identical.

## Stories

The six stories were supplied already researched and verified for 20 November 2026: Trump delaying the Iran war decision to 2027, Voyager 1 passing one light-day, Cyclone Akvan making landfall in Odisha with 300,000 evacuated, Europe ready for talks with Russia, GTA 6 sales passing $1.8 billion, and the Houthi strike on Riyadh damaging the Saudi wealth fund tower. No casualty figures anywhere. The ICJ Myanmar ruling was deliberately left out, since it was 19 November news, not 20 November.

## Generation

Six flat editorial illustrations were generated, one per story, each prompted with no text, no words, no letters, no numbers. All six were read back visually and passed on the second generation round: Washington (White House, blank calendar, clock, figure at a desk), Space (golden probe crossing a dashed marker line), India (cyclone spiral over a coastal town with evacuees), Europe (round table handshake under EU and Russian flags), Gaming (neon tropical city with a game controller and a sports car), Gulf (Riyadh skyline, damaged tower, smoke, streaks of light). The first generation round was lost to a bad bulk rename that overwrote the image files with their sidecar files, so all six were regenerated and renamed one file at a time.

## Compose

A build-time only compose script (PIL) drew the page on the layout pattern of the 19 November entry: cream paper, serif masthead THE WORLD TODAY, date FRIDAY 20 NOVEMBER 2026, double rule, 3 by 2 grid, each panel a centre-cropped illustration above a red tag, bold headline, and one line sub-caption, all text in DejaVu. Headline and sub-caption sizes are adaptive, one shared size each, stepping down until every text fits two lines, and the script asserts no panel overflows.

## Self-review

First compose: all six headlines and sub-captions spelled exactly, no garbled or cut-off text, no overflow, but the Space panel was mostly empty sky with a tiny probe, and the text areas had a large empty gap at the bottom. Fix: the image height grew from 218 to 258 pixels, and the Space illustration is cropped to the band around the probe before fitting. Second compose: Voyager is prominent, all text exact, every illustration matches its caption, no defects left. Final entry.png is 1024 by 1024, 649998 bytes.

## main.py

Written fresh from scratch, standard library only. It validates entry.png (PNG magic, IHDR chunk present with length 13 and non-zero dimensions, width and height each at most 1024, size at most 1048576 bytes), copies it to $MAKEFUN_OUTPUT_DIR or /output, then re-reads the output file's own PNG header and asserts its sha256, size, and dimensions equal the source. A second pass added the IHDR length check, the zero-dimension check, and a clear error when the source file is missing.

## Test results

- `python3 -m py_compile main.py`: passed.
- Ran main.py twice to two separate output dirs: outputs byte-identical (cmp clean), sha256 equal to the source in both runs.
- Output confirmed 1024 by 1024 and under 1 MiB.
- Negative test, non-PNG file: rejected with ValueError naming the file.
- Negative test, 1200 by 1200 PNG: rejected with ValueError naming the file.

## Cleanup

The assets directory and the compose script were deleted from the repo after composing. A copy of the compose script is kept at /tmp/news-image-20261120-compose.py for reference. The repo ends with exactly entry.png, main.py, README.md, LICENSE, and BUILD_LOG.md. Nothing was committed, submitted, or bundled.
