# Five-Day Build Runbook
### From zero to a validated thin-slice ontology you can demo

*Everything here is copy-pasteable. Where you must make a judgment call yourself, there's a **🛑 YOUR CALL** marker with the specific decision and my recommendation. Verified against O\*NET 30.3 (site updated 14 July 2026).*

---

## ⚠️ Read this first: two corrections to the recon report

O\*NET 30.3 restructured the Content Model into a three-dimensional (Worker / Job / Market) structure. Two changes matter enormously to your build:

**1. `Tools Used` is discontinued.** It is no longer updated or included in the database as of 30.3; O\*NET advises using the last version from the **30.2** release. Your ontology's Tool/Equipment class must be populated from a frozen 30.2 snapshot. *Note this in your thesis — a core O\*NET category being frozen is direct evidence for your "O\*NET's maintenance model is failing" argument.*

**2. Skill↔Work Activity linkage files now exist.** 30.3 added:
- `Essential Skills to Work Activities` (110 rows)
- `Transferable Skills to Work Activities` (122 rows)
- `Abilities to Work Activities` (381 rows)

This is the big one. It means **you can derive task→skill edges entirely from O\*NET source data**, no LLM required for the baseline:

```
Task → DWA → IWA → GWA (Work Activity) → Essential/Transferable Skill
```

Your Group C contribution is now *cheaper, faster, and far more defensible* than the LLM route. See Day 4.

**3. The `Skills` file is now split** into `Essential Skills` (17,880 rows) and `Transferable Skills` (44,700 rows). This maps beautifully onto your A1 essential/optional competency question — though note O\*NET's "essential vs transferable" is a *different* distinction from ESCO's "essential vs optional." Don't conflate them (see Day 3).

Migration reference (keep open): `https://www.onetcenter.org/dl_files/30_3_migration_reference.xlsx`

---

## Day 1 — Environment and data acquisition (~3 hours)

### 1.1 Set up the repo

```bash
mkdir -p ~/onet-ontology/{data/raw,data/interim,data/processed,ontology,scripts,notebooks,docs}
cd ~/onet-ontology
git init
python3 -m venv .venv && source .venv/bin/activate
pip install pandas openpyxl owlready2 rdflib requests
printf ".venv/\ndata/raw/\n__pycache__/\n" > .gitignore
```

> `data/raw/` is gitignored (large + redistributable-with-attribution, cleaner to re-fetch). Your *scripts* are the reproducible artifact, not the raw data.

### 1.2 Download the O\*NET 30.3 files you need

```bash
cd ~/onet-ontology/data/raw
BASE="https://www.onetcenter.org/dl_files/database/db_30_3_csv"

# Occupation spine
curl -O $BASE/occupation_data.csv
curl -O $BASE/job_zones.csv
curl -O $BASE/job_titles.csv
curl -O $BASE/sample_of_reported_titles.csv
curl -O $BASE/related_occupations.csv

# Tasks (your atomic unit)
curl -O $BASE/task_statements.csv
curl -O $BASE/task_ratings.csv
curl -O $BASE/task_categories.csv

# The activity chain — this is what makes task→skill possible
curl -O $BASE/tasks_to_dwas.csv
curl -O $BASE/gwas_to_iwas_to_dwas.csv
curl -O $BASE/gwas_to_iwas.csv
curl -O $BASE/work_activities.csv

# Skills / knowledge / abilities
curl -O $BASE/essential_skills.csv
curl -O $BASE/transferable_skills.csv
curl -O $BASE/knowledge.csv
curl -O $BASE/abilities.csv

# ⭐ The new linkage files — the core of your Day 4
curl -O $BASE/essential_skills_to_work_activities.csv
curl -O $BASE/transferable_skills_to_work_activities.csv
curl -O $BASE/abilities_to_work_activities.csv

# Software
curl -O $BASE/software_skills.csv

# Metadata / reference
curl -O $BASE/content_model_reference.csv
curl -O $BASE/scales_reference.csv
curl -O $BASE/occupation_level_metadata.csv
```

