# Domain Name System (DNS)

## Purpose

DNS translates human-readable domain names (e.g., `example.com`) into the IP addresses computers use to locate each other on a network. Without DNS, users would need to memorize numeric IP addresses for every service they want to reach.

## DNS Hierarchy

DNS is structured as an inverted tree:

```
.                          (Root)
├── com.                   (Top-Level Domain - TLD)
│   └── example.com.       (Second-Level Domain)
│       └── www.example.com.  (Subdomain/Host)
├── org.
├── net.
└── pk., uk., de., ...     (Country-code TLDs)
```

| Level | Example | Managed By |
|---|---|---|
| Root | `.` | Root server operators (13 logical root server clusters worldwide) |
| TLD | `.com`, `.org`, `.pk` | Registry operators per TLD |
| Authoritative | `example.com`'s name servers | The domain owner/their DNS provider |

## DNS Record Types

| Record | Purpose |
|---|---|
| A | Maps a hostname to an IPv4 address |
| AAAA | Maps a hostname to an IPv6 address |
| CNAME | Aliases one hostname to another hostname |
| MX | Specifies mail servers for a domain |
| NS | Specifies authoritative name servers for a domain |
| TXT | Holds arbitrary text, often used for verification (SPF, DKIM) |
| PTR | Maps an IP address back to a hostname (reverse DNS) |
| SOA | Holds administrative information about a DNS zone |

## DNS Resolution Process

1. A client queries its configured DNS resolver (often the ISP's resolver or a public resolver such as `8.8.8.8` or `1.1.1.1`).
2. If the resolver doesn't already have the answer cached, it queries a root server, which points it to the relevant TLD server.
3. The TLD server points the resolver to the domain's authoritative name server.
4. The authoritative server returns the actual record (e.g., the A record with the IP address).
5. The resolver caches the answer (per the record's TTL) and returns it to the client.

This is known as recursive resolution from the client's point of view, and iterative resolution from the resolver's point of view as it walks up the hierarchy.

## Useful Tools

- `nslookup example.com`
- `dig example.com`
- `dig example.com MX`

Both tools allow you to query specific record types and specific name servers directly, which is useful for troubleshooting and for enumeration during security assessments.
