# Edge coverage and vocabulary stats

Source: `data/processed/task_skill_derived.csv` + O*NET 30.3 raw files. No imputation.

## Tasks with zero skill edges

| Occupation | Zero-skill tasks | Tasks in slice |
|---|---:|---:|
| 15-1212.00 Information Security Analysts | **0** | 11 |
| 15-1242.00 Database Administrators | **0** | 18 |
| 15-1252.00 Software Developers | **0** | 17 |
| 15-1254.00 Web Developers | **0** | 29 |
| 15-2051.00 Data Scientists | **0** | 16 |

**Result: 0 tasks with zero skill edges** across all 91 slice tasks. Every task in the five-occupation slice obtained ≥1 structural Task→DWA→GWA→Skill edge.

(Therefore there are no zero-skill task examples to list.)

## Distribution of edges per task

| Statistic | Value |
|---|---:|
| Tasks | 91 |
| Min edges/task | 1 |
| 25th percentile | 3 |
| Median | 5 |
| 75th percentile | 8 |
| Max edges/task | 26 |
| Mean | 6.70 |

### Sparse tasks (fewest edges — not zero)

| SOC | Task ID | #edges | Task (truncated) |
|---|---|---:|---|
| 15-1212.00 | 5322 | 1 | Document computer security and emergency measures policies, procedures, and tests. |
| 15-1254.00 | 14726 | 1 | Document test plans, testing procedures, or test results. |
| 15-1254.00 | 14728 | 1 | Document technical factors such as server load, bandwidth, database performance, and browser and ... |
| 15-2051.00 | 21829 | 1 | Deliver oral or written presentations of the results of mathematical modeling and data analysis t... |
| 15-1242.00 | 1315 | 2 | Revise company definition of data as defined in data dictionary. |
| 15-1252.00 | 21662 | 2 | Analyze user needs and software requirements to determine feasibility of design within time and c... |
| 15-1252.00 | 21670 | 2 | Modify existing software to correct errors, adapt it to new hardware, or upgrade interfaces and i... |
| 15-1252.00 | 21661 | 2 | Analyze information to determine, recommend, and plan installation of a new system or modificatio... |
| 15-1252.00 | 21672 | 2 | Obtain and evaluate information on factors such as reporting formats required, costs, or security... |
| 15-1254.00 | 14711 | 2 | Select programming languages, design tools, or applications. |

## Distinct skill vocabulary

| Universe | Distinct skill Element IDs |
|---|---:|
| In derived 610 edges | **25** |
| In `essential_skills` + `transferable_skills` rating files (occupation×skill) | 35 (essential 10 + transferable 25) |
| In skill↔work-activity linkage files | 32 |
| Content Model Reference under `2.A` (Basic Skills branch) | 13 elements (includes non-leaf) |
| Content Model Reference under `2.B` (Cross-Functional Skills branch) | 31 elements (includes non-leaf) |

**Coverage of linkage universe:** 25 / 32 skill elements appear in the slice-derived edges (78%).

**Coverage of rating-file skill IDs:** 25 / 35 (71%).

Note: O*NET 30.3's rated skill inventory is small (35 leaf skill elements across essential+transferable). The chain can only emit skills that appear in the ~110+122 skill↔WA linkage rows.

## GWA funnel — which work activities do the most routing?

| Rank | GWA | #tasks (of 91) | #edges | #occs in slice |
|---:|---|---:|---:|---:|
| 1 | Working with Computers (`4.A.3.b.1`) | 21 | 110 | 5 |
| 2 | Thinking Creatively (`4.A.2.b.2`) | 14 | 30 | 4 |
| 3 | Analyzing Data or Information (`4.A.2.a.4`) | 12 | 26 | 4 |
| 4 | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment (`4.A.3.b.2`) | 12 | 36 | 5 |
| 5 | Providing Consultation and Advice to Others (`4.A.4.b.6`) | 7 | 105 | 4 |
| 6 | Documenting/Recording Information (`4.A.3.b.6`) | 6 | 6 | 3 |
| 7 | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | 6 | 66 | 3 |
| 8 | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | 6 | 90 | 3 |
| 9 | Judging the Qualities of Objects, Services, or People (`4.A.2.a.1`) | 5 | 10 | 3 |
| 10 | Inspecting Equipment, Structures, or Materials (`4.A.1.b.2`) | 4 | 16 | 3 |
| 11 | Updating and Using Relevant Knowledge (`4.A.2.b.3`) | 3 | 15 | 3 |
| 12 | Monitoring Processes, Materials, or Surroundings (`4.A.1.a.2`) | 3 | 15 | 3 |
| 13 | Communicating with Supervisors, Peers, or Subordinates (`4.A.4.a.2`) | 3 | 9 | 2 |
| 14 | Training and Teaching Others (`4.A.4.b.3`) | 3 | 42 | 3 |
| 15 | Getting Information (`4.A.1.a.1`) | 3 | 9 | 2 |
| 16 | Making Decisions and Solving Problems (`4.A.2.b.1`) | 2 | 14 | 1 |
| 17 | Organizing, Planning, and Prioritizing Work (`4.A.2.b.6`) | 1 | 5 | 1 |
| 18 | Communicating with People Outside the Organization (`4.A.4.a.3`) | 1 | 6 | 1 |

- Distinct GWAs used in slice: **18**
- Tasks touching at least one of top-3 GWAs: **41 / 91** (45%)
- Edges through top-3 GWAs: **166 / 610** (27%)
- Edges through top-5 GWAs: **307 / 610** (50%)

**Reading:** The chain is **somewhat funnelled** but not collapsed to 2–3 activities only. 
`Working with Computers` (4.A.3.b.1) is the single largest task hub (21/91 tasks). 
Top 3 GWAs account for ~27% of edges; 18 distinct GWAs appear. 
High-fanout GWAs (e.g. Providing Consultation, Guiding Subordinates) produce many skill edges per task and can dilute occupation-specific signal — worth watching in the hand review.

## Dead ends (DWA with no onward GWA→skill mapping)

Checked for the five-occupation slice:

1. Every DWA linked from slice tasks appears in `gwas_to_iwas_to_dwas.csv` (0 orphan DWAs).
2. Every such DWA has a non-null GWA.
3. Every such GWA appears in essential and/or transferable `*_skills_to_work_activities.csv` (0 GWAs without skill links).
4. Consistent with zero zero-skill tasks above.

**No dead-end DWA→GWA→skill paths in this slice.**