**Tools/equipment (from the frozen 30.2 release):**
```bash
curl -O https://www.onetcenter.org/dl_files/database/db_30_2_csv/tools_used.csv
```
If that 404s, get it from the archive page `https://www.onetcenter.org/db_releases.html` → 30.2 → CSV. **Verify the exact filename before assuming.**

**Migration reference (Excel, for UNSPSC→Content Model ID crosswalk):**
```bash
curl -O https://www.onetcenter.org/dl_files/30_3_migration_reference.xlsx
```

### 1.3 Download ESCO

ESCO requires a (free) login for the bulk download.
1. Go to `https://esco.ec.europa.eu/en/use-esco/download`
2. Select **ESCO v1.2.1**, language **English**, format **CSV** (also grab **Turtle/RDF** if you want to explore it in Protégé later).
3. Unzip into `data/raw/esco/`.

The three files you actually need: `occupations_en.csv`, `skills_en.csv`, `occupationSkillRelations_en.csv`.

> Faster alternative for a 5-day sprint: skip the bulk download and hit the API per occupation.
> `https://ec.europa.eu/esco/api/search?text=software%20developer&language=en&type=occupation`
> then `https://ec.europa.eu/esco/api/resource/occupation?uri=<conceptUri>&language=en`
> The occupation payload includes `hasEssentialSkill` and `hasOptionalSkill` arrays directly. For 5 occupations this is minutes of work vs. wrangling a 19-file CSV package.

### 1.4 Download the crosswalks

- **SOC 2010 ↔ ISCO-08:** `https://www.bls.gov/soc/` → Crosswalks → `isco_soc_crosswalk.xls`
- **SOC 2010 ↔ SOC 2018:** same page (you need this bridge — your codes are 2018, the ISCO crosswalk is 2010)
- **O\*NET crosswalks index:** `https://www.onetcenter.org/crosswalks.html`

### 1.5 Sanity check — print the columns

Column names changed in 30.3. **Never assume; always print first.**

```python
# scripts/00_inspect.py
import pandas as pd, glob, os
for f in sorted(glob.glob("data/raw/*.csv")):
    try:
        df = pd.read_csv(f, nrows=3)
        print(f"\n=== {os.path.basename(f)} ({len(pd.read_csv(f)):,} rows)")
        print(list(df.columns))
    except Exception as e:
        print(f"\n=== {os.path.basename(f)} — ERROR: {e}")
```

```bash
cd ~/onet-ontology && python scripts/00_inspect.py > docs/column_inventory.txt && cat docs/column_inventory.txt
```

**Day 1 done when:** `column_inventory.txt` exists and you've eyeballed the actual column names for `tasks_to_dwas`, `gwas_to_iwas_to_dwas`, and `essential_skills_to_work_activities`. Those three drive everything.

---

## Day 2 — Extract the five-occupation slice (~4 hours)

### 2.1 Filter everything to your five occupations

```python
# scripts/01_extract_slice.py
import pandas as pd, pathlib

RAW = pathlib.Path("data/raw"); OUT = pathlib.Path("data/interim"); OUT.mkdir(exist_ok=True, parents=True)

SOC = {
    "15-1252.00": "Software Developers",
    "15-2051.00": "Data Scientists",
    "15-1254.00": "Web Developers",
    "15-1242.00": "Database Administrators",
    "15-1212.00": "Information Security Analysts",
}

def occ_col(df):
    """30.3 column naming varies; find the O*NET-SOC code column."""
    for c in df.columns:
        if "SOC" in c.upper() and "CODE" in c.upper():
            return c
    raise KeyError(f"no SOC column in {list(df.columns)}")

FILES = ["occupation_data", "task_statements", "task_ratings", "essential_skills",
         "transferable_skills", "knowledge", "abilities", "software_skills",
         "work_activities", "job_zones", "sample_of_reported_titles", "related_occupations"]

for name in FILES:
    p = RAW / f"{name}.csv"
    if not p.exists():
        print(f"SKIP {name} (not downloaded)"); continue
    df = pd.read_csv(p, dtype=str)
    try:
        col = occ_col(df)
    except KeyError:
        print(f"SKIP {name} (no SOC column — reference file)"); continue
    sub = df[df[col].isin(SOC)]
    sub.to_csv(OUT / f"{name}_slice.csv", index=False)
    print(f"{name}: {len(sub):,} rows")
```

