# Install on Cursor

## GitHub CLI (recommended)

Requires `gh` v2.90.0 or later.

```
gh skill install ace-lectures/req-audit bertrand --agent cursor --scope user
gh skill install ace-lectures/req-audit frida    --agent cursor --scope user
gh skill install ace-lectures/req-audit peggy    --agent cursor --scope user
```

Use `--scope project` from inside your document repository for a project-scoped install that your
teammates get by cloning.

## Manual

```
git clone https://github.com/ace-lectures/req-audit ~/req-audit
mkdir -p ~/.agents/skills
ln -s ~/req-audit/skills/bertrand ~/.agents/skills/bertrand
ln -s ~/req-audit/skills/frida    ~/.agents/skills/frida
ln -s ~/req-audit/skills/peggy    ~/.agents/skills/peggy
```

## Where they land

| Scope | Path |
|---|---|
| User | `~/.agents/skills/<persona>/` — or `~/.cursor/skills/<persona>/` |
| Project | `<repo>/.agents/skills/<persona>/` — or `<repo>/.cursor/skills/<persona>/` |

Cursor also reads `.claude/skills/` and `.codex/skills/` for compatibility, so an install done for
another agent is usually already visible here. Prefer `.agents/skills/` — one folder serves every
agent that reads the shared convention.

## Use it

Open your document repository and ask the agent for the persona by name — with a section id for `bertrand` and `frida`.
