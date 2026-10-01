# Nesta ESCO precision sample

Source: `data/processed/nesta_task_esco.csv` (unfiltered).
20 tasks stratified across the five occupations (~4 each).
Mark each mapping **P** (plausible) / **I** (implausible) / **G** (generic/dilutive).

Skill-level rows have `esco_uri`; group-level rows have `esco_group_code` only.

## 15-1212.00 — Information Security Analysts

### Task 5320

**Task text:** Perform risk assessments and execute tests of data processing system to ensure functioning of data processing activities and security measures.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Perform risk assessments | make risk assessment | skill | 0.9358219271117243 | `esco_uri`=http://data.europa.eu/esco/skill/594bd121-9614-4e87-9ecf-6ccb95507efe |P |
| 2 | execute tests of data processing system | execute system testing procedures | skill | 0.7645986971331532 | `esco_uri`=http://data.europa.eu/esco/skill/465ff64a-1271-4064-8ed1-e969cb68d8b4 |P |

### Task 5321

**Task text:** Encrypt data transmissions and erect firewalls to conceal confidential information as it is being transmitted and to keep out tainted digital transfers.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Encrypt data transmissions | database and network design and administration | most_common_level_3 | 0.20388349514563106 | `esco_group_code`=K0612 |G |
| 2 | erect firewalls | implement a firewall | skill | 0.740152069932386 | `esco_uri`=http://data.europa.eu/esco/skill/e5b5053e-0ef6-4c4e-a3f2-42f955f4322c |P |

### Task 5323

**Task text:** Review violations of computer security procedures and discuss procedures with violators to ensure violations are not repeated.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Review violations | analysing and evaluating information and data | most_common_level_3 | 0.39316239316239315 | `esco_group_code`=S2.7.0 |G |

### Task 5322

**Task text:** Document computer security and emergency measures policies, procedures, and tests.

_No mapped skills (null placeholder row)._

| # | ojo_skill | match_skill | match_type | match_score | id/uri | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | — | — | — | — | — | |

## 15-1242.00 — Database Administrators

### Task 1306

**Task text:** Develop data models describing data elements and how they are used, following procedures and using pen, template, or computer software.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Develop data models | data models | skill | 0.8599852197581022 | `esco_uri`=http://data.europa.eu/esco/skill/fecf8a0d-62c4-4e71-9b03-0f4fc2ad7bf5 |P |
| 2 | describing data elements | managing and analysing digital data | most_common_level_3 | 0.20930232558139536 | `esco_group_code`=S5.5.2 |P |

### Task 1313

**Task text:** Write and code logical and physical database descriptions and specify identifiers of database to management system, or direct others in coding descriptions.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Write and code logical and physical database descriptions | define database physical structure | skill | 0.7028443858294183 | `esco_uri`=http://data.europa.eu/esco/skill/022dc430-872a-473a-9cf4-fed4895e58ad |P |
| 2 | coding | a product coding system | skill | 0.7127205910348874 | `esco_uri`=http://data.europa.eu/esco/skill/af582ee4-bbc8-436c-96f2-df0cb2049f5d |P |

### Task 1302

**Task text:** Approve, schedule, plan, and supervise the installation and testing of new products and improvements to computer systems, such as the installation of new databases.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Approve, schedule, plan, and supervise the installation and testing of new products and improvements to | directing operational activities | most_common_level_3 | 0.38144329896907214 | `esco_group_code`=S4.2.1 |P |

### Task 21651

**Task text:** Test changes to database applications or systems.

_No mapped skills (null placeholder row)._

| # | ojo_skill | match_skill | match_type | match_score | id/uri | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | — | — | — | — | — | |

## 15-1252.00 — Software Developers

### Task 21667