```bash
python scripts/01_extract_slice.py
```

### 2.2 Build the task→DWA→GWA→skill chain

This is the heart of the build. Adjust column names to match your `column_inventory.txt`.

```python
# scripts/02_task_skill_chain.py
import pandas as pd, pathlib

RAW = pathlib.Path("data/raw"); INT = pathlib.Path("data/interim")
OUT = pathlib.Path("data/processed"); OUT.mkdir(exist_ok=True, parents=True)

tasks   = pd.read_csv(INT/"task_statements_slice.csv", dtype=str)
t2dwa   = pd.read_csv(RAW/"tasks_to_dwas.csv", dtype=str)
dwa_ref = pd.read_csv(RAW/"gwas_to_iwas_to_dwas.csv", dtype=str)
es2wa   = pd.read_csv(RAW/"essential_skills_to_work_activities.csv", dtype=str)
ts2wa   = pd.read_csv(RAW/"transferable_skills_to_work_activities.csv", dtype=str)
cmr     = pd.read_csv(RAW/"content_model_reference.csv", dtype=str)

print("tasks_to_dwas:", list(t2dwa.columns))
print("gwas_to_iwas_to_dwas:", list(dwa_ref.columns))
print("essential_skills_to_work_activities:", list(es2wa.columns))

# --- CHAIN (rename to match your actual columns) ---
# Step 1: Task -> DWA
chain = tasks.merge(t2dwa, on="Task ID", how="left")
# Step 2: DWA -> IWA -> GWA
chain = chain.merge(dwa_ref, on="DWA ID", how="left")
# Step 3: GWA (Work Activity element) -> Skill element
skill_links = pd.concat([
    es2wa.assign(skill_kind="essential"),
    ts2wa.assign(skill_kind="transferable"),
])
# NOTE: verify the join key — likely the GWA/Work Activity Element ID column
chain = chain.merge(skill_links, left_on="Element ID", right_on="Work Activity Element ID", how="left")

# Attach human-readable names
names = cmr[["Element ID", "Element Name"]].rename(
    columns={"Element ID": "Skill Element ID", "Element Name": "Skill Name"})
chain = chain.merge(names, on="Skill Element ID", how="left")

chain.to_csv(OUT/"task_skill_derived.csv", index=False)
print(f"\nDerived {len(chain):,} task→skill candidate edges")
print(chain[["O*NET-SOC Code","Task","Skill Name","skill_kind"]].head(20).to_string())
```

**Weight the edges with occupation-specific importance.** The chain gives you *structure* (which skills a task type implies); O\*NET's per-occupation ratings give you *strength*. Join `essential_skills_slice.csv` (Importance/Level per occupation×skill) onto the derived edges. An edge that is both structurally derived *and* rated high-importance for that occupation is high confidence; structurally derived but low-importance is low confidence. **That confidence score is your provenance value and your thesis's quantitative backbone.**

### 2.3 Verify the five crosswalk mappings by hand

Do not automate this. Open `isco_soc_crosswalk.xls` and the ESCO API, and fill this table in `docs/crosswalk.md`:

| O\*NET-SOC (2018) | SOC 2010 | ISCO-08 | ESCO conceptUri | Cardinality | Confidence | Notes |
|---|---|---|---|---|---|---|
| 15-1252.00 Software Developers | 15-1132 + 15-1133 | 2512 | *(verify)* | many→1 | | 2018 merged two 2010 codes |
| 15-1254.00 Web Developers | 15-1134 | 2513 | *(verify)* | ~1:1 | | ISCO 2513 broader (multimedia) |
| 15-1242.00 Database Administrators | 15-1141 | 2521 | *(verify)* | 1→many | | 2018 split DBA vs Database Architects |
| 15-1212.00 Information Security Analysts | 15-1122 | 2529 or 2523 | *(verify)* | ambiguous | | ICT security specialist vs technician |
| 15-2051.00 Data Scientists | *none (new in 2018)* | 2511? 2120? | *(verify)* | **weak** | **low** | No clean ISCO home |

