# Envicon Workflow Plugin

Org-shareable Claude Code marketplace bundling:

- **envicon-workflow** — OpenSpec, Obsidian vault, and LightRAG skills
- **claude-mem** — persistent memory and context compression (pinned companion)

## Quick install

```text
/plugin marketplace add <org>/envicon-workflow-plugin
/plugin install envicon-workflow@envicon-workflow
/plugin install claude-mem@envicon-workflow
```

Replace `<org>` with your GitHub organization or username.

## Prerequisites (each developer, once)

```bash
# OpenSpec
npm install -g @fission-ai/openspec@latest

# LightRAG Python deps
pip install -r plugins/envicon-workflow/scripts/lightrag/requirements.txt
```

Set `OPENAI_API_KEY` for LightRAG scripts. Claude Code and Node.js are required for claude-mem.

## Per-project setup

In any repo where you use these skills:

```bash
openspec init --tools claude
```

## Skill cheat sheet

| Task | Skill |
|------|-------|
| Check tooling | `/envicon-workflow:envicon-setup` |
| Explore an idea | `/envicon-workflow:openspec-explore` |
| Propose a change | `/envicon-workflow:openspec-propose` |
| Implement tasks | `/envicon-workflow:openspec-apply-change` |
| Archive change | `/envicon-workflow:openspec-archive-change` |
| New Phase 1 vault | `/envicon-workflow:obsidian-vault-setup` |
| PE review / export | `/envicon-workflow:obsidian-report-review` |
| Index EDR PDF | `/envicon-workflow:lightrag-ingest` |
| Search EDR corpus | `/envicon-workflow:lightrag-query` |
| Compress context | `/compact` (claude-mem auto-injects memory) |

## Updates

```text
/plugin marketplace update envicon-workflow
/plugin update envicon-workflow@envicon-workflow
/plugin update claude-mem@envicon-workflow
```

## Local development

```bash
claude plugin validate .
cc --plugin-dir ./plugins/envicon-workflow
```

Test marketplace install:

```text
/plugin marketplace add C:\path\to\envicon-workflow-plugin
/plugin install envicon-workflow@envicon-workflow
```

## Org-wide rollout (Jason / admin)

Add to managed settings so the marketplace auto-registers:

```json
{
  "extraKnownMarketplaces": {
    "envicon-workflow": {
      "source": { "source": "github", "repo": "<org>/envicon-workflow-plugin" }
    }
  },
  "enabledPlugins": {
    "envicon-workflow@envicon-workflow": true,
    "claude-mem@envicon-workflow": true
  }
}
```

If `strictKnownMarketplaces` is enabled, add `<org>/envicon-workflow-plugin` to the allowlist.

### Project-level nudge

Add to shared repos' `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "envicon-workflow": {
      "source": { "source": "github", "repo": "<org>/envicon-workflow-plugin" }
    }
  },
  "enabledPlugins": {
    "envicon-workflow@envicon-workflow": true,
    "claude-mem@envicon-workflow": true
  }
}
```

## What's not in v1

- Caveman (test post-KH proposal)
- Phase 1 Automator (paused)
- DWG text organizer (paused)

## Versioning

Bump `version` in both:

- `plugins/envicon-workflow/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json` (envicon-workflow entry)

Re-pin `claude-mem` `ref` in marketplace.json for org-wide memory updates.
