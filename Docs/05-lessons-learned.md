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

# Phase 3 Lessons Learned

## Telegram API

The Telegram Bot API provides a simple and reliable mechanism for sending automated security notifications.

---

## Modular Design

Separating the notification logic into telegram_notifier.py significantly improves code maintainability and reusability.

---

## Sliding Time Window

Using a sliding time window reduces false positives and ensures that only recent connection attempts are considered.

---

## Threshold Detection

Using

```
count == THRESHOLD
```

instead of

```
count >= THRESHOLD
```

prevents duplicate notifications.

---

## Common Issues

- DNS resolution failure.
- Running Scapy without root privileges.
- Incorrect variable initialization.
- timedelta comparison with integers.
- SSH command waiting for password input.
- Multiple notifications generated before threshold logic was corrected.

---

## Conclusion

The notification subsystem is now stable and ready to be integrated with the Cisco automatic response module during the next phase.

# Phase 4 Lessons Learned

- Cisco IOS can be remotely managed using Netmiko through SSH.
- Separating the Cisco module from the detection engine improves code modularity.
- Moving sensitive information to a .env file prevents credential exposure.
- try/except/finally blocks improve application robustness during router communication failures.
- Dynamic Cisco ACLs provide an effective automated response against detected SSH attacks.
- Keeping each module focused on a single responsibility simplifies maintenance and future extensions.