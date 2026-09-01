#!/usr/bin/env python3
"""Copy shared/ material into every persona skill's references/ directory.

A skill folder must be self-contained: `gh skill install <repo> <skill>` copies only that
folder, so a reference to ../../shared/ would break on install. shared/ stays the single source
of truth and this script materialises it into each skill.

    python3 scripts/sync.py            # write the copies
    python3 scripts/sync.py --check    # exit 1 if any copy is missing or stale
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"

BANNER = "<!-- GENERATED from shared/{name} by scripts/sync.py — do not edit. -->"


def render(source: Path) -> str:
    return BANNER.format(name=source.name) + "\n\n" + source.read_text()


def targets():
    """Yield (source, destination) for every shared file and every skill."""
    for skill in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file()):
        for source in sorted(SHARED.glob("*.md")):
            yield source, skill / "references" / source.name


def main(argv):
    check = "--check" in argv[1:]
    stale = []

    for source, dest in targets():
        want = render(source)
        if check:
            have = dest.read_text() if dest.is_file() else None
            if have != want:
                stale.append((dest, "missing" if have is None else "stale"))
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(want)

    if not check:
        return 0

    for dest, why in stale:
        print(f"{dest.relative_to(ROOT)}: {why} — run `make sync`", file=sys.stderr)
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
