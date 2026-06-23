# Skills Assessment — Approach and Command Reference

The Network Foundations skills assessment is individualized per learner and changes between attempts. This file does not contain — and intentionally will not contain — specific assessment questions, target details, or flag values. Publishing exact answers would conflict with HTB Academy's academic integrity policy and would defeat the purpose of the assessment. What follows is a general methodology and command reference, the same toolkit used while working through the assessment, applicable to any networking diagnostics task.

## General Troubleshooting/Discovery Flow

1. Confirm local interface configuration (IP, subnet mask, gateway, DNS).
2. Test basic reachability to a known-good host (ping).
3. Confirm DNS resolution is working.
4. Trace the path to the target to identify where, if anywhere, connectivity breaks down.
5. Identify what services are listening locally or on the target.
6. Check the local ARP table if working within the same broadcast domain.

## Command Reference

### Interface / IP Configuration

| OS | Command |
|---|---|
| Linux | `ip a` or `ifconfig` |
| Windows | `ipconfig /all` |

### Connectivity Testing

| OS | Command |
|---|---|
| Linux | `ping -c 4 <host>` |
| Windows | `ping -n 4 <host>` |

### DNS Resolution

| Tool | Command |
|---|---|
| nslookup | `nslookup <domain>` |
| dig | `dig <domain>` |

### Path Tracing

| OS | Command |
|---|---|
| Linux | `traceroute <host>` |
| Windows | `tracert <host>` |

### ARP Table

| OS | Command |
|---|---|
| Linux | `arp -a` or `ip neigh` |
| Windows | `arp -a` |

### Listening Services / Open Ports

| OS | Command |
|---|---|
| Linux | `ss -tulnp` or `netstat -tulnp` |
| Windows | `netstat -ano` |

### Routing Table

| OS | Command |
|---|---|
| Linux | `ip route` or `route -n` |
| Windows | `route print` |

## Notes

The companion script in `scripts/network_toolkit.py` wraps several of these checks (local IP, DNS resolution, ping, traceroute, ARP table, and a basic port check) into a single cross-platform utility, for repeated practice of these exact diagnostics outside of the live assessment.
