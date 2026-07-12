# mir — using the openmirlab toolbox

User-facing capability map for openmirlab's published packages. This file is a
ROUTER and a CACHE: it maps "what you want to do with audio/music" to the
right package, but ground truth lives in each repo's own README — read those
at answer time, never answer from this file alone. Entries reflect the state
at the last-verified date below; treat older claims as hints to re-check.

Last verified: 2026-07-12 (24-repo README/CLAUDE.md sweep; confirmed publish
status per-repo via each README's own PyPI badge / private-track notice,
not from memory).

## Capability map

Only packages a user outside the org can actually install are listed here
(PyPI or a public GitHub repo). A separate set of research/derivative
packages exists but stays private for now (no license clearance to
redistribute, or a pending user call) — those aren't listed, since pointing
someone at a repo they can't reach isn't a real recommendation.

| You want to… | Package | Install | Notes |
|---|---|---|---|
| Analyze song structure (tempo/BPM, beats, downbeats, segments like verse/chorus) | `all-in-one-infer` | `pip install all-in-one-infer` | Includes built-in source separation (demucs-infer) and beat tracking (madmom-infer, plain PyPI dep now — the old git-madmom workaround is gone); GPU recommended, CPU/macOS work |
| Beat/downbeat/onset DSP primitives (modernized madmom) | `madmom-infer` | `pip install madmom-infer` | Published. numpy backend is the bit-identical-verified reference; optional differentiable torch frontend via `madmom-infer[torch]` |
| Separate a song into stems (vocals/drums/bass/other) | `demucs-infer` | `pip install demucs-infer` | The general-purpose workhorse (HTDemucs) |
| Separate vocals with SOTA community models | `bs-roformer-infer` / `melband-roformer-infer` | `pip install bs-roformer-infer` · `pip install melband-roformer-infer` | Multiple registry models per package (vocals/instrumental/dereverb variants) — see each README's model table |
| Separate a mix with an alternative multi-stem / drum-focused model | `mdxnet-infer` | `pip install git+https://github.com/openmirlab/mdxnet-infer` | Public GitHub, not yet on PyPI. MDX23C TFC-TDF, includes a DrumSep checkpoint |
| Transcribe music to MIDI (multi-instrument) | `mt3-infer` | `pip install mt3-infer` | Wraps 3 independent MT3 ports (MR-MT3/MT3-PyTorch/YourMT3) behind one API — see README for which backend fits |
| Transcribe to lead sheet (melody + chords) | `sheetsage-infer` | `pip install sheetsage-infer` | Now installs cleanly via plain pip (`madmom-infer>=0.1.0` replaced the old git dep) |
| Recognize chords (large vocabulary) | `lv-chordia` | `pip install lv-chordia` | Bundles its own ~28MB weight ensemble in the wheel (documented size-based exception — no separate download step) |
| Tag/classify music audio (genre/mood/instruments) | `maest-infer` | `pip install maest-infer` | AGPL-3.0 — check license fit |
| Synthesize guitar audio from control signals (DDSP) | `ddsp-guitar-infer` | `pip install git+https://github.com/openmirlab/ddsp-guitar-infer` | Public GitHub, not yet on PyPI. String-wise DDSP synth |
| Generate audio continuations (research) | `jukebox-infer` | `pip install jukebox-infer` | Large checkpoints (~6.2GB); 5b/5b_lyrics model sizes are present but unused/untested internally — stick to the default unless you've verified them yourself |

## Ground rules for helping users

- **Weights download at first use** (never bundled): first run needs network +
  disk; cache locations and model choices live in each repo's README.
- **License layering**: package code is permissive, but some model WEIGHTS
  carry non-commercial licenses. If the user hints at commercial use, check
  the specific model's weights license before recommending.
- **Pipelines compose**: common chains — separate first, then analyze
  (demucs-infer → all-in-one-infer does this internally); separate → transcribe
  per-stem (demucs-infer → mt3-infer) improves transcription of dense mixes.
- **Version floors matter**: recommend the latest release; known-broken floors
  are listed in the map above.
