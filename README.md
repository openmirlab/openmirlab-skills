# openmirlab-skills

A [Claude Code](https://claude.com/claude-code) plugin for the
[openmirlab](https://github.com/openmirlab) music-AI toolbox — source
separation, song-structure analysis, music transcription, chord
recognition, audio tagging, classical MIR/DSP, and time/pitch processing. The toolbox includes
inference-only model packages and native audio tools.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Why this exists

OpenMIRLab maintains many independent music and audio packages. Their install paths, licenses and APIs differ, so this plugin routes a concrete task to a suitable package and reads that package's current README before showing runnable code. It is a guide to the toolbox, not a shared model runtime.

## Acknowledgments

- [OpenMIRLab](https://github.com/openmirlab) maintains this plugin and the packages it describes.
- The original model researchers, code authors and checkpoint hosts are credited in each linked package's own README; this plugin contains no model code or weights. See, for example, [madmom-infer](https://github.com/openmirlab/madmom-infer) and [demucs-infer](https://github.com/openmirlab/demucs-infer).

## Citation

Not applicable: this routing plugin introduces no research model or single paper to cite. Cite the original model or algorithm named in the package README used for a result.

## Features

- Match source separation, transcription, chords, tagging, analysis and DSP tasks to public packages.
- Show package-specific installation, usage and licensing guidance grounded in each repo's current README.
- Surface relevant limitations such as checkpoint licenses and historical PyPI versions.

## Scope

This plugin supplies instructions and a capability map. It does not install packages for the user, run models, host checkpoints or define a shared inference lifecycle.

## Install

```
/plugin marketplace add openmirlab/openmirlab-skills
/plugin install mir@openmirlab-skills
```

`mir`'s `CLAUDE.md` is a capability map (task → package → known-good
install command, with license flags), and `/mir:use` walks you from
"separate the vocals in this mp3" to working code that produces real
output on your own file.

## Quick Start

After installing the plugin, ask its usage skill for a concrete workflow:

```text
/mir:use Separate the vocals from my song and show the Python code.
```

The skill checks the relevant package's current README, then gives an install command and a runnable example for your input.

## The toolbox

Maintained packages install from their public GitHub repositories with `pip install git+https://github.com/openmirlab/<name>.git`. Existing PyPI versions are historical snapshots and receive no new releases. For pytimestretch, follow its [uv installation
guide](https://github.com/openmirlab/pytimestretch#install), including native
source-build requirements or the matching Actions wheel. For pyqmdsp, use its
[uv installation guide](https://github.com/openmirlab/pyqmdsp#install); source
checkouts require recursive submodules and C/C++17.

| Task | Package | Status |
|---|---|---|
| Time stretching, pitch shifting, forward-only marker warp, Bungee Basic hold/reverse scrubbing, PaulStretch spectral stretch/compression | [pytimestretch](https://github.com/openmirlab/pytimestretch) | GitHub; GPL-2.0-only; source build needs a C++20 toolchain |
| Classical beat/onset/downbeat, spectral and tonal analysis, segmentation and DSP | [pyqmdsp](https://github.com/openmirlab/pyqmdsp) | GitHub; GPL-2.0-or-later; direct qm-dsp without Vamp; C/C++17 source build or matching Actions wheel |
| Song structure (BPM, beats, downbeats, segments) | [all-in-one-infer](https://github.com/openmirlab/all-in-one-infer) | GitHub |
| Beat/downbeat/onset DSP primitives (modernized madmom) | [madmom-infer](https://github.com/openmirlab/madmom-infer) | GitHub |
| Source separation (vocals/drums/bass/other) | [demucs-infer](https://github.com/openmirlab/demucs-infer) | GitHub |
| SOTA vocal separation | [bs-roformer-infer](https://github.com/openmirlab/bs-roformer-infer) · [melband-roformer-infer](https://github.com/openmirlab/melband-roformer-infer) | GitHub |
| Alternative multi-stem / drum-stem separation | [mdxnet-infer](https://github.com/openmirlab/mdxnet-infer) | GitHub |
| AudioSet tagging and native clip embeddings | [efficientat-infer](https://github.com/openmirlab/efficientat-infer) · [panns-infer](https://github.com/openmirlab/panns-infer) | GitHub; mn04/mn10 or CNN14; compare accuracy on your own sounds |
| Fine-grained music/text retrieval | [figma-infer](https://github.com/openmirlab/figma-infer) | GitHub source; 10-second 24 kHz windows; checkpoint CC BY-NC 4.0, no PyPI release |
| Music → MIDI transcription (multi-instrument) | [mt3-infer](https://github.com/openmirlab/mt3-infer) | GitHub |
| Music → lead sheet | [sheetsage-infer](https://github.com/openmirlab/sheetsage-infer) | GitHub |
| Chord recognition | [lv-chordia](https://github.com/openmirlab/lv-chordia) | GitHub |
| Genre/subgenre ranking | [maest-infer](https://github.com/openmirlab/maest-infer) | GitHub |
| Guitar synthesis (DDSP) | [ddsp-guitar-infer](https://github.com/openmirlab/ddsp-guitar-infer) | GitHub |
| Audio generation (research) | [jukebox-infer](https://github.com/openmirlab/jukebox-infer) | GitHub |

See [LANDSCAPE.md](./LANDSCAPE.md) for tools outside the openmirlab
toolbox itself that are also worth knowing about (general-purpose MIR
libraries, evaluation frameworks, and more as the list grows).

## Package context

Upstream MIR research code goes stale fast — abandoned repos, compiled
extensions that stop building, PyPI releases years behind. The inference
packages are modernized, inference-only, pip-installable rebuilds: no training
code, no compiled dependencies in the core install, and refactors are held to a bit-identical-output bar against
the original. Model weights normally download at first use. Explicit package
exceptions exist: `lv-chordia` includes its approximately 28 MB ensemble for
offline installation. Check each package README for its acquisition method
and separate weight license, including non-commercial restrictions.

pytimestretch is a native audio-tool package: it binds Rubber Band and
Signalsmith for precise duration and pitch work, libpaulstretch for a
separate spectral stretch/compression effect with approximate output length,
and Bungee Basic for the default marker-aligned `time_warp` and a separate
exact-length `time_scrub` operation that can hold or reverse the source playhead.
It compiles all four engines into its
wheels. It has no model weights or inference session. Read its README for the
uv source-build workflow and development wheel artifacts; it is not on PyPI.

## Runtime and checkpoint convention

The inference packages expose independent, reusable model sessions: callers
can explicitly load, infer, release, and inspect status/cache state without a
shared runtime dependency. Each package owns its release-pinned checkpoint
configuration (including URLs and SHA-256 digests) in its installed package;
this plugin is a routing aid, not the runtime source of checkpoint truth.

## Development

Validate the marketplace manifest and skill frontmatter from a checkout:

```bash
python3 tools/validate.py
```

When updating package guidance, check the target package's current README and public install status first. Keep `plugins/mir/CLAUDE.md` aligned with its actual task and package coverage.

## License

This skills plugin is MIT-licensed. Each package and its model weights retain
their own licenses; consult the capability map and the package README.
Weight distribution follows the download-by-default policy and documented
package exceptions above.

## Support

Report plugin guidance or installation problems in [openmirlab-skills issues](https://github.com/openmirlab/openmirlab-skills/issues). Report model or package behavior in the corresponding package repository.
