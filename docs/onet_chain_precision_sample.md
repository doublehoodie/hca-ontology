# O*NET chain precision sample

Source: `data/processed/task_skill_derived.csv` (Task→DWA→GWA→Skill).
Evaluation set: **same 20 tasks** as [`docs/nesta_precision_sample.md`](nesta_precision_sample.md), same order and occupation grouping.
Unit listed: unique `(task_id, skill_name)` — multiple DWA/GWA paths to the same skill collapsed; `paths` = number of chain edges.
Mark each row **P** / **I** / **G**. Leave blank until hand-coded.

## Summary (before grading)

- Tasks: **20** (identical set to Nesta precision sample)
- Total unique `(task_id, skill_name)` pairs: **132**
- Tasks with zero O*NET chain skill edges: **0**

| Occupation | Tasks in sample | Unique skill pairs |
|---|---:|---:|
| 15-1212.00 Information Security Analysts | 4 | 15 |
| 15-1242.00 Database Administrators | 4 | 33 |
| 15-1252.00 Software Developers | 4 | 37 |
| 15-1254.00 Web Developers | 4 | 18 |
| 15-2051.00 Data Scientists | 4 | 29 |

## 15-1212.00 — Information Security Analysts

### Task 5320

**Task text:** Perform risk assessments and execute tests of data processing system to ensure functioning of data processing activities and security measures.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Critical Thinking | essential | 1 path | Inspecting Equipment, Structures, or Materials |P |
| 2 | Operations Monitoring | transferable | 1 path | Inspecting Equipment, Structures, or Materials |P |
| 3 | Troubleshooting | transferable | 1 path | Inspecting Equipment, Structures, or Materials |P |
| 4 | Quality Control Analysis | transferable | 1 path | Inspecting Equipment, Structures, or Materials |P |

### Task 5321

**Task text:** Encrypt data transmissions and erect firewalls to conceal confidential information as it is being transmitted and to keep out tainted digital transfers.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Working with Computers |G |
| 2 | Critical Thinking | essential | 1 path | Working with Computers |G |
| 3 | Complex Problem Solving | transferable | 1 path | Working with Computers |G |
| 4 | Programming | transferable | 1 path | Working with Computers |I |
| 5 | Systems Analysis | transferable | 1 path | Working with Computers |P |

### Task 5323

**Task text:** Review violations of computer security procedures and discuss procedures with violators to ensure violations are not repeated.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Working with Computers |G |
| 2 | Critical Thinking | essential | 1 path | Working with Computers |G |
| 3 | Complex Problem Solving | transferable | 1 path | Working with Computers |G |
| 4 | Programming | transferable | 1 path | Working with Computers |I |
| 5 | Systems Analysis | transferable | 1 path | Working with Computers |I |

### Task 5322

**Task text:** Document computer security and emergency measures policies, procedures, and tests.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Writing | essential | 1 path | Documenting/Recording Information |P |

## 15-1242.00 — Database Administrators

### Task 1306

**Task text:** Develop data models describing data elements and how they are used, following procedures and using pen, template, or computer software.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment |G |
| 2 | Writing | essential | 1 path | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment |G |
| 3 | Instructing | transferable | 1 path | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment |I |

### Task 1313

**Task text:** Write and code logical and physical database descriptions and specify identifiers of database to management system, or direct others in coding descriptions.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Critical Thinking | essential | 2 paths | Thinking Creatively; Working with Computers |G |
| 2 | Technology Design | transferable | 1 path | Thinking Creatively |P |
| 3 | Reading Comprehension | essential | 1 path | Working with Computers |G |
| 4 | Complex Problem Solving | transferable | 1 path | Working with Computers |G |
| 5 | Programming | transferable | 1 path | Working with Computers |P |
| 6 | Systems Analysis | transferable | 1 path | Working with Computers |P |

### Task 1302

