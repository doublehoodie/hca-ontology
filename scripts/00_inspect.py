"""Inventory columns and row counts for files under data/raw/."""
from __future__ import annotations

import csv
import glob
import os
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

# ESCO conceptSchemes has very large fields
csv.field_size_limit(10_000_000)


def inspect_csv(path: Path) -> None:
    try:
        df = pd.read_csv(path, dtype=str, nrows=3, low_memory=False)
        n = len(pd.read_csv(path, dtype=str, low_memory=False))
        print(f"\n=== {path.relative_to(ROOT)} ({n:,} rows)")
        print(list(df.columns))
    except Exception as e:
        # Fallback for pathological CSVs
        try:
            with path.open(newline="", encoding="utf-8") as fh:
                reader = csv.reader(fh)
                header = next(reader)
                n = sum(1 for _ in reader)
            print(f"\n=== {path.relative_to(ROOT)} ({n:,} rows) [csv module]")
            print(header)
        except Exception as e2:
            print(f"\n=== {path.relative_to(ROOT)} — ERROR: {e} / fallback: {e2}")


def inspect_excel(path: Path) -> None:
    try:
        xl = pd.ExcelFile(path)
        print(f"\n=== {path.relative_to(ROOT)} [excel] sheets={xl.sheet_names}")
        for sheet in xl.sheet_names:
            # SOC crosswalk has title rows before the header
            df = pd.read_excel(path, sheet_name=sheet, header=None, dtype=str)
            print(f"  sheet '{sheet}': {len(df):,} raw rows, first non-empty rows:")
            shown = 0
            for i, row in df.iterrows():
                vals = [str(v) for v in row.tolist() if pd.notna(v) and str(v).strip()]
                if not vals:
                    continue
                print(f"    row {i}: {vals[:8]}")
                shown += 1
                if shown >= 6:
                    break
    except Exception as e:
        print(f"\n=== {path.relative_to(ROOT)} — ERROR: {e}")


def inspect_txt(path: Path) -> None:
    try:
        # Tools Used.txt is tab-separated
        df = pd.read_csv(path, sep="\t", dtype=str, nrows=3)
        n = len(pd.read_csv(path, sep="\t", dtype=str))
        print(f"\n=== {path.relative_to(ROOT)} ({n:,} rows) [tsv]")
        print(list(df.columns))
    except Exception as e:
        print(f"\n=== {path.relative_to(ROOT)} — ERROR: {e}")


def main() -> None:
    print(f"RAW = {RAW}")
    csv_paths = sorted(RAW.glob("*.csv")) + sorted((RAW / "esco").glob("*.csv"))
    for p in csv_paths:
        inspect_csv(p)
    for p in sorted(RAW.glob("*.xlsx")) + sorted(RAW.glob("*.xls")):
        inspect_excel(p)
    for p in sorted(RAW.glob("*.txt")):
        inspect_txt(p)

    # Explicit join-key checklist for Day 2
    print("\n" + "=" * 72)
    print("JOIN KEY CHECKLIST (must match exactly)")
    print("=" * 72)
    checks = {
        "tasks_to_dwas.csv": ["Task ID", "DWA Element ID", "O*NET-SOC Code"],
        "gwas_to_iwas_to_dwas.csv": ["DWA Element ID", "GWA Element ID", "IWA Element ID"],
        "essential_skills_to_work_activities.csv": [
            "Work Activities Element ID",
            "Essential Skills Element ID",
        ],
        "transferable_skills_to_work_activities.csv": [
            "Work Activities Element ID",
            "Transferable Skills Element ID",
        ],
        "task_statements.csv": ["Task ID", "O*NET-SOC Code"],
        "essential_skills.csv": ["O*NET-SOC Code", "Element ID"],
        "transferable_skills.csv": ["O*NET-SOC Code", "Element ID"],
    }
    for name, required in checks.items():
        path = RAW / name
        cols = list(pd.read_csv(path, dtype=str, nrows=0).columns)
        missing = [c for c in required if c not in cols]
        status = "OK" if not missing else f"MISSING {missing}"
        print(f"{name}: {status}")
        if missing:
            print(f"  actual columns: {cols}")


if __name__ == "__main__":
    main()
