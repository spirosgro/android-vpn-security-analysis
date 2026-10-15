#!/usr/bin/env python3
"""Validate the structure and arithmetic of the archived aggregate findings."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "data" / "results" / "reported_findings.csv"
EXPECTED = {
    "applications_analyzed",
    "mean_mobsf_score",
    "apps_with_possible_hardcoded_secrets",
    "mean_detected_trackers",
    "apps_with_sha1_indicators",
    "apps_with_md5_indicators",
    "apps_with_rsa_below_2048",
    "apps_with_cleartext_traffic_indicator",
    "mean_dangerous_permissions",
    "apps_in_reported_low_risk_category",
}


def main() -> None:
    with RESULTS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    errors: list[str] = []
    metrics = {row["metric"] for row in rows}
    missing = EXPECTED - metrics
    unexpected = metrics - EXPECTED
    if missing:
        errors.append(f"Missing metrics: {sorted(missing)}")
    if unexpected:
        errors.append(f"Unexpected metrics: {sorted(unexpected)}")

    for row in rows:
        metric = row["metric"]
        try:
            value = float(row["value"])
        except ValueError:
            errors.append(f"{metric}: value is not numeric")
            continue

        if row["evidence_status"] != "reported_unverified":
            errors.append(f"{metric}: historical value must be reported_unverified")
        if value < 0:
            errors.append(f"{metric}: value cannot be negative")

        denominator = row["denominator"].strip()
        if denominator and int(float(denominator)) != 20:
            errors.append(f"{metric}: expected denominator 20")

        if row["unit"] == "percent":
            if not 0 <= value <= 100:
                errors.append(f"{metric}: percentage outside 0..100")
            if denominator:
                implied_count = value * int(float(denominator)) / 100
                if abs(implied_count - round(implied_count)) > 1e-9:
                    errors.append(
                        f"{metric}: {value}% of {denominator} does not imply a whole app count"
                    )

    if errors:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(errors))

    print(f"Validated {len(rows)} reported findings.")
    print("All percentage findings map to whole counts in the 20-application cohort.")
    print("All historical rows are explicitly labeled reported_unverified.")
    print("This validation checks structure and arithmetic; it does not reproduce MobSF scans.")


if __name__ == "__main__":
    main()
