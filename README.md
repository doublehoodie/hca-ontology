# HCA Ontology Thesis Build

Master's thesis project (I/O Psychology) building a thin-slice occupation ontology from **O\*NET 30.3** task→skill structure, with optional ESCO / ISCO crosswalk evidence. Repo: [doublehoodie/hca-ontology](https://github.com/doublehoodie/hca-ontology).

This repository contains:

- Reproducible Python scripts for a **five-occupation** O\*NET slice and a **Task → DWA → IWA → GWA → Skill** derivation (no imputed edges)
- Documentation of data inventory, coverage gaps, edge quality audit, and crosswalk evidence
- A Protégé-authored schema at [`ontology/schema.ttl`](ontology/schema.ttl)
- A five-day build runbook ([`five-day-build-runbook.md`](five-day-build-runbook.md))

## Research question

TODO

## Findings and their interpretation

TODO

## Known limitations

TODO

---

## Occupations in the thin slice

Exact O\*NET-SOC codes used by [`scripts/01_extract_slice.py`](scripts/01_extract_slice.py):

| O\*NET-SOC Code | Title |
|---|---|
| `15-1252.00` | Software Developers |
| `15-2051.00` | Data Scientists |
| `15-1254.00` | Web Developers |
| `15-1242.00` | Database Administrators |
| `15-1212.00` | Information Security Analysts |

Filter column (verified against inventory): `O*NET-SOC Code`.

## Repository structure

```
.
├── data/
│   ├── raw/              # gitignored — re-fetch (see Data sources)
│   ├── interim/          # five-occupation CSV slices (*_slice.csv)
│   └── processed/        # task_skill_derived.csv
├── docs/                 # inventories, audits, crosswalk evidence
├── ontology/
│   └── schema.ttl        # Day 3 Protégé schema (Turtle)
├── scripts/
│   ├── 00_inspect.py
│   ├── 01_extract_slice.py
│   └── 02_task_skill_chain.py
├── notebooks/            # empty placeholder directory
├── five-day-build-runbook.md
└── README.md
```

Local-only / untracked (not in git): Word notes, screenshots, large RDF/ZIP dumps, and **`occo.owl`** (see below).

## Reproduce the pipeline

Requires Python 3 (developed with system Python 3.9.x). There is **no** `requirements.txt` in the repo yet; packages installed for this build were:

```text
pandas openpyxl xlrd owlready2 rdflib requests
```

(`xlrd` is needed to read `ISCO_SOC_Crosswalk.xls`.)

### 1. Clone and environment

```bash
git clone https://github.com/doublehoodie/hca-ontology.git
cd hca-ontology
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pandas openpyxl xlrd owlready2 rdflib requests
```

### 2. Populate `data/raw/` (gitignored)

Create directories:

```bash
mkdir -p data/raw/esco data/interim data/processed docs scripts ontology
```

**O\*NET 30.3 CSV** (from `https://www.onetcenter.org/dl_files/database/db_30_3_csv/`):

`occupation_data.csv`, `job_zones.csv`, `job_titles.csv`, `sample_of_reported_titles.csv`, `related_occupations.csv`, `task_statements.csv`, `task_ratings.csv`, `task_categories.csv`, `tasks_to_dwas.csv`, `gwas_to_iwas_to_dwas.csv`, `gwas_to_iwas.csv`, `work_activities.csv`, `essential_skills.csv`, `transferable_skills.csv`, `knowledge.csv`, `abilities.csv`, `essential_skills_to_work_activities.csv`, `transferable_skills_to_work_activities.csv`, `abilities_to_work_activities.csv`, `software_skills.csv`, `content_model_reference.csv`, `scales_reference.csv`, `occupation_level_metadata.csv`

Also:

- `https://www.onetcenter.org/dl_files/30_3_migration_reference.xlsx` → `data/raw/30_3_migration_reference.xlsx`
- **Tools Used (frozen 30.2):** the runbook’s `db_30_2_csv/tools_used.csv` URL 404s. This build used `Tools Used.txt` extracted from `https://www.onetcenter.org/dl_files/database/db_30_2_text.zip` (member path `db_30_2_text/Tools Used.txt`; tab-separated). Place as `data/raw/Tools Used.txt`.

