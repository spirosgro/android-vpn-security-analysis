# Remediation backlog

| Priority | Action | Evidence for closure |
|---|---|---|
| P0 | Revoke and rotate any validated embedded production credential | rotation record, scope review, regression scan |
| P0 | Correct certificate validation or tunnel endpoint authentication failures | negative TLS tests and successful trusted-endpoint tests |
| P0 | Remove cleartext transmission of sensitive data | network security configuration and runtime traffic evidence |
| P1 | Protect exported components and remove unintended entry points | manifest diff and authorized component tests |
| P1 | Minimize permissions and document feature justification | permission matrix, product-owner approval, runtime verification |
| P1 | Verify tunnel routes, DNS handling, always-on mode, and lockdown behavior | emulator/device test record and packet-capture summary |
| P1 | Replace security-relevant MD5/SHA-1 use and short RSA keys | code/config diff and cryptographic test evidence |
| P2 | Remove unnecessary trackers and document retained telemetry | SDK inventory, data-flow map, privacy notice and consent evidence |
| P2 | Add dependency and secret scanning to CI | CI policy, failing test fixture, protected secret store |
| P2 | Reduce sensitive logs and define retention | log review, redaction tests, retention configuration |
| P3 | Generate an SBOM and monitor dependencies | signed SBOM, vulnerability-monitoring record |

Priority must be based on validated impact, exposure, exploitability, and affected data. Automated severity labels alone do not determine remediation order.
