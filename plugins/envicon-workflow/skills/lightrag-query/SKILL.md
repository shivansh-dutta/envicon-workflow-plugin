---
name: lightrag-query
description: Query a LightRAG index built from ingested EDR documents. Use when searching EDR corpus for sites, contaminants, or regulatory records during Phase 1 research.
---

# LightRAG Query (EDR)

Search an ingested EDR corpus. Requires prior `lightrag-ingest` on the same project.

## Query

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/lightrag/query.py "Projects/<name>" "your question here"
```

### Options

```bash
# Hybrid mode (default) — best for most EDR searches
python .../query.py "Projects/<name>" "UST releases within 500 ft" --mode hybrid

# JSON output for structured downstream use
python .../query.py "Projects/<name>" "NPL sites downgradient" --json
```

Modes: `naive`, `local`, `global`, `hybrid`, `mix`.

## Example questions

- "List petroleum spill sites within 1000 feet of the subject property"
- "What NYS DEC registered tanks are reported upgradient?"
- "Summarize historical industrial uses mentioned in the EDR"

## Use results in Obsidian

Format query hits as EDR notes using `obsidian-vault-setup` template in `EDR_Database_Hits/`.

## Guardrails

- Verify index exists (`Projects/<name>/.lightrag/`) before querying.
- Cross-check LightRAG answers against source PDF pages — RAG is assistive, not authoritative.
- Prefer `--mode hybrid` for EDR database searches.
