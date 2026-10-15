# Methodology

## Objective

Assess the static attack surface of authorized Android VPN application packages and produce findings that are traceable to evidence, app versions, and verification controls.

## Study design

1. Define inclusion criteria before collecting samples.
2. Record package name, version name, version code, acquisition source and time, and SHA-256 for every APK.
3. Pin the MobSF version and container digest.
4. Run each APK under the same configuration.
5. Export the JSON report and record the scan timestamp.
6. Normalize app metadata, security score, permissions, trackers, candidate secrets, manifest findings, network-security configuration, and certificate findings.
7. Review every high-impact automated finding manually.
8. Map validated findings to current OWASP MASVS controls.
9. Use an emulator and test account for dynamic confirmation where authorization permits.
10. Publish only redacted aggregates and non-sensitive evidence.

## Evidence levels

| Level | Meaning | Example |
|---|---|---|
| E0 | Reported historical aggregate only | “75% had candidate secrets” from the archived deck |
| E1 | Automated static indicator | MobSF flags an exported component |
| E2 | Analyst-validated static finding | The component is externally reachable and lacks an expected guard |
| E3 | Authorized runtime confirmation | A test demonstrates the impact in an isolated environment |

## Required controls

- Fix the cohort and sampling criteria before comparing product groups.
- Preserve hashes and versions; product names alone are insufficient.
- Distinguish app-signing algorithms, bundled assets, third-party libraries, protocol cryptography, and VPN tunnel configuration.
- Treat secrets and tracker detections as leads until manually validated.
- Assess permissions against declared product features and current Android behavior.
- Report uncertainty, false-positive handling, missing data, and analyst decisions.

## Metrics

Use counts and proportions with explicit denominators. For small cohorts, publish raw counts beside percentages. Avoid causal or market-wide claims from a convenience sample. A MobSF score may support triage but should not be the sole outcome metric.
