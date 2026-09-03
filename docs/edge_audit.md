# Edge quality audit

Source: `data/processed/task_skill_derived.csv` (610 edges, O*NET 30.3 chain).
Importance = occupation-level `Data Value` where `Scale ID=IM` joined onto structural edges.
**No fabricated edges.** Data Scientists has no importance ratings — ranked by edge frequency instead.

Hand-review column: mark each edge **P** (plausible) / **I** (implausible) yourself.

## Part A — Highest / lowest importance-weighted skills by occupation

Ranking unit: distinct `(Skill Element ID, skill_kind)` aggregated with **mean** importance across that occupation's derived edges for that skill (importance is constant per occupation×skill in O*NET ratings, so mean = the occupation rating).

### 15-1252.00 — Software Developers (149 edges, 23 distinct skills)

**Top 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Programming (`2.B.3.e`) | transferable | 4.00 | 1 | |
| 2 | Critical Thinking (`2.A.2.a`) | essential | 3.88 | 17 | |
| 3 | Judgment and Decision Making (`2.B.4.e`) | transferable | 3.62 | 2 | |
| 4 | Reading Comprehension (`2.A.1.a`) | essential | 3.50 | 11 | |
| 5 | Active Learning (`2.A.2.b`) | essential | 3.50 | 5 | |

**Bottom 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Management of Personnel Resources (`2.B.5.d`) | transferable | 2.25 | 7 | |
| 2 | Learning Strategies (`2.A.2.c`) | essential | 2.62 | 5 | |
| 3 | Negotiation (`2.B.1.d`) | transferable | 2.62 | 6 | |
| 4 | Operations Monitoring (`2.B.3.g`) | transferable | 2.75 | 1 | |
| 5 | Persuasion (`2.B.1.c`) | transferable | 2.75 | 7 | |

### 15-2051.00 — Data Scientists (65 edges, 20 distinct skills)

**No Importance ratings in O*NET 30.3 for this occupation** (see `docs/data_coverage.md`). Ranking by edge frequency only.

**Most frequent (proxy for top)**

| Rank | Skill | Kind | #edges | Face-valid? |
|---:|---|---|---:|---|
| 1 | Reading Comprehension (`2.A.1.a`) | essential | 13 | |
| 2 | Critical Thinking (`2.A.2.a`) | essential | 13 | |
| 3 | Complex Problem Solving (`2.B.2.i`) | transferable | 5 | |
| 4 | Writing (`2.A.1.c`) | essential | 4 | |
| 5 | Active Listening (`2.A.1.b`) | essential | 4 | |

**Least frequent (proxy for bottom)**

| Rank | Skill | Kind | #edges | Face-valid? |
|---:|---|---|---:|---|
| 1 | Social Perceptiveness (`2.B.1.a`) | transferable | 1 | |
| 2 | Monitoring (`2.A.2.d`) | essential | 1 | |
| 3 | Learning Strategies (`2.A.2.c`) | essential | 1 | |
| 4 | Speaking (`2.A.1.d`) | essential | 1 | |
| 5 | Time Management (`2.B.5.a`) | transferable | 1 | |

### 15-1254.00 — Web Developers (185 edges, 25 distinct skills)

**Top 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Programming (`2.B.3.e`) | transferable | 4.12 | 9 | |
| 2 | Critical Thinking (`2.A.2.a`) | essential | 3.75 | 25 | |
| 3 | Reading Comprehension (`2.A.1.a`) | essential | 3.62 | 22 | |
| 4 | Complex Problem Solving (`2.B.2.i`) | transferable | 3.62 | 12 | |
| 5 | Active Listening (`2.A.1.b`) | essential | 3.50 | 11 | |

**Bottom 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Troubleshooting (`2.B.3.k`) | transferable | 2.12 | 2 | |
| 2 | Operations Monitoring (`2.B.3.g`) | transferable | 2.25 | 3 | |
| 3 | Management of Personnel Resources (`2.B.5.d`) | transferable | 2.38 | 3 | |
| 4 | Technology Design (`2.B.3.b`) | transferable | 2.50 | 5 | |
| 5 | Quality Control Analysis (`2.B.3.m`) | transferable | 2.75 | 2 | |