**ESCO v1.2.1** English CSV package → unzip into `data/raw/esco/` (files such as `occupations_en.csv`, `skills_en.csv`, `occupationSkillRelations_en.csv`, …).

**BLS crosswalks** → `data/raw/`:

- `soc_2010_to_2018_crosswalk.xlsx`
- `ISCO_SOC_Crosswalk.xls`

### 3. Run scripts (in order)

From the repo root, with `.venv` activated:

```bash
# Column / row inventory → docs/column_inventory.txt
python scripts/00_inspect.py > docs/column_inventory.txt

# Five-occupation slices → data/interim/*_slice.csv
python scripts/01_extract_slice.py

# Task→DWA→GWA→Skill chain → data/processed/task_skill_derived.csv
# Also regenerates docs/task_skill_gaps.md
python scripts/02_task_skill_chain.py
```

**Join keys used by the chain** (must match inventory; do not substitute lookalikes):

1. `Task ID` — `task_statements_slice` ⋉ `tasks_to_dwas`
2. `DWA Element ID` — result ⋉ `gwas_to_iwas_to_dwas`
3. `GWA Element ID` = `Work Activities Element ID` — result ⋉ essential/transferable `*_skills_to_work_activities`
4. `O*NET-SOC Code` + `Skill Element ID` + `skill_kind` — result ⋉ skill rating slices

Missing hops stay **null** (reported in `docs/task_skill_gaps.md`); nothing is imputed.

### 4. Expected pipeline outputs (as of last run in this workspace)

| Artifact | Notes |
|---|---|
| `data/interim/occupation_data_slice.csv` | 5 rows (one per occupation) |
| `data/interim/task_statements_slice.csv` | 91 task rows |
| `data/processed/task_skill_derived.csv` | **610** structural edges; 25 distinct `Skill Element ID`s; provenance columns `data_source`, `source_version`, `derivation`, `skill_kind`, hop IDs, optional Importance/Level |

## Docs index

| File | Contents |
|---|---|
| [`docs/day1-2_plan.md`](docs/day1-2_plan.md) | Approved Day 1–2 execution plan through Call #1 |
| [`docs/column_inventory.txt`](docs/column_inventory.txt) | Row counts and column lists for `data/raw/` (and ESCO), plus join-key checklist |
| [`docs/task_skill_gaps.md`](docs/task_skill_gaps.md) | Per-hop null counts and per-occupation edge/importance coverage after the chain |
| [`docs/data_coverage.md`](docs/data_coverage.md) | Empirical confirmation that `15-2051.00` has zero skill/ability/knowledge/WA/task_ratings rows; 29 occupations share that pattern |
| [`docs/edge_audit.md`](docs/edge_audit.md) | Importance-ranked skills per occupation + 10-task hand review tables (P/I/G) |
| [`docs/edge_coverage_stats.md`](docs/edge_coverage_stats.md) | Zero-skill task count, edges-per-task distribution, skill vocabulary coverage, GWA funnel |
| [`docs/software_linkage_feasibility.md`](docs/software_linkage_feasibility.md) | Investigation: no O\*NET 30.3 file links software/tools to tasks or DWAs |
| [`docs/crosswalk.md`](docs/crosswalk.md) | SOC 2010↔2018 / ISCO / ESCO evidence pack; Call #1 decision cells blank |

## Data sources (versions and licenses)

