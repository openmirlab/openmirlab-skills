# mir — using the openmirlab toolbox

User-facing capability map for openmirlab's published packages. This file is a
ROUTER and a CACHE: it maps "what you want to do with audio/music" to the
right package, but ground truth lives in each repo's own README — read those
at answer time, never answer from this file alone. Entries reflect the state
at the last-verified date below; treat older claims as hints to re-check.

Last verified: 2026-07-22 (Demucs checkpoint/model-selection refresh; other
package publish status remains from the 2026-07-15 README/CLAUDE.md sweep,
confirmed per-repo rather than from memory).

## Capability map

Only packages a user outside the org can actually install are listed here
(PyPI or a public GitHub repo). A separate set of research/derivative
packages exists but stays private for now (no license clearance to
redistribute, or a pending user call) — those aren't listed, since pointing
someone at a repo they can't reach isn't a real recommendation.

| You want to… | Package | Install | Notes |
|---|---|---|---|
| Analyze song structure (tempo/BPM, beats, downbeats, segments like verse/chorus) | `all-in-one-infer` | `pip install all-in-one-infer` | Includes built-in source separation (demucs-infer) and beat tracking (madmom-infer); `AllInOneSession` reuses Harmonix plus a lazy session-owned HTDemucs separator for mixed input, while `analyze()` remains the lazy one-shot API and direct stems input never loads Demucs |
| Beat/downbeat/onset DSP primitives (modernized madmom) | `madmom-infer` | `pip install madmom-infer` | Published. numpy backend is the bit-identical-verified reference; optional differentiable torch frontend via `madmom-infer[torch]`. Use `MadmomAnalyzer` for reusable `load`/`infer`/`release` lifecycle; checkpoint metadata is package-owned. |
| Separate a song into music, vocal/instrumental, cinematic, or drum-kit stems | `demucs-infer` | `pip install demucs-infer` | The general-purpose HTDemucs workhorse plus registry choices for UVR (`vocals`/`non_vocals`), CDX23 (`music`/`sfx`/`speech`), MSST vocals, and DrumSep. `DemucsSession` provides explicit reusable lifecycle and package-owned checkpoint metadata; use the package README for exact model names and weight licenses. |
| Separate vocals with SOTA community models | `bs-roformer-infer` / `melband-roformer-infer` | `pip install bs-roformer-infer` · `pip install melband-roformer-infer` | Multiple registry models per package (vocals/instrumental/dereverb variants) — see each README's model table |
| Separate a mix with an alternative multi-stem / drum-focused model | `mdxnet-infer` | `pip install git+https://github.com/openmirlab/mdxnet-infer` | Public GitHub, not yet on PyPI. MDX23C TFC-TDF, includes a DrumSep checkpoint. `MDXNetSession` owns explicit lifecycle and package-local checkpoint metadata. |
| Transcribe music to MIDI (multi-instrument) | `mt3-infer` | `pip install mt3-infer` | Wraps 3 independent MT3 ports (MR-MT3/MT3-PyTorch/YourMT3) behind one API — see README for which backend fits |
| Transcribe to lead sheet (melody + chords) | `sheetsage-infer` | `pip install sheetsage-infer` | `SheetSageSession` provides explicit load/infer/release lifecycle; `sheetsage()` remains the lazy one-shot API |
| Recognize chords (large vocabulary) | `lv-chordia` | `pip install lv-chordia` | Bundles its own ~28MB weight ensemble in the wheel (documented size-based exception — no separate download step) |
| Tag/classify music audio (genre/mood/instruments) | `maest-infer` | `pip install maest-infer` | AGPL-3.0 — check license fit |
| Synthesize guitar audio from control signals (DDSP) | `ddsp-guitar-infer` | `pip install git+https://github.com/openmirlab/ddsp-guitar-infer` | Public GitHub, not yet on PyPI. String-wise DDSP synth |
| Generate audio continuations (research) | `jukebox-infer` | `pip install jukebox-infer` | `JukeboxSession` provides explicit load/infer/release lifecycle; large checkpoints (~6.2GB) remain lazy and package-owned |

## Ground rules for helping users

- **Weights download at first use** (never bundled): first run needs network +
  disk; cache locations and model choices live in each repo's README.
- **Independent lifecycle:** the inference packages own their model session,
  cache, checkpoint verification, and release; callers may wrap them in a
  higher-level manager without a shared runtime dependency. Read the package
  README for the exact session class and override parameters.
- **Package-owned checkpoint source:** each package reads its release-pinned
  checkpoint metadata from its own config file. The skills router is guidance,
  not a live checkpoint catalog; verify URLs and digests against the package
  at answer time.
- **License layering**: package code is permissive, but some model WEIGHTS
  carry non-commercial licenses. If the user hints at commercial use, check
  the specific model's weights license before recommending.
- **Pipelines compose**: common chains — separate first, then analyze
  (demucs-infer → all-in-one-infer does this internally); separate → transcribe
  per-stem (demucs-infer → mt3-infer) improves transcription of dense mixes.
- **Version floors matter**: recommend the latest release; known-broken floors
  are listed in the map above.
