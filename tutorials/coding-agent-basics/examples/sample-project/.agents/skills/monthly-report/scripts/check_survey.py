#!/usr/bin/env python3
"""Report basic data-quality facts for the tutorial's fictional survey CSV."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parents[4] / "data/raw/survey_results.csv"
    with source.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    ids = Counter(row["respondent_id"] for row in rows)
    duplicates = sorted(identifier for identifier, count in ids.items() if count > 1)
    missing_scores = sum(not row["score"].strip() for row in rows)
    non_numeric_scores = [
        row["respondent_id"]
        for row in rows
        if row["score"].strip() and not row["score"].strip().isdigit()
    ]

    print(f"input rows: {len(rows)}")
    print(f"duplicate respondent IDs: {', '.join(duplicates) or 'none'}")
    print(f"missing scores: {missing_scores}")
    print(f"non-numeric score respondent IDs: {', '.join(non_numeric_scores) or 'none'}")


if __name__ == "__main__":
    main()
