# Software / tools ↔ task linkage feasibility

**Investigation only** — no pipeline built. Question: can task→software (or task→tool) edges be derived from O\*NET 30.3 the way task→skill edges were?

## Bottom line

**No.** In the downloaded O\*NET 30.3 CSV set (plus frozen 30.2 `Tools Used.txt`), there is **no file that links software or tools to tasks, DWAs, IWAs, or work activities**. Software and tools are **occupation-level only**. A defensible task→software edge cannot be derived from source rows without inventing a linkage.

## What exists (occupation-level)

| File | Grain | Columns (relevant) |
|---|---|---|
| `software_skills.csv` | occupation × workplace example × software category | `O*NET-SOC Code`, `Workplace Example`, `Element ID`, `Element Name`, `Hot Technology`, `In Demand` |
| `Tools Used.txt` (from 30.2 text zip; discontinued in 30.3) | occupation × tool example × UNSPSC commodity | `O*NET-SOC Code`, `Example`, `Commodity Code`, `Commodity Title` |

Neither file contains `Task ID`, `DWA Element ID`, `IWA Element ID`, or `GWA Element ID` / Work Activities Element ID.

## Files that *do* mention tasks or DWAs

| File | Has Task ID? | Has software/tool fields? |
|---|---|---|
| `task_statements.csv` | yes | no |
| `task_ratings.csv` | yes | no |
| `tasks_to_dwas.csv` | yes (+ DWA) | no |
| `gwas_to_iwas_to_dwas.csv` | no (activity hierarchy only) | no |
| `essential_skills_to_work_activities.csv` | no | no (skills ↔ WA only) |
| `transferable_skills_to_work_activities.csv` | no | no |
| `abilities_to_work_activities.csv` | no | no |

**Intersection check:** no CSV in `data/raw/` contains both `Task ID` and any of `Workplace Example` / `Commodity Code` / `Hot Technology`.

## How software sits in the Content Model

From `content_model_reference.csv`:

```
2          Worker Requirements
└─ 2.E     Software Skills
   ├─ 2.E.1 … 2.E.17   category branches (e.g. Development software, Data management…)
   └─ 2.E.x.y          leaf categories (e.g. 2.E.7.b Development environment software)
```

- `software_skills.csv` rows point at **leaf/category Element IDs under `2.E`**, plus a free-text `Workplace Example` (product name).
- That is a **taxonomy of software types**, not a bridge to Tasks (`5.A`) or Work Activities (`4.A`).
- Tasks live under Occupation-Specific Information (`5.A`); work activities under `4.A.*`. No Content Model parent/child edge connects `2.E.*` to `5.A` or `4.A` as a use/requires relation in these tables.

Tools (30.2) use UNSPSC commodity codes, not Content Model Element IDs — a separate encoding, also occupation-scoped.

## What would be required for a defensible task→software edge

Something O\*NET does **not** ship in this release, for example:
- `tasks_to_software` / `dwas_to_software` / `work_activities_to_software`, or
- Software examples attached to DWA/GWA rows

Absent that, options that **break** the thesis non-negotiable (every edge traceable to a source row) include LLM inference, string-matching task text to product names, or assigning all occupation software to every task. Those are out of scope here and are not recommended as baseline edges.

## Practical implication for the ontology

- **Occupation → usesSoftware** can be populated directly from `software_skills.csv` (with Hot Technology / In Demand as datatype properties).
- **Task → usesSoftware** cannot be populated from O\*NET 30.3 without a new evidence source; leave unmapped / null and report as a gap (parallel to how missing Importance for Data Scientists was handled).

## Ambiguity flag (not resolved)

Whether a *future* O\*NET release or the 30.3 migration reference describes a planned software↔activity linkage was not assumed. Sheet titles in `30_3_migration_reference.xlsx` were scanned for software/tool mentions; that does not create a row-level linkage file. If you want a deeper read of specific migration sheets, say which sheet — still no invented edges.
