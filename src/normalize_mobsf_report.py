#!/usr/bin/env python3
"""Normalize selected fields from one MobSF Android JSON report.

The script creates an inventory/triage row. It does not confirm vulnerabilities.
MobSF report keys may change between versions, so missing fields are left blank
and the pinned MobSF version should always be recorded with the evidence set.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "app_name",
    "package_name",
    "version_name",
    "version_code",
    "sha256",
    "security_score",
    "high_findings",
    "warning_findings",
    "dangerous_permissions",
    "detected_trackers",
    "candidate_secrets",
    "manifest_high",
    "manifest_warning",
    "certificate_high",
    "certificate_warning",
    "evidence_level",
]


def mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def count_items(value: Any) -> int | str:
    if isinstance(value, (list, tuple, set, dict)):
        return len(value)
    if isinstance(value, int):
        return value
    return ""


def summary_value(section: dict[str, Any], key: str) -> int | str:
    value = section.get(key, "")
    if isinstance(value, list):
        return len(value)
    if isinstance(value, (int, float)):
        return int(value)
    return ""


def normalize(report: dict[str, Any]) -> dict[str, Any]:
    appsec = mapping(report.get("appsec"))
    permissions = mapping(report.get("permissions"))
    trackers = mapping(report.get("trackers"))
    manifest = mapping(mapping(report.get("manifest_analysis")).get("manifest_summary"))
    certificate = mapping(
        mapping(report.get("certificate_analysis")).get("certificate_summary")
    )

    dangerous_permissions = sum(
        1
        for details in permissions.values()
        if isinstance(details, dict)
        and str(details.get("status", "")).lower() == "dangerous"
    )

    return {
        "app_name": report.get("app_name", ""),
        "package_name": report.get("package_name", ""),
        "version_name": report.get("version_name", ""),
        "version_code": report.get("version_code", ""),
        "sha256": report.get("sha256", ""),
        "security_score": appsec.get("security_score", report.get("security_score", "")),
        "high_findings": count_items(appsec.get("high", [])),
        "warning_findings": count_items(appsec.get("warning", [])),
        "dangerous_permissions": dangerous_permissions,
        "detected_trackers": trackers.get("detected_trackers", ""),
        "candidate_secrets": count_items(report.get("secrets", [])),
        "manifest_high": summary_value(manifest, "high"),
        "manifest_warning": summary_value(manifest, "warning"),
        "certificate_high": summary_value(certificate, "high"),
        "certificate_warning": summary_value(certificate, "warning"),
        "evidence_level": "E1_automated_static_indicator",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="MobSF JSON report")
    parser.add_argument("--output", type=Path, required=True, help="Output CSV path")
    args = parser.parse_args()

    report = json.loads(args.report.read_text(encoding="utf-8"))
    if not isinstance(report, dict):
        raise SystemExit("Expected a JSON object at the report root.")

    row = normalize(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerow(row)

    print(json.dumps(row, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