### 15-1242.00 — Database Administrators (133 edges, 25 distinct skills)

**Top 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Critical Thinking (`2.A.2.a`) | essential | 3.88 | 21 | |
| 2 | Complex Problem Solving (`2.B.2.i`) | transferable | 3.88 | 9 | |
| 3 | Reading Comprehension (`2.A.1.a`) | essential | 3.75 | 19 | |
| 4 | Active Listening (`2.A.1.b`) | essential | 3.75 | 6 | |
| 5 | Judgment and Decision Making (`2.B.4.e`) | transferable | 3.75 | 4 | |

**Bottom 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Negotiation (`2.B.1.d`) | transferable | 2.00 | 1 | |
| 2 | Technology Design (`2.B.3.b`) | transferable | 2.38 | 5 | |
| 3 | Troubleshooting (`2.B.3.k`) | transferable | 2.50 | 1 | |
| 4 | Quality Control Analysis (`2.B.3.m`) | transferable | 2.50 | 1 | |
| 5 | Persuasion (`2.B.1.c`) | transferable | 2.62 | 3 | |

### 15-1212.00 — Information Security Analysts (78 edges, 23 distinct skills)

**Top 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Reading Comprehension (`2.A.1.a`) | essential | 4.00 | 8 | |
| 2 | Critical Thinking (`2.A.2.a`) | essential | 3.88 | 9 | |
| 3 | Active Listening (`2.A.1.b`) | essential | 3.75 | 5 | |
| 4 | Complex Problem Solving (`2.B.2.i`) | transferable | 3.75 | 4 | |
| 5 | Speaking (`2.A.1.d`) | essential | 3.62 | 3 | |

**Bottom 5 by importance**

| Rank | Skill | Kind | Importance | #edges | Face-valid? |
|---:|---|---|---:|---:|---|
| 1 | Troubleshooting (`2.B.3.k`) | transferable | 2.12 | 1 | |
| 2 | Persuasion (`2.B.1.c`) | transferable | 2.62 | 2 | |
| 3 | Negotiation (`2.B.1.d`) | transferable | 2.62 | 2 | |
| 4 | Programming (`2.B.3.e`) | transferable | 2.62 | 4 | |
| 5 | Social Perceptiveness (`2.B.1.a`) | transferable | 2.75 | 3 | |

---

## Part B — 10-task hand review (mark each edge P/I/G)

Selected for occupation spread; includes 2 Data Scientists tasks. Derivation path = DWA → IWA → GWA from source linkage rows.
G = technically true but so broadly applicable it carries little discriminating information

### Task 5315 — Information Security Analysts (`15-1212.00`)

**Task text:** Confer with users to discuss issues such as computer data access needs, security violations, and programming changes.

