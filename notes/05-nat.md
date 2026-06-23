# Network Address Translation (NAT)

## Purpose

NAT allows devices using private (non-routable) IP addresses to communicate on the public internet by translating their private addresses to a public address at the network boundary (typically a router/gateway). This conserves the limited pool of public IPv4 addresses, since an entire private network can share a small number of public addresses.

## Types of NAT

| Type | Mapping | Description |
|---|---|---|
| Static NAT | One-to-one, fixed | A specific private IP is always translated to the same specific public IP. Common for servers that need a consistent public-facing address. |
| Dynamic NAT | One-to-one, from a pool | A private IP is translated to any available public IP from a configured pool, assigned on demand. |
| PAT (Port Address Translation) / NAT Overload | Many-to-one | Many private IPs share a single public IP, distinguished by unique source port numbers. This is the type used in virtually every home and small office router. |

## Port Address Translation (PAT) in Practice

Since PAT is the most common form of NAT encountered in practice, it's worth understanding the mechanism:

1. An internal host (e.g., `192.168.1.10:54321`) sends a packet to an external server.
2. The router/NAT device rewrites the source address to its own public IP and assigns a unique source port (e.g., `203.0.113.5:61000`), recording this mapping in a NAT translation table.
3. The external server replies to the public IP/port.
4. The router consults its NAT table, rewrites the destination back to `192.168.1.10:54321`, and forwards the reply to the correct internal host.

This is what allows dozens of devices on a home network to all share a single public IP address simultaneously.
