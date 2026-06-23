# Network Communication

## MAC Addresses

A MAC (Media Access Control) address is a 48-bit address burned into a NIC, usually written as six hex octets (e.g., `00:1A:2B:3C:4D:5E`). The first 24 bits (OUI) identify the manufacturer; the last 24 bits identify the specific device. MAC addresses operate at Layer 2 and are only meaningful within the local network segment (broadcast domain) — they are not used for routing across networks.

## IP Addresses

An IPv4 address is a 32-bit logical address, written in dotted-decimal notation (e.g., `192.168.1.10`), used for routing traffic across networks at Layer 3.

### Private (RFC 1918) Address Ranges

| Range | CIDR | Typical Use |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | /8 | Large enterprise networks |
| 172.16.0.0 – 172.31.255.255 | /12 | Medium-sized networks |
| 192.168.0.0 – 192.168.255.255 | /16 | Home/small office networks |

Private addresses are not routable on the public internet; devices using them rely on NAT to communicate externally.

### Public vs Private

Public IP addresses are globally unique and routable on the internet. Private IP addresses are reused across countless internal networks and only have meaning within their own LAN.

## Ports

A port is a 16-bit number (0–65535) used alongside an IP address to identify a specific process/service on a host.

| Range | Name | Use |
|---|---|---|
| 0 – 1023 | Well-known ports | Standard services (HTTP, FTP, SSH, DNS) |
| 1024 – 49151 | Registered ports | Assigned to specific applications by IANA |
| 49152 – 65535 | Dynamic/private ports | Temporary, used for outbound client connections |

### Common Well-Known Ports

| Port | Protocol | Service |
|---|---|---|
| 20/21 | TCP | FTP (data/control) |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP (server/client) |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 3389 | TCP | RDP |

## Address Resolution Protocol (ARP)

ARP resolves a known IP address to its corresponding MAC address on the local network segment. The process:

1. A host needs to send a packet to an IP address on its local subnet but only knows the destination's IP, not its MAC.
2. It broadcasts an ARP request: "Who has this IP address?"
3. The device with that IP responds directly with an ARP reply containing its MAC address.
4. The requesting host caches the mapping in its ARP table for future use, avoiding repeated broadcasts.

ARP tables can be viewed with `arp -a` on both Windows and Linux. Because ARP has no built-in authentication, it is also a common target for ARP spoofing/poisoning attacks, where an attacker sends forged ARP replies to redirect traffic through their own machine.

## TCP vs UDP

| Aspect | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery, retransmission, ordering | No delivery guarantee |
| Overhead | Higher | Lower |
| Use cases | Web browsing, file transfer, email | DNS queries, streaming, VoIP, gaming |

### TCP Three-Way Handshake

1. Client sends `SYN`
2. Server responds `SYN-ACK`
3. Client responds `ACK`

The connection is now established and data transfer begins. Termination uses a comparable four-step exchange (`FIN`/`ACK` in each direction).
