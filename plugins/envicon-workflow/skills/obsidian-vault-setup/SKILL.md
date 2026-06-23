---
name: obsidian-vault-setup
description: Set up or explain the Phase 1 Obsidian vault structure (LegalVault, TemplateVault, Projects, EDR hits, dashboard transclusion). Use when starting a new Phase 1 project, initializing vault folders, or answering vault layout questions.
---

# Obsidian Vault Setup (Phase 1 ESA)

Guide the user through Envicon's Obsidian-based Phase 1 report workflow.

## Vault root

The **vault root** is the project repository root (e.g. Phase 1 Report Generator checkout). In Obsidian: **Open folder as vault** → select that root.

## Directory layout

```
<repo-root>/
├── LegalVault/              # Regulatory reference (PE-verified stubs)
├── TemplateVault/           # Blank section templates + EDR hit template
├── Projects/
│   └── <project-name>/
│       ├── Raw/             # EDR PDF + site photos
│       ├── EDR_Database_Hits/
│       ├── Historical_Records/
│       ├── Report_Sections/
│       ├── Site_Notes/
│       ├── Export/
│       ├── 00_Project_Dashboard.md
│       └── scout_keywords.json
```

## Initialize a new project

If `scripts/init_project.py` exists in the repo:

```bash
python scripts/init_project.py --name "<project-name>" --address "<site address>"
```

Otherwise create `Projects/<project-name>/` manually and copy section templates from `TemplateVault/` into `Report_Sections/`.

## Dashboard transclusion

`00_Project_Dashboard.md` assembles the full report via Obsidian embeds:

```markdown
![[Report_Sections/01_Executive_Summary]]
![[Report_Sections/02_Site_Description]]
![[Report_Sections/03_Historical_Review]]
![[Report_Sections/04_Regulatory_Review]]
![[Report_Sections/05_Site_Reconnaissance]]
![[Report_Sections/06_Interviews]]
![[Report_Sections/07_Findings]]
![[Report_Sections/08_Conclusions]]
```

Adjust section filenames to match `TemplateVault/` naming in the repo.

## EDR hit note template

New hits in `EDR_Database_Hits/` follow `TemplateVault/EDR_Hit_Template.md`:

```yaml
---
site_name: ""
address: ""
database_source: ""
distance_ft: null
direction: ""
program_id: ""
status: ""
nysdec_program: ""
preliminary_classification: ""
---

# EDR Hit: <site name>

## Raw Extract
<!-- verbatim EDR text -->

## Assessment Notes
<!-- DRAFT: REC/CREC/HREC classification narrative -->
```

## LegalVault PE review

`LegalVault/` files ship with `last_verified: NEEDS_VERIFICATION`. A licensed PE must review each regulatory file and set a real date before the Writer agent produces citable output.

Run vault check if available:

```bash
python scripts/check_vault.py
```

## Guardrails

- Do not rename vault folders without updating pipeline scripts.
- Keep exactly one EDR PDF in `Raw/` per project.
- Site photos: `.jpg`, `.jpeg`, `.png`, `.tiff`, `.webp` in `Raw/`.
