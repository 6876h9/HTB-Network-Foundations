# Network Concepts

## What Is a Network

A network is a collection of interconnected devices (nodes) that exchange data over communication links. Nodes include computers, phones, printers, servers, and any other addressable endpoint.

## Network Types by Scope

| Type | Scope | Typical Owner | Example |
|---|---|---|---|
| PAN (Personal Area Network) | A few meters | Individual | Bluetooth between a phone and headset |
| LAN (Local Area Network) | A building or campus | Single org/individual | Home or office Wi-Fi |
| MAN (Metropolitan Area Network) | A city | ISP/municipality | City-wide fiber network |
| WAN (Wide Area Network) | Country/continent/global | Multiple orgs/ISPs | The internet |

LANs are fast, cheap to maintain, and locally owned. WANs connect multiple LANs together over long distances, are generally slower per hop due to distance and intermediate routing, and are collectively owned/operated by ISPs and carriers.

## Network Topologies

| Topology | Description | Trade-off |
|---|---|---|
| Bus | All devices share a single backbone cable | Simple, but one break disrupts the whole segment |
| Star | All devices connect to a central switch/hub | Easy to manage, single point of failure at the center |
| Ring | Each device connects to exactly two neighbors, forming a loop | Predictable traffic flow, a single break can disrupt the ring (mitigated with dual-ring designs) |
| Mesh | Devices interconnect directly with many/all others | Highly resilient, expensive to wire/maintain |
| Hybrid | Combination of the above | Used in most real-world enterprise networks |

## The OSI Model (7 Layers)

| Layer | Name | Function | Example Protocols/Units |
|---|---|---|---|
| 7 | Application | User-facing services | HTTP, FTP, DNS |
| 6 | Presentation | Data formatting, encryption, compression | TLS, JPEG, ASCII |
| 5 | Session | Establishes/manages/terminates sessions | NetBIOS, RPC |
| 4 | Transport | End-to-end delivery, reliability | TCP, UDP (Segments) |
| 3 | Network | Logical addressing and routing | IP, ICMP (Packets) |
| 2 | Data Link | Physical addressing, framing | Ethernet, ARP (Frames) |
| 1 | Physical | Raw bit transmission over media | Cables, radio, voltages (Bits) |

A common mnemonic: "Please Do Not Throw Sausage Pizza Away" (Physical, Data Link, Network, Transport, Session, Presentation, Application).

## The TCP/IP Model (4 Layers)

| TCP/IP Layer | Maps to OSI Layers | Function |
|---|---|---|
| Application | 5, 6, 7 | User-facing protocols (HTTP, DNS, SMTP) |
| Transport | 4 | TCP/UDP, ports, reliability |
| Internet | 3 | IP addressing and routing |
| Link (Network Access) | 1, 2 | Physical transmission, MAC addressing |

This is the model the actual internet is built on; the OSI model is primarily a teaching/reference framework.

## Encapsulation

As data moves down the stack for transmission, each layer wraps the data from the layer above it with its own header (and sometimes a trailer):

```
Application data
  -> Segment   (Transport layer adds TCP/UDP header)
    -> Packet  (Network layer adds IP header)
      -> Frame (Data Link layer adds MAC header/trailer)
        -> Bits (Physical layer transmits as electrical/optical/radio signal)
```

The receiving device reverses this process (decapsulation), stripping headers layer by layer until the original application data is recovered.
