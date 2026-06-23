# envicon-workflow plugin

Claude Code skills for Envicon Phase 1 workflows.

## Skills

| Skill | Purpose |
|-------|---------|
| `envicon-setup` | Verify prerequisites |
| `openspec-explore` | Think through ideas before spec'ing |
| `openspec-propose` | Create change proposal + artifacts |
| `openspec-apply-change` | Implement from tasks |
| `openspec-archive-change` | Archive completed change |
| `openspec-sync-specs` | Sync delta specs to main |
| `obsidian-vault-setup` | Phase 1 vault structure |
| `obsidian-report-review` | PE review + Pandoc export |
| `lightrag-ingest` | Index EDR PDFs |
| `lightrag-query` | Search EDR corpus |

Invoke as `/envicon-workflow:<skill-name>` after install.

## Scripts

- `scripts/lightrag/ingest.py` — PDF text extraction + LightRAG indexing
- `scripts/lightrag/query.py` — hybrid RAG queries

Requires `OPENAI_API_KEY` for LightRAG (embeddings + LLM).

## Per-project setup

```bash
openspec init --tools claude
pip install -r scripts/lightrag/requirements.txt
```
