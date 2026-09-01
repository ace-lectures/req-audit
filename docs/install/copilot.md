# Install on GitHub Copilot (VS Code, Copilot CLI)

## GitHub CLI (recommended)

Requires `gh` v2.90.0 or later.

```
gh skill install ace-lectures/req-audit bertrand --agent github-copilot --scope user
gh skill install ace-lectures/req-audit frida    --agent github-copilot --scope user
gh skill install ace-lectures/req-audit peggy    --agent github-copilot --scope user
```

Browse before installing with `gh skill install ace-lectures/req-audit` on its own.

Use `--scope project` from inside your document repository to commit the personas alongside the
document, so every team member has them after a clone.

## Manual

```
git clone https://github.com/ace-lectures/req-audit ~/req-audit
mkdir -p ~/.agents/skills
ln -s ~/req-audit/skills/bertrand ~/.agents/skills/bertrand
ln -s ~/req-audit/skills/frida    ~/.agents/skills/frida
ln -s ~/req-audit/skills/peggy    ~/.agents/skills/peggy
```

## Where they land

| Scope | Paths scanned |
|---|---|
| User | `~/.copilot/skills/`, `~/.agents/skills/`, `~/.claude/skills/` |
| Workspace | `.github/skills/`, `.agents/skills/`, `.claude/skills/` |

Any of them works. `.agents/skills/` is the one that also serves Codex, Cursor and Gemini CLI.

## Use it

Open your document repository in VS Code, start an agent-mode chat, and ask for the persona by
name.
