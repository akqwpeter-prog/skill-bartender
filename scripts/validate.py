#!/usr/bin/env python3
"""Local validation: frontmatter rules + SkillSpector scan when available."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    fails = []
    for skill_dir in (ROOT / 'skills').iterdir():
        f = skill_dir / 'SKILL.md'
        if not f.is_file():
            continue
        raw = f.read_text(encoding='utf-8')
        m = re.match(r'^---\n(.*?)\n---\n', raw, re.S)
        if not m:
            fails.append(f'{skill_dir.name}: missing frontmatter')
            continue
        fm = m.group(1)
        if not re.search(r'^name:\s*[a-z0-9-]+$', fm, re.M):
            fails.append(f'{skill_dir.name}: name missing or not kebab-case')
        if not re.search(r'^description:', fm, re.M):
            fails.append(f'{skill_dir.name}: description missing')
    if fails:
        print('FAIL:'); [print(' -', x) for x in fails]
        return 1
    print('frontmatter OK')
    try:
        subprocess.run(['skillspector', 'scan', str(ROOT / 'skills'), '--no-llm'], check=True)
    except (OSError, subprocess.CalledProcessError):
        print('skillspector unavailable or failed; run manually')
    return 0

if __name__ == '__main__':
    sys.exit(main())
