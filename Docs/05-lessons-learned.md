# Lessons Learned

This document records every important lesson, issue and solution encountered during the project.

---

# Lesson 1

## Problem

Ubuntu Server had no Internet access.

## Cause

The Cisco router had no WAN interface connected to the Internet.

## Solution

- Added a PA-2FE-TX module.
- Configured FastEthernet1/0 as the WAN interface.
- Connected it to the GNS3 NAT node.
- Configured DHCP on the WAN interface.
- Configured Cisco PAT (NAT Overload).

---

# Lesson 2

## Problem

APT failed with DNS and connectivity errors.

## Cause

The laboratory had Internet connectivity only over IPv4, while APT attempted IPv6 connections first.

## Solution

Forced APT to use IPv4.

---

# Lesson 3

## Problem

OpenSSH service appeared as "inactive (dead)".

## Cause

Ubuntu 24.04 uses systemd socket activation.

## Solution

Verified the SSH service using:

systemctl status ssh.socket

instead of relying only on:

systemctl status ssh

---

# Lesson 4

## Engineering Decision

TCP SYN packets alone should not trigger an attack alert.

## Reason

Every legitimate SSH connection starts with a TCP SYN packet.

## Final Strategy

Version 1

Simple end-to-end implementation.

Version 2

Improve detection using:

- SYN rate
- SSH authentication logs
- Multiple correlated indicators

This strategy was validated by the project supervisor.

---

# Phase 03 Lessons Learned

- Python virtual environments simplify dependency management.
- Scapy requires administrator privileges for packet capture.
- Berkeley Packet Filters (BPF) significantly reduce unnecessary traffic processing.
- TCP SYN packets provide an effective indicator of new SSH connection attempts.
- A cumulative counter is insufficient for brute-force detection.
- A sliding time window greatly improves detection accuracy.
- Incremental validation after each development step simplifies debugging.

