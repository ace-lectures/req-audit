#!/usr/bin/env python3
"""Validate the req-audit skill catalogue.

Checks that every persona skill is a well-formed, self-contained, agent-agnostic Agent Skill
covering the whole document under review. Exits non-zero with one line per problem.

    python3 scripts/validate.py
    python3 scripts/validate.py --template ../cas-handbook-req-template
"""

import argparse
import json
import re
import sys
from pathlib import Path

import sync

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"
PLUGIN = ROOT / ".claude-plugin"

SCOPE_KEY = "req-audit-scope"
SCOPES = {"section", "document"}

BOOKS = {"G": "goals", "E": "environment", "S": "system", "P": "project"}

# Naming any of these inside a skill body would tie it to one agent. Docs and the Claude Code
# plugin manifests are exempt: that is where agent-specific instructions belong.
AGENT_NAMES = ["Claude", "Codex", "Cursor", "Gemini", "Copilot", "ChatGPT", "Anthropic",
               "OpenAI", "Antigravity", "Windsurf", "Cline", "Zed"]

ROW = re.compile(r'^\| ([GESP]\.\d) \| ([^|]+?) \| `([^`]+)` \| `<<(\w+)>>` \| (\d) \|', re.M)

problems = []


def fail(where, message):
    problems.append(f"{where}: {message}")


def frontmatter(path):
    """Parse the frontmatter of a SKILL.md. Handles block scalars and one level of nesting."""
    lines = path.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    fields, key, mode = {}, None, None
    for line in lines[1:end]:
        top = re.match(r'^([A-Za-z][\w-]*):\s*(.*)$', line)
        if top:
            key, value = top.group(1), top.group(2).strip()
            if value in (">", ">-", "|", "|-"):
                fields[key], mode = "", "scalar"
            elif value == "":
                fields[key], mode = {}, "map"
            else:
                fields[key], mode = value, None
        elif key and line.strip():
            nested = re.match(r'^\s+([A-Za-z][\w-]*):\s*(.*)$', line)
            if mode == "map" and nested:
                fields[key][nested.group(1)] = nested.group(2).strip()
            elif mode == "scalar":
                fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def sections():
    """The section inventory, from shared/document-map.md."""
    return ROW.findall((SHARED / "document-map.md").read_text())


def check_inventory(rows):
    where = "shared/document-map.md"
    ids = [r[0] for r in rows]
    if len(ids) != len(set(ids)):
        fail(where, "duplicate section ids")
    if len(ids) != 26:
        fail(where, f"expected 26 sections, found {len(ids)}")
    for sid, _title, path, anchor, milestone in rows:
        letter, number = sid.split(".")
        expected = f"parts/{BOOKS[letter]}/{letter}{number}.adoc"
        if path != expected:
            fail(where, f"{sid}: path is `{path}`, convention says `{expected}`")
        if anchor != f"{letter}{number}".lower():
            fail(where, f"{sid}: anchor is `<<{anchor}>>`, expected `<<{letter.lower()}{number}>>`")
        if milestone not in "123":
            fail(where, f"{sid}: milestone `{milestone}` is not 1, 2 or 3")


