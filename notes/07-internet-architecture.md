# Internet Architecture

## ISP Tiers

| Tier | Description |
|---|---|
| Tier 1 | Forms the global backbone; peers with other Tier 1 providers without paying for transit; can reach the entire internet through peering alone |
| Tier 2 | Regional/national providers; peer with some networks but also pay Tier 1 providers for transit to reach the rest of the internet |
| Tier 3 | Local/last-mile ISPs; purchase transit from Tier 1/2 providers to deliver internet access to homes and businesses |

## Internet Exchange Points (IXPs)

IXPs are physical locations where multiple networks (ISPs, content providers, CDNs) interconnect directly to exchange traffic, rather than routing through third-party transit providers. This reduces latency and transit costs for the networks involved.

## Autonomous Systems and BGP

The internet is divided into Autonomous Systems (AS) — networks under a single administrative entity, each identified by a unique AS number. Routing between Autonomous Systems is handled by BGP (Border Gateway Protocol), which exchanges reachability information between ASes so traffic can find a path across the global internet.

## Last-Mile Connectivity

| Medium | Description |
|---|---|
| DSL | Uses existing copper telephone lines |
| Cable | Uses coaxial cable, shared with cable TV infrastructure |
| Fiber | Uses fiber-optic cable, offering the highest bandwidth and lowest latency |
| Satellite | Used where terrestrial infrastructure is impractical; higher latency |

## Content Delivery Networks (CDNs)

CDNs cache copies of content (web pages, video, static assets) at servers distributed geographically close to end users. This reduces latency and load on the origin server by serving requests from a nearby edge node rather than routing every request back to a single central server.