| Source | Version / form | Role in this repo | License |
|---|---|---|---|
| [O\*NET Database](https://www.onetcenter.org/database.html) | **30.3** CSV (`db_30_3_csv`) | Occupation spine, tasks, skills, WA linkages, software | **CC BY** (as used for this project) |
| O\*NET Tools Used | **30.2** text release (`Tools Used.txt`) | Frozen tools/equipment examples (discontinued in 30.3) | TODO confirm whether same CC BY terms as database |
| [ESCO](https://esco.ec.europa.eu/en/use-esco/download) | **v1.2.1** English CSV | Occupation candidates / skill relations for crosswalk evidence | TODO record exact ESCO redistribution terms from the download package |
| BLS SOC crosswalks | SOC 2010↔2018 (`.xlsx`); ISCO-08↔2010 SOC (`.xls`) | Bridge O\*NET-SOC 2018 → ISCO → ESCO | TODO record BLS terms of use |

Raw files live under `data/raw/` and are **not** committed (see gitignore).

## What is gitignored (and why)

From [`.gitignore`](.gitignore):

| Pattern | Why |
|---|---|
| `data/raw/` | Large redistributable source dumps; scripts + docs are the reproducible artifact — re-fetch with attribution |
| `.venv/` | Local virtualenv |
| `__pycache__/`, `*.pyc` | Python bytecode |
| `*.rdf`, `*.zip` | Very large ESCO/RDF archives (local copies may exist outside git) |
| `.DS_Store`, `~$*` | OS / Office lockfiles |

## Untracked local reference: `occo.owl`

**Not committed** to this repository. Local copy on disk (filesystem date 2025-07-09 in this workspace).

From the file’s ontology header:

| Field | Value |
|---|---|
| Title | Occupation Ontology (**OccO**) |
| IRI | `http://purl.obolibrary.org/obo/occo.owl` |
| `owl:versionInfo` | `1.0.66` / `2025-10-06` |
| `owl:versionIRI` | `http://purl.obolibrary.org/obo/occo/releases/2025-10-06/occo.owl` |
| License | Creative Commons Attribution 4.0 (`http://creativecommons.org/licenses/by/4.0/`) |
| Description (excerpt) | Ontology of human occupations based on BLS SOC and the related O\*NET system; developed following OBO Foundry principles |
| Creators (from header) | Damion Dooley, Jie Zheng, John Beverley, John Judkins, Matthew Diller, Oliver He, Sam Smith, William Duncan, William R. Hogan; contributor Eric Merrell |

How this local file was obtained (download URL / mirror) is **TODO** if not recorded elsewhere in your notes.

## Ontology schema (`ontology/schema.ttl`)

Hand-authored in Protégé (OWL API export note in file: OWL API 4.5.29). Ontology IRI in file: `http://hcaontology.org/yanzhou/ontologies/`.

**Classes present:** `Occupation`, `Task`, `Skill`, `EssentialSkill`, `TransferableSkill`, `Knowledge`, `Ability`, `WorkActivity`, `GWA`, `IWA`, `DWA`, `Software`, `Tool`, `Credential`, `IssuingBody`, `SourceRecord`, `RegulatedOccupation` (defined class).

**Notable axioms:** `requiresSkill` property-chain involving `performsTask`; pairwise disjointness of `Occupation`, `Skill`, `Software`, `Task`, `Tool`.

The file also contains a small set of **example named individuals** (e.g. `SoftwareDeveloper`, `WriteCode`, `Programming`) used while authoring — not the populated O\*NET slice.

## Current status

| Area | Status |
|---|---|
| Day 1 — env, raw acquisition, column inventory | Done (raw kept local / gitignored) |
| Day 2 — five-occupation slice + task→skill chain | Done (`task_skill_derived.csv`, 610 edges) |
| Edge quality hand audit (`docs/edge_audit.md`) | Partially scored (P/I/G on 10-task sample; some cells still blank) |
| Crosswalk Call #1 (Data Scientists mapping) | **Open** — evidence in `docs/crosswalk.md`; decision cells blank |
| Day 3 — Protégé schema | `ontology/schema.ttl` present |
| Day 4 — populate individuals from slice / reasoner | **Not started** (no `scripts/03_populate.py` in repo) |
| Day 5 — CQ validation / demo | **Not started** |

Open judgment calls from the runbook that still need the author (not automated): Call #1 (Data Scientists ESCO/ISCO mapping), Call #2 (O\*NET essential/transferable vs ESCO essential/optional), Call #3 (how much to trust / threshold derived edges).
