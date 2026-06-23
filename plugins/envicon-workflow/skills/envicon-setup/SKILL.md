---
name: envicon-setup
description: Verify prerequisites for Envicon workflow plugins (OpenSpec CLI, Node, Python, LightRAG deps). Use when onboarding a new machine or troubleshooting missing tools before running workflow skills.
---

# Envicon Setup

Run these checks before using other `envicon-workflow` skills.

## Steps

1. **Node.js** — required for OpenSpec and claude-mem:
   ```bash
   node --version
   ```

2. **OpenSpec CLI** — install if missing:
   ```bash
   npm install -g @fission-ai/openspec@latest
   openspec --version
   ```

3. **Python 3.10+** — required for LightRAG scripts:
   ```bash
   python --version
   ```

4. **LightRAG dependencies** — from the plugin root (`${CLAUDE_PLUGIN_ROOT}`):
   ```bash
   pip install -r scripts/lightrag/requirements.txt
   ```

5. **Project OpenSpec init** — in the target project repo (once per project):
   ```bash
   openspec init --tools claude
   ```

6. **claude-mem** — confirm installed:
   ```
   /plugin list
   ```
   Expect `claude-mem@envicon-workflow` enabled. Worker should start on session start.

## Report

Summarize pass/fail for each check. If any fail, give the exact install command and stop before running workflow skills.
