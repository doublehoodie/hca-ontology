# Crosswalk evidence pack (Day 2.3 → Call #1)

**Purpose:** Traceable evidence for O\*NET-SOC (2018) → SOC 2010 → ISCO-08 → ESCO candidates.  
**Rule:** Evidence only. Cardinality / Confidence / chosen ESCO URI are **blank for you**. No LLM-inferred mappings.

Sources read:
- `data/raw/soc_2010_to_2018_crosswalk.xlsx` (sheet `Sorted by 2010`; header Excel row 9 / pandas index 8)
- `data/raw/ISCO_SOC_Crosswalk.xls` (sheets `2010 SOC to ISCO-08` and `ISCO-08 to 2010 SOC`; header row index 6)
- `data/raw/esco/occupations_en.csv` (exact `preferredLabel` match unless noted)

Join path used for evidence:
1. Strip O\*NET decimal: `15-2051.00` → `15-2051`
2. Look up `2018 SOC Code` in SOC 2010↔2018 → `2010 SOC Code`(s)
3. Look up each `2010 SOC Code` in ISCO×SOC 2010 file → `ISCO-08 Code`(s)
4. List ESCO occupation candidates from local CSV (label / ISCO group)

---

## Summary table (decision cells blank)

| O\*NET-SOC (2018) | SOC 2010 (evidence) | ISCO-08 (via 2010 SOC) | ESCO candidate(s) (local CSV) | Cardinality | Confidence | Notes (yours) |
|---|---|---|---|---|---|---|
| 15-1252.00 Software Developers | 15-1132 + 15-1133 | 2512 Software developers | `software developer` → `http://data.europa.eu/esco/occupation/f2b15a0e-e65a-438a-affb-29b9d50b77d1` (iscoGroup 2512, code 2512.4) | | | |
| 15-1254.00 Web Developers | 15-1134 | 2513 Web and multimedia developers; also 3514 Web technicians | `web developer` → `http://data.europa.eu/esco/occupation/c40a2919-48a9-40ea-b506-1f34f693496d` (iscoGroup 2513, code 2513.5) | | | |
| 15-1242.00 Database Administrators | 15-1141 | 2521 Database designers and administrators | `database administrator` → `http://data.europa.eu/esco/occupation/8c57af09-719c-42b3-be40-6ed4946236cc` (iscoGroup 2521, code 2521.1) | | | |
| 15-1212.00 Information Security Analysts | 15-1122 | 2529 Database and network professionals n.e.c. | Multiple ICT security\* under 2529; also technician 3512 — see appendix (no exact preferredLabel “information security analyst”) | | | |
| 15-2051.00 Data Scientists | **15-2099** Mathematical Science Occupations, All Other | **3314** Statistical, mathematical and related associate professionals (via 15-2099) | Exact label `data scientist` → `http://data.europa.eu/esco/occupation/258e46f9-0075-4a2e-adae-1ff0477e0f30` (**iscoGroup 2511**, code 2511.4) | | | |

---

## 🛑 YOUR CALL #1 — Data Scientists mapping

There is **no clean agreement** across the three sources:

| Path | Result |
|---|---|
| SOC 2010↔2018 | 15-2051 ← 15-2099 (residual “All Other”, not a dedicated 2010 Data Scientist code) |
| ISCO via that 2010 code | **3314** (associate professionals — math/stats) |
| ESCO exact label | `data scientist` filed under **ISCO 2511** (Systems analysts), URI above |

Runbook options (not selected here):
- **(a)** Map to ESCO “data scientist” (ISCO 2511) and record low confidence
- **(b)** Leave unmapped; populate skills from O\*NET only
- **(c)** Drop Data Scientists from the slice

Runbook recommendation was **(a)** — recorded for reference only; **your decision cell stays blank**.

Also note (from Task 4/5): O\*NET 30.3 has **no** `essential_skills` / `transferable_skills` / `abilities` / `knowledge` / `work_activities` / `task_ratings` rows for `15-2051.00` in this release slice. Structural Task→DWA→GWA→Skill edges exist (65) but all Importance ratings are null. See `docs/task_skill_gaps.md`.

