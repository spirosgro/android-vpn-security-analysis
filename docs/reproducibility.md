# Reproducibility

## What is missing from the archived study

- APK hashes and exact versions
- acquisition dates and inclusion criteria
- raw MobSF JSON reports
- MobSF container digest and configuration
- analyst validation notes
- per-application observations
- dynamic test evidence

The original aggregate results cannot be independently reproduced without these artifacts.

## Re-run workflow

1. Obtain explicit authorization for every application sample.
2. Create a private evidence store and complete `data/templates/app_inventory_template.csv`.
3. Pin a MobSF release and Docker image digest. Do not rely on a floating `latest` tag for an evidence-bearing run.
4. Scan each APK and export `/api/v1/report_json` output.
5. Keep raw reports private because candidate secrets, package paths, endpoints, and certificates may be sensitive.
6. Normalize each report:

   ```bash
   python src/normalize_mobsf_report.py private-evidence/report.json --output output/app-summary.csv
   ```

7. Record findings in `data/templates/finding_template.csv` and validate high-impact items manually.
8. Add authorized dynamic tests for tunnel routing, DNS behavior, TLS validation, and sensitive data flows.
9. Publish redacted aggregates with exact denominators and evidence levels.

## Reproducibility checklist

- [ ] cohort definition frozen before analysis
- [ ] all APK SHA-256 hashes recorded
- [ ] app versions and acquisition timestamps recorded
- [ ] MobSF version and image digest pinned
- [ ] JSON reports retained privately
- [ ] analyst decisions recorded
- [ ] false positives tracked
- [ ] percentages include denominators
- [ ] dynamic claims backed by runtime evidence
- [ ] public files scanned for secrets and identifiers
