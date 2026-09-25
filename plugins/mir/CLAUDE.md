# mir — using the openmirlab toolbox

User-facing capability map for openmirlab's publicly available packages. This file is a
ROUTER and a CACHE: it maps "what you want to do with audio/music" to the
right package, but ground truth lives in each repo's own README — read those
at answer time, never answer from this file alone. Entries reflect the state
at the last-verified date below; treat older claims as hints to re-check.

Last verified: 2026-09-15 for madmom-infer's internal v0.3.0 tag; the pcunwa
RoFormer inventory was refreshed 2026-07-31, and other package publish status
remains from the 2026-07-15 README/CLAUDE.md sweep. pytimestretch's public-source
entry was updated for `time_scrub` on 2026-09-25; it has no PyPI release.

## Capability map

Only packages a user outside the org can actually install are listed here
(PyPI or a public GitHub repo). A separate set of research/derivative
packages exists but stays private for now (no license clearance to
redistribute, or a pending user call) — those aren't listed, since pointing
someone at a repo they can't reach isn't a real recommendation.

| You want to… | Package | Install | Notes |
|---|---|---|---|
| Stretch duration, shift pitch, or warp audio to frame markers | `pytimestretch` | uv source install or Actions wheel; follow its README | Public GitHub, not on PyPI. GPL-2.0-only combined distribution; direct Rubber Band/Signalsmith bindings, C++20 toolchain needed for source builds. NumPy frame-major arrays; `duration_ratio` is output/input, the inverse of librosa/pyrubberband `rate`. These operations return exact frame counts. No inference lifecycle or weights. |
| Hold or reverse a source playhead while output time continues | `pytimestretch.time_scrub` | uv source install or Actions wheel; follow its README | Separate Bungee Basic binding, not a `time_stretch` backend. `(output_frame, source_frame)` control points may hold or reverse the source; output length is exact. Mono/stereo NumPy audio at 8–192 kHz; optional global pitch within ±24 semitones, no formant preservation. Dense transients and stationary grains have documented artifacts. GPL-2.0-only combined distribution. |
| Make long, smeared spectral textures or compress with PaulStretch's sound | `pytimestretch.extreme_stretch` | uv source install or Actions wheel; follow its README | Direct libpaulstretch binding, separate from the precise backends. Mono/stereo NumPy audio needs at least 81,920 frames; `duration_ratio >= 1e-5` is passed through unchanged, and values below 1 shorten audio. Output length is approximate and spectral phase changes across calls. Combined distribution is GPL-2.0-only. |
| Analyze song structure (tempo/BPM, beats, downbeats, segments like verse/chorus) | `all-in-one-infer` | `pip install all-in-one-infer` | Includes built-in source separation (demucs-infer) and beat tracking (madmom-infer); `AllInOneSession` reuses Harmonix plus a lazy session-owned HTDemucs separator for mixed input, while `analyze()` remains the lazy one-shot API and direct stems input never loads Demucs |
| Beat/downbeat/onset DSP primitives (modernized madmom) | `madmom-infer` | `pip install madmom-infer` | PyPI remains at 0.2.0. Internal deployments use Git tag `v0.3.0`; install `"madmom-infer[numba] @ git+https://github.com/openmirlab/madmom-infer@v0.3.0"` for exact compiled Viterbi, or add `[torch]` for the optional neural frontend. Use `MadmomAnalyzer` for reusable lifecycle; checkpoint metadata is package-owned. |
| Separate a song into music, vocal/instrumental, cinematic, or drum-kit stems | `demucs-infer` | `pip install demucs-infer` | The general-purpose HTDemucs workhorse plus registry choices for UVR (`vocals`/`non_vocals`), CDX23 (`music`/`sfx`/`speech`), MSST vocals, and DrumSep. `DemucsSession` provides explicit reusable lifecycle and package-owned checkpoint metadata; use the package README for exact model names and weight licenses. |
| Separate vocals with SOTA community models | `bs-roformer-infer` / `melband-roformer-infer` | `pip install bs-roformer-infer` · `pip install melband-roformer-infer` | BS covers 16 direct `pcunwa` checkpoints across standard/Xe, Siamese, HyperACE v1/v2, FNO, Large-Inst, Resurrection, Revive, and Value Residual; MelBand covers 20 direct `pcunwa` checkpoints across Big, Small, Instrumental, Kim FT, and InstVoc Duality families. Read each README for exact names and the unresolved weight-license gate. |
| Separate a mix with an alternative multi-stem / drum-focused model | `mdxnet-infer` | `pip install git+https://github.com/openmirlab/mdxnet-infer` | Public GitHub, not yet on PyPI. MDX23C TFC-TDF registry: DrumSep, vocals/instrumental, dereverb, 4-stem, and SFX recipes. `MDXNetSession` owns explicit lifecycle and package-local checkpoint metadata; see its README for names and license caveats. |
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
- **License layering**: inspect both package code and any weights.
  pytimestretch's combined distribution is GPL-2.0-only; some model weights carry non-commercial
  licenses. Check the relevant package's README/NOTICE before recommending
  a use with licensing constraints.
- **Pipelines compose**: common chains — separate first, then analyze
  (demucs-infer → all-in-one-infer does this internally); separate → transcribe
  per-stem (demucs-infer → mt3-infer) improves transcription of dense mixes.
- **Version floors matter**: recommend the latest release; known-broken floors
  are listed in the map above.
