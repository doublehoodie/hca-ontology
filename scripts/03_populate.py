"""Populate ontology/populated.owl from the five-occupation O*NET slice.

Call #2 (a): O*NET essential/transferable → onetSkillCategory + EssentialSkill/
TransferableSkill classes. ESCO requiresEssentialSkill/requiresOptionalSkill are
NOT filled from O*NET skill_kind.

Call #1 still open: no mapsToESCO / ESCO necessity edges.

Call #3 open: accept all structural derived edges. Occupation-specific Importance
lives in data/processed/task_skill_derived.csv — not copied onto shared skill
individuals (would collide across occupations). No imputation.

Demo named individuals from schema.ttl are removed before slice population.
"""
from __future__ import annotations

import datetime
import pathlib
import re
import sys

import pandas as pd
from owlready2 import (
    OwlReadyInconsistentOntologyError,
    destroy_entity,
    get_ontology,
    sync_reasoner,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]
INT = ROOT / "data" / "interim"
PROC = ROOT / "data" / "processed"
SCHEMA_TTL = ROOT / "ontology" / "schema.ttl"
SCHEMA_OWL = ROOT / "ontology" / "schema.rdfxml.owl"  # owlready2-friendly conversion of schema.ttl
OUT = ROOT / "ontology" / "populated.owl"

SOURCE = "O*NET 30.3"
DERIV_SOURCE = "O*NET 30.3 derived: Task→DWA→IWA→GWA→Skill"
NOW = datetime.datetime.now().replace(microsecond=0).isoformat()

DEMO_INDIVIDUALS = {
    "AnalyzeData",
    "DataScientist",
    "Laptop",
    "Programming",
    "Python",
    "SoftwareDeveloper",
    "StatisticalAnalysis",
    "WriteCode",
}


def safe(s: object, maxlen: int = 80) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "_", str(s))[:maxlen]


def as_bool(v: object) -> bool | None:
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    s = str(v).strip().upper()
    if s in {"Y", "YES", "TRUE", "1"}:
        return True
    if s in {"N", "NO", "FALSE", "0"}:
        return False
    return None


def set_str(ind, prop: str, value: str) -> None:
    setattr(ind, prop, [value])


def set_float(ind, prop: str, value: float) -> None:
    setattr(ind, prop, [float(value)])


def set_bool(ind, prop: str, value: bool) -> None:
    setattr(ind, prop, [value])


def set_datetime(ind, prop: str, value: str) -> None:
    setattr(ind, prop, [datetime.datetime.fromisoformat(value)])


def load_schema():
    """Protégé Turtle is authoritative; owlready2 loads RDF/XML more reliably."""
    if not SCHEMA_TTL.exists():
        raise FileNotFoundError(f"Missing schema: {SCHEMA_TTL}")
    from rdflib import Graph

    g = Graph()
    g.parse(str(SCHEMA_TTL), format="turtle")
    g.serialize(str(SCHEMA_OWL), format="xml")
    return get_ontology(SCHEMA_OWL.as_uri()).load()


def cls(onto, name: str):
    """Resolve class by local name.

    Protégé export uses base IRI with a trailing double-slash
    (`.../ontologies//Class`), which does not bind to onto.ClassName.
    """
    for c in onto.classes():
        if c.name == name:
            return c
    raise KeyError(f"Class not found in schema: {name}")


def prop_set(ind, prop_name: str, values) -> None:
    """Set datatype/object values when the property entity exists on the individual."""
    # properties are accessed via ontology; use setattr with python attribute names
    setattr(ind, prop_name, values)


