# Install on Gemini CLI

## GitHub CLI (recommended)

Requires `gh` v2.90.0 or later.

```
gh skill install ace-lectures/req-audit bertrand --agent gemini-cli --scope user
gh skill install ace-lectures/req-audit frida    --agent gemini-cli --scope user
gh skill install ace-lectures/req-audit peggy    --agent gemini-cli --scope user
```

Use `--scope project` from inside your document repository for a workspace-scoped install.

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
| User | `~/.agents/skills/<persona>/`, or `~/.gemini/skills/<persona>/` |
| Workspace | `<repo>/.agents/skills/<persona>/`, or `<repo>/.gemini/skills/<persona>/` |

Both locations work. `.agents/skills/` is the shared convention and takes precedence when a skill
name appears in both, so prefer it. The same folder then also serves Codex, Cursor and Copilot.

## Use it

Start the CLI in your document repository and ask for the persona by name, with a section id for `bertrand` and `frida`.
