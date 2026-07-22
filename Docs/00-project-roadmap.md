# Automated Network Self-Defense System (ANSDS)

## Project Goal

Design and implement an Automated Network Self-Defense System (ANSDS) capable of detecting SSH brute-force attacks, notifying the administrator in real time through Telegram, and automatically blocking malicious hosts on a Cisco router using Netmiko and Access Control Lists (ACLs).

The project follows a modular architecture to ensure scalability, maintainability, and ease of future development.

---

# Development Methodology

Each project phase follows the same workflow:

1. Technical implementation
2. Technical validation
3. Screenshots
4. Documentation
5. LaTeX report
6. GitHub version
7. Presentation version
8. Git commit
9. GitHub push
10. Next phase prompt generation

No phase is considered complete until all ten steps have been successfully completed.

---

# Project Roadmap

## Phase 1 — Network Infrastructure ✅

### Objectives

- Build the GNS3 laboratory.
- Configure the Cisco router.
- Configure the Cisco switch.
- Configure Ubuntu Server.
- Configure Kali Linux.
- Configure NAT connectivity.
- Deploy the OpenSSH server.
- Validate end-to-end connectivity.

### Deliverables

- Complete laboratory topology.
- Functional network infrastructure.
- SSH connectivity successfully validated.

**Status:** Completed

---

## Phase 2 — SSH Detection Engine ✅

### Objectives

- Analyze the SSH protocol using Wireshark.
- Study the TCP Three-Way Handshake.
- Identify exploitable TCP header fields.
- Install Python and Scapy.
- Capture SSH packets.
- Detect TCP SYN packets.
- Count SSH connection attempts.
- Implement threshold-based detection.
- Implement a 10-second sliding time window.
- Validate the detection engine.

### Deliverables

- Functional SSH detection engine.
- Automatic TCP SYN detection.
- Threshold-based SSH brute-force detection.

**Status:** Completed

---

## Phase 3 — Telegram Notifications ✅

### Objectives

- Create a Telegram Bot.
- Retrieve the Bot Token.
- Retrieve the Chat ID.
- Develop a reusable Telegram notification module.
- Integrate the Telegram module into the SSH detection engine.
- Generate professional security alerts.
- Automatically notify the administrator after attack detection.

### Deliverables

- telegram_notifier.py
- test_telegram.py
- Updated ssh_detector.py
- Professional Telegram security alerts.

**Status:** Completed

---

## Phase 4 — Cisco Automatic Response

### Objectives

- Install and configure Netmiko.
- Connect securely to the Cisco router.
- Generate Access Control Lists (ACLs).
- Automatically block malicious source IP addresses.
- Validate automatic network response.

### Expected Deliverables

- Cisco automation module.
- Automatic ACL deployment.
- Successful attacker isolation.

**Status:** Planned

---

## Phase 5 — Detection Improvements

### Objectives

- Correlate TCP SYN detection with SSH authentication logs.
- Reduce false positives.
- Improve alert quality.
- Enhance detection reliability.

### Expected Deliverables

- Hybrid detection engine.
- Improved detection accuracy.

**Status:** Planned

---

## Phase 6 — Final System Integration

### Objectives

- Integrate all ANSDS modules.
- Validate the complete automated defense workflow.
- Perform end-to-end testing.
- Evaluate overall system performance.

### Expected Deliverables

- Fully integrated Automated Network Self-Defense System.

**Status:** Planned

---

## Phase 7 — Final Validation

### Objectives

- Execute complete attack scenarios.
- Perform functional validation.
- Perform technical validation.
- Finalize project documentation.
- Prepare the final demonstration.

### Expected Deliverables

- Fully validated ANSDS.
- Final project ready for presentation and deployment.

**Status:** Planned

---

# Current Project Status

| Phase | Title | Status |
|--------|------------------------------|-----------|
| 1 | Network Infrastructure | Completed |
| 2 | SSH Detection Engine | Completed |
| 3 | Telegram Notifications | Completed |
| 4 | Cisco Automatic Response | Planned |
| 5 | Detection Improvements | Planned |
| 6 | Final System Integration | Planned |
| 7 | Final Validation | Planned |

---

# Final System Architecture

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
Automatic ACL Deployment
    │
    ▼
Automated Network Self-Defense System (ANSDS)
```