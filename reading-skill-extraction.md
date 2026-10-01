# Reading: skill extraction and ESCO linking
### What the field already knows, and what it means for your build

*Annotated for the Build and Validate stages. Each entry ends with why it matters to you specifically. Citations are in a form you can drop into a lit review.*

---

## The headline for your method

The field has converged on a **three-stage pipeline** for linking free text to a large controlled vocabulary like ESCO:

1. **Extract** — find the skill-bearing span in the text
2. **Retrieve** — embed the span, vector-search the taxonomy for top-*k* candidates
3. **Rank** — a second model (often an LLM) picks or re-ranks among those candidates

Do **not** hand all ~13,900 ESCO skills to an LLM and ask it to pick. That is the documented failure mode — the model invents skill labels and codes that don't exist. Retrieval constrains the output space to real concepts.

**Your adaptation:** you're not extracting from noisy job ads. O\*NET task statements are already clean, single-purpose sentences. So stage 1 is largely free — the task statement *is* the span, or at most needs light decomposition. That makes your problem meaningfully easier than the published benchmarks, and worth saying explicitly in your methods chapter.

---

## Core papers

**Zhang, Jensen, Sonniks & Plank (2022). SkillSpan: Hard and soft skill extraction from English job postings.** NAACL 2022.
The benchmark that defined the task. 265 annotated English job postings, ~14.5K sentences, 12.5K+ annotated spans, with a hard/soft skill distinction. Everything after this cites it.
→ *For you:* the standard citation for "skill extraction is an established task with real benchmarks." Also the source of realistic performance expectations — span-level F1 in the 50s–60s is state of the art, not a weak result.

**Zhang, van der Goot & Plank (2023). ESCOXLM-R: Multilingual taxonomy-driven pre-training for the job market domain.** ACL 2023.
Pre-trains a language model on ESCO itself, then fine-tunes for downstream job-market tasks. Beat prior state of the art on six of nine datasets across four languages.
→ *For you:* evidence that ESCO's structure carries usable signal beyond its labels — which is part of your argument for using it as the vocabulary.

**Nguyen, Zhang, Montariol & Bosselut (2024). Rethinking skill extraction in the job market domain using large language models.** NLP4HR 2024, pp. 27–42.
Tests in-context learning against supervised models on six uniformized skill-extraction datasets. Key finding, and it's nuanced: **LLMs do not match supervised models on raw performance, but handle syntactically complex and ambiguous skill mentions better.**
→ *For you:* the honest citation for why LLM-based linking is defensible but not automatically superior. Cite it when you justify a hybrid rather than an LLM-only approach — and when a reviewer asks why you didn't just fine-tune a supervised model (answer: no annotated task→skill training data exists, which is the gap you're filling).

**Zhang, van der Goot & Plank (2024). Entity linking in the job market domain.** EACL Findings.
Treats skill-to-ESCO as an entity-linking problem specifically, rather than classification.
→ *For you:* this is the framing you want. Your task is entity linking — mapping a mention to a canonical concept — not classification into a small label set. Use that vocabulary in your methods.

**Decorte et al. (2024). JobSKAPE: A framework for generating synthetic job postings to enhance skill matching.** NLP4HR 2024.
Generates synthetic training data to address the scarcity of annotated skill-linking data, formalizing the extraction → candidate-selection → matching pipeline.
→ *For you:* mostly useful as the clearest statement of the pipeline structure. The synthetic-data angle is a fallback if you ever need training data you don't have.

**Zhang et al. (2024). NNOSE: Nearest neighbor occupational skill extraction.** EACL 2024.
Uses a nearest-neighbour datastore across skill datasets to improve extraction, particularly for rare skills.
→ *For you:* directly relevant if your ESCO retrieval struggles on long-tail technical skills — which is exactly where the value of leaving O\*NET's 35-skill vocabulary lies.

---

## Tools you could use instead of building

**Nesta Skills Extractor (`ojd_daps_skills`)** — nestauk.github.io/ojd_daps_skills
Open-source Python library that extracts skill phrases from text and **maps them onto a taxonomy of your choice — ESCO, Lightcast Open Skills, or a custom one**. `pip install ojd_daps_skills`. Used in production on Nesta's Open Jobs Observatory across millions of job adverts.
One documented behaviour worth knowing: ESCO doesn't contain "React", but the model detected React as a skill in context and mapped it to the ESCO skill "use scripting programming" — graceful degradation to the nearest existing concept rather than failure.
→ *For you:* **test this first, before writing any pipeline.** If it works acceptably on O\*NET task statements, your Build stage collapses from weeks to days. Note the caveat: it was trained on job adverts, not task statements, so validate on a sample before committing. The custom-taxonomy support also means you could map onto a filtered ESCO subset.

**ESCOX** — open-source (MIT), embedding-based ESCO matching plus LLM, with GUI and API.
→ *For you:* a second option if Nesta's doesn't fit. MIT license means no redistribution concerns.

**SkillGPT** — LLM-based skill extraction and standardization to ESCO, exposed as a REST API.
→ *For you:* mainly a citation; the API dependency makes it less attractive than a library you run locally.

---

## Benchmarks to set expectations

- Span-level skill extraction: **F1 in the 50s–60s** is state of the art
- End-to-end ESCO linking: **F1 around 0.54–0.56** in recent multilingual work
- LLMs underperform supervised models on raw metrics but handle complex mentions better

**Use these as your yardstick.** If your task→ESCO linking lands near 0.6, that is a *good* result against published baselines — not a disappointment. Write the benchmark into your proposal *before* you run anything, so the number you get is interpreted against a pre-registered expectation rather than a vibe.

**Related evaluation resources:** MELO (arXiv:2410.08319) is a multilingual entity-linking benchmark for occupations; TalentCLEF 2025 ran a shared task on job title and skill matching. Both are useful if you want an external comparison point.

---

## What this changes about your build

1. **Try Nesta's library before writing code.** Half a day to test; potentially weeks saved.
2. **Structure as retrieve-then-rank**, never LLM-over-full-taxonomy. Embed ESCO once, vector search per task, LLM ranks top-*k*.
3. **Call it entity linking**, not classification — that's the literature's framing and it makes your work legible to that audience.
4. **Your task is easier than the benchmarks** because O\*NET task statements are clean and single-purpose, unlike job ads. Say so, and expect to beat ~0.55 — but note that no published benchmark exists for *task*-level linking, which is why your validation against ESCO's essential-skill sets matters.
5. **Set the expectation now.** ~0.55 F1 is the field's current ceiling for this class of problem. Anything near it is publishable.

---

## Still to pull (Validate stage)

- **EC/DOL ESCO–O\*NET crosswalk technical report** — `esco.ec.europa.eu/system/files/2022-12/ONET ESCO Technical Report.pdf`. Method template: they mapped two occupational vocabularies using ML plus human validation, and documented mapping guidelines and QA. Directly parallel to your validation design, and a strong citation.