**Task text:** Approve, schedule, plan, and supervise the installation and testing of new products and improvements to computer systems, such as the installation of new databases.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Critical Thinking | essential | 2 paths | Organizing, Planning, and Prioritizing Work; Guiding, Directing, and Motivating Subordinates |G |
| 2 | Complex Problem Solving | transferable | 1 path | Organizing, Planning, and Prioritizing Work |G |
| 3 | Judgment and Decision Making | transferable | 1 path | Organizing, Planning, and Prioritizing Work |P |
| 4 | Systems Analysis | transferable | 1 path | Organizing, Planning, and Prioritizing Work |P |
| 5 | Time Management | transferable | 2 paths | Organizing, Planning, and Prioritizing Work; Guiding, Directing, and Motivating Subordinates |P |
| 6 | Active Listening | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 7 | Writing | essential | 1 path | Guiding, Directing, and Motivating Subordinates | G|
| 8 | Speaking | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 9 | Active Learning | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 10 | Learning Strategies | essential | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 11 | Monitoring | essential | 1 path | Guiding, Directing, and Motivating Subordinates |P |
| 12 | Social Perceptiveness | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 13 | Coordination | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |P |
| 14 | Persuasion | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 15 | Negotiation | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 16 | Instructing | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 17 | Service Orientation | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 18 | Management of Personnel Resources | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |P |

### Task 21651

**Task text:** Test changes to database applications or systems.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Critical Thinking | essential | 1 path | Inspecting Equipment, Structures, or Materials |G |
| 2 | Operations Monitoring | transferable | 1 path | Inspecting Equipment, Structures, or Materials |P |
| 3 | Troubleshooting | transferable | 1 path | Inspecting Equipment, Structures, or Materials |P |
| 4 | Quality Control Analysis | transferable | 1 path | Inspecting Equipment, Structures, or Materials |P |
| 5 | Reading Comprehension | essential | 1 path | Judging the Qualities of Objects, Services, or People | G|
| 6 | Monitoring | essential | 1 path | Judging the Qualities of Objects, Services, or People |G |

## 15-1252.00 — Software Developers

### Task 21667

**Task text:** Design, develop and modify software systems, using scientific analysis and mathematical models to predict and measure outcomes and consequences of design.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Analyzing Data or Information |G |
| 2 | Critical Thinking | essential | 3 paths | Analyzing Data or Information; Thinking Creatively |G |
| 3 | Technology Design | transferable | 2 paths | Thinking Creatively |P |

### Task 21669

**Task text:** Develop or direct software system testing or validation procedures, programming, or documentation.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment |G |
| 2 | Writing | essential | 2 paths | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment; Guiding, Directing, and Motivating Subordinates |P |
| 3 | Instructing | transferable | 2 paths | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment; Guiding, Directing, and Motivating Subordinates |I |
| 4 | Active Listening | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 5 | Speaking | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 6 | Critical Thinking | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 7 | Active Learning | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 8 | Learning Strategies | essential | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 9 | Monitoring | essential | 1 path | Guiding, Directing, and Motivating Subordinates |P |
| 10 | Social Perceptiveness | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 11 | Coordination | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |P |
| 12 | Persuasion | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 13 | Negotiation | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 14 | Service Orientation | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 15 | Time Management | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 16 | Management of Personnel Resources | transferable | 1 path | Guiding, Directing, and Motivating Subordinates | P|

### Task 21666

**Task text:** Coordinate installation of software system.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Active Listening | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 2 | Writing | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 3 | Speaking | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 4 | Critical Thinking | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 5 | Active Learning | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 6 | Learning Strategies | essential | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 7 | Monitoring | essential | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 8 | Social Perceptiveness | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 9 | Coordination | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |P |
| 10 | Persuasion | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 11 | Negotiation | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 12 | Instructing | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 13 | Service Orientation | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |I |
| 14 | Time Management | transferable | 1 path | Guiding, Directing, and Motivating Subordinates |G |
| 15 | Management of Personnel Resources | transferable | 1 path | Guiding, Directing, and Motivating Subordinates | I|

### Task 21668

**Task text:** Determine system performance standards.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment |G |
| 2 | Writing | essential | 1 path | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment | G|
| 3 | Instructing | transferable | 1 path | Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment |I |

## 15-1254.00 — Web Developers

### Task 14713

**Task text:** Respond to user email inquiries, or set up automated systems to send responses.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Active Listening | essential | 1 path | Communicating with People Outside the Organization |G |
| 2 | Writing | essential | 1 path | Communicating with People Outside the Organization |P |
| 3 | Speaking | essential | 1 path | Communicating with People Outside the Organization |I |
| 4 | Social Perceptiveness | transferable | 1 path | Communicating with People Outside the Organization |G |
| 5 | Persuasion | transferable | 1 path | Communicating with People Outside the Organization |I |
| 6 | Service Orientation | transferable | 1 path | Communicating with People Outside the Organization |P |

