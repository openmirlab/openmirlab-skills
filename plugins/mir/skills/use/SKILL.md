---
name: use
description: Teach someone how to actually use openmirlab's code — pick the right package for a music/audio task, install it, and write the Python (or CLI) that produces real output. Use when someone asks "how do I separate vocals / analyze song structure / transcribe to MIDI / recognize chords / tag audio", "how do I use <openmirlab package>", "show me the code for X", or wants to chain packages into a pipeline. Always teaches with runnable code grounded in the target repo's current README/API — never from memory alone.
---

# mir use — teach the code, not just the tool name

The job is done when the user has **working code producing real output on
their own audio file** — not when they've been told a package name.

## Process

1. **Clarify the task, not the tool.** Users often name a tool they heard of
   when a different one fits better. Establish: input (file? stems? live?),
   desired output (stems? MIDI? chords? segments? tags?), platform (GPU? mac?
   CPU-only?), and whether use is commercial (weights licensing — see the
   capability map's flags).
2. **Route via the capability map** (plugin CLAUDE.md). The map is a **cache
   of hints, not ground truth** — note its last-verified date. If two packages
   compete, state the practical difference in one sentence each and pick a
   default rather than dumping options.
3. **Ground in the repo's CURRENT docs before showing any code.** Read the
   chosen package's README (GitHub, or local checkout if present) for the
   current API, model names, and CLI flags. APIs and model registries change;
   teaching from memory produces plausible-but-dead code. Cite the version
   you're teaching against.
4. **Teach in this order:**
   a. Install command + import smoke-check (`python -c "import x"`).
   b. **A minimal runnable example on the user's actual file** — prefer the
      Python API (shows the result object) with the CLI one-liner as the
      alternative. Keep it under ~10 lines.
   c. **Explain the output**: what the result object/files contain, units
      (seconds? frames? MIDI numbers?), where files land on disk.
   d. First-run expectations: model weights download (size, cache path,
      one-time), GPU vs CPU speed reality.
   e. The two or three parameters actually worth knowing — not the full
      option surface.
5. **Pipelines**: when the task needs multiple packages (separate →
   transcribe per stem; separate → analyze), show the glue code explicitly —
   intermediate file formats, sample-rate expectations between stages, and
   where quality is won or lost.
6. **Troubleshoot from the known-issues flags** in the capability map before
   debugging blindly (version floors, broken CLI entry points, install traps).
7. **Feedback loop**: a broken install, dead weights URL, or doc-reality
   mismatch is an org-side bug — tell the user, and suggest filing an issue
   on the affected repo. If the capability map itself is stale, propose a
   gated update to this plugin's CLAUDE.md.

## Communication Style
- Default to English. Mirror the user's language when they write in another
  (e.g. reply in Traditional Chinese to Traditional Chinese).
- Explain concepts in simple, direct, plain language; use analogies for the
  complex parts.
- Keep explanations concise and actionable; no jargon, no filler.
