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
| Phase 2 | SSH Traffic Analysis | Completed |
| Phase 3 | Telegram Notification System | Completed |
| Phase 4 | Cisco Automatic Response | Completed |
| Phase 5 | Advanced Attack Detection | Completed |
| Phase 6 | System Integration | Planned |
| Phase 7 | Final Validation | Planned |

---

## System Architecture

```
                    Network Traffic
                          │
                          ▼
                  Scapy Packet Capture
                          │
                          ▼
                Attack Detection Engine
                          │
             ┌────────────┴────────────┐
             │                         │
        SSH Detection            Nmap Scan Detection
             │                         │
             └────────────┬────────────┘
                          ▼
                  Attack Validation
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
       Telegram Alert          Netmiko Response
                                      │
                                      ▼
                                Cisco Router
                                      │
                                      ▼
                                    ACL
                                      │
                                      ▼
                              Attacker Blocked
```

---

## Project Structure

```text
Automated-Network-Self-Defense-System/

├── Docs/
├── GNS3/
├── Presentation/
├── Report/
├── Resources/
├── Scripts/
│   ├── Cisco/
│   │   └── cisco_acl_manager.py
│   ├── Detection/
│   │   ├── nmap_detector.py
│   │   └── ssh_detector.py
│   ├── Logging/
│   │   └── ansds_logger.py
│   └── Telegram/
│       └── telegram_notifier.py
├── README.md
└── .gitignore
```

---

## Technologies

- Python
- Scapy
- Requests
- Telegram Bot API
- Netmiko
- Cisco IOS
- GNS3
- Wireshark
- Nmap
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
- Cisco router automation
- Dynamic ACL-based attacker blocking
- Netmiko-based network device control
- Nmap scan detection
- SYN scan detection
- FIN scan detection
- NULL scan detection
- Xmas scan detection
- Advanced attack detection

---

## Upcoming Features

- Complete ANSDS integration
- Correlation of multiple detection indicators
- Extended attack detection
- Complete system validation

---

## Project Context

This project was developed as part of an engineering internship.

Automated Network Self-Defense System (ANSDS)

The Automated Network Self-Defense System (ANSDS) is an engineering internship project designed to automatically detect SSH brute-force attacks, notify the network administrator in real time, and automatically respond by blocking malicious hosts on a Cisco router.