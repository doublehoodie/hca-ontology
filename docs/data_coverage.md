# O\*NET 30.3 data coverage — Data Scientists gap

Generated empirically from `data/raw/*.csv`. No imputation.

## Exact counts for `15-2051.00` (Data Scientists)

| File | Rows for `15-2051.00` |
|---|---:|
| `essential_skills.csv` | **0** |
| `transferable_skills.csv` | **0** |
| `knowledge.csv` | **0** |
| `abilities.csv` | **0** |
| `work_activities.csv` | **0** |
| `task_ratings.csv` | **0** |
| `task_statements.csv` | **16** |
| `software_skills.csv` | **87** |

**Confirmed:** Data Scientists has task statements and software rows, and zero rows in all six rating/activity files listed above. The gap is in the full release files, not an artifact of the five-occupation slice filter.

## Is this isolated or systematic?

| Metric | Count |
|---|---:|
| Occupations in `occupation_data.csv` | 1,016 |
| Occupations with ≥1 `task_statements` row | 923 |
| Occupations with `essential_skills` | 894 |
| Occupations with `transferable_skills` | 894 |
| Occupations with `knowledge` | 894 |
| Occupations with `abilities` | 894 |
| Occupations with `work_activities` | 894 |
| Occupations with `task_ratings` | 894 |
| Occupations with `software_skills` | 923 |

**Same pattern as Data Scientists** (has task statements; zero rows in all of essential_skills, transferable_skills, knowledge, abilities, work_activities, task_ratings):

**29 occupations** (29 / 923 ≈ **3.1%** of occupations that have tasks).

All 29 of those also have ≥1 `software_skills` row (same as Data Scientists).

The six rating/activity files cover exactly the same 894 occupation set in this release — when one is missing, all six are missing.

### The 29 occupations

| O\*NET-SOC | Title | n_tasks | n_software |
|---|---|---:|---:|
| 11-1031.00 | Legislators | 30 | 32 |
| 11-2032.00 | Public Relations Managers | 20 | 65 |
| 13-1082.00 | Project Management Specialists | 20 | 90 |
| 13-2051.00 | Financial and Investment Analysts | 26 | 180 |
| 13-2054.00 | Financial Risk Specialists | 30 | 190 |
| 15-1255.00 | Web and Digital Interface Designers | 30 | 236 |
| 15-1299.04 | Penetration Testers | 22 | 67 |
| 15-1299.06 | Digital Forensics Analysts | 20 | 64 |
| 15-1299.07 | Blockchain Engineers | 17 | 50 |
| **15-2051.00** | **Data Scientists** | **16** | **87** |
| 17-3028.00 | Calibration Technologists and Technicians | 15 | 16 |
| 19-4044.00 | Hydrologic Technicians | 16 | 21 |
| 25-2055.00 | Special Education Teachers, Kindergarten | 30 | 21 |
| 27-2091.00 | Disc Jockeys, Except Radio | 19 | 6 |
| 27-4015.00 | Lighting Technicians | 16 | 12 |
| 29-1212.00 | Cardiologists | 25 | 3 |
| 29-1242.00 | Orthopedic Surgeons, Except Pediatric | 15 | 12 |
| 29-1243.00 | Pediatric Surgeons | 18 | 12 |
| 29-2042.00 | Emergency Medical Technicians | 12 | 20 |
| 29-2043.00 | Paramedics | 13 | 24 |
| 29-2072.00 | Medical Records Specialists | 17 | 109 |
| 29-9021.00 | Health Information Technologists and Medical Registrars | 16 | 109 |
| 33-9094.00 | School Bus Monitors | 18 | 2 |
| 39-1014.00 | First-Line Supervisors of Entertainment and Recreation Workers, Except Gambling Services | 19 | 9 |
| 39-4012.00 | Crematory Operators | 12 | 5 |
| 41-3091.00 | Sales Representatives of Services, Except Advertising, Insurance, Financial Services, and Travel | 15 | 13 |
| 53-1044.00 | First-Line Supervisors of Passenger Attendants | 19 | 15 |
| 53-3054.00 | Taxi Drivers | 16 | 15 |
| 53-6032.00 | Aircraft Service Attendants | 18 | 12 |

## Interpretation (factual only)

- This is a **systematic coverage gap**, not an isolated Data Scientists anomaly: **29 occupations** share the pattern.
- Several are newer or restructured 2018 SOC titles (Data Scientists, Blockchain Engineers, Penetration Testers, Project Management Specialists, etc.).
- Consequence for the thesis slice: structural Task→DWA→GWA→Skill edges can still be derived for Data Scientists from generic linkage tables, but **occupation-specific Importance/Level weights cannot** be attached from O\*NET 30.3 source rows (all null). See `docs/task_skill_gaps.md`.

## Method

```text
For each file: count rows where column "O*NET-SOC Code" == "15-2051.00"
Pattern: occupations present in task_statements minus those present in
essential_skills ∩ transferable_skills ∩ knowledge ∩ abilities ∩
work_activities ∩ task_ratings  →  identical 29-set for each pairwise
"has tasks but missing X" check on those six files.
```
