# Team Install Guide — Envicon Workflow Plugin

Share this with anyone who needs Claude Code workflow skills.

## 1. Install plugins

In Claude Code:

```text
/plugin marketplace add <org>/envicon-workflow-plugin
/plugin install envicon-workflow@envicon-workflow
/plugin install claude-mem@envicon-workflow
```

## 2. One-time machine setup

```bash
npm install -g @fission-ai/openspec@latest
pip install -r <path-to-claude-plugins-cache>/envicon-workflow/.../scripts/lightrag/requirements.txt
```

Or after install, run `/envicon-workflow:envicon-setup` — it will print exact paths.

Set environment variables:

- `OPENAI_API_KEY` — for LightRAG ingest/query
- `ANTHROPIC_API_KEY` — for Claude Code sessions (if not using Claude subscription)

## 3. Per-project init

In your project repo:

```bash
openspec init --tools claude
```

## 4. Daily workflow

| When | What |
|------|------|
| Starting work | `/compact` if context is heavy; claude-mem recalls prior sessions |
| New feature | `/envicon-workflow:openspec-propose` |
| Implementing | `/envicon-workflow:openspec-apply-change` |
| Phase 1 project | `/envicon-workflow:obsidian-vault-setup` |
| EDR search (on demand) | ingest then query skills |
| PE review | `/envicon-workflow:obsidian-report-review` |

## 5. For Jason (org admin)

To auto-enable for everyone, add to managed settings:

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

If marketplace allowlisting is enforced, add `<org>/envicon-workflow-plugin` to `strictKnownMarketplaces`.

## Support

Full docs: [README.md](README.md)
