# Automated Network Self-Defense System (ANSDS)

## Overview

The Automated Network Self-Defense System (ANSDS) is a final-year engineering project designed to automatically detect SSH brute-force attacks, notify the network administrator in real time, and automatically respond by blocking malicious hosts on a Cisco router.

The project is developed progressively using a modular architecture, allowing each component to be validated independently before system integration.

---

## Project Objectives

- Detect SSH brute-force attacks.
- Analyze network traffic using Scapy.
- Send real-time security notifications through Telegram.
- Automatically block attackers using Cisco ACLs and Netmiko.
- Build a complete automated network self-defense chain.

---

## Current Project Status

| Phase | Description | Status |
|--------|-------------|--------|
| Phase 1 | Network Infrastructure | Completed |
| Phase 2 | SSH Detection Engine | Completed |
| Phase 3 | Telegram Notification System | Completed |
| Phase 4 | Cisco Automatic Response | Planned |
| Phase 5 | Detection Improvements | Planned |
| Phase 6 | System Integration | Planned |
| Phase 7 | Final Validation | Planned |

---

## System Architecture

```
Attacker
    │
    ▼
Scapy Packet Capture
    │
    ▼
SSH Detection Engine
    │
    ▼
Telegram Notification Module
    │
    ▼
Netmiko Automation
    │
    ▼
Cisco Router
    │
    ▼
Access Control List (ACL)
    │
    ▼
Automated Network Self-Defense System
```

---

## Project Structure

```
Automated-Network-Self-Defense-System/

├── Docs/
├── GNS3/
├── Presentation/
├── Report/
├── Resources/
├── Scripts/
│   ├── Detection/
│   └── Telegram/
├── README.md
└── .gitignore
```

---

## Technologies

- Python
- Scapy
- Requests
- Telegram Bot API
- Netmiko (planned)
- Cisco IOS
- GNS3
- Ubuntu Server
- Kali Linux
- Git
- LaTeX

---

## Completed Features

- Network laboratory deployment
- SSH protocol analysis
- TCP SYN detection
- Sliding time window
- Threshold-based SSH brute-force detection
- Telegram Bot integration
- Automatic security notifications
- Modular notification subsystem

---

## Upcoming Features

- Cisco router automation
- Automatic ACL generation
- Dynamic attacker blocking
- Hybrid detection improvements
- Complete ANSDS integration

---

## Author

Final-Year Engineering Project

Automated Network Self-Defense System (ANSDS)