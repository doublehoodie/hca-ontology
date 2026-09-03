"""Derive task→DWA→GWA→skill edges from O*NET 30.3 source tables only.

Join keys verified against docs/column_inventory.txt (Task 3).
Missing hops stay null and are reported — never imputed.
"""
from __future__ import annotations

import pathlib

import pandas as pd

RAW = pathlib.Path("data/raw")
INT = pathlib.Path("data/interim")
OUT = pathlib.Path("data/processed")
DOCS = pathlib.Path("docs")
OUT.mkdir(exist_ok=True, parents=True)
DOCS.mkdir(exist_ok=True, parents=True)

DERIVATION = "Task→DWA→IWA→GWA→Skill via O*NET linkage files (left joins; nulls preserved)"
SOURCE_VERSION = "O*NET 30.3"
DATA_SOURCE = "O*NET"


def require_cols(df: pd.DataFrame, cols: list[str], name: str) -> None:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise KeyError(
            f"{name}: expected columns {missing} absent. "
            f"Actual columns: {list(df.columns)}. "
            "Do not substitute lookalike columns — halt and re-check inventory."
        )


def main() -> None:
    tasks = pd.read_csv(INT / "task_statements_slice.csv", dtype=str)
    t2dwa = pd.read_csv(RAW / "tasks_to_dwas.csv", dtype=str)
    dwa_ref = pd.read_csv(RAW / "gwas_to_iwas_to_dwas.csv", dtype=str)
    es2wa = pd.read_csv(RAW / "essential_skills_to_work_activities.csv", dtype=str)
    ts2wa = pd.read_csv(RAW / "transferable_skills_to_work_activities.csv", dtype=str)
    ess_ratings = pd.read_csv(INT / "essential_skills_slice.csv", dtype=str)
    tra_ratings = pd.read_csv(INT / "transferable_skills_slice.csv", dtype=str)

    require_cols(tasks, ["O*NET-SOC Code", "Task ID", "Task"], "task_statements_slice")
    require_cols(t2dwa, ["Task ID", "DWA Element ID"], "tasks_to_dwas")
    require_cols(
        dwa_ref,
        ["DWA Element ID", "IWA Element ID", "GWA Element ID"],
        "gwas_to_iwas_to_dwas",
    )
    require_cols(
        es2wa,
        ["Essential Skills Element ID", "Work Activities Element ID"],
        "essential_skills_to_work_activities",
    )
    require_cols(
        ts2wa,
        ["Transferable Skills Element ID", "Work Activities Element ID"],
        "transferable_skills_to_work_activities",
    )
    require_cols(ess_ratings, ["O*NET-SOC Code", "Element ID", "Scale ID", "Data Value"], "essential_skills_slice")
    require_cols(tra_ratings, ["O*NET-SOC Code", "Element ID", "Scale ID", "Data Value"], "transferable_skills_slice")

    print("tasks_to_dwas:", list(t2dwa.columns))
    print("gwas_to_iwas_to_dwas:", list(dwa_ref.columns))
    print("essential_skills_to_work_activities:", list(es2wa.columns))
    print("transferable_skills_to_work_activities:", list(ts2wa.columns))

    # Keep task slice columns; join only DWA ids/names from t2dwa (avoid Date/Domain Source clash)
    t2dwa_slim = t2dwa[
        ["Task ID", "DWA Element ID", "DWA Element Name"]
    ].drop_duplicates()

    # Step 1: Task -> DWA
    chain = tasks.merge(t2dwa_slim, on="Task ID", how="left")

    # Step 2: DWA -> IWA -> GWA
    dwa_ref_slim = dwa_ref[
        [
            "DWA Element ID",
            "DWA Element Name",
            "IWA Element ID",
            "IWA Element Name",
            "GWA Element ID",
            "GWA Element Name",
        ]
    ].drop_duplicates(subset=["DWA Element ID"])
    # Prefer hierarchy names when present; keep task-link DWA name if hierarchy missing
    chain = chain.merge(
        dwa_ref_slim,
        on="DWA Element ID",
        how="left",
        suffixes=("_from_task_link", ""),
    )
    if "DWA Element Name_from_task_link" in chain.columns:
        chain["DWA Element Name"] = chain["DWA Element Name"].fillna(
            chain["DWA Element Name_from_task_link"]
        )
        chain = chain.drop(columns=["DWA Element Name_from_task_link"])

    # Step 3: GWA -> Skill element (essential + transferable), left joins then concat
    es_links = es2wa.rename(
        columns={
            "Essential Skills Element ID": "Skill Element ID",
            "Essential Skills Element Name": "Skill Name",
            "Work Activities Element ID": "GWA Element ID",
            "Work Activities Element Name": "GWA Element Name_from_skill_link",
        }
    ).assign(skill_kind="essential")

    ts_links = ts2wa.rename(
        columns={
            "Transferable Skills Element ID": "Skill Element ID",
            "Transferable Skills Element Name": "Skill Name",
            "Work Activities Element ID": "GWA Element ID",
            "Work Activities Element Name": "GWA Element Name_from_skill_link",
        }
    ).assign(skill_kind="transferable")

    skill_links = pd.concat([es_links, ts_links], ignore_index=True)
    skill_links = skill_links[
        ["GWA Element ID", "Skill Element ID", "Skill Name", "skill_kind", "GWA Element Name_from_skill_link"]
    ].drop_duplicates()

    # Rows with null GWA still kept (left); skill cols null
    chain = chain.merge(skill_links, on="GWA Element ID", how="left")
    if "GWA Element Name_from_skill_link" in chain.columns:
        chain["GWA Element Name"] = chain["GWA Element Name"].fillna(
            chain["GWA Element Name_from_skill_link"]
        )
        chain = chain.drop(columns=["GWA Element Name_from_skill_link"])

    # Step 4: attach occupation-specific ratings (Importance / Level) when present
    def pivot_ratings(ratings: pd.DataFrame, kind: str) -> pd.DataFrame:
        # Keep Importance and Level as separate columns; null if absent
        keep = ratings[
            ["O*NET-SOC Code", "Element ID", "Element Name", "Scale ID", "Scale Name", "Data Value"]
        ].copy()
        keep = keep.rename(columns={"Element ID": "Skill Element ID"})
        imp = keep[keep["Scale ID"] == "IM"][
            ["O*NET-SOC Code", "Skill Element ID", "Element Name", "Data Value"]
        ].rename(
            columns={
                "Data Value": "importance_data_value",
                "Element Name": "Skill Name_from_rating",
            }
        )
        lvl = keep[keep["Scale ID"] == "LV"][
            ["O*NET-SOC Code", "Skill Element ID", "Data Value"]
        ].rename(columns={"Data Value": "level_data_value"})
        out = imp.merge(lvl, on=["O*NET-SOC Code", "Skill Element ID"], how="outer")
        out["rating_skill_kind"] = kind
        return out

    ess_piv = pivot_ratings(ess_ratings, "essential")
    tra_piv = pivot_ratings(tra_ratings, "transferable")
    ratings = pd.concat([ess_piv, tra_piv], ignore_index=True)

    chain = chain.merge(
        ratings,
        left_on=["O*NET-SOC Code", "Skill Element ID", "skill_kind"],
        right_on=["O*NET-SOC Code", "Skill Element ID", "rating_skill_kind"],
        how="left",
    )
    if "Skill Name_from_rating" in chain.columns:
        chain["Skill Name"] = chain["Skill Name"].fillna(chain["Skill Name_from_rating"])
        chain = chain.drop(columns=["Skill Name_from_rating"])
    chain = chain.drop(columns=["rating_skill_kind"], errors="ignore")

    # Provenance
    chain["data_source"] = DATA_SOURCE
    chain["source_version"] = SOURCE_VERSION
    chain["derivation"] = DERIVATION

    # Stable column order (ids first, then provenance/ratings)
    preferred = [
        "O*NET-SOC Code",
        "Title",
        "Task ID",
        "Task",
        "Task Type",
        "DWA Element ID",
        "DWA Element Name",
        "IWA Element ID",
        "IWA Element Name",
        "GWA Element ID",
        "GWA Element Name",
        "Skill Element ID",
        "Skill Name",
        "skill_kind",
        "importance_data_value",
        "level_data_value",
        "data_source",
        "source_version",
        "derivation",
        "Date",
        "Domain Source",
        "Incumbents Responding",
    ]
    cols = [c for c in preferred if c in chain.columns] + [
        c for c in chain.columns if c not in preferred
    ]
    chain = chain[cols]

    out_path = OUT / "task_skill_derived.csv"
    chain.to_csv(out_path, index=False)
    print(f"\nDerived {len(chain):,} task→skill candidate edges → {out_path}")
    sample_cols = [
        c
        for c in [
            "O*NET-SOC Code",
            "Task",
            "Skill Name",
            "skill_kind",
            "importance_data_value",
        ]
        if c in chain.columns
    ]
    print(chain[sample_cols].head(20).to_string())

    # Gap report
    n_tasks = tasks["Task ID"].nunique()
    tasks_with_dwa = chain.loc[chain["DWA Element ID"].notna(), "Task ID"].nunique()
    tasks_no_dwa = n_tasks - tasks_with_dwa

    # Among rows that have DWA
    has_dwa = chain["DWA Element ID"].notna()
    dwa_ids = chain.loc[has_dwa, "DWA Element ID"].nunique()
    dwa_with_gwa = chain.loc[has_dwa & chain["GWA Element ID"].notna(), "DWA Element ID"].nunique()

    has_gwa = chain["GWA Element ID"].notna()
    gwa_ids = chain.loc[has_gwa, "GWA Element ID"].nunique()
    gwa_with_skill = chain.loc[has_gwa & chain["Skill Element ID"].notna(), "GWA Element ID"].nunique()

    structural = chain["Skill Element ID"].notna()
    n_structural = int(structural.sum())
    n_with_importance = int((structural & chain["importance_data_value"].notna()).sum())
    n_no_importance = n_structural - n_with_importance

    # Per-occupation rating coverage note
    occ_counts = (
        tasks.groupby("O*NET-SOC Code")["Task ID"]
        .nunique()
        .rename("n_tasks")
        .to_frame()
    )
    for code in occ_counts.index:
        sub = chain[chain["O*NET-SOC Code"] == code]
        occ_counts.loc[code, "n_edges"] = len(sub)
        occ_counts.loc[code, "n_structural_skill_edges"] = int(sub["Skill Element ID"].notna().sum())
        occ_counts.loc[code, "n_with_importance"] = int(
            (sub["Skill Element ID"].notna() & sub["importance_data_value"].notna()).sum()
        )

    occ_lines = [
        "| O*NET-SOC Code | n_tasks | n_edges | n_structural_skill_edges | n_with_importance |",
        "|---|---:|---:|---:|---:|",
    ]
    for idx, r in occ_counts.iterrows():
        occ_lines.append(
            f"| {idx} | {int(r.n_tasks)} | {int(r.n_edges)} | "
            f"{int(r.n_structural_skill_edges)} | {int(r.n_with_importance)} |"
        )
    occ_table = "\n".join(occ_lines)

    gap_md = f"""# Task→Skill chain gap report

Generated by `scripts/02_task_skill_chain.py`.
Source: {SOURCE_VERSION}. Derivation: `{DERIVATION}`.
**No imputation** — missing hops are null.

## Hop coverage

| Metric | Count | Notes |
|---|---:|---|
| Distinct tasks in slice | {n_tasks} | from `task_statements_slice.csv` |
| Tasks with ≥1 DWA | {tasks_with_dwa} | via `tasks_to_dwas` on `Task ID` |
| Tasks with no DWA | {tasks_no_dwa} | null `DWA Element ID` |
| Distinct DWAs among linked tasks | {dwa_ids} | |
| Distinct DWAs with GWA | {dwa_with_gwa} | via `gwas_to_iwas_to_dwas` on `DWA Element ID` |
| Distinct GWAs among linked rows | {gwa_ids} | |
| Distinct GWAs with ≥1 skill link | {gwa_with_skill} | via essential/transferable `*_to_work_activities` on `GWA Element ID` = `Work Activities Element ID` |
| Structural skill edges (non-null Skill Element ID) | {n_structural} | |
| Structural edges with occupation Importance rating | {n_with_importance} | join on `O*NET-SOC Code` + `Skill Element ID` + `skill_kind` |
| Structural edges missing Importance | {n_no_importance} | left null — not imputed |

## Per-occupation summary

{occ_table}

## Known slice gap (Task 4)

`15-2051.00` Data Scientists has task statements and software rows but **zero rows** in
`essential_skills`, `transferable_skills`, `knowledge`, `abilities`, `work_activities`,
and `task_ratings` slices. Structural Task→DWA→GWA→Skill edges may still exist from
generic linkage tables; occupation-specific importance/level will be null for this SOC.

## Join keys used

1. `Task ID` — `task_statements_slice` ⋉ `tasks_to_dwas`
2. `DWA Element ID` — result ⋉ `gwas_to_iwas_to_dwas`
3. `GWA Element ID` = `Work Activities Element ID` — result ⋉ essential/transferable skill↔WA files
4. `O*NET-SOC Code` + `Skill Element ID` (+ `skill_kind`) — result ⋉ skill rating slices
"""
    gap_path = DOCS / "task_skill_gaps.md"
    gap_path.write_text(gap_md)
    print(f"\nWrote {gap_path}")


if __name__ == "__main__":
    main()