🛑 **YOUR CALL #1 — how to handle the Data Scientists mapping.** There is no defensible ISCO-08 home for it. Options: (a) map to ESCO "data scientist" (which ESCO files under ISCO 2511) and record low confidence; (b) leave it unmapped and populate its skills from O\*NET only; (c) drop it from the slice and use 4 occupations. **My recommendation: (a).** It's honest, it exercises your confidence/provenance machinery on a real edge case, and "the crosswalk breaks on the newest occupation" is a *finding*, not a failure — it's evidence for your thesis that static taxonomies lag emerging work.

**Day 2 done when:** `data/processed/task_skill_derived.csv` exists with plausible edges, and `docs/crosswalk.md` is filled in by hand with confidence values.

---

## Day 3 — Author the schema in Protégé (~4 hours)

Build this by hand. It's small, you must be able to defend every axiom, and the reasoner feedback loop is why Protégé exists.

### 3.1 Classes

Create as subclasses of `owl:Thing`:
`Occupation`, `Task`, `Skill`, `Knowledge`, `Ability`, `WorkActivity`, `Software`, `Tool`, `Credential`, `IssuingBody`, `SourceRecord`

Sub-classes: under `Skill` → `EssentialSkill`, `TransferableSkill`. Under `WorkActivity` → `GWA`, `IWA`, `DWA`.

Declare `Occupation`, `Task`, `Skill`, `Software`, `Tool` **pairwise disjoint** (Protégé: select them → "Disjoint With"). This makes your domain axioms actually catch errors later.

### 3.2 Object properties

| Property | Domain | Range | Notes |
|---|---|---|---|
| `performsTask` | `Occupation` | `Task` | safe to constrain |
| `requiresSkill` | *(blank)* | `Skill` | multi-level — leave domain blank |
| `requiresEssentialSkill` | *(blank)* | `Skill` | **sub-property of `requiresSkill`** |
| `requiresOptionalSkill` | *(blank)* | `Skill` | **sub-property of `requiresSkill`** |
| `requiresKnowledge` | *(blank)* | `Knowledge` | |
| `requiresAbility` | `Occupation` | `Ability` | |
| `usesSoftware` | *(blank)* | `Software` | |
| `usesTool` | *(blank)* | `Tool` | |
| `realizesActivity` | `Task` | `DWA` | the O\*NET chain |
| `narrowerActivity` | `WorkActivity` | `WorkActivity` | GWA→IWA→DWA |
| `requiresCredential` | `Occupation` | `Credential` | |
| `issuedBy` | `Credential` | `IssuingBody` | |
| `mapsToESCO` / `mapsToISCO` | `Occupation` | *(blank)* | crosswalk edges |

**The property chain** (this is your C2/C3 mechanism): select `requiresSkill` → **SubProperty Of (Chain)** → `performsTask o requiresSkill`.

### 3.3 Datatype properties (provenance — do not skip)

`dataSource` (string), `sourceVersion` (string), `lastUpdated` (dateTime), `confidence` (float), `importanceScore` (float), `levelScore` (float), `socCode` (string), `escoUri` (string), `taskType` (string, Core/Supplemental), `isHotTechnology` (boolean), `isInDemand` (boolean)

### 3.4 One defined class (free inference win)

Create `RegulatedOccupation`, set it **Equivalent To**: `Occupation and (requiresCredential some Credential)`. Run HermiT. Nothing will classify yet in the Tech slice — which is itself the correct answer, and it'll light up when you add Healthcare. Cheap demo of DL inference for your advisor.

Save as `ontology/schema.ttl` (Turtle). Commit.

