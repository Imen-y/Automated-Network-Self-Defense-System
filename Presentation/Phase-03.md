# Phase 3 — Telegram Notification System

---

# Objective

Integrate a Telegram notification subsystem into the Automated Network Self-Defense System (ANSDS) to automatically notify the administrator whenever an SSH brute-force attack is detected.

The notification module is designed to be independent from the SSH detection engine and reusable by future project components.

---

# Motivation

Detecting an attack is only the first step of an automated defense system.

A real self-defense architecture must immediately inform the administrator before executing any automatic response.

Telegram provides a simple, reliable and real-time communication channel through its official Bot API.

---

# Phase Architecture

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
Telegram Bot
```

---

# Implemented Components

- Telegram Bot creation
- Bot Token retrieval
- Chat ID retrieval
- Telegram API communication
- Reusable Python notification module
- Integration with the SSH detection engine
- Automatic security notifications

---

# Notification Workflow

```
TCP SYN Packet

        │

        ▼

Scapy Detection

        │

        ▼

Threshold Verification

        │

        ▼

Alert Generation

        │

        ▼

Telegram Notification
```

---

# Professional Alert Content

Each notification contains:

- Attack Type
- Severity
- Date
- Time
- Source IP
- Destination IP
- Destination Port
- Protocol
- Number of Attempts
- Detection Time Window
- Detection Status

---

# Experimental Validation

The notification subsystem was validated using multiple SSH brute-force simulations generated from the Kali Linux machine.

The detector successfully:

- captured TCP SYN packets;
- counted SSH attempts;
- detected the configured threshold;
- generated an alert;
- transmitted the notification through Telegram.

---

# Results

The developed subsystem is capable of:

- automatically notifying the administrator;
- providing structured security information;
- preparing the data required for Cisco automatic response.

---

# Phase Outcome

The Automated Network Self-Defense System now supports:

```
SSH Detection

        │

        ▼

Automatic Telegram Notification
```

The notification subsystem is fully operational and ready to be integrated with the Cisco automatic response module.

---

# Next Phase

Phase 4 — Cisco Automatic Response

Objectives:

- Install Netmiko.
- Connect to the Cisco router.
- Generate Access Control Lists (ACLs).
- Automatically block malicious IP addresses.
- Validate the complete automated response workflow.