# Automated Network Self-Defense System (ANSDS)

> Automated detection and response system for SSH attacks using Python, Scapy, Netmiko and Cisco IOS.

---

## Project Overview

This project was developed during my engineering internship.

The objective is to build an Automated Network Self-Defense System capable of detecting malicious SSH connection attempts, sending real-time alerts and automatically isolating attackers using Cisco network automation.

Unlike traditional demonstrations, the project combines:

- Network Administration
- Python Automation
- Network Security
- Cisco IOS
- Network Monitoring
- Security Automation (SOAR concepts)

---

## Architecture

```
                    Internet
                        │
                    GNS3 NAT
                        │
                 Cisco Router (R1)
               Fa1/0           Fa0/0
                 WAN             LAN
                                 │
                              Switch
                          ┌──────┴──────┐
                          │             │
                 Ubuntu Server      Kali Linux
                    Victim          Attacker
```

---

## Project Workflow

```
Attacker

↓

SSH SYN Flood / Brute Force

↓

Scapy detects abnormal SYN packets

↓

Python Detection Engine

↓

Telegram Notification

↓

Netmiko

↓

Cisco Router

↓

Automatic ACL Injection

↓

Attacker Blocked
```

---

## Technologies

| Category | Technology |
|----------|------------|
| Network Simulation | GNS3 |
| Router | Cisco IOS |
| Operating System | Ubuntu Server 24.04 |
| Attacker | Kali Linux |
| Programming Language | Python 3 |
| Packet Analysis | Scapy |
| Network Automation | Netmiko |
| Notifications | Telegram Bot API |
| Version Control | Git & GitHub |
| Documentation | LaTeX |

---

## Current Progress

- [x] Network Topology
- [x] Cisco Router Configuration
- [x] Ubuntu Server Configuration
- [x] Kali Linux Configuration
- [x] NAT / Internet Access
- [x] SSH Server Deployment
- [ ] Packet Sniffing with Scapy
- [ ] SYN Detection Engine
- [ ] Telegram Alert
- [ ] Automatic Blocking using Netmiko
- [ ] Final Demonstration

---

## Repository Structure

```
Automated-Network-Self-Defense-System/

│
├── Docs/
├── GNS3/
├── Report/
├── Screenshots/
├── Scripts/
│
├── README.md
└── .gitignore
```

---

## Screenshots

(Images will be added during the project.)

---

## Future Improvements

- Suricata integration
- Snort rule comparison
- Grafana dashboard
- ELK integration
- Multi-router support

---

## Author

Engineering Internship Project

2026