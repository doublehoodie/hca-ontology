# O*NET chain precision results

Grades from [`docs/onet_chain_precision_sample.md`](onet_chain_precision_sample.md) (unchanged).
Unit of analysis: **unique `(task_id, skill_name)`** pairs.
Blockquote audit notes under tables (if any) were ignored; only table rows were parsed.
Tasks with no chain edges would be **excluded from precision** and reported under coverage (none in this sample).

## Duplicate-pair check

Sheet already unique: **132** table skill rows → **132** unique `(task_id, skill_name)` pairs.
No duplicate pairs. No inconsistently graded duplicates.

## Sample coverage

- Tasks in sample: **20**
- Tasks with zero O*NET chain skill edges: **0**
- Tasks with ≥1 graded mapping: **20**
- Unique graded pairs: **132**
- Ungraded (blank P/I/G) rows: **0**

## Overall precision

**N=132** unique pairs: P=38, I=34, G=60
- Strict precision P/(P+I+G) = 38/132 = **28.8%**
- Lenient precision (P+G)/(P+I+G) = 98/132 = **74.2%**
- Dilution rate G/(P+I+G) = 60/132 = **45.5%**

## Per-occupation precision

### 15-1212.00 — Information Security Analysts

Sample tasks: 4; zero-edge tasks: **0**.

**N=15** unique pairs: P=6, I=3, G=6
- Strict precision P/(P+I+G) = 6/15 = **40.0%**
- Lenient precision (P+G)/(P+I+G) = 12/15 = **80.0%**
- Dilution rate G/(P+I+G) = 6/15 = **40.0%**

### 15-1242.00 — Database Administrators

Sample tasks: 4; zero-edge tasks: **0**.

**N=33** unique pairs: P=12, I=6, G=15
- Strict precision P/(P+I+G) = 12/33 = **36.4%**
- Lenient precision (P+G)/(P+I+G) = 27/33 = **81.8%**
- Dilution rate G/(P+I+G) = 15/33 = **45.5%**

### 15-1252.00 — Software Developers

Sample tasks: 4; zero-edge tasks: **0**.

**N=37** unique pairs: P=6, I=12, G=19
- Strict precision P/(P+I+G) = 6/37 = **16.2%**
- Lenient precision (P+G)/(P+I+G) = 25/37 = **67.6%**
- Dilution rate G/(P+I+G) = 19/37 = **51.4%**

### 15-1254.00 — Web Developers

Sample tasks: 4; zero-edge tasks: **0**.

**N=18** unique pairs: P=5, I=6, G=7
- Strict precision P/(P+I+G) = 5/18 = **27.8%**
- Lenient precision (P+G)/(P+I+G) = 12/18 = **66.7%**
- Dilution rate G/(P+I+G) = 7/18 = **38.9%**

### 15-2051.00 — Data Scientists

Sample tasks: 4; zero-edge tasks: **0**.

**N=29** unique pairs: P=9, I=7, G=13
- Strict precision P/(P+I+G) = 9/29 = **31.0%**
- Lenient precision (P+G)/(P+I+G) = 22/29 = **75.9%**
- Dilution rate G/(P+I+G) = 13/29 = **44.8%**

## Per-derivation GWA

When a collapsed unique pair lists multiple GWAs (joined by `;`), the same grade is attributed to **each** listed GWA. Sorted by **I+G** descending (then N).

| Derivation (GWA name) | N | P | I | G | Strict | Lenient | Dilution | I+G |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Guiding, Directing, and Motivating Subordinates | 45 | 9 | 16 | 20 | 20.0% | 64.4% | 44.4% | 36 |
| Working with Computers | 25 | 4 | 7 | 14 | 16.0% | 72.0% | 56.0% | 21 |
| Providing Consultation and Advice to Others | 15 | 4 | 5 | 6 | 26.7% | 66.7% | 40.0% | 11 |
| Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment | 9 | 1 | 3 | 5 | 11.1% | 66.7% | 55.6% | 8 |
| Making Decisions and Solving Problems | 7 | 3 | 0 | 4 | 42.9% | 100.0% | 57.1% | 4 |
| Communicating with People Outside the Organization | 6 | 2 | 2 | 2 | 33.3% | 66.7% | 33.3% | 4 |
| Analyzing Data or Information | 4 | 0 | 0 | 4 | 0.0% | 100.0% | 100.0% | 4 |
| Thinking Creatively | 6 | 3 | 0 | 3 | 50.0% | 100.0% | 50.0% | 3 |
| Updating and Using Relevant Knowledge | 5 | 2 | 2 | 1 | 40.0% | 60.0% | 20.0% | 3 |
| Organizing, Planning, and Prioritizing Work | 5 | 3 | 0 | 2 | 60.0% | 100.0% | 40.0% | 2 |
| Judging the Qualities of Objects, Services, or People | 2 | 0 | 0 | 2 | 0.0% | 100.0% | 100.0% | 2 |
| Inspecting Equipment, Structures, or Materials | 8 | 7 | 0 | 1 | 87.5% | 100.0% | 12.5% | 1 |
| Documenting/Recording Information | 2 | 2 | 0 | 0 | 100.0% | 100.0% | 0.0% | 0 |

Highest noise (I+G volume): **Guiding, Directing, and Motivating Subordinates** (I=16, G=20) and **Working with Computers** (I=7, G=14). Highest dilution among GWAs with N≥4: **Analyzing Data or Information** (100% G) and **Working with Computers** (56.0% G). Cleanest large bucket: **Inspecting Equipment, Structures, or Materials** (strict 87.5%, dilution 12.5%).

## Side-by-side vs Nesta (same 20 tasks)

Figures for Nesta from [`docs/nesta_precision_results.md`](nesta_precision_results.md) (all match types). O*NET from this file.

| method | tasks with any link | strict precision | lenient precision |
|---|---:|---:|---:|
| Nesta ESCO extract | 15 / 20 | 77.3% (17/22) | 90.9% (20/22) |
| O*NET Task→DWA→GWA→Skill chain | 20 / 20 | 28.8% (38/132) | 74.2% (98/132) |

## Method notes

- Grades read from the P/I/G column in the precision sample; no grades were modified.
- Strict = P / (P+I+G); lenient = (P+G) / (P+I+G); dilution = G / (P+I+G).
- Multi-GWA derivation cells credit each listed GWA with the pair’s single grade.
