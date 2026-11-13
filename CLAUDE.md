# openmirlab-skills maintainer guide

This repository is the OpenMIRLab toolbox router. `plugins/mir/CLAUDE.md` maps tasks to installable packages, and `plugins/mir/skills/use/SKILL.md` teaches a concrete package workflow. The plugin contains no model code, checkpoint weights or inference runtime. Original research, code authors and weight hosts belong in each package's README, which the skill reads before writing examples.

The top-level README follows the organization order: Why, Acknowledgments, Citation (no single paper), Features, Scope, Install, Quick Start, details, Development, License, Support. Keep its install command aligned with `.claude-plugin/marketplace.json` and the package map aligned with actual public GitHub sources. Run `python3 tools/validate.py` after plugin edits; check example commands against the active plugin and target package README.
