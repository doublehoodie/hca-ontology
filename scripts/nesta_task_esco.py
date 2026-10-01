"""Run Nesta SkillsExtractor (ESCO taxonomy) on the five-occupation task slice.

Two-step API only (extract_skills does not map):
  sm = SkillsExtractor(taxonomy_name="esco")
  docs = sm.extract_skills(list_of_texts)
  mapped = sm.map_skills(docs)

No filtering, thresholding, LLM correction, or imputation of mappings.
Tasks with zero mapped skills emit one row with null skill fields.
"""
from __future__ import annotations

import pathlib
import sys

import pandas as pd
from ojd_daps_skills.extract_skills.extract_skills import SkillsExtractor

ROOT = pathlib.Path(__file__).resolve().parents[1]
TASKS = ROOT / "data" / "interim" / "task_statements_slice.csv"
OUT = ROOT / "data" / "processed" / "nesta_task_esco.csv"

ESCO_SKILL_PREFIX = "http://data.europa.eu/esco/skill/"

OUT_COLS = [
    "task_id",
    "soc_code",
    "task_text",
    "ojo_skill",
    "match_skill",
    "match_score",
    "match_type",
    "match_id",
    "esco_uri",
    "esco_group_code",
]


def main() -> int:
    tasks = pd.read_csv(TASKS, dtype=str)
    required = ["O*NET-SOC Code", "Task ID", "Task"]
    missing = [c for c in required if c not in tasks.columns]
    if missing:
        raise KeyError(f"{TASKS}: missing columns {missing}; actual={list(tasks.columns)}")

    texts = tasks["Task"].fillna("").astype(str).tolist()
    print(f"Loaded {len(tasks)} tasks from {TASKS}")

    sm = SkillsExtractor(taxonomy_name="esco")
    print("extract_skills ...")
    docs = sm.extract_skills(texts)
    print("map_skills ...")
    mapped = sm.map_skills(docs)

    if len(mapped) != len(tasks):
        raise RuntimeError(
            f"Nesta returned {len(mapped)} docs for {len(tasks)} tasks — refusing to align"
        )

    rows: list[dict] = []
    for i, (_, task_row) in enumerate(tasks.iterrows()):
        doc = mapped[i]
        base = {
            "task_id": task_row["Task ID"],
            "soc_code": task_row["O*NET-SOC Code"],
            "task_text": task_row["Task"],
        }
        mapped_skills = list(getattr(doc._, "mapped_skills", None) or [])
        if not mapped_skills:
            rows.append(
                {
                    **base,
                    "ojo_skill": None,
                    "match_skill": None,
                    "match_score": None,
                    "match_type": None,
                    "match_id": None,
                    "esco_uri": None,
                    "esco_group_code": None,
                }
            )
            continue
        for m in mapped_skills:
            match_id = m.get("match_id")
            match_type = m.get("match_type")
            esco_uri = None
            esco_group_code = None
            mid = None if match_id is None else str(match_id).strip()
            if mid == "":
                mid = None
            # Skill-level hits get a concept URI; group/hierarchy codes do not.
            if match_type == "skill" and mid is not None:
                esco_uri = ESCO_SKILL_PREFIX + mid
            elif mid is not None:
                esco_group_code = mid
            rows.append(
                {
                    **base,
                    "ojo_skill": m.get("ojo_skill"),
                    "match_skill": m.get("match_skill"),
                    "match_score": m.get("match_score"),
                    "match_type": match_type,
                    "match_id": match_id,
                    "esco_uri": esco_uri,
                    "esco_group_code": esco_group_code,
                }
            )

    out_df = pd.DataFrame(rows, columns=OUT_COLS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(OUT, index=False)
    print(f"Wrote {len(out_df)} rows → {OUT}")
    print(f"  tasks represented: {out_df['task_id'].nunique()}")
    print(f"  rows with match_id: {out_df['match_id'].notna().sum()}")
    print(f"  skill-level esco_uri: {(out_df['esco_uri'].notna()).sum()}")
    print(f"  group-level esco_group_code: {(out_df['esco_group_code'].notna()).sum()}")
    print(f"  null-skill placeholder rows: {out_df['match_id'].isna().sum()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
