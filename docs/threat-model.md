# Android VPN client threat model

## Assets

- user traffic and DNS queries
- VPN credentials, tokens, and device-bound keys
- account and subscription data
- application configuration and logs
- update channel and signing identity
- user trust in the tunnel state and endpoint identity

## Trust boundaries

1. Android user and application UI
2. application process and local storage
3. Android `VpnService` and the local TUN interface
4. cryptographic tunnel and remote VPN gateway
5. provider control plane and authentication services
6. third-party SDKs, analytics, crash reporting, and advertising services
7. application distribution and update infrastructure

## Priority abuse cases

| Abuse case | Security effect | Evidence to collect | Primary control area |
|---|---|---|---|
| Tunnel bypass or split-routing error | Traffic leaves outside the intended tunnel | route configuration, always-on/lockdown behavior, runtime packet capture | MASVS-NETWORK |
| Weak endpoint authentication | Attacker impersonates a gateway | TLS configuration, certificate validation, pinning decision, dynamic MITM test | MASVS-NETWORK |
| Embedded reusable credential | Unauthorized access to backend services | static candidate, validity test in a controlled environment, privilege scope | MASVS-STORAGE / AUTH |
| Excessive or unexplained permission | Expanded local data access | manifest, feature justification, runtime permission behavior | MASVS-PLATFORM / PRIVACY |
| Third-party SDK collection | Undisclosed or excessive telemetry | SDK inventory, destination domains, privacy notice, consent and retention | MASVS-PRIVACY |
| Exported component abuse | Another app invokes privileged behavior | manifest flags, intent filters, permission guards, proof of reachability | MASVS-PLATFORM |
| Sensitive logging | Tokens, endpoints, or user data leak to logs | source review and runtime logs | MASVS-STORAGE / PRIVACY |
| Insecure update or dependency | Compromised code reaches users | signing, dependency inventory, update validation, SBOM | MASVS-CODE |

## Static-analysis boundary

Static analysis is strong for inventory and triage. It cannot establish actual tunnel routing, endpoint authentication, DNS leakage, tracker activation, secret validity, or runtime exploitability on its own. Those questions require controlled dynamic testing.
