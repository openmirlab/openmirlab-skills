# MIR landscape

A different question from "what should openmirlab build next": this file
asks **"is this worth using, full stop?"** — and most of what belongs here
will never need rescuing, because it's already well-maintained (`librosa`
isn't going anywhere; that's exactly why it belongs on a "what to use"
list rather than a modernization to-do list).

Scaffold only for now (2026-07-12) — structure and format decided, seeded
with a few extremely well-known anchors to prove the shape out, everything
else deliberately left as an empty stub rather than filled from memory. A
real pass (survey each task category, verify every entry) is future work,
not done here.

Dashboard, not law — updates freely, no ceremony required.

## The one hard rule

This file is a set of **recommendations**, not just leads to chase, so the
verification bar is high. Every entry's license and maintenance status
must be checked against a primary source
(`gh api repos/X/Y --jq '{license: .license.spdx_id, pushed_at, archived}'`,
or the project's own docs for non-GitHub projects) at add time, with the
date recorded. An entry nobody has re-checked in a long time is a claim
that's aging, not a live fact — re-verify before recommending it to
someone, don't just relay what's written here.

## Entry format

```
- **Name** ([link](url)) — license, verified <date>. What it does, why
  it's notable or distinctive. Maturity: Active / Maintenance-mode /
  Stalled / Archived. openmirlab overlap: none / partial (`pkg-name`) /
  superseded by (`pkg-name`). **Recommendation**: one line.
```

- **Active**: recent commits, responsive to issues/PRs.
- **Maintenance-mode**: still gets releases, but slow-moving — fine to
  depend on, don't expect fast bug turnaround.
- **Stalled**: no clear activity in a long while, not formally abandoned —
  usable today, but a real risk for anything long-lived. A stalled-but-
  valuable tool is exactly the kind of thing worth flagging clearly here
  as "usable with caution," even if nobody's actively picking it up.
- **Archived**: upstream has explicitly stopped. Still might be worth
  using if it's finished and stable; say so if it is.

## General-purpose DSP / feature-extraction toolkits

- **librosa** ([librosa/librosa](https://github.com/librosa/librosa)) —
  ISC, verified 2026-07-12 (pushed within the last two days at verification
  time, 8.5k stars). The default choice for audio feature extraction in
  Python — STFT/mel/chroma/onset/tempo primitives, widely taught and cited.
  Maturity: **Active**. openmirlab overlap: none — general toolkit, not a
  specific model. **Recommendation**: default starting point for anyone
  doing audio-domain feature engineering in Python; not a source-separation
  or transcription tool itself.
- **essentia** ([MTG/essentia](https://github.com/MTG/essentia)) —
  AGPL-3.0, verified 2026-07-12 (pushed within the last month, 3.6k stars).
  C++ core with Python bindings from the Music Technology Group (UPF,
  Barcelona) — broader algorithm coverage than librosa in places (rhythm,
  tonal, high-level descriptors) and faster, at the cost of a heavier
  install and a copyleft license. Maturity: **Active**. openmirlab overlap:
  none directly, though several openmirlab packages reimplement individual
  algorithms essentia also has (e.g. beat tracking). **Recommendation**:
  reach for it when you need an algorithm librosa doesn't have or need the
  C++ performance — but AGPL-3.0 is a real constraint, check it fits before
  depending on it in anything redistributed.

## Evaluation & benchmarking

- **mir_eval** ([craffel/mir_eval](https://github.com/craffel/mir_eval)) —
  MIT, verified 2026-07-12 (pushed ~5 months before verification, 706
  stars — slower-moving than the two above but not stalled). The standard
  reference implementation for MIR evaluation metrics (onset/beat/chord/
  segmentation/melody/separation scoring) — used to score research output,
  the mirror-image of what openmirlab's own `-infer` packages deliberately
  exclude by design (they ship inference only, never eval-metric code).
  Maturity: **Maintenance-mode**. openmirlab overlap: none —
  openmirlab packages are inference-only by design and don't ship
  evaluation code; this is exactly the tool you'd reach for to score their
  output yourself. **Recommendation**: the correct tool when you need to
  measure MIR output against ground truth, not just produce it.

## Source separation

_No entries logged yet — openmirlab's own toolbox already covers this task
well (demucs-infer, bs-roformer-infer, melband-roformer-infer, mdxnet-infer)
so a landscape pass here should focus on what's notable *outside* that
lineup._

## Music transcription

_No entries logged yet._

## Beat / tempo / structure

_No entries logged yet._

## Chord / key recognition

_No entries logged yet._

## Tagging / classification

_No entries logged yet._

## Symbolic / MIDI processing

_No entries logged yet._

## Generation / synthesis

_No entries logged yet._
