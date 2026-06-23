# Components of a Network

## Core Devices

| Device | OSI Layer | Function |
|---|---|---|
| Hub | Physical (1) | Repeats incoming signal to all connected ports; no intelligence, creates one large collision domain |
| Switch | Data Link (2) | Forwards frames based on destination MAC address using a CAM (MAC address) table; each port is its own collision domain |
| Router | Network (3) | Forwards packets between different networks based on IP addresses; maintains a routing table |
| Access Point (AP) | Data Link (2) | Bridges wireless clients to a wired network |
| Modem | Physical (1) | Converts digital signals to/from the format used by the ISP's transmission medium (DSL, cable, fiber) |
| Firewall | Varies (3-7 depending on type) | Filters traffic based on defined rules |
| NIC (Network Interface Card) | Physical/Data Link | Hardware that connects a host to the network; has a burned-in MAC address |
| Server | Application | Provides resources/services (files, DNS, web pages, authentication) to clients |

## Switch vs Hub vs Router (Quick Comparison)

| Aspect | Hub | Switch | Router |
|---|---|---|---|
| Layer | 1 | 2 | 3 |
| Forwarding decision | None (broadcasts to all ports) | MAC address (CAM table) | IP address (routing table) |
| Collision domain | One shared domain | One domain per port | One domain per port |
| Broadcast domain | Same as collision domain | Single, unless VLANs are used | Routers separate broadcast domains |

## How a Switch Learns

A switch builds its CAM table dynamically: when a frame arrives, the switch records the source MAC address against the port it arrived on. If the destination MAC is already known, the frame is forwarded only to that port. If unknown, the frame is flooded out every other port (unicast flooding) until a reply is seen.

## How a Router Forwards Traffic

A router examines the destination IP address of an incoming packet, consults its routing table for the best matching route (longest prefix match), and forwards the packet out the appropriate interface toward the next hop. Routes can be added manually (static routing) or learned dynamically via routing protocols (e.g., OSPF, BGP).
