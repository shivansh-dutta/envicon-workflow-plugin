---
name: obsidian-report-review
description: Guide PE review of drafted Phase 1 sections in Obsidian and export to docx via Pandoc. Use when reviewing report drafts, filling placeholders, or preparing final export.
---

# Obsidian Report Review & Export

## Open the project in Obsidian

1. Launch Obsidian → **Open folder as vault**
2. Select the repository root (contains `LegalVault/`, `Projects/`)
3. Navigate to `Projects/<project-name>/00_Project_Dashboard.md`

The dashboard transcludes all 8 section files. Edits in embedded sections update the source files.

## PE review checklist

For each section in `Report_Sections/`:

- [ ] Banner present: `> **DRAFT — PE REVIEW REQUIRED**`
- [ ] All `<!-- FILL IN MANUALLY: ... -->` blocks completed
- [ ] All `<!-- DRAFT: ... -->` AI narratives reviewed and corrected
- [ ] Regulatory citations trace to verified `LegalVault/` files
- [ ] EDR hits in `EDR_Database_Hits/` have classification (REC/CREC/HREC/De Minimis)
- [ ] Executive Summary findings table matches Section 07

## Navigate related content

| Location | Purpose |
|----------|---------|
| `EDR_Database_Hits/` | Per-site database records from EDR |
| `Historical_Records/` | Historical source observations |
| `Site_Notes/` | PE scratch notes |
| `_writer_notes.md` | Writer agent session notes |

Use Obsidian wikilinks `[[note-name]]` to cross-reference hits and sections.

## Export to Word

After PE review is complete, run export (paths assume Phase 1 Report Generator layout):

```bash
python pipeline.py --project Projects/<project-name> --phase export
```

Output:

```
Projects/<project-name>/Export/<project-name>_Phase1_ESA_DRAFT.docx
```

Optional PDF:

```bash
python pipeline.py --project Projects/<project-name> --phase export --pdf
```

**Note:** Pandoc does not resolve Obsidian `![[]]` transclusion. Export concatenates section markdown files directly — ensure section files are complete before export.

## Prerequisites

- Pandoc installed: https://pandoc.org/installing.html
- `TemplateVault/pandoc/reference.docx` present for styled output

## Guardrails

- Do not export until PE review placeholders are filled.
- Export phase may skip vault check — only run after citations are verified.