def check_skill(skill, rows):
    rel = skill.relative_to(ROOT)
    fields = frontmatter(skill / "SKILL.md")
    if fields is None:
        fail(f"{rel}/SKILL.md", "no YAML frontmatter block at the top of the file")
        return
    for required in ("name", "description"):
        if not fields.get(required):
            fail(f"{rel}/SKILL.md", f"frontmatter is missing `{required}`")

    # Agent Skills spec constraints on name and description.
    name = fields.get("name")
    if isinstance(name, str) and name:
        if name != skill.name:
            fail(f"{rel}/SKILL.md", f"frontmatter name `{name}` != directory `{skill.name}`")
        if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name) or len(name) > 64:
            fail(f"{rel}/SKILL.md",
                 f"name `{name}` breaks the spec: 1-64 lowercase alphanumerics and single hyphens")
    description = fields.get("description")
    if isinstance(description, str) and len(description) > 1024:
        fail(f"{rel}/SKILL.md", f"description is {len(description)} chars, the spec allows 1024")

    metadata = fields.get("metadata")
    scope = metadata.get(SCOPE_KEY) if isinstance(metadata, dict) else None
    if scope not in SCOPES:
        fail(f"{rel}/SKILL.md",
             f"frontmatter needs `metadata.{SCOPE_KEY}` set to one of {sorted(SCOPES)}")
        return

    criteria = skill / "references" / "criteria"
    checks = skill / "references" / "checks"

    if scope == "section":
        if checks.exists():
            fail(str(rel), "section-scoped personas file material under references/criteria/, "
                           "not references/checks/")
        covered = set()
        for letter, book in BOOKS.items():
            path = criteria / f"{book}.md"
            if not path.is_file():
                fail(str(rel), f"missing references/criteria/{book}.md")
                continue
            covered |= set(re.findall(r'^## \(([GESP]\.\d)\)', path.read_text(), re.M))
        if not (criteria / "cross-cutting.md").is_file():
            fail(str(rel), "missing references/criteria/cross-cutting.md")
        for sid in (r[0] for r in rows):
            if sid not in covered:
                fail(str(rel), f"no criteria entry for section {sid}")
    else:
        if criteria.exists():
            fail(str(rel), "document-scoped personas file material under references/checks/, "
                           "not references/criteria/")
        if not (checks / "_index.md").is_file():
            fail(str(rel), "missing references/checks/_index.md")


def check_leakage():
    for path in sorted(list(SKILLS.rglob("*.md")) + list(SHARED.glob("*.md"))):
        text = path.read_text()
        for name in AGENT_NAMES:
            if re.search(rf'\b{name}\b', text):
                fail(str(path.relative_to(ROOT)),
                     f"names the agent `{name}` — skill bodies must stay agent-agnostic")


def check_plugin():
    for name in ("marketplace.json", "plugin.json"):
        path = PLUGIN / name
        if not path.is_file():
            fail(f".claude-plugin/{name}", "missing")
            continue
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            fail(f".claude-plugin/{name}", f"invalid JSON: {exc}")
            continue
        if name == "marketplace.json":
            for entry in data.get("plugins", []):
                source = entry.get("source")
                if not isinstance(source, str):
                    continue
                if not (ROOT / source).is_dir():
                    fail(".claude-plugin/marketplace.json",
                         f"plugin `{entry.get('name')}` source `{source}` does not resolve")


def check_template(template, rows):
    path = Path(template) / ".github" / "course" / "sections.json"
    if not path.is_file():
        fail(str(path), "not found — is --template pointing at cas-handbook-req-template?")
        return
    upstream = {}
    for entry in json.loads(path.read_text()):
        sid = entry["id"]
        if sid.endswith("-update"):
            continue
        upstream[f"{sid[0]}.{sid[1:]}"] = entry["milestone"]
    ours = {r[0]: int(r[4]) for r in rows}
    for sid in sorted(set(upstream) | set(ours)):
        if sid not in ours:
            fail("shared/document-map.md", f"{sid} exists upstream but not here")
        elif sid not in upstream:
            fail("shared/document-map.md", f"{sid} does not exist upstream")
        elif upstream[sid] != ours[sid]:
            fail("shared/document-map.md",
                 f"{sid}: milestone {ours[sid]} here, {upstream[sid]} upstream")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", help="path to a cas-handbook-req-template checkout")
    args = parser.parse_args()

    rows = sections()
    check_inventory(rows)

    skills = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not skills:
        fail("skills/", "no skills found")
    for skill in skills:
        if not (skill / "SKILL.md").is_file():
            fail(str(skill.relative_to(ROOT)), "directory has no SKILL.md")
            continue
        check_skill(skill, rows)

    if sync.main(["sync.py", "--check"]):
        fail("skills/*/references", "generated copies are out of date")

    check_leakage()
    check_plugin()
    if args.template:
        check_template(args.template, rows)

    for problem in problems:
        print(problem, file=sys.stderr)
    print(f"{len(problems)} problem(s); {len(skills)} skill(s), {len(rows)} section(s) checked",
          file=sys.stderr if problems else sys.stdout)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
