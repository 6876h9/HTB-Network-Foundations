#!/usr/bin/env python3
"""
network_toolkit.py

A small cross-platform companion utility built to exercise the concepts
covered in HTB Academy's "Network Foundations" module: local addressing,
DNS resolution, reachability testing, path tracing, ARP table inspection,
and basic TCP port checks.

Author: 6876h9

Usage:
    python3 network_toolkit.py --ip
    python3 network_toolkit.py --resolve example.com
    python3 network_toolkit.py --ping example.com
    python3 network_toolkit.py --traceroute example.com
    python3 network_toolkit.py --arp
    python3 network_toolkit.py --ports example.com --port-list 21,22,80,443

Note:
    Only run connectivity and port checks against hosts you own or are
    explicitly authorized to test.
"""

import argparse
import platform
import socket
import subprocess


def get_local_ip():
    """Return the local IP address used for outbound traffic."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    except OSError:
        ip = "127.0.0.1"
    finally:
        sock.close()
    return ip


def resolve_dns(domain):
    """Resolve a domain name to its IPv4 address."""
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as exc:
        return f"Resolution failed: {exc}"


def ping_host(host, count=4):
    """Ping a host using the platform-appropriate ping syntax."""
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = ["ping", flag, str(count), host]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    except FileNotFoundError:
        return "ping is not available on this system."


def traceroute_host(host):
    """Trace the path to a host using tracert (Windows) or traceroute (Linux/macOS)."""
    cmd = ["tracert", host] if platform.system().lower() == "windows" else ["traceroute", host]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    except FileNotFoundError:
        return "traceroute/tracert is not installed on this system."


def show_arp_table():
    """Display the local ARP cache (IP-to-MAC mappings on the local segment)."""
    try:
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    except FileNotFoundError:
        return "arp is not available on this system."


def check_ports(host, ports):
    """Check whether a list of TCP ports are open on a host."""
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5)
        try:
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
        finally:
            sock.close()
    return open_ports


def main():
    parser = argparse.ArgumentParser(
        description="Network Foundations companion diagnostics toolkit."
    )
    parser.add_argument("--ip", action="store_true",
                         help="Show the local outbound IP address.")
    parser.add_argument("--resolve", metavar="DOMAIN",
                         help="Resolve a domain name to an IPv4 address.")
    parser.add_argument("--ping", metavar="HOST",
                         help="Ping a host.")
    parser.add_argument("--traceroute", metavar="HOST",
                         help="Trace the route to a host.")
    parser.add_argument("--arp", action="store_true",
                         help="Show the local ARP table.")
    parser.add_argument("--ports", metavar="HOST",
                         help="Host to check ports on.")
    parser.add_argument("--port-list", metavar="PORTS",
                         default="21,22,23,25,53,80,443,3389",
                         help="Comma-separated TCP ports to check "
                              "(default: common service ports).")

    args = parser.parse_args()
    ran_anything = False

    if args.ip:
        print(f"Local IP address: {get_local_ip()}")
        ran_anything = True

    if args.resolve:
        print(f"{args.resolve} -> {resolve_dns(args.resolve)}")
        ran_anything = True

    if args.ping:
        print(ping_host(args.ping))
        ran_anything = True

    if args.traceroute:
        print(traceroute_host(args.traceroute))
        ran_anything = True

    if args.arp:
        print(show_arp_table())
        ran_anything = True

    if args.ports:
        ports = [int(p.strip()) for p in args.port_list.split(",")]
        open_ports = check_ports(args.ports, ports)
        if open_ports:
            print(f"Open ports on {args.ports}: {open_ports}")
        else:
            print(f"No open ports found on {args.ports} from the checked list: {ports}")
        ran_anything = True

    if not ran_anything:
        parser.print_help()


if __name__ == "__main__":
    main()