### Task 14707

**Task text:** Write supporting code for Web applications or Web sites.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Critical Thinking | essential | 2 paths | Thinking Creatively; Working with Computers |G |
| 2 | Technology Design | transferable | 1 path | Thinking Creatively |P |
| 3 | Reading Comprehension | essential | 1 path | Working with Computers | G|
| 4 | Complex Problem Solving | transferable | 1 path | Working with Computers |G |
| 5 | Programming | transferable | 1 path | Working with Computers |P|
| 6 | Systems Analysis | transferable | 1 path | Working with Computers |I |

### Task 14728

**Task text:** Document technical factors such as server load, bandwidth, database performance, and browser and device types.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Writing | essential | 1 path | Documenting/Recording Information |P |

### Task 14705

**Task text:** Renew domain name registrations.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Working with Computers |G |
| 2 | Critical Thinking | essential | 1 path | Working with Computers |G|
| 3 | Complex Problem Solving | transferable | 1 path | Working with Computers |I |
| 4 | Programming | transferable | 1 path | Working with Computers |I |
| 5 | Systems Analysis | transferable | 1 path | Working with Computers |I|

## 15-2051.00 — Data Scientists

### Task 21831

**Task text:** Identify business problems or management objectives that can be addressed through data analysis.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Making Decisions and Solving Problems |G |
| 2 | Active Listening | essential | 1 path | Making Decisions and Solving Problems |G |
| 3 | Critical Thinking | essential | 1 path | Making Decisions and Solving Problems |G |
| 4 | Active Learning | essential | 1 path | Making Decisions and Solving Problems |G |
| 5 | Complex Problem Solving | transferable | 1 path | Making Decisions and Solving Problems |P |
| 6 | Judgment and Decision Making | transferable | 1 path | Making Decisions and Solving Problems |P |
| 7 | Systems Evaluation | transferable | 1 path | Making Decisions and Solving Problems |P |

### Task 21835

**Task text:** Read scientific articles, conference papers, or other sources of research to identify emerging analytic trends and technologies.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Updating and Using Relevant Knowledge |P |
| 2 | Active Listening | essential | 1 path | Updating and Using Relevant Knowledge |I |
| 3 | Active Learning | essential | 1 path | Updating and Using Relevant Knowledge |P |
| 4 | Learning Strategies | essential | 1 path | Updating and Using Relevant Knowledge |I |
| 5 | Time Management | transferable | 1 path | Updating and Using Relevant Knowledge |G |

### Task 21823

**Task text:** Analyze, manipulate, or process large sets of data using statistical software.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Analyzing Data or Information |G |
| 2 | Critical Thinking | essential | 1 path | Analyzing Data or Information |G |

### Task 21836

**Task text:** Recommend data-driven solutions to key stakeholders.

| # | skill_name | skill_kind (essential/transferable) | paths | derivation (GWA name) | P/I/G |
|---:|---|---|---:|---|---|
| 1 | Reading Comprehension | essential | 1 path | Providing Consultation and Advice to Others |G |
| 2 | Active Listening | essential | 1 path | Providing Consultation and Advice to Others |G |
| 3 | Writing | essential | 1 path | Providing Consultation and Advice to Others |G |
| 4 | Speaking | essential | 1 path | Providing Consultation and Advice to Others |P |
| 5 | Critical Thinking | essential | 1 path | Providing Consultation and Advice to Others |G |
| 6 | Monitoring | essential | 1 path | Providing Consultation and Advice to Others |I |
| 7 | Social Perceptiveness | transferable | 1 path | Providing Consultation and Advice to Others |G |
| 8 | Coordination | transferable | 1 path | Providing Consultation and Advice to Others |I |
| 9 | Persuasion | transferable | 1 path | Providing Consultation and Advice to Others | P|
| 10 | Instructing | transferable | 1 path | Providing Consultation and Advice to Others |P |
| 11 | Service Orientation | transferable | 1 path | Providing Consultation and Advice to Others |I |
| 12 | Complex Problem Solving | transferable | 1 path | Providing Consultation and Advice to Others |G |
| 13 | Judgment and Decision Making | transferable | 1 path | Providing Consultation and Advice to Others | P|
| 14 | Systems Analysis | transferable | 1 path | Providing Consultation and Advice to Others |I |
| 15 | Systems Evaluation | transferable | 1 path | Providing Consultation and Advice to Others |I |
