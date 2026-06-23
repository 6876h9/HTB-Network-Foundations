# Network Security

## The CIA Triad

| Principle | Goal | Example Controls |
|---|---|---|
| Confidentiality | Prevent unauthorized disclosure of data | Encryption, access controls |
| Integrity | Ensure data remains accurate and unaltered | Hashing, digital signatures, checksums |
| Availability | Ensure systems/data are accessible when needed | Redundancy, backups, DDoS mitigation |

Every security control can generally be mapped back to protecting one or more sides of this triad.

## Firewalls

| Type | Layer | Description |
|---|---|---|
| Packet-filtering | 3/4 | Stateless; allows/denies traffic based on source/destination IP, port, and protocol |
| Stateful | 3/4 | Tracks the state of active connections, only allowing traffic that matches an established or expected session |
| Proxy/Application-layer | 7 | Inspects and filters traffic based on application-layer content, not just headers |
| Next-Generation Firewall (NGFW) | 3-7 | Combines stateful inspection with deep packet inspection, application awareness, and intrusion prevention |

Firewalls can also be classified by placement: network-based (protecting an entire segment) versus host-based (protecting a single machine, e.g., Windows Defender Firewall, iptables/nftables on Linux).

## Intrusion Detection vs Prevention

| System | Function | Placement | Action |
|---|---|---|---|
| IDS (Intrusion Detection System) | Monitors traffic and generates alerts | Typically out-of-band (passive tap/mirror) | Detects only — does not block traffic |
| IPS (Intrusion Prevention System) | Monitors traffic and actively blocks malicious activity | Inline, in the traffic path | Detects and blocks |

Both can use:

- **Signature-based detection** — matches traffic against known attack patterns; effective against known threats but blind to novel ones.
- **Anomaly-based detection** — establishes a baseline of normal behavior and flags deviations; can catch novel attacks but is more prone to false positives.
