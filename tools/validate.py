"""Self-test for this marketplace repo: marketplace.json parses and points at
real plugins; every SKILL.md has valid frontmatter (name + description).
Run: python tools/validate.py (exits non-zero on any failure)."""
import json, sys, re
from pathlib import Path

root = Path(__file__).parent.parent
errors = []

mp = json.loads((root / '.claude-plugin' / 'marketplace.json').read_text())
for plugin in mp['plugins']:
    src = root / plugin['source']
    if not (src / 'CLAUDE.md').is_file():
        errors.append(f"{plugin['name']}: missing CLAUDE.md at {src}")
    skills = list((src / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append(f"{plugin['name']}: no skills found under {src}/skills")
    for sk in skills:
        text = sk.read_text()
        m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
        if not m:
            errors.append(f"{sk}: missing frontmatter block")
            continue
        fm = m.group(1)
        for field in ('name:', 'description:'):
            if field not in fm:
                errors.append(f"{sk}: frontmatter missing {field}")

for e in errors:
    print(f"FAIL: {e}")
print(f"{'FAILED' if errors else 'OK'}: {len(mp['plugins'])} plugins checked")
sys.exit(1 if errors else 0)
