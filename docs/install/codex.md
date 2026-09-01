# Install on Codex

## GitHub CLI (recommended)

Requires `gh` v2.90.0 or later.

```
gh skill install ace-lectures/req-audit bertrand --agent codex --scope user
gh skill install ace-lectures/req-audit frida    --agent codex --scope user
gh skill install ace-lectures/req-audit peggy    --agent codex --scope user
```

Use `--scope project` from inside your document repository to install into its `.agents/skills/`
instead, so the whole team gets them by cloning.

## Manual

```
git clone https://github.com/ace-lectures/req-audit ~/req-audit
mkdir -p ~/.agents/skills
ln -s ~/req-audit/skills/bertrand ~/.agents/skills/bertrand
ln -s ~/req-audit/skills/frida    ~/.agents/skills/frida
ln -s ~/req-audit/skills/peggy    ~/.agents/skills/peggy
```

For a project-scoped install, use `<repo>/.agents/skills/` instead of `~/.agents/skills/`.

Restart Codex — the CLI session, and the IDE extension if you use one — so it loads the new
skills.

## Where they land

| Scope | Path |
|---|---|
| User | `~/.agents/skills/<persona>/` |
| Repository | `<repo>/.agents/skills/<persona>/` |

Codex scans `.agents/skills` in every directory from your working directory up to the repository
root. Note that `~/.codex/` is the personal *configuration* directory — shareable skills go in
`.agents/skills`, not there.

## Use it

Open your document repository and ask for the persona by name — "review G.3 as bertrand", or
invoke it from the slash-command menu.
