"""Filter O*NET occupation-keyed files to the five-occupation thin slice."""
from __future__ import annotations

import pathlib

import pandas as pd

RAW = pathlib.Path("data/raw")
OUT = pathlib.Path("data/interim")
OUT.mkdir(exist_ok=True, parents=True)

SOC = {
    "15-1252.00": "Software Developers",
    "15-2051.00": "Data Scientists",
    "15-1254.00": "Web Developers",
    "15-1242.00": "Database Administrators",
    "15-1212.00": "Information Security Analysts",
}

# Only accept the literal primary occupation code column from inventory.
PRIMARY_SOC_COL = "O*NET-SOC Code"

FILES = [
    "occupation_data",
    "task_statements",
    "task_ratings",
    "essential_skills",
    "transferable_skills",
    "knowledge",
    "abilities",
    "software_skills",
    "work_activities",
    "job_zones",
    "sample_of_reported_titles",
    "related_occupations",
]


def main() -> None:
    for name in FILES:
        p = RAW / f"{name}.csv"
        if not p.exists():
            print(f"SKIP {name} (not downloaded)")
            continue
        df = pd.read_csv(p, dtype=str)
        if PRIMARY_SOC_COL not in df.columns:
            print(f"SKIP {name} (no '{PRIMARY_SOC_COL}' — reference/other file)")
            print(f"  columns: {list(df.columns)}")
            continue
        sub = df[df[PRIMARY_SOC_COL].isin(SOC)].copy()
        out = OUT / f"{name}_slice.csv"
        sub.to_csv(out, index=False)
        counts = sub[PRIMARY_SOC_COL].value_counts().to_dict()
        print(f"{name}: {len(sub):,} rows")
        for code in SOC:
            print(f"  {code}: {counts.get(code, 0)}")


if __name__ == "__main__":
    main()
