---
name: lightrag-ingest
description: Ingest EDR PDFs from a Phase 1 project Raw/ folder into a LightRAG knowledge graph index. Use for on-demand EDR document ingestion before Scout/Researcher work. Requires OPENAI_API_KEY.
---

# LightRAG Ingest (EDR)

On-demand ingestion of EDR PDFs into a per-project LightRAG index. **Run manually** to control API credit usage.

## Prerequisites

1. Run `envicon-setup` or verify Python deps:
   ```bash
   pip install -r ${CLAUDE_PLUGIN_ROOT}/scripts/lightrag/requirements.txt
   ```
2. Set `OPENAI_API_KEY` in `.env` or environment (LightRAG embeddings + LLM).
3. Project folder exists with EDR PDF in `Raw/`:
   ```
   Projects/<name>/Raw/YourEDRReport.pdf
   ```

## Ingest

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/lightrag/ingest.py "Projects/<name>"
```

Use an absolute path to the project folder if not cwd-relative.

## Output

Index written to:

```
Projects/<name>/.lightrag/
```

This directory is gitignored. Re-run ingest after swapping the EDR PDF.

## After ingestion

Use `lightrag-query` to search the corpus, or feed results into Obsidian EDR hit notes.

## Guardrails

- One EDR PDF per project in `Raw/` (Phase 1 convention).
- Scanned pages with no extractable text are skipped silently.
- Do not auto-run ingest in loops — user must request explicitly.