🛑 **YOUR CALL #2 — reconciling O\*NET "Essential/Transferable" with ESCO "essential/optional".** These are *different distinctions*. O\*NET's is about skill *type* (foundational vs portable); ESCO's is about *necessity* for the occupation. Options: (a) keep both as separate properties (`onetSkillCategory` datatype property + ESCO-derived `requiresEssentialSkill`/`requiresOptionalSkill`); (b) collapse them and lose information; (c) use only one source. **My recommendation: (a).** Two distinct facts, modeled distinctly, each with its own provenance. Conflating them would be the kind of silent semantic error a committee will find.

---

## Day 4 — Populate with a script (~5 hours)

```python
# scripts/03_populate.py
from owlready2 import *
import pandas as pd, pathlib, datetime, re

onto = get_ontology("file://ontology/schema.ttl").load()
NOW = datetime.datetime.now().isoformat()

def safe(s):
    """O*NET strings -> valid OWL identifiers."""
    return re.sub(r'[^A-Za-z0-9_]', '_', str(s))[:80]

INT = pathlib.Path("data/interim"); PROC = pathlib.Path("data/processed")
occ_df   = pd.read_csv(INT/"occupation_data_slice.csv", dtype=str)
task_df  = pd.read_csv(INT/"task_statements_slice.csv", dtype=str)
soft_df  = pd.read_csv(INT/"software_skills_slice.csv", dtype=str)
skill_df = pd.read_csv(INT/"essential_skills_slice.csv", dtype=str)
chain_df = pd.read_csv(PROC/"task_skill_derived.csv", dtype=str)

with onto:
    occ_idx, task_idx, skill_idx = {}, {}, {}

    # Occupations
    for _, r in occ_df.iterrows():
        code = r["O*NET-SOC Code"]
        ind = onto.Occupation(safe(r["Title"]))
        ind.socCode = [code]
        ind.dataSource = ["O*NET 30.3"]; ind.lastUpdated = [NOW]; ind.confidence = [1.0]
        occ_idx[code] = ind

    # Tasks + performsTask
    for _, r in task_df.iterrows():
        t = onto.Task(f"Task_{safe(r['Task ID'])}")
        t.taskType = [r.get("Task Type", "")]
        t.dataSource = ["O*NET 30.3"]; t.lastUpdated = [NOW]; t.confidence = [1.0]
        task_idx[r["Task ID"]] = t
        occ_idx[r["O*NET-SOC Code"]].performsTask.append(t)

    # Software (occupation-level), with hot/in-demand flags
    for _, r in soft_df.iterrows():
        s = onto.Software(safe(r.get("Workplace Example") or r.get("Element Name")))
        s.dataSource = ["O*NET 30.3"]; s.lastUpdated = [NOW]
        occ_idx[r["O*NET-SOC Code"]].usesSoftware.append(s)

    # ⭐ Derived task→skill edges with confidence
    for _, r in chain_df.dropna(subset=["Skill Name"]).iterrows():
        t = task_idx.get(r["Task ID"])
        if t is None: continue
        nm = safe(r["Skill Name"])
        sk = skill_idx.setdefault(nm, onto.Skill(nm))
        sk.dataSource = ["O*NET 30.3 derived: Task→DWA→GWA→Skill"]
        sk.lastUpdated = [NOW]
        t.requiresSkill.append(sk)

onto.save(file="ontology/populated.owl", format="rdfxml")
print("Saved ontology/populated.owl")

# Run the reasoner
with onto:
    try:
        sync_reasoner(infer_property_values=True)
        print("✓ Reasoner: consistent")
    except OwlReadyInconsistentOntologyError:
        print("✗ INCONSISTENT — open in Protégé and run HermiT to find the clash")
```

```bash
python scripts/03_populate.py
```

Then open `ontology/populated.owl` in Protégé, **Reasoner ▸ Start reasoner**, select an occupation individual, and confirm skills appear as **inferred** (yellow) via the property chain — not asserted. **That yellow highlight is your demo.**

