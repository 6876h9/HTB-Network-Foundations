# HTB Academy — Network Foundations

Personal study notes and a companion diagnostics script for HTB Academy's **Network Foundations** module.

| | |
|---|---|
| **Module** | Network Foundations |
| **Platform** | HTB Academy |
| **Difficulty** | Fundamental |
| **Sections** | 12 |
| **Reward** | +10 Cubes |
| **Status** | Completed |
| **Author** | `6876h9` |

## About This Module

Network Foundations is a theory-driven module, not an exploit or flag-capture challenge. It introduces the core concepts required to understand how networks function: network types, the OSI/TCP-IP models, addressing, DHCP, NAT, DNS, internet architecture, wireless networking, and baseline security concepts. Because there is no vulnerability or exploit involved, this repository is structured as a notes and reference repo rather than a writeup with a solve script.

## Module Sections

1. Introduction to Networks
2. Network Concepts
3. Components of a Network
4. Network Communication
5. Dynamic Host Configuration Protocol (DHCP)
6. Network Address Translation (NAT)
7. Domain Name System (DNS)
8. Internet Architecture
9. Wireless Networks
10. Network Security
11. Data Flow Example
12. Skills Assessment

## Repository Structure

```
HTB-Network-Foundations/
├── README.md
├── .gitignore
├── notes/
│   ├── 01-network-concepts.md
│   ├── 02-network-components.md
│   ├── 03-network-communication.md
│   ├── 04-dhcp.md
│   ├── 05-nat.md
│   ├── 06-dns.md
│   ├── 07-internet-architecture.md
│   ├── 08-wireless-networks.md
│   ├── 09-network-security.md
│   └── 10-skills-assessment-approach.md
├── scripts/
│   └── network_toolkit.py
└── screenshots/
    └── (module completion screenshot)
```

## Notes

The `notes/` directory contains a condensed reference for each major topic in the module, written for quick review rather than as a verbatim copy of the course material.

The Skills Assessment note (`10-skills-assessment-approach.md`) intentionally does **not** contain specific assessment questions, flags, or answers. HTB Academy's skills assessments are individualized per learner, and publishing exact answers would conflict with their academic integrity policy. That file is a generic command/methodology reference only.

## Companion Script — `network_toolkit.py`

A small cross-platform (Windows/Linux) Python utility that exercises the concepts covered in the module: local IP detection, DNS resolution, ping, traceroute, ARP table inspection, and a basic TCP port check.

### Usage

```
python3 scripts/network_toolkit.py --ip
python3 scripts/network_toolkit.py --resolve example.com
python3 scripts/network_toolkit.py --ping example.com
python3 scripts/network_toolkit.py --traceroute example.com
python3 scripts/network_toolkit.py --arp
python3 scripts/network_toolkit.py --ports example.com --port-list 21,22,80,443
```

No third-party dependencies are required; the script uses only the Python standard library.

**Authorized use only.** The ping and port-check functions should only be run against hosts you own or have explicit permission to test.

## Screenshots

Module completion screenshot belongs in the `screenshots/` directory.

## License

This repository is for personal study and reference purposes.
