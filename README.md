# openmirlab-skills

A [Claude Code](https://claude.com/claude-code) plugin for the
[openmirlab](https://github.com/openmirlab) music-AI toolbox — source
separation, song-structure analysis, music transcription, chord
recognition, and audio tagging, all as modern, inference-only,
pip-installable packages.

## Install

```
/plugin marketplace add openmirlab/openmirlab-skills
/plugin install mir@openmirlab-skills
```

`mir`'s `CLAUDE.md` is a capability map (task → package → known-good
install command, with license flags), and `/mir:use` walks you from
"separate the vocals in this mp3" to working code that produces real
output on your own file.

## The toolbox

Packages marked **PyPI** install with a plain `pip install <name>`. Packages
marked **GitHub** are public but not yet PyPI-published — install straight
from the repo (`pip install git+https://github.com/openmirlab/<name>`) until
their release lands.

| Task | Package | Status |
|---|---|---|
| Song structure (BPM, beats, downbeats, segments) | [all-in-one-infer](https://github.com/openmirlab/all-in-one-infer) | PyPI |
| Beat/downbeat/onset DSP primitives (modernized madmom) | [madmom-infer](https://github.com/openmirlab/madmom-infer) | PyPI |
| Source separation (vocals/drums/bass/other) | [demucs-infer](https://github.com/openmirlab/demucs-infer) | PyPI |
| SOTA vocal separation | [bs-roformer-infer](https://github.com/openmirlab/bs-roformer-infer) · [melband-roformer-infer](https://github.com/openmirlab/melband-roformer-infer) | PyPI |
| Alternative multi-stem / drum-stem separation | [mdxnet-infer](https://github.com/openmirlab/mdxnet-infer) | GitHub |
| Music → MIDI transcription (multi-instrument) | [mt3-infer](https://github.com/openmirlab/mt3-infer) | PyPI |
| High-resolution piano transcription (with pedal) | [hr-piano-transcribe-infer](https://github.com/openmirlab/hr-piano-transcribe-infer) | GitHub |
| Music → lead sheet | [sheetsage-infer](https://github.com/openmirlab/sheetsage-infer) | PyPI |
| Chord recognition | [lv-chordia](https://github.com/openmirlab/lv-chordia) | PyPI |
| Audio tagging/classification | [maest-infer](https://github.com/openmirlab/maest-infer) | PyPI |
| Drum one-shot sample extraction | [dose-infer](https://github.com/openmirlab/dose-infer) | GitHub |
| Guitar synthesis (DDSP) | [ddsp-guitar-infer](https://github.com/openmirlab/ddsp-guitar-infer) | GitHub |
| Neural-codec audio effects / granular resynthesis | [latenteffect](https://github.com/openmirlab/latenteffect) | GitHub |
| Audio generation (research) | [jukebox-infer](https://github.com/openmirlab/jukebox-infer) | PyPI |

See [LANDSCAPE.md](./LANDSCAPE.md) for tools outside the openmirlab
toolbox itself that are also worth knowing about (general-purpose MIR
libraries, evaluation frameworks, and more as the list grows).

## Why these packages exist

Upstream MIR research code goes stale fast — abandoned repos, compiled
extensions that stop building, PyPI releases years behind. Every package
here is a modernized, inference-only, pip-installable rebuild: no training
code, no compiled dependencies in the core install, no git-URL
dependencies, and refactors are held to a bit-identical-output bar against
the original. Model weights are never bundled — they download at first
use, and some carry their own (occasionally non-commercial) licenses; the
capability map flags these.

## License

MIT. Model weights are never bundled by any openmirlab package.