**Task Type:** Core  
**# derived skill edges:** 16

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I/G |
|---:|---|---|---:|---|---|---|---|
| 1 | Reading Comprehension | essential | 4.00 | Troubleshoot issues with computer applications or systems. (`4.A.3.b.1.d.2`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.d.2 → 4.A.3.b.1.d → 4.A.3.b.1 → 2.A.1.a` |P |
| 2 | Critical Thinking | essential | 3.88 | Troubleshoot issues with computer applications or systems. (`4.A.3.b.1.d.2`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.d.2 → 4.A.3.b.1.d → 4.A.3.b.1 → 2.A.2.a` |P |
| 3 | Critical Thinking | essential | 3.88 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.2.a` |P |
| 4 | Active Listening | essential | 3.75 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.1.b` |P |
| 5 | Complex Problem Solving | transferable | 3.75 | Troubleshoot issues with computer applications or systems. (`4.A.3.b.1.d.2`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.d.2 → 4.A.3.b.1.d → 4.A.3.b.1 → 2.B.2.i` |P |
| 6 | Speaking | essential | 3.62 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.1.d` |P |
| 7 | Monitoring | essential | 3.38 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.2.d` |P |
| 8 | Systems Analysis | transferable | 3.38 | Troubleshoot issues with computer applications or systems. (`4.A.3.b.1.d.2`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.d.2 → 4.A.3.b.1.d → 4.A.3.b.1 → 2.B.4.g` |P |
| 9 | Time Management | transferable | 3.12 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.5.a` |P |
| 10 | Coordination | transferable | 3.00 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.b` |P |
| 11 | Management of Personnel Resources | transferable | 2.88 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.5.d` |P |
| 12 | Service Orientation | transferable | 2.88 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.f` |P |
| 13 | Social Perceptiveness | transferable | 2.75 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.a` |P |
| 14 | Negotiation | transferable | 2.62 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.d` |P |
| 15 | Persuasion | transferable | 2.62 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.c` |P |
| 16 | Programming | transferable | 2.62 | Troubleshoot issues with computer applications or systems. (`4.A.3.b.1.d.2`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.d.2 → 4.A.3.b.1.d → 4.A.3.b.1 → 2.B.3.e` |P |

### Task 5314 — Information Security Analysts (`15-1212.00`)

**Task text:** Develop plans to safeguard computer files against accidental or unauthorized modification, destruction, or disclosure and to meet emergency data processing needs.

**Task Type:** Core  
**# derived skill edges:** 3

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I/G |
|---:|---|---|---:|---|---|---|---|
| 1 | Reading Comprehension | essential | 4.00 | Develop computer or information security policies or procedures. (`4.A.3.b.2.f.9`) | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment (`4.A.3.b.2`) | `4.A.3.b.2.f.9 → 4.A.3.b.2.f → 4.A.3.b.2 → 2.A.1.a` |P |
| 2 | Writing | essential | 3.50 | Develop computer or information security policies or procedures. (`4.A.3.b.2.f.9`) | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment (`4.A.3.b.2`) | `4.A.3.b.2.f.9 → 4.A.3.b.2.f → 4.A.3.b.2 → 2.A.1.c` |P |
| 3 | Instructing | transferable | 2.88 | Develop computer or information security policies or procedures. (`4.A.3.b.2.f.9`) | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment (`4.A.3.b.2`) | `4.A.3.b.2.f.9 → 4.A.3.b.2.f → 4.A.3.b.2 → 2.B.1.e` |P |

### Task 1301 — Database Administrators (`15-1242.00`)

**Task text:** Plan, coordinate, and implement security measures to safeguard information in computer files against accidental or unauthorized damage, modification or disclosure.

**Task Type:** Core  
**# derived skill edges:** 8

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I/G |
|---:|---|---|---:|---|---|---|---|
| 1 | Complex Problem Solving | transferable | 3.88 | Implement security measures for computer or information systems. (`4.A.3.b.1.b.1`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.b.1 → 4.A.3.b.1.b → 4.A.3.b.1 → 2.B.2.i` |P |
| 2 | Critical Thinking | essential | 3.88 | Implement security measures for computer or information systems. (`4.A.3.b.1.b.1`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.b.1 → 4.A.3.b.1.b → 4.A.3.b.1 → 2.A.2.a` |P |
| 3 | Reading Comprehension | essential | 3.75 | Implement security measures for computer or information systems. (`4.A.3.b.1.b.1`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.b.1 → 4.A.3.b.1.b → 4.A.3.b.1 → 2.A.1.a` |P |
| 4 | Reading Comprehension | essential | 3.75 | Develop computer or information security policies or procedures. (`4.A.3.b.2.f.9`) | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment (`4.A.3.b.2`) | `4.A.3.b.2.f.9 → 4.A.3.b.2.f → 4.A.3.b.2 → 2.A.1.a` |P |
| 5 | Programming | transferable | 3.38 | Implement security measures for computer or information systems. (`4.A.3.b.1.b.1`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.b.1 → 4.A.3.b.1.b → 4.A.3.b.1 → 2.B.3.e` |P |
| 6 | Writing | essential | 3.25 | Develop computer or information security policies or procedures. (`4.A.3.b.2.f.9`) | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment (`4.A.3.b.2`) | `4.A.3.b.2.f.9 → 4.A.3.b.2.f → 4.A.3.b.2 → 2.A.1.c` |P |
| 7 | Systems Analysis | transferable | 3.12 | Implement security measures for computer or information systems. (`4.A.3.b.1.b.1`) | Working with Computers (`4.A.3.b.1`) | `4.A.3.b.1.b.1 → 4.A.3.b.1.b → 4.A.3.b.1 → 2.B.4.g` |P |
| 8 | Instructing | transferable | 3.00 | Develop computer or information security policies or procedures. (`4.A.3.b.2.f.9`) | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment (`4.A.3.b.2`) | `4.A.3.b.2.f.9 → 4.A.3.b.2.f → 4.A.3.b.2 → 2.B.1.e` |P |

### Task 21648 — Database Administrators (`15-1242.00`)

**Task text:** Identify, evaluate and recommend hardware or software technologies to achieve desired database performance.

**Task Type:** Core  
**# derived skill edges:** 17

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I/G |
|---:|---|---|---:|---|---|---|---|
| 1 | Complex Problem Solving | transferable | 3.88 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.2.i` |P |
| 2 | Critical Thinking | essential | 3.88 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.2.a` |P |
| 3 | Active Listening | essential | 3.75 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.b` |P |
| 4 | Judgment and Decision Making | transferable | 3.75 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.e` |P |
| 5 | Reading Comprehension | essential | 3.75 | Evaluate utility of software or hardware technologies. (`4.A.2.a.1.g.8`) | Judging the Qualities of Objects, Services, or People (`4.A.2.a.1`) | `4.A.2.a.1.g.8 → 4.A.2.a.1.g → 4.A.2.a.1 → 2.A.1.a` |P |
| 6 | Reading Comprehension | essential | 3.75 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.a` |P |
| 7 | Speaking | essential | 3.38 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.d` |P |
| 8 | Monitoring | essential | 3.25 | Evaluate utility of software or hardware technologies. (`4.A.2.a.1.g.8`) | Judging the Qualities of Objects, Services, or People (`4.A.2.a.1`) | `4.A.2.a.1.g.8 → 4.A.2.a.1.g → 4.A.2.a.1 → 2.A.2.d` |P |
| 9 | Monitoring | essential | 3.25 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.2.d` |P |
| 10 | Writing | essential | 3.25 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.c` |P |
| 11 | Systems Analysis | transferable | 3.12 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.g` |P |
| 12 | Systems Evaluation | transferable | 3.12 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.h` |P |
| 13 | Coordination | transferable | 3.00 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.b` |P |
| 14 | Instructing | transferable | 3.00 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.e` |P |
| 15 | Service Orientation | transferable | 2.88 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.f` |P |
| 16 | Social Perceptiveness | transferable | 2.88 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.a` |G |
| 17 | Persuasion | transferable | 2.62 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.c` |P |

### Task 21666 — Software Developers (`15-1252.00`)

**Task text:** Coordinate installation of software system.

**Task Type:** Supplemental  
**# derived skill edges:** 15

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I/G |
|---:|---|---|---:|---|---|---|---|
| 1 | Critical Thinking | essential | 3.88 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.A.2.a` |P |
| 2 | Active Learning | essential | 3.50 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.A.2.b` |P |
| 3 | Active Listening | essential | 3.38 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.A.1.b` |P |
| 4 | Writing | essential | 3.25 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.A.1.c` |P |
| 5 | Speaking | essential | 3.12 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.A.1.d` |P |
| 6 | Time Management | transferable | 3.12 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.5.a` |P |
| 7 | Coordination | transferable | 3.00 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.1.b` |P |
| 8 | Monitoring | essential | 3.00 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.A.2.d` |P |
| 9 | Instructing | transferable | 2.88 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.1.e` |P |
| 10 | Service Orientation | transferable | 2.88 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.1.f` |P |
| 11 | Social Perceptiveness | transferable | 2.88 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.1.a` |G |
| 12 | Persuasion | transferable | 2.75 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.1.c` |P |
| 13 | Learning Strategies | essential | 2.62 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.A.2.c` |G |
| 14 | Negotiation | transferable | 2.62 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.1.d` |P |
| 15 | Management of Personnel Resources | transferable | 2.25 | Coordinate software or hardware installation. (`4.A.4.b.4.e.4`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.e.4 → 4.A.4.b.4.e → 4.A.4.b.4 → 2.B.5.d` |P |

### Task 21677 — Software Developers (`15-1252.00`)

**Task text:** Supervise and assign work to programmers, designers, technologists, technicians, or other engineering or scientific personnel.

**Task Type:** Supplemental  
**# derived skill edges:** 26

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I/G |
|---:|---|---|---:|---|---|---|---|
| 1 | Critical Thinking | essential | 3.88 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.A.2.a` |P |
| 2 | Critical Thinking | essential | 3.88 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.A.2.a` |P |
| 3 | Active Learning | essential | 3.50 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.A.2.b` |P |
| 4 | Active Listening | essential | 3.38 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.A.1.b` |P |
| 5 | Active Listening | essential | 3.38 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.A.1.b` |P |
| 6 | Writing | essential | 3.25 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.A.1.c` |P |
| 7 | Speaking | essential | 3.12 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.A.1.d` |P |
| 8 | Speaking | essential | 3.12 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.A.1.d` |P |
| 9 | Time Management | transferable | 3.12 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.B.5.a` |P |
| 10 | Time Management | transferable | 3.12 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.5.a` |P |
| 11 | Coordination | transferable | 3.00 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.B.1.b` |P |
| 12 | Coordination | transferable | 3.00 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.1.b` |P |
| 13 | Monitoring | essential | 3.00 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.A.2.d` |P |
| 14 | Monitoring | essential | 3.00 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.A.2.d` |P |
| 15 | Instructing | transferable | 2.88 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.1.e` |P |
| 16 | Service Orientation | transferable | 2.88 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.B.1.f` |P |
| 17 | Service Orientation | transferable | 2.88 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.1.f` |P |
| 18 | Social Perceptiveness | transferable | 2.88 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.B.1.a` |P |
| 19 | Social Perceptiveness | transferable | 2.88 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.1.a` |P |
| 20 | Persuasion | transferable | 2.75 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.B.1.c` |P |
| 21 | Persuasion | transferable | 2.75 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.1.c` |P |
| 22 | Learning Strategies | essential | 2.62 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.A.2.c` |P |
| 23 | Negotiation | transferable | 2.62 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.B.1.d` |P |
| 24 | Negotiation | transferable | 2.62 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.1.d` |P |
| 25 | Management of Personnel Resources | transferable | 2.25 | Assign duties or work schedules to employees. (`4.A.4.b.1.f.6`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.f.6 → 4.A.4.b.1.f → 4.A.4.b.1 → 2.B.5.d` |P |
| 26 | Management of Personnel Resources | transferable | 2.25 | Supervise information technology personnel. (`4.A.4.b.4.a.7`) | Guiding, Directing, and Motivating Subordinates (`4.A.4.b.4`) | `4.A.4.b.4.a.7 → 4.A.4.b.4.a → 4.A.4.b.4 → 2.B.5.d` |P |

### Task 14708 — Web Developers (`15-1254.00`)

**Task text:** Communicate with network personnel or Web site hosting agencies to address hardware or software issues affecting Web sites.

**Task Type:** Core  
**# derived skill edges:** 26

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I/G |
|---:|---|---|---:|---|---|---|---|
| 1 | Critical Thinking | essential | 3.75 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.2.a` |P |
| 2 | Critical Thinking | essential | 3.75 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.2.a` |P |
| 3 | Complex Problem Solving | transferable | 3.62 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.2.i` |P |
| 4 | Reading Comprehension | essential | 3.62 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.a` |P |
| 5 | Active Listening | essential | 3.50 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.1.b` |P |
| 6 | Active Listening | essential | 3.50 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.b` |P |
| 7 | Judgment and Decision Making | transferable | 3.38 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.e` |P |
| 8 | Speaking | essential | 3.25 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.1.d` |P |
| 9 | Speaking | essential | 3.25 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.d` |P |
| 10 | Systems Analysis | transferable | 3.12 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.g` |P |
| 11 | Writing | essential | 3.12 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.c` |P |
| 12 | Coordination | transferable | 3.00 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.b` |P |
| 13 | Coordination | transferable | 3.00 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.b` |P |
| 14 | Monitoring | essential | 3.00 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.A.2.d` |P |
| 15 | Monitoring | essential | 3.00 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.2.d` |P |
| 16 | Systems Evaluation | transferable | 3.00 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.h` |P |
| 17 | Time Management | transferable | 3.00 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.5.a` |P |
| 18 | Persuasion | transferable | 2.88 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.c` |P |
| 19 | Persuasion | transferable | 2.88 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.c` |P |
| 20 | Service Orientation | transferable | 2.88 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.f` |P |
| 21 | Service Orientation | transferable | 2.88 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.f` |P |
| 22 | Social Perceptiveness | transferable | 2.88 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.a` |P |
| 23 | Social Perceptiveness | transferable | 2.88 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.a` |P |
| 24 | Instructing | transferable | 2.75 | Provide technical support for computer network issues. (`4.A.4.b.6.d.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.5 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.e` |P |
| 25 | Negotiation | transferable | 2.75 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.1.d` |P |
| 26 | Management of Personnel Resources | transferable | 2.38 | Collaborate with others to resolve information technology issues. (`4.A.4.b.1.a.3`) | Coordinating the Work and Activities of Others (`4.A.4.b.1`) | `4.A.4.b.1.a.3 → 4.A.4.b.1.a → 4.A.4.b.1 → 2.B.5.d` |P |

### Task 14725 — Web Developers (`15-1254.00`)

**Task text:** Evaluate or recommend server hardware or software.

**Task Type:** Core  
**# derived skill edges:** 17

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I |
|---:|---|---|---:|---|---|---|---|
| 1 | Critical Thinking | essential | 3.75 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.2.a` |P |
| 2 | Complex Problem Solving | transferable | 3.62 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.2.i` |P |
| 3 | Reading Comprehension | essential | 3.62 | Evaluate utility of software or hardware technologies. (`4.A.2.a.1.g.8`) | Judging the Qualities of Objects, Services, or People (`4.A.2.a.1`) | `4.A.2.a.1.g.8 → 4.A.2.a.1.g → 4.A.2.a.1 → 2.A.1.a` |P |
| 4 | Reading Comprehension | essential | 3.62 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.a` |P |
| 5 | Active Listening | essential | 3.50 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.b` |P |
| 6 | Judgment and Decision Making | transferable | 3.38 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.e` |P |
| 7 | Speaking | essential | 3.25 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.d` |P |
| 8 | Systems Analysis | transferable | 3.12 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.g` |P |
| 9 | Writing | essential | 3.12 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.1.c` |P |
| 10 | Coordination | transferable | 3.00 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.b` |P |
| 11 | Monitoring | essential | 3.00 | Evaluate utility of software or hardware technologies. (`4.A.2.a.1.g.8`) | Judging the Qualities of Objects, Services, or People (`4.A.2.a.1`) | `4.A.2.a.1.g.8 → 4.A.2.a.1.g → 4.A.2.a.1 → 2.A.2.d` |P |
| 12 | Monitoring | essential | 3.00 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.A.2.d` |P |
| 13 | Systems Evaluation | transferable | 3.00 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.4.h` |P |
| 14 | Persuasion | transferable | 2.88 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.c` |P |
| 15 | Service Orientation | transferable | 2.88 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.f` |P |
| 16 | Social Perceptiveness | transferable | 2.88 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.a` |P |
| 17 | Instructing | transferable | 2.75 | Provide recommendations to others about computer hardware. (`4.A.4.b.6.d.3`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.d.3 → 4.A.4.b.6.d → 4.A.4.b.6 → 2.B.1.e` |P |

### Task 21836 — Data Scientists (`15-2051.00`)

**Task text:** Recommend data-driven solutions to key stakeholders.

**Task Type:** nan  
**# derived skill edges:** 15

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I |
|---:|---|---|---:|---|---|---|---|
| 1 | Active Listening | essential |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.A.1.b` |P |
| 2 | Complex Problem Solving | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.2.i` |P |
| 3 | Coordination | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.1.b` |P |
| 4 | Critical Thinking | essential |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.A.2.a` |P |
| 5 | Instructing | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.1.e` |P |
| 6 | Judgment and Decision Making | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.4.e` |P |
| 7 | Monitoring | essential |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.A.2.d` |P |
| 8 | Persuasion | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.1.c` |P |
| 9 | Reading Comprehension | essential |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.A.1.a` |P |
| 10 | Service Orientation | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.1.f` |P |
| 11 | Social Perceptiveness | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.1.a` |P |
| 12 | Speaking | essential |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.A.1.d` |P |
| 13 | Systems Analysis | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.4.g` |P |
| 14 | Systems Evaluation | transferable |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.B.4.h` |P |
| 15 | Writing | essential |  | Advise others on analytical techniques. (`4.A.4.b.6.e.5`) | Providing Consultation and Advice to Others (`4.A.4.b.6`) | `4.A.4.b.6.e.5 → 4.A.4.b.6.e → 4.A.4.b.6 → 2.A.1.c` |P |

### Task 21825 — Data Scientists (`15-2051.00`)

**Task text:** Apply sampling techniques to determine groups to be surveyed or use complete enumeration methods.

**Task Type:** nan  
**# derived skill edges:** 7

| # | Skill | Kind | Imp. | DWA | GWA | Path | P/I |
|---:|---|---|---:|---|---|---|---|
| 1 | Active Learning | essential |  | Determine appropriate methods for data analysis. (`4.A.2.b.1.d.10`) | Making Decisions and Solving Problems (`4.A.2.b.1`) | `4.A.2.b.1.d.10 → 4.A.2.b.1.d → 4.A.2.b.1 → 2.A.2.b` |P |
| 2 | Active Listening | essential |  | Determine appropriate methods for data analysis. (`4.A.2.b.1.d.10`) | Making Decisions and Solving Problems (`4.A.2.b.1`) | `4.A.2.b.1.d.10 → 4.A.2.b.1.d → 4.A.2.b.1 → 2.A.1.b` |P |
| 3 | Complex Problem Solving | transferable |  | Determine appropriate methods for data analysis. (`4.A.2.b.1.d.10`) | Making Decisions and Solving Problems (`4.A.2.b.1`) | `4.A.2.b.1.d.10 → 4.A.2.b.1.d → 4.A.2.b.1 → 2.B.2.i` |P |
| 4 | Critical Thinking | essential |  | Determine appropriate methods for data analysis. (`4.A.2.b.1.d.10`) | Making Decisions and Solving Problems (`4.A.2.b.1`) | `4.A.2.b.1.d.10 → 4.A.2.b.1.d → 4.A.2.b.1 → 2.A.2.a` |P |
| 5 | Judgment and Decision Making | transferable |  | Determine appropriate methods for data analysis. (`4.A.2.b.1.d.10`) | Making Decisions and Solving Problems (`4.A.2.b.1`) | `4.A.2.b.1.d.10 → 4.A.2.b.1.d → 4.A.2.b.1 → 2.B.4.e` |P |
| 6 | Reading Comprehension | essential |  | Determine appropriate methods for data analysis. (`4.A.2.b.1.d.10`) | Making Decisions and Solving Problems (`4.A.2.b.1`) | `4.A.2.b.1.d.10 → 4.A.2.b.1.d → 4.A.2.b.1 → 2.A.1.a` |P |
| 7 | Systems Evaluation | transferable |  | Determine appropriate methods for data analysis. (`4.A.2.b.1.d.10`) | Making Decisions and Solving Problems (`4.A.2.b.1`) | `4.A.2.b.1.d.10 → 4.A.2.b.1.d → 4.A.2.b.1 → 2.B.4.h` |P |
