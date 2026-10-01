# Nesta ESCO precision results

Grades from [`docs/nesta_precision_sample.md`](nesta_precision_sample.md) (unchanged).
Unit of analysis: **unique `(task_id, match_skill)`** pairs.
If the same ESCO concept appears more than once for a task, it is counted once.
Tasks with no mappings are **excluded from precision** and reported under coverage.

## Duplicate-pair check

### Duplicates graded consistently (collapsed to one)

- Task `21667` / `statistics` — 2 raw rows, all **P** (`most_common_level_3`)

No inconsistently graded duplicate pairs.

## Sample coverage (precision denominator exclusions)

- Tasks in sample: **20**
- Tasks with no mappings: **5** — excluded from precision, counted against coverage
  - Task IDs: 14705, 21651, 21668, 21836, 5322
- Tasks with ≥1 graded mapping: **15**
- Unique graded pairs (consistent): **22**
  - skill-level: **12**
  - group-level: **10**

## Overall precision

**All match types** (N=22 unique pairs): P=17, I=2, G=3
- Strict precision P/(P+I+G) = 17/22 = **77.3%**
- Lenient precision (P+G)/(P+I+G) = 20/22 = **90.9%**

**match_type == "skill"** (N=12 unique pairs): P=12, I=0, G=0
- Strict precision P/(P+I+G) = 12/12 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 12/12 = **100.0%**

**Group-level match_types (`most_common_level_*`, `top_level_*`, etc.)** (N=10 unique pairs): P=5, I=2, G=3
- Strict precision P/(P+I+G) = 5/10 = **50.0%**
- Lenient precision (P+G)/(P+I+G) = 8/10 = **80.0%**

## Per-occupation precision

### 15-1212.00 — Information Security Analysts

Sample tasks: 4; no-mapping tasks: **1** (excluded from precision).

**All match types** (N=5 unique pairs): P=3, I=0, G=2
- Strict precision P/(P+I+G) = 3/5 = **60.0%**
- Lenient precision (P+G)/(P+I+G) = 5/5 = **100.0%**

**match_type == "skill"** (N=3 unique pairs): P=3, I=0, G=0
- Strict precision P/(P+I+G) = 3/3 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 3/3 = **100.0%**

**Group-level** (N=2 unique pairs): P=0, I=0, G=2
- Strict precision P/(P+I+G) = 0/2 = **0.0%**
- Lenient precision (P+G)/(P+I+G) = 2/2 = **100.0%**

### 15-1242.00 — Database Administrators

Sample tasks: 4; no-mapping tasks: **1** (excluded from precision).

**All match types** (N=5 unique pairs): P=5, I=0, G=0
- Strict precision P/(P+I+G) = 5/5 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 5/5 = **100.0%**

**match_type == "skill"** (N=3 unique pairs): P=3, I=0, G=0
- Strict precision P/(P+I+G) = 3/3 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 3/3 = **100.0%**

**Group-level** (N=2 unique pairs): P=2, I=0, G=0
- Strict precision P/(P+I+G) = 2/2 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 2/2 = **100.0%**

### 15-1252.00 — Software Developers

Sample tasks: 4; no-mapping tasks: **1** (excluded from precision).

**All match types** (N=4 unique pairs): P=4, I=0, G=0
- Strict precision P/(P+I+G) = 4/4 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 4/4 = **100.0%**

**match_type == "skill"** (N=2 unique pairs): P=2, I=0, G=0
- Strict precision P/(P+I+G) = 2/2 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 2/2 = **100.0%**

**Group-level** (N=2 unique pairs): P=2, I=0, G=0
- Strict precision P/(P+I+G) = 2/2 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 2/2 = **100.0%**

### 15-1254.00 — Web Developers

Sample tasks: 4; no-mapping tasks: **1** (excluded from precision).

**All match types** (N=5 unique pairs): P=2, I=2, G=1
- Strict precision P/(P+I+G) = 2/5 = **40.0%**
- Lenient precision (P+G)/(P+I+G) = 3/5 = **60.0%**

**match_type == "skill"** (N=2 unique pairs): P=2, I=0, G=0
- Strict precision P/(P+I+G) = 2/2 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 2/2 = **100.0%**

**Group-level** (N=3 unique pairs): P=0, I=2, G=1
- Strict precision P/(P+I+G) = 0/3 = **0.0%**
- Lenient precision (P+G)/(P+I+G) = 1/3 = **33.3%**

### 15-2051.00 — Data Scientists

Sample tasks: 4; no-mapping tasks: **1** (excluded from precision).

**All match types** (N=3 unique pairs): P=3, I=0, G=0
- Strict precision P/(P+I+G) = 3/3 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 3/3 = **100.0%**

**match_type == "skill"** (N=2 unique pairs): P=2, I=0, G=0
- Strict precision P/(P+I+G) = 2/2 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 2/2 = **100.0%**

**Group-level** (N=1 unique pairs): P=1, I=0, G=0
- Strict precision P/(P+I+G) = 1/1 = **100.0%**
- Lenient precision (P+G)/(P+I+G) = 1/1 = **100.0%**

## Method notes

- Grades read from the P/I/G column in the precision sample; no grades were modified.
- Strict = P / (P+I+G); lenient = (P+G) / (P+I+G).
- Group-level = any `match_type` other than `skill`.
- Placeholder rows (`—`) on no-mapping tasks contribute to the no-mapping count only.