def main() -> int:
    occ_df = pd.read_csv(INT / "occupation_data_slice.csv", dtype=str)
    task_df = pd.read_csv(INT / "task_statements_slice.csv", dtype=str)
    soft_df = pd.read_csv(INT / "software_skills_slice.csv", dtype=str)
    chain_df = pd.read_csv(PROC / "task_skill_derived.csv", dtype=str)

    required = {
        "occupation_data_slice": (occ_df, ["O*NET-SOC Code", "Title"]),
        "task_statements_slice": (task_df, ["O*NET-SOC Code", "Task ID", "Task"]),
        "software_skills_slice": (
            soft_df,
            ["O*NET-SOC Code", "Workplace Example", "Element Name", "Hot Technology", "In Demand"],
        ),
        "task_skill_derived": (
            chain_df,
            [
                "O*NET-SOC Code",
                "Task ID",
                "Skill Name",
                "Skill Element ID",
                "skill_kind",
                "DWA Element ID",
                "DWA Element Name",
            ],
        ),
    }
    for name, (df, cols) in required.items():
        missing = [c for c in cols if c not in df.columns]
        if missing:
            raise KeyError(f"{name}: missing columns {missing}; actual={list(df.columns)}")

    onto = load_schema()

    with onto:
        for name in DEMO_INDIVIDUALS:
            ind = None
            for cand in onto.individuals():
                if cand.name == name:
                    ind = cand
                    break
            if ind is not None:
                destroy_entity(ind)

        occ_idx: dict[str, object] = {}
        task_idx: dict[str, object] = {}
        skill_idx: dict[str, object] = {}
        soft_idx: dict[str, object] = {}
        dwa_idx: dict[str, object] = {}

        for _, r in occ_df.iterrows():
            code = r["O*NET-SOC Code"]
            ind = cls(onto, "Occupation")(safe(r["Title"]))
            set_str(ind, "socCode", code)
            set_str(ind, "dataSource", SOURCE)
            set_str(ind, "sourceVersion", SOURCE)
            set_datetime(ind, "lastUpdated", NOW)
            set_float(ind, "confidence", 1.0)
            occ_idx[code] = ind

        for _, r in task_df.iterrows():
            tid = r["Task ID"]
            t = cls(onto, "Task")(f"Task_{safe(tid)}")
            tt = r.get("Task Type", "")
            if isinstance(tt, str) and tt.strip() and tt.lower() != "nan":
                set_str(t, "taskType", tt.strip())
            set_str(t, "dataSource", SOURCE)
            set_str(t, "sourceVersion", SOURCE)
            set_datetime(t, "lastUpdated", NOW)
            set_float(t, "confidence", 1.0)
            task_idx[tid] = t
            occ = occ_idx.get(r["O*NET-SOC Code"])
            if occ is not None:
                occ.performsTask.append(t)

        for _, r in soft_df.iterrows():
            label = r.get("Workplace Example") or r.get("Element Name")
            if label is None or str(label).strip() == "" or str(label).lower() == "nan":
                continue
            key = safe(label)
            s = soft_idx.get(key)
            if s is None:
                s = cls(onto, "Software")(key)
                set_str(s, "dataSource", SOURCE)
                set_str(s, "sourceVersion", SOURCE)
                set_datetime(s, "lastUpdated", NOW)
                hot = as_bool(r.get("Hot Technology"))
                if hot is not None:
                    set_bool(s, "isHotTechnology", hot)
                demand = as_bool(r.get("In Demand"))
                if demand is not None:
                    set_bool(s, "isInDemand", demand)
                soft_idx[key] = s
            occ = occ_idx.get(r["O*NET-SOC Code"])
            if occ is not None and s not in list(occ.usesSoftware):
                occ.usesSoftware.append(s)

        n_skill_links = 0
        n_dwa_links = 0
        n_structural_rows = 0

        for _, r in chain_df.iterrows():
            tid = r["Task ID"]
            t = task_idx.get(tid)
            if t is None:
                continue

            dwa_id = r.get("DWA Element ID")
            if isinstance(dwa_id, str) and dwa_id.strip() and dwa_id.lower() != "nan":
                dwa = dwa_idx.get(dwa_id)
                if dwa is None:
                    dwa = cls(onto, "DWA")(f"DWA_{safe(dwa_id)}")
                    set_str(dwa, "dataSource", SOURCE)
                    set_str(dwa, "sourceVersion", SOURCE)
                    set_datetime(dwa, "lastUpdated", NOW)
                    dwa_idx[dwa_id] = dwa
                if dwa not in list(t.realizesActivity):
                    t.realizesActivity.append(dwa)
                    n_dwa_links += 1

            sk_name = r.get("Skill Name")
            sk_eid = r.get("Skill Element ID")
            if sk_name is None or str(sk_name).strip() == "" or str(sk_name).lower() == "nan":
                continue
            if sk_eid is None or str(sk_eid).strip() == "" or str(sk_eid).lower() == "nan":
                continue

            n_structural_rows += 1
            kind = str(r.get("skill_kind", "")).strip().lower()
            # Stable key from O*NET element id + O*NET type (Call #2)
            sk_key = f"Skill_{safe(sk_eid)}_{safe(kind or 'unknown')}"
            sk = skill_idx.get(sk_key)
            if sk is None:
                if kind == "essential":
                    sk = cls(onto, "EssentialSkill")(sk_key)
                elif kind == "transferable":
                    sk = cls(onto, "TransferableSkill")(sk_key)
                else:
                    sk = cls(onto, "Skill")(sk_key)
                set_str(sk, "dataSource", DERIV_SOURCE)
                set_str(sk, "sourceVersion", SOURCE)
                set_datetime(sk, "lastUpdated", NOW)
                if kind in {"essential", "transferable"}:
                    set_str(sk, "onetSkillCategory", kind)
                skill_idx[sk_key] = sk

            # Assert on Task only — occupation skills inferred via property chain
            if sk not in list(t.requiresSkill):
                t.requiresSkill.append(sk)
                n_skill_links += 1

    # RDF/XML serialization breaks on Protégé's `.../ontologies//` IRIs (empty
    # path segment). Save Turtle, then emit RDF/XML via rdflib for Protégé.
    out_ttl = OUT.with_suffix(".ttl")
    onto.save(file=str(out_ttl), format="ntriples")
    from rdflib import Graph

    g = Graph()
    g.parse(str(out_ttl), format="nt")
    g.serialize(str(OUT), format="xml")
    print(f"Saved {OUT} (via ntriples → RDF/XML)")
    print(f"  also kept {out_ttl}")
    print(f"  occupations: {len(occ_idx)}")
    print(f"  tasks: {len(task_idx)}")
    print(f"  software: {len(soft_idx)}")
    print(f"  skills: {len(skill_idx)}")
    print(f"  DWAs: {len(dwa_idx)}")
    print(f"  unique task→skill assertions: {n_skill_links}")
    print(f"  structural chain rows consumed: {n_structural_rows}")
    print(f"  task→DWA realizesActivity assertions: {n_dwa_links}")
    print("  Call #2(a): onetSkillCategory set; ESCO requiresEssential/Optional unused")
    print("  Call #1 open: no mapsToESCO")

    with onto:
        try:
            sync_reasoner(infer_property_values=True)
            print("Reasoner: consistent")
            for code, occ in list(occ_idx.items())[:3]:
                skills = list(getattr(occ, "requiresSkill", []) or [])
                print(f"  {code} {occ.name}: inferred/asserted requiresSkill={len(skills)}")
        except OwlReadyInconsistentOntologyError:
            print("Reasoner: INCONSISTENT — inspect in Protégé / HermiT")
            return 2
        except Exception as e:
            print(f"Reasoner skipped/failed ({type(e).__name__}: {e})")
            print("  populated.owl written; run HermiT in Protégé for the yellow-inferred demo")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