**Task text:** Design, develop and modify software systems, using scientific analysis and mathematical models to predict and measure outcomes and consequences of design.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | develop software systems , using scientific analysis and mathematical models to predict and measure outcomes and consequences of design | statistics | most_common_level_3 | 0.2903225806451613 | `esco_group_code`=K0542 |P |
| 2 | modify software systems , using scientific analysis and mathematical models to predict and measure outcomes and consequences of design | statistics | most_common_level_3 | 0.29508196721311475 | `esco_group_code`=K0542 |P |
| 3 | using scientific analysis | utilise scientific methods | skill | 0.7582706240457857 | `esco_uri`=http://data.europa.eu/esco/skill/7a34b3d9-bd3b-4f4e-a0f6-f97439901cb7 |P |

### Task 21669

**Task text:** Develop or direct software system testing or validation procedures, programming, or documentation.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Develop or direct software system testing or validation procedures | implement system testing procedures | skill | 0.7884609752384839 | `esco_uri`=http://data.europa.eu/esco/skill/465ff64a-1271-4064-8ed1-e969cb68d8b4 |P |

### Task 21666

**Task text:** Coordinate installation of software system.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Coordinate installation of software system | setting up computer systems | most_common_level_3 | 0.8983050847457628 | `esco_group_code`=S5.2.1 |P |

### Task 21668

**Task text:** Determine system performance standards.

_No mapped skills (null placeholder row)._

| # | ojo_skill | match_skill | match_type | match_score | id/uri | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | — | — | — | — | — | |

## 15-1254.00 — Web Developers

### Task 14713

**Task text:** Respond to user email inquiries, or set up automated systems to send responses.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Respond to user email inquiries | respond to inquiries by customers | skill | 0.7483250566467252 | `esco_uri`=http://data.europa.eu/esco/skill/cace7a77-38b7-4cdf-8171-e17692bef5f6 |P |

### Task 14707

**Task text:** Write supporting code for Web applications or Web sites.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Write supporting code | technical or academic writing | most_common_level_3 | 0.5806451612903226 | `esco_group_code`=S1.13.3 |I |
| 2 | Web applications | web programming | skill | 0.7450166195956461 | `esco_uri`=http://data.europa.eu/esco/skill/69bbd53f-fbb0-4476-b4b2-ef7844464e28 |P |
| 3 | Web sites | library, information and archival studies | most_common_level_3 | 0.4305555555555556 | `esco_group_code`=K0322 |I |

### Task 14728

**Task text:** Document technical factors such as server load, bandwidth, database performance, and browser and device types.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | browser | software and applications development and analysis | most_common_level_3 | 0.2898550724637681 | `esco_group_code`=K0613 |G |

### Task 14705

**Task text:** Renew domain name registrations.

_No mapped skills (null placeholder row)._

| # | ojo_skill | match_skill | match_type | match_score | id/uri | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | — | — | — | — | — | |

## 15-2051.00 — Data Scientists

### Task 21831

**Task text:** Identify business problems or management objectives that can be addressed through data analysis.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Identify business problems or management objectives | analyse business objectives | skill | 0.8067390571898769 | `esco_uri`=http://data.europa.eu/esco/skill/408fcc8e-d4e6-43e7-ab27-b617a1dced98 |P |

### Task 21835

**Task text:** Read scientific articles, conference papers, or other sources of research to identify emerging analytic trends and technologies.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Read scientific articles | read articles | skill | 0.7991808703986092 | `esco_uri`=http://data.europa.eu/esco/skill/935f7adb-b7fb-474f-a509-cddee89889d1 |P |

### Task 21823

**Task text:** Analyze, manipulate, or process large sets of data using statistical software.

| # | ojo_skill | match_skill | match_type | match_score | id / uri or group code | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | Analyze, manipulate, or process large sets of data using statistical software | programming computer systems | most_common_level_3 | 0.6119402985074627 | `esco_group_code`=S5.1.0 |P |

### Task 21836

**Task text:** Recommend data-driven solutions to key stakeholders.

_No mapped skills (null placeholder row)._

| # | ojo_skill | match_skill | match_type | match_score | id/uri | P/I/G |
|---:|---|---|---|---:|---|---|
| 1 | — | — | — | — | — | |
