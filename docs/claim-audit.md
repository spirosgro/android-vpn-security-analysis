# Claim audit

## Purpose

The archived presentation contains useful aggregate observations but does not include the evidence required to reproduce or independently verify the 20 application scans. This audit defines which claims can be published and how they must be phrased.

## Retained as reported results

The application count, mean MobSF score, hardcoded-secret prevalence, mean tracker count, SHA-1 and MD5 indicators, short-RSA prevalence, cleartext-traffic indicator, mean dangerous-permission count, and low-risk category count are preserved in `data/results/reported_findings.csv`. Every row is marked `reported_unverified`.

## Corrected interpretations

| Archived interpretation | Public edition correction |
|---|---|
| Weak primitives prove weak VPN cryptography | A static match must be tied to a security-relevant code path, certificate, signature, or tunnel protocol before drawing that conclusion |
| A hardcoded-secret match is an exposed credential | It is a candidate secret until validity, privilege, environment, and reachability are confirmed |
| Tracker presence proves a privacy violation | It triggers a privacy review of purpose, disclosure, consent, data flow, and retention |
| A VPN needs only one permission | Permission necessity depends on features and platform requirements; each permission must be justified individually |
| Five dangerous permissions means five times over-privileged | No defensible universal baseline was retained, so the multiplier is removed |
| Premium, freemium, and free products can be ranked | Per-application observations and sampling controls are unavailable, so comparative product claims are removed |
| A MobSF score is a product security grade | It is one automated static-analysis signal and requires manual and dynamic testing |

## Removed claims

- vendor-specific recommendations and avoidance lists
- claims that open source licensing alone predicts stronger security
- market-size figures that were not needed for the technical analysis
- direct mappings from every finding to the legacy OWASP Mobile Top 10 without control-level evidence

## Publication decision

The repository is suitable for a portfolio when the evidence boundary remains visible. It demonstrates security reasoning, correction of overclaims, data handling, and a repeatable assessment design. It must not be presented as an independently reproduced benchmark of named VPN vendors.