🛑 **YOUR CALL #3 — how much to trust the derived edges.** The `essential_skills_to_work_activities` file is only ~110 rows, meaning it links skill *elements* to work-activity *elements* generically, not per-occupation. So the derived edges are structurally sound but coarse. Options: (a) accept all derived edges, weighted by that occupation's skill importance rating; (b) threshold — keep only edges where the occupation's importance rating for that skill exceeds some cutoff; (c) hand-review a sample and report precision. **My recommendation: (a) + (c).** Populate everything with confidence = the occupation's normalized importance score, then hand-review ~30 edges to report an accuracy figure. That gives you a quantitative validation result in a day, which is exactly what a committee wants.

---

## Day 5 — Validate and prepare the demo (~4 hours)

### 5.1 Run each Core competency question as a query

```python
# scripts/04_validate_cqs.py
from owlready2 import *
onto = get_ontology("file://ontology/populated.owl").load()
sync_reasoner()

print("A1 — occupations requiring a given skill:")
# adapt the skill name to one that exists in your data
for o in onto.Occupation.instances():
    skills = [s.name for s in o.requiresSkill]
    print(f"  {o.name}: {len(skills)} skills")

print("\nB1 — pairwise essential-skill overlap (transition targets):")
occs = list(onto.Occupation.instances())
for i, a in enumerate(occs):
    for b in occs[i+1:]:
        sa, sb = set(a.requiresSkill), set(b.requiresSkill)
        if sa and sb:
            j = len(sa & sb) / len(sa | sb)
            print(f"  {a.name} ↔ {b.name}: Jaccard {j:.2f} ({len(sa & sb)} shared)")

print("\nC2 — which skills come from which task (sample):")
for t in list(onto.Task.instances())[:5]:
    print(f"  {t.name}: {[s.name for s in t.requiresSkill]}")
```

Record pass/fail for **A1, A2, A3, B1, B2, C1, C2, C3, E3** in `docs/cq_results.md`. Whatever fails tells you precisely what to build next — that's the deliverable, not a problem.

### 5.2 The C3 demo (the money shot)

In Protégé: pick an occupation, note its inferred skill count. Delete one `performsTask` assertion. **Reasoner ▸ Synchronize reasoner.** Watch the skill profile shrink automatically. Re-add it; watch it return. **That thirty-second demo is your entire thesis argument made visible** — one task edit repropagates with zero manual maintenance, which is exactly what O\*NET's release cycle cannot do.

### 5.3 What to bring to the meeting

1. `docs/cq_results.md` — which of the nine Core CQs pass
2. The live Protégé C3 demo
3. `docs/crosswalk.md` — the five hand-verified mappings with confidence
4. The B1 Jaccard table — computed transition targets vs. O\*NET's own `related_occupations.csv` (**a free validation**: does your skill-derived similarity match O\*NET's editorially-curated related occupations? Agreement is a validation result; divergence is an interesting finding either way)
5. The two O\*NET 30.3 findings above — Tools Used frozen, and the new skill↔activity linkages

---

## Where you're on your own after this

Everything above is mechanical. These are genuinely yours:

- **The three 🛑 calls** — mapping confidence for Data Scientists, O\*NET-vs-ESCO essential semantics, and derived-edge trust thresholds.
- **The attribution method write-up.** Document *how* you derived task→skill (the chain, the weighting, the thresholds) as you go. This is your methods chapter and your actual contribution — the code is just its implementation.
- **Whether ESCO enters the baseline at all in v1.** Given the 30.3 skill↔activity linkages, you can build a complete, coherent slice from O\*NET alone. Adding ESCO buys you essential/optional semantics and synonyms but costs you the lossy crosswalk. **Consider deferring ESCO to v2** and presenting the O\*NET-only slice as v1 — cleaner, faster, one vocabulary, and it lets you *demonstrate* the crosswalk problem rather than being blocked by it.
- **The data contract with Tianwei** (intermediate format, SOC anchoring, confidence thresholds, baseline/update-layer separation).

## If you fall behind

Cut in this order: drop to **3 occupations** (Software Developers, Data Scientists, Information Security Analysts — maximum skill contrast); **drop ESCO entirely** for v1; drop the Tools/30.2 pull; drop credentials. **Never cut:** the property chain, the provenance fields, and the C3 demo. Those three *are* the thesis.
