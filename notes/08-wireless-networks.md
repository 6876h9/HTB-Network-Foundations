# Wireless Networks

## 802.11 Standards

| Standard | Band | Approx. Max Speed | Notes |
|---|---|---|---|
| 802.11a | 5 GHz | 54 Mbps | Less interference, shorter range |
| 802.11b | 2.4 GHz | 11 Mbps | Longer range, more interference |
| 802.11g | 2.4 GHz | 54 Mbps | Backward compatible with 802.11b |
| 802.11n (Wi-Fi 4) | 2.4/5 GHz | ~600 Mbps | Introduced MIMO (multiple antennas) |
| 802.11ac (Wi-Fi 5) | 5 GHz | Multi-Gbps | Introduced MU-MIMO |
| 802.11ax (Wi-Fi 6) | 2.4/5 GHz | Multi-Gbps | Improved efficiency in dense environments via OFDMA |

## 2.4 GHz vs 5 GHz

| Aspect | 2.4 GHz | 5 GHz |
|---|---|---|
| Range | Longer (better wall penetration) | Shorter |
| Interference | Higher (shared with Bluetooth, microwaves, baby monitors) | Lower |
| Available channels | Fewer non-overlapping channels (typically 1, 6, 11) | Many more non-overlapping channels |
| Speed | Lower | Higher |

## SSID

The Service Set Identifier (SSID) is the human-readable name broadcast by a wireless access point, used by clients to identify and connect to a specific network.

## Wireless Security Protocols

| Protocol | Status | Notes |
|---|---|---|
| WEP | Deprecated/broken | Uses RC4; trivially crackable with modern tools, should never be used |
| WPA | Deprecated | Improved on WEP with TKIP, but still has known weaknesses |
| WPA2 | Widely deployed | Uses AES-CCMP; considered strong, though vulnerable to the KRACK attack if unpatched |
| WPA3 | Current standard | Uses SAE (Simultaneous Authentication of Equals) handshake, provides forward secrecy and stronger protection against offline brute-force attacks |

## Mobile Hotspot

A mobile hotspot uses a device's cellular data connection and shares it over Wi-Fi (or USB/Bluetooth tethering) to provide internet access to other nearby devices, effectively turning the cellular connection into a small WAN-to-LAN bridge.
