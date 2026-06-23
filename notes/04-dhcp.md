# Dynamic Host Configuration Protocol (DHCP)

## Purpose

DHCP automatically assigns IP addresses and other network configuration (subnet mask, default gateway, DNS servers) to hosts joining a network, removing the need for manual configuration on every device.

## Roles

| Role | Function |
|---|---|
| DHCP Server | Maintains a pool (scope) of available addresses and leases them to clients |
| DHCP Client | Requests an address from the server when joining the network |
| DHCP Relay Agent | Forwards DHCP requests across subnet boundaries to a centralized DHCP server when the server isn't on the same local segment |

## The DORA Process

DHCP address assignment happens in four steps, commonly remembered as DORA:

1. **Discover** — The client broadcasts a `DHCPDISCOVER` message looking for any available DHCP server.
2. **Offer** — A DHCP server responds with a `DHCPOFFER`, proposing an IP address and lease terms.
3. **Request** — The client broadcasts a `DHCPREQUEST`, formally requesting the offered address (this is broadcast so any other DHCP servers that made offers know they were not selected).
4. **Acknowledge** — The server confirms with a `DHCPACK`, finalizing the lease.

## IP Address Leasing

Addresses are not assigned permanently — they are leased for a configured duration. As the lease approaches expiration:

- At roughly 50% of the lease time (T1), the client attempts to renew with the original server.
- At roughly 87.5% of the lease time (T2), if renewal hasn't succeeded, the client broadcasts to renew with any available DHCP server.
- If the lease fully expires without renewal, the client must restart the DORA process.

## IP Address Conservation

Because IPv4 address space is limited, DHCP scopes and lease durations are tuned to conserve addresses:

- Shorter lease times free up addresses faster for reuse in high-turnover environments (e.g., guest Wi-Fi).
- Subnetting/scoping limits how many addresses are allocated to a given segment, avoiding waste.
- Reservations can be used to permanently tie a known MAC address to a specific IP without consuming a "floating" lease.