**Correction to runbook table:** SOC 2010 is not “none (new in 2018)” — the BLS crosswalk lists **15-2099**. It is still a weak/residual predecessor.

---

## Appendix A — SOC 2010 ↔ 2018 row excerpts

File: `data/raw/soc_2010_to_2018_crosswalk.xlsx`, sheet `Sorted by 2010`.

| 2010 SOC Code | 2010 SOC Title | 2018 SOC Code | 2018 SOC Title |
|---|---|---|---|
| 15-1122 | Information Security Analysts | 15-1212 | Information Security Analysts |
| 15-1132 | Software Developers, Applications (#) | 15-1252 | Software Developers (##) |
| 15-1133 | Software Developers, Systems Software (#) | 15-1252 | Software Developers (##) |
| 15-1134 | Web Developers (#) | 15-1254 | Web Developers |
| 15-1141 | Database Administrators (#) | 15-1242 | Database Administrators |
| 15-2099 | Mathematical Science Occupations, All Other (#) | 15-2051 | Data Scientists |

Also present (not selected): 15-1132/15-1133 also map to 15-1253 (SQA); 15-1134 also to 15-1255; 15-1141 also to 15-1243 (Database Architects). Cardinality judgment is yours.

---

## Appendix B — ISCO-08 ↔ 2010 SOC row excerpts

File: `data/raw/ISCO_SOC_Crosswalk.xls`, sheet `2010 SOC to ISCO-08` (confirmed sheet name).

| 2010 SOC Code | ISCO-08 Code | ISCO-08 Title EN |
|---|---|---|
| 15-1132 | 2512 | Software developers |
| 15-1133 | 2512 | Software developers |
| 15-1134 | 2513 | Web and multimedia developers |
| 15-1134 | 3514 | Web technicians |
| 15-1141 | 2521 | Database designers and administrators |
| 15-1122 | 2529 | Database and network professionals not elsewhere classified |
| 15-2099 | 3314 | Statistical, mathematical and related associate professionals |

Same ISCO codes appear on sheet `ISCO-08 to 2010 SOC`.

---

## Appendix C — ESCO occupation candidates (`occupations_en.csv`)

Exact `preferredLabel` matches:

| preferredLabel | conceptUri | iscoGroup | code |
|---|---|---|---|
| software developer | http://data.europa.eu/esco/occupation/f2b15a0e-e65a-438a-affb-29b9d50b77d1 | 2512 | 2512.4 |
| web developer | http://data.europa.eu/esco/occupation/c40a2919-48a9-40ea-b506-1f34f693496d | 2513 | 2513.5 |
| database administrator | http://data.europa.eu/esco/occupation/8c57af09-719c-42b3-be40-6ed4946236cc | 2521 | 2521.1 |
| data scientist | http://data.europa.eu/esco/occupation/258e46f9-0075-4a2e-adae-1ff0477e0f30 | 2511 | 2511.4 |

Information Security — no exact preferredLabel match for “information security analyst”. Label-contains candidates:

| preferredLabel | conceptUri | iscoGroup | code |
|---|---|---|---|
| ICT security administrator | http://data.europa.eu/esco/occupation/0464b062-cea6-4164-b10d-956c61956ae7 | 2529 | 2529.6 |
| chief ICT security officer | http://data.europa.eu/esco/occupation/276ba420-ef09-4a0e-b215-2c2e2f80ad28 | 2529 | 2529.1 |
| cybersecurity risk manager | http://data.europa.eu/esco/occupation/7754d570-9519-48c2-b1c9-8e165f8bca0f | 2529 | 2529.8 |
| ICT security technician | http://data.europa.eu/esco/occupation/a44a1dc5-be08-4840-8bd5-770c4ac1ca6d | 3512 | 3512.3 |
| director of compliance and information security | http://data.europa.eu/esco/occupation/b1ed68f8-8d51-4bcc-8825-bd554859480f | 1213 | 1213.9 |

(Plus niche gambling compliance title under 1213 — likely irrelevant.)

---

## Status

- Evidence pack complete.
- **Awaiting your Call #1 decision** (and any Cardinality/Confidence fills).
- Do **not** proceed to Day 3 (Protégé schema) until you say so.
