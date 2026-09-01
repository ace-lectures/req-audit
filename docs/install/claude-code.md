# Install on Claude Code

Two routes. The plugin marketplace installs all three personas at once and keeps them
updatable; the GitHub CLI route installs one persona at a time.

## Marketplace (recommended)

In Claude Code, from any directory:

```
/plugin marketplace add ace-lectures/req-audit
/plugin install req-audit@ace-lectures
```

This installs all three personas. The install command opens a details view where you pick a scope. Choose **user** if you want the
personas available in every project, or **project** to pin them to your document repository.

Then invoke a persona by name:

```
/req-audit:bertrand
/req-audit:frida
/req-audit:peggy
```

To update later:

```
/plugin marketplace update ace-lectures
```

## GitHub CLI

Requires `gh` v2.90.0 or later.

```
gh skill install ace-lectures/req-audit bertrand --agent claude-code --scope user
gh skill install ace-lectures/req-audit frida    --agent claude-code --scope user
gh skill install ace-lectures/req-audit peggy    --agent claude-code --scope user
```

Use `--scope project` from inside your document repository to install into its `.claude/skills/`
instead. Invoked as `/bertrand`, `/frida` and `/peggy`.

## Manual

```
git clone https://github.com/ace-lectures/req-audit ~/req-audit
mkdir -p ~/.claude/skills
ln -s ~/req-audit/skills/bertrand ~/.claude/skills/bertrand
ln -s ~/req-audit/skills/frida    ~/.claude/skills/frida
ln -s ~/req-audit/skills/peggy    ~/.claude/skills/peggy
```

Claude Code picks up new skills without a restart, unless the `skills` directory itself did not
exist when the session started.

## Where they land

| Scope | Path |
|---|---|
| User | `~/.claude/skills/<persona>/` |
| Project | `<repo>/.claude/skills/<persona>/` |

## Check it worked

Run `/skills`. `bertrand`, `frida` and `peggy` should be listed. All three are marked
`disable-model-invocation`, so they never activate on their own: you always choose the persona.
