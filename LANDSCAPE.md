# MIR landscape

A different question from "what should openmirlab build next": this file
asks **"is this worth using, full stop?"** — and most of what belongs here
will never need rescuing, because it's already well-maintained (`librosa`
isn't going anywhere; that's exactly why it belongs on a "what to use"
list rather than a modernization to-do list).

First full pass: 2026-07-12 — every entry below was verified against a
primary source on that date (GitHub API for license/activity/archived
status, PyPI API for installability, project pages/model cards for weights
licensing). Coverage is curated, not exhaustive: 3-5 entries per category,
picked on the bar "would a practitioner in 2026 actually reach for this?"

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

Where a tool's main value is its pretrained model, the **weights license
is checked separately from the code license** — they frequently differ,
and the weights license is usually the one that constrains you.

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
- **torchaudio** ([pytorch/audio](https://github.com/pytorch/audio)) —
  BSD-2-Clause, verified 2026-07-12 (pushed same day, 2,902 stars).
  PyTorch-native audio I/O, transforms, and feature extraction (mel/MFCC/
  STFT, resampling, forced alignment). The PyTorch team declared it
  officially in "maintenance phase" at v2.9 (2025), feature-frozen, with
  decode/encode folded into TorchCodec. Maturity: **Maintenance-mode**
  (official, not inferred). openmirlab overlap: none. **Recommendation**:
  still the default for GPU-native features inside PyTorch pipelines; pin
  versions given the maintenance-phase API churn.
- **nnAudio** ([KinWaiCheuk/nnAudio](https://github.com/KinWaiCheuk/nnAudio)) —
  MIT, verified 2026-07-12 (pushed 2026-05-21, 1,128 stars).
  GPU-accelerated spectrogram/CQT/mel/STFT implemented as trainable PyTorch
  conv layers — much faster than librosa inside training loops. Maturity:
  **Active** (version bump Dec 2025). openmirlab overlap: none.
  **Recommendation**: use when feature extraction sits inside a training
  loop and CPU cost is the bottleneck.
- **Pedalboard** ([spotify/pedalboard](https://github.com/spotify/pedalboard)) —
  GPL-3.0, verified 2026-07-12 (pushed 2026-07-08, 6,198 stars). Spotify's
  audio-effects and VST3/AU-hosting library; widely used for realistic
  data augmentation in ML/MIR pipelines. Maturity: **Active**. openmirlab
  overlap: none. **Recommendation**: the go-to for augmentation/
  effects-chain needs; note the GPL-3.0 linking implications.
- **audioFlux** ([libAudioFlux/audioFlux](https://github.com/libAudioFlux/audioFlux)) —
  MIT, verified 2026-07-12 (pushed 2026-03-06, 3,333 stars). C-core
  feature-extraction library spanning classic and deep-learning-oriented
  transforms, positioned as a faster librosa/essentia alternative.
  Maturity: **Active** source (real commits Feb–Mar 2026), but the PyPI
  release has been stuck at 0.1.9 since May 2024 — build from source for
  current code. openmirlab overlap: none. **Recommendation**: worth
  evaluating for extraction throughput; treat the stale PyPI wheel as the
  install reality until it catches up.
- **aubio** ([aubio/aubio](https://github.com/aubio/aubio)) — GPL-3.0,
  verified 2026-07-12 (pushed 2026-04-10, 3,722 stars). Small C library
  (+ Python bindings) for real-time onset/pitch/tempo/beat detection.
  Maturity: **Active** on GitHub, but the PyPI wheel has been frozen at
  0.4.9 since 2019 — build from source or use conda-forge for current
  code. openmirlab overlap: partial (`madmom-infer`) — both touch
  beat/onset DSP; aubio is the lightweight real-time option vs. madmom's
  research-grade accuracy. **Recommendation**: fast, dependency-light
  onset/pitch for embedded/real-time contexts, not benchmark-grade beat
  tracking.

## Evaluation & benchmarking

- **mir_eval** ([craffel/mir_eval](https://github.com/craffel/mir_eval)) —
  MIT, verified 2026-07-12 (pushed ~5 months before verification, 706
  stars — slower-moving than the toolkits above but not stalled). The
  standard reference implementation for MIR evaluation metrics (onset/beat/
  chord/segmentation/melody/separation scoring) — used to score research
  output. Maturity: **Maintenance-mode**. openmirlab overlap: none —
  openmirlab packages are inference-only by design and don't ship
  evaluation code; this is exactly the tool you'd reach for to score their
  output yourself. **Recommendation**: the correct tool when you need to
  measure MIR output against ground truth, not just produce it.
- **mirdata** ([mir-dataset-loaders/mirdata](https://github.com/mir-dataset-loaders/mirdata)) —
  BSD-3-Clause, verified 2026-07-12 (pushed 2026-06-23, 411 stars).
  Canonical loader/validator for ~50 standard MIR datasets (audio,
  annotations, checksums). Maturity: **Active** (v1.0.0 released
  2025-09-23). openmirlab overlap: none. **Recommendation**: the standard
  dataset-loading layer for MIR evaluation and benchmarking work.
- **museval** ([sigsep/sigsep-mus-eval](https://github.com/sigsep/sigsep-mus-eval)) —
  MIT, verified 2026-07-12 (pushed 2026-05-21, 237 stars). Reference BSS
  Eval v4 implementation (SDR/SIR/SAR/ISR) from the SiSEC/MDX challenge
  organizers — the standard metric harness for source-separation quality.
  Maturity: **Maintenance-mode**, borderline stalled (last substantive fix
  2024-06, last PyPI release 2023-05). openmirlab overlap: partial
  (`demucs-infer`, `bs-roformer-infer`, `melband-roformer-infer`,
  `mdxnet-infer`) — the natural way to score any of their output.
  **Recommendation**: the standard for separation eval; pin the version
  and don't expect fast upstream fixes.
- **JAMS** ([marl/jams](https://github.com/marl/jams)) — ISC, verified
  2026-07-12 (pushed 2025-06-18, 203 stars). JSON Annotated Music
  Specification — schema + I/O for multi-annotator MIR annotations
  (chords, beats, segments, tags), from the NYU MARL lab behind mir_eval.
  Maturity: **Stalled** — no commits in 12+ months. openmirlab overlap:
  none. **Recommendation**: fine for annotation interchange, but treat it
  as a frozen/finished artifact, not an actively developed one.

## Source separation

- **python-audio-separator** ([nomadkaraoke/python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator)) —
  MIT, verified 2026-07-12 (pushed 2026-07-08, 1,277 stars). CLI/Python
  API wrapper unifying dozens of community-trained separation checkpoints
  (MDX-Net, VR-Arch, Demucs, MDXC/Roformer) behind one interface; PyPI
  `audio-separator` 0.44.3 (2026-07-08). Maturity: **Active**. openmirlab
  overlap: partial (`demucs-infer`, `mdxnet-infer`). **Recommendation**:
  best single entry point when you need to try many separation models fast
  without hand-rolling each architecture's loader.
- **Music-Source-Separation-Training (MSST)** ([ZFTurbo/Music-Source-Separation-Training](https://github.com/ZFTurbo/Music-Source-Separation-Training)) —
  MIT, verified 2026-07-12 (pushed same day, 1,436 stars). The community's
  working framework for training *and* running the current SOTA
  checkpoints (BS-RoFormer, Mel-Band RoFormer, SCNet); commits land daily.
  Maturity: **Active**. openmirlab overlap: partial (`bs-roformer-infer`,
  `melband-roformer-infer`, `mdxnet-infer`). **Recommendation**: the
  practitioner reach-for when you need the newest checkpoint or want to
  fine-tune, not just run inference.
- **UVR (Ultimate Vocal Remover)** ([Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui)) —
  MIT, verified 2026-07-12 (pushed 2025-03-13, 25,368 stars). Desktop
  **app** (not a library) bundling the major separation-model families for
  non-coders; the de facto consumer/prosumer standard. Maturity:
  **Maintenance-mode** (slowed since early 2025 but functional, huge
  community). openmirlab overlap: partial (`demucs-infer`,
  `mdxnet-infer`). **Recommendation**: point non-technical users here; not
  for pipeline integration.
- **Demucs** ([facebookresearch/demucs](https://github.com/facebookresearch/demucs)) —
  MIT, verified 2026-07-12 (pushed 2024-04-24, 10,301 stars, archived).
  The waveform-domain separator that defined the Demucs family. Maturity:
  **Archived** (finished/stable, still fine to run). openmirlab overlap:
  superseded by (`demucs-infer`). **Recommendation**: use `demucs-infer`
  instead; this is the upstream lineage.
- **Open-Unmix** ([sigsep/open-unmix-pytorch](https://github.com/sigsep/open-unmix-pytorch)) —
  MIT, verified 2026-07-12 (pushed 2024-06-17, 1,495 stars). Simple,
  well-documented spectrogram-masking baseline from the SiSEC/MUSDB
  lineage. Maturity: **Stalled** (2+ years without commits). openmirlab
  overlap: none. **Recommendation**: for teaching or a lightweight
  footprint only — separation quality trails Roformer-era models badly
  now.

## Music transcription

- **basic-pitch** ([spotify/basic-pitch](https://github.com/spotify/basic-pitch)) —
  Apache-2.0, verified 2026-07-12 (pushed 2025-11-13, 5,282 stars; PyPI
  0.4.0, 2024-08-16). Lightweight, instrument-agnostic polyphonic
  pitch/note detector (CNN, fast on CPU, ONNX/TF/CoreML exports).
  Maturity: **Maintenance-mode** (repo sees doc/infra commits; the core
  package hasn't shipped a PyPI release in ~2 years but is stable and
  widely embedded). openmirlab overlap: partial (`mt3-infer`) — both
  output MIDI from audio, but basic-pitch is single-stream note detection,
  not instrument-separated. **Recommendation**: still the go-to for quick,
  cheap audio→MIDI when you don't need instrument separation.
- **MT3** ([magenta/mt3](https://github.com/magenta/mt3)) — Apache-2.0,
  verified 2026-07-12 (pushed 2026-07-09, 1,728 stars). The original
  T5X-based multi-task multitrack transcription model; the field's
  long-standing baseline. Maturity: **Active**. openmirlab overlap:
  superseded by (`mt3-infer`). **Recommendation**: use `mt3-infer`
  instead; keep this for reference/benchmarking.
- **YourMT3+** ([mimbres/YourMT3](https://github.com/mimbres/YourMT3)) —
  GPL-3.0, verified 2026-07-12 (pushed 2024-11-29, 235 stars). Enhanced
  MT3-style architecture (MoE decoder, cross-dataset stem augmentation)
  that placed in the top 2 of the 2025 AMT Challenge, beating the MT3
  baseline. Maturity: **Stalled** (no push in ~20 months, not archived).
  openmirlab overlap: partial (`mt3-infer`) — same task class, materially
  better multi-instrument accuracy in published benchmarks.
  **Recommendation**: worth evaluating for quality gains, but GPL-3.0
  copyleft needs review before integrating into anything redistributed.
- **piano_transcription_inference** ([qiuqiangkong/piano_transcription_inference](https://github.com/qiuqiangkong/piano_transcription_inference)) —
  **no LICENSE file** (all rights reserved by default), verified
  2026-07-12 (pushed 2025-01-26, 469 stars; PyPI 0.0.6, 2025-01-26).
  Pip-installable inference wrapper around the ByteDance high-resolution
  piano transcription model (piano-only onset/frame, with pedal); the
  research repo it packages (bytedance/piano_transcription) is archived
  and also carries no license. Maturity: **Maintenance-mode**. openmirlab
  overlap: partial (`mt3-infer`) — piano-specialized, typically more
  accurate than generic multi-instrument MT3 on piano-only audio.
  **Recommendation**: excellent for piano-only research/prototyping; do
  not ship it in a product without securing explicit licensing from the
  author first.

## Pitch / F0 estimation

- **torchcrepe** ([maxrmorrison/torchcrepe](https://github.com/maxrmorrison/torchcrepe)) —
  MIT, verified 2026-07-12 (pushed 2025-05-16, 522 stars; PyPI 0.0.24,
  2025-05-16). PyTorch reimplementation of CREPE with differentiable
  pitch/periodicity output. Maturity: **Maintenance-mode**. openmirlab
  overlap: none. **Recommendation**: the default baseline pitch tracker
  for PyTorch pipelines.
- **FCPE** ([CNChTu/FCPE](https://github.com/CNChTu/FCPE)) — MIT, verified
  2026-07-12 (pushed 2025-10-14, 201 stars). Lightweight context-based
  pitch estimator; per its 2025 paper, accuracy competitive with RMVPE at
  a fraction of the parameters (10.6M vs 90.4M), fast enough for real-time
  SVC/RVC pipelines. Maturity: **Active**. openmirlab overlap: none.
  **Recommendation**: preferred when latency/size matters and
  near-RMVPE accuracy is acceptable.
- **PESTO** ([SonyCSLParis/pesto](https://github.com/SonyCSLParis/pesto)) —
  LGPL-3.0, verified 2026-07-12 (pushed 2025-10-15, 295 stars; PyPI
  `pesto-pitch` 2.0.1, 2025-02-18). Self-supervised, extremely light
  (0.13M params) real-time pitch estimator from Sony CSL,
  ISMIR-published. Maturity: **Active**. openmirlab overlap: none.
  **Recommendation**: strong pick for streaming/embedded pitch tracking
  where model size is the constraint.
- **PENN** ([interactiveaudiolab/penn](https://github.com/interactiveaudiolab/penn)) —
  MIT, verified 2026-07-12 (pushed 2025-04-02, 277 stars; PyPI `penn`
  1.0.0). Academic pitch-estimation toolkit (FCNF0++) with rigorous
  benchmarking against CREPE/DIO/etc. Maturity: **Maintenance-mode**.
  openmirlab overlap: none. **Recommendation**: use when you need a
  research-grade, benchmarked baseline rather than a production shortcut.

## Beat / tempo / structure

- **Beat This!** ([CPJKU/beat_this](https://github.com/CPJKU/beat_this)) —
  MIT for **both code and published model weights**, verified 2026-07-12
  (pushed 2026-05-28, 331 stars). ISMIR 2024 beat/downbeat tracker that
  drops DBN post-processing entirely; widely regarded as the practical
  post-madmom upgrade, and unlike madmom it carries no non-commercial
  restriction on its weights. Maturity: **Active**. openmirlab overlap:
  none. **Recommendation**: best default pick for new beat/downbeat
  integrations today.
- **madmom** ([CPJKU/madmom](https://github.com/CPJKU/madmom)) — dual
  license: BSD-2-Clause (source code) / **CC-BY-NC-SA-4.0 (pretrained
  models — non-commercial only)**, verified 2026-07-12 (pushed 2026-03-20,
  1,670 stars, not archived). Classic Python audio/music signal-processing
  library; its DBN/HMM beat-decoding backend is still widely used as a
  post-processing stage even in newer pipelines. Maturity:
  **Maintenance-mode**. openmirlab overlap: superseded by
  (`madmom-infer`). **Recommendation**: use via `madmom-infer`; note the
  model weights are non-commercial-only, a real constraint for product
  use.
- **BeatNet** ([mjhydri/BeatNet](https://github.com/mjhydri/BeatNet)) —
  CC-BY-4.0, verified 2026-07-12 (pushed 2026-04-13, 502 stars). CRNN +
  particle-filter joint beat/downbeat/tempo/meter tracker (ISMIR 2021),
  notable for real-time/streaming operation, which madmom doesn't do well.
  Maturity: **Active**. openmirlab overlap: none. **Recommendation**:
  reach for it specifically for live/streaming use cases; check CC-BY-4.0
  terms fit your use.
- **MSAF** ([urinieto/msaf](https://github.com/urinieto/msaf)) — MIT,
  verified 2026-07-12 (pushed 2026-03-04, 554 stars; recent activity is
  doc/CI fixes only). Music Structure Analysis Framework bundling multiple
  classic segmentation algorithms (Foote, CNMF, SF, etc.) plus an eval
  harness. Maturity: **Maintenance-mode**. openmirlab overlap: partial
  (`all-in-one-infer`). **Recommendation**: research-grade segmentation
  experimentation/benchmarking rather than a plug-and-play production
  tool.
- **All-In-One** ([mir-aidj/all-in-one](https://github.com/mir-aidj/all-in-one)) —
  MIT, verified 2026-07-12 (pushed 2024-05-09; last real code commit
  2023-10-10, 800 stars). Joint beat/downbeat/structure/tag model with
  single-call convenience. Maturity: **Stalled** (~2.5 years without
  commits). openmirlab overlap: superseded by (`all-in-one-infer`).
  **Recommendation**: use via `all-in-one-infer`, not upstream directly.

## Chord / key recognition

- **chord-extractor** ([ohollo/chord-extractor](https://github.com/ohollo/chord-extractor)) —
  GPL-2.0, verified 2026-07-12 (pushed 2025-08-14, 244 stars; PyPI 0.1.3,
  2025-08-14). Python wrapper around the Chordino Vamp plugin (below) —
  handles the awkward Vamp SDK setup, format conversion, and
  multiprocessing. Maturity: **Maintenance-mode**. openmirlab overlap:
  partial (`lv-chordia`). **Recommendation**: the pragmatic way to get
  well-validated Chordino chords from Python; GPL-2.0 may block
  closed-source commercial use.
- **Chordino / NNLS-Chroma** ([c4dm/nnls-chroma](https://github.com/c4dm/nnls-chroma)) —
  GPL-2.0, verified 2026-07-12 (pushed 2020-04-24, 15 stars). Matthias
  Mauch's original Queen Mary Vamp plugin; the reference chord/chroma
  estimator behind Sonic Visualiser/Sonic Annotator/Tony, and the
  algorithm chord-extractor wraps. Maturity: **Stalled** but
  stable/finished. openmirlab overlap: partial (`lv-chordia`).
  **Recommendation**: use through chord-extractor's Python front door
  rather than raw Vamp plumbing.
- **BTC-ISMIR19** ([jayg996/BTC-ISMIR19](https://github.com/jayg996/BTC-ISMIR19)) —
  MIT, verified 2026-07-12 (pushed 2020-05-23, 201 stars). Bidirectional
  Transformer for Chord Recognition, ISMIR 2019 reference implementation;
  still the most-cited deep-learning chord baseline in papers. Maturity:
  **Stalled**. openmirlab overlap: partial (`lv-chordia`).
  **Recommendation**: useful research baseline/comparison point, not
  packaged for production use as-is.
- **autochord** ([cjbayron/autochord](https://github.com/cjbayron/autochord)) —
  Apache-2.0, verified 2026-07-12 (pushed 2023-04-09, 162 stars).
  Pip-installable, simple-API Python chord recognizer. Maturity:
  **Stalled** (~3 years). openmirlab overlap: partial (`lv-chordia`).
  **Recommendation**: a quick, permissively-licensed option worth a spike
  test, but there's no maintenance to lean on.

## Tagging / classification

- **MERT** ([yizhilll/MERT](https://github.com/yizhilll/MERT)) —
  Apache-2.0 (code and weights), verified 2026-07-12 (pushed 2025-05-25,
  477 stars). Self-supervised acoustic+musical dual-teacher transformer
  for music representation learning; strong published numbers across 14
  MIR tasks (tagging, key, beat, etc.), widely used as a feature backbone.
  Maturity: **Maintenance-mode**. openmirlab overlap: partial
  (`maest-infer`) — both are pretrained transformer embeddings usable for
  tagging/downstream probing. **Recommendation**: best-in-class
  general-purpose music embedding backbone, and permissively licensed.
- **CLAP** ([LAION-AI/CLAP](https://github.com/LAION-AI/CLAP)) — repo
  license CC0-1.0; the commonly-used weights
  (`laion/clap-htsat-unfused` on Hugging Face) are Apache-2.0, verified
  2026-07-12 (repo pushed 2023-11-01, 2,216 stars). Contrastive text-audio
  embedding model enabling zero-shot tagging, text-to-audio
  retrieval/search — a cross-modal capability PANNs/MERT don't have.
  Maturity: **Stalled** (no code changes since late 2023, but the weights
  are finished and still broadly used downstream via HF).
  openmirlab overlap: partial (`maest-infer`) — both produce audio
  embeddings for tagging; CLAP adds the text-alignment angle.
  **Recommendation**: the pick for any text-query-driven tagging/search
  feature; don't expect upstream code activity.
- **PANNs** ([qiuqiangkong/audioset_tagging_cnn](https://github.com/qiuqiangkong/audioset_tagging_cnn)) —
  MIT, verified 2026-07-12 (pushed 2024-07-25, 1,762 stars).
  AudioSet-pretrained CNN tagger (Cnn14 etc.); the long-running default
  baseline for general-purpose audio tagging and embeddings, still a
  common building block inside other tools. Maturity: **Stalled** but
  stable/finished. openmirlab overlap: partial (`maest-infer`) —
  overlapping tagging use case, PANNs is broader (all of AudioSet, not
  music-specific). **Recommendation**: a lightweight, well-understood
  fallback/baseline rather than a primary tool.

## Symbolic / MIDI processing

- **pretty_midi** ([craffel/pretty-midi](https://github.com/craffel/pretty-midi)) —
  MIT, verified 2026-07-12 (pushed 2026-02-18, 1,032 stars; PyPI 0.2.11,
  2025-10-08). The de facto Python object model for
  reading/writing/analyzing MIDI (notes, tempo, key/time signature,
  piano-roll conversion). Maturity: **Active**. openmirlab overlap: none.
  **Recommendation**: still the default choice for MIDI post-processing
  after any transcription pipeline.
- **music21** ([cuthbertLab/music21](https://github.com/cuthbertLab/music21)) —
  BSD-3-Clause, verified 2026-07-12 (pushed 2026-07-11, 2,528 stars; PyPI
  10.5.0, 2026-06-17). Full musicology toolkit: score parsing
  (MusicXML/MIDI/ABC/Humdrum), harmonic/voice-leading analysis, notation
  rendering. Maturity: **Active**, very well maintained. openmirlab
  overlap: none. **Recommendation**: reach for this when the task is
  score-level/theory analysis, not just note-event manipulation.
- **mido** ([mido/mido](https://github.com/mido/mido)) — MIT, verified
  2026-07-12 (pushed 2026-06-27, 1,624 stars; PyPI 1.3.3, 2024-10-25).
  Low-level MIDI I/O — real-time ports, raw message parsing, file
  read/write. Maturity: **Active**. openmirlab overlap: none.
  **Recommendation**: pair with pretty_midi/music21 when you need
  real-time MIDI I/O or raw message-level control they don't offer.
- **MidiTok** ([Natooz/MidiTok](https://github.com/Natooz/MidiTok)) — MIT,
  verified 2026-07-12 (pushed 2026-07-02, 882 stars; PyPI 3.0.6.post1,
  2025-07-22). Symbolic-music tokenizers (REMI, TSD, Structured, etc.) for
  feeding MIDI into transformer/LLM-style generation and analysis models —
  the standard building block for 2025-26 symbolic-music ML work.
  Maturity: **Active**. openmirlab overlap: none. **Recommendation**: the
  right tool whenever you're tokenizing MIDI for a transformer, rather
  than hand-rolling encodings.
- **symusic** ([Yikai-Liao/symusic](https://github.com/Yikai-Liao/symusic)) —
  MIT, verified 2026-07-12 (pushed 2026-06-22, 183 stars; PyPI 0.6.0,
  2026-04-08). C++-backed, Python-bound MIDI/score data structure — orders
  of magnitude faster than pretty_midi/music21 for bulk parsing; used
  internally by MidiTok for speed. Maturity: **Active**. openmirlab
  overlap: none. **Recommendation**: swap in when pretty_midi becomes a
  bottleneck on large corpora (dataset prep, batch tokenization).

## Generation / synthesis

- **ACE-Step 1.5** ([ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)) —
  MIT, verified 2026-07-12 (pushed 2026-06-26, 11,583 stars). Fast,
  low-VRAM (<4GB) local music foundation model with LoRA personalization
  and a Gradio UI/REST/CLI; the fastest-growing project of anything
  checked in this pass. Maturity: **Active**. openmirlab overlap: none.
  **Recommendation**: the top pick for local/open music generation in
  2026 — permissive license, real momentum, consumer-hardware friendly.
- **MusicGen (audiocraft)** ([facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)) —
  code MIT, **weights CC-BY-NC-4.0 (non-commercial only)**, verified
  2026-07-12 via the repo's `LICENSE_weights` + HF model cards (pushed
  2026-03-03, 23,471 stars). Text/melody-conditioned music generation LM;
  still the reference implementation most tooling builds on. Maturity:
  **Active**. openmirlab overlap: none. **Recommendation**: solid for
  research and non-commercial use; the NC weights license rules out
  commercial deployment.
- **Stable Audio Tools** ([Stability-AI/stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools)) —
  code MIT; weights under the Stability AI Community License (free below
  a revenue threshold; not OSI-approved), verified 2026-07-12 (pushed
  2026-07-02, 3,812 stars). Training/inference framework behind Stable
  Audio Open and the newer Stable Audio 3.0 open-weight release (May
  2026) — long-form, high-quality text-to-audio/music. Maturity:
  **Active**. openmirlab overlap: none. **Recommendation**: strong
  open-weights option; read the community-license revenue clause before
  any commercial use.
- **YuE** ([multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE)) —
  Apache-2.0 for code **and** weights (confirmed switched from earlier
  more restrictive terms), verified 2026-07-12 (pushed 2025-06-04, 6,322
  stars). Full-song generation (vocals + accompaniment, multi-lingual
  lyrics) — the most Suno-like fully-open option. Maturity:
  **Maintenance-mode** (no commits in over a year, not archived).
  openmirlab overlap: none. **Recommendation**: the fully-permissive pick
  for full-song generation experiments; watch for renewed activity.
- **Jukebox** ([openai/jukebox](https://github.com/openai/jukebox)) —
  custom Noncommercial Use License (code and generated content both
  NC-only, verified via the repo's LICENSE), verified 2026-07-12 (pushed
  2024-06-19, archived, 8,031 stars). Historically important raw-audio
  generation model. Maturity: **Archived**. openmirlab overlap: superseded
  by (`jukebox-infer`). **Recommendation**: use `jukebox-infer` for a
  modern-PyTorch install; the NC license applies either way.
