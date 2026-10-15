# Android VPN Application Security Analysis

![Repository cover](assets/repo-cover.png)

An evidence-aware portfolio edition of a university study that used MobSF static analysis to examine 20 Android VPN applications. The repository preserves the aggregate coursework findings, corrects claims that exceed the available evidence, and turns the study into a repeatable mobile application security workflow.

> **Evidence boundary:** the original APK set, per-application MobSF JSON reports, scan timestamps, version manifest, and analyst validation notes were not found with the archived presentation. Every historical number is therefore labeled `reported_unverified`. The repository does not claim to reproduce the original experiment.

## What this project demonstrates

- Android application security review with MobSF
- evidence triage across permissions, trackers, secrets, certificates, and manifest findings
- OWASP MASVS-aligned interpretation
- careful separation of static indicators from confirmed vulnerabilities
- reproducible data schemas, validation, and remediation prioritization
- privacy-safe publication without APKs, credentials, or classmates' identifiers

## Reported coursework findings

| Metric | Reported result | Interpretation limit |
|---|---:|---|
| Applications analyzed | 20 | The app/version inventory is unavailable |
| Mean MobSF score | 48.9/100 | Tool score, not a complete security rating |
| Apps with possible hardcoded secrets | 75% | Static matches require analyst validation |
| Mean detected trackers | 6.1 per app | Presence does not establish malicious behavior |
| Apps with SHA-1 indicators | 55% | Context and cryptographic purpose are unknown |
| Apps with MD5 indicators | 40% | Context and cryptographic purpose are unknown |
| Apps with RSA keys below 2048 bits | 20% | Certificate/key role was not preserved |
| Mean dangerous permissions | 4.9 per app | Necessity must be assessed per feature and Android version |

The source presentation also reported that no application received its low-risk category. This is retained as a historical tool-output claim, not an independent product verdict.

## Repository contents

- [Technical report](report/vpn-android-security-analysis-report.docx) — the complete English analysis.
- [Presentation](presentation/vpn-android-security-analysis-presentation.pptx) — a concise English briefing deck.
- [Reported findings](data/results/reported_findings.csv) — machine-readable historical aggregates with evidence status.
- [Claim audit](docs/claim-audit.md) — what was retained, corrected, or removed.
- [Methodology](docs/methodology.md) — a repeatable, version-controlled assessment design.
- [Threat model](docs/threat-model.md) — trust boundaries and abuse cases for an Android VPN client.
- [Remediation backlog](docs/remediation-backlog.md) — prioritized engineering actions.
- [Reproducibility guide](docs/reproducibility.md) — MobSF workflow and evidence handling.
- [MobSF normalizer](src/normalize_mobsf_report.py) — converts a JSON report into a stable one-row CSV summary.
- [Result validator](src/validate_reported_findings.py) — checks percentages, counts, units, and evidence labels.

## Quick start

The code uses the Python standard library.

```bash
python src/validate_reported_findings.py
python src/normalize_mobsf_report.py examples/synthetic-mobsf-report.json --output output/app-summary.csv
```

For a new authorized assessment, pin a MobSF container image by digest, record each APK hash and version, export JSON reports, and keep raw reports outside the public repository. See [Reproducibility](docs/reproducibility.md).

## Key corrections to the archived presentation

- A static indicator for SHA-1, MD5, or a short RSA key does not by itself prove that the VPN tunnel uses weak cryptography.
- A detected string that resembles a secret is a candidate finding until its scope, validity, and exposure are confirmed.
- Tracker detection is a privacy review input, not proof of harmful processing.
- `INTERNET` is not the only permission a legitimate VPN app may need. Permission necessity depends on declared features, Android version, foreground-service behavior, notifications, billing, and support functions.
- Price, licensing model, and brand reputation cannot be ranked from the retained aggregate evidence.

## Ethical and legal scope

Only analyze applications you are authorized to assess. Do not commit APKs, API keys, user traffic, VPN profiles, credentials, or raw reports containing sensitive strings. Follow application terms, applicable law, and coordinated disclosure practices.

## Provenance

The original Greek presentation was collaborative university coursework prepared by Spiros Grouztidis and two classmates. Their names and student identifiers are omitted from this public edition. Spiros Grouztidis prepared this English portfolio edition, including the claim audit, reproducibility workflow, code, threat model, report, and presentation.

## License

Code is licensed under the MIT License in [LICENSE-CODE](LICENSE-CODE). Original written and visual material is licensed under the terms in [LICENSE.md](LICENSE.md). Third-party tools, standards, product names, and cited material remain subject to their own terms.
