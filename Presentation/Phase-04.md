# Phase 4 — Cisco Automatic Response with Netmiko

---

# Objective

Integrate an automatic Cisco response module into the Automated Network Self-Defense System (ANSDS) to automatically block malicious IP addresses detected by the SSH detection engine.

The Cisco module is designed to remain independent from the detection and notification modules while providing reusable network response capabilities.

---

# Motivation

Detecting an attack and notifying the administrator are essential steps, but they do not actively protect the network.

A complete automated self-defense system must be capable of immediately applying a security countermeasure after detecting an attack.

Cisco Access Control Lists (ACLs) provide an efficient mechanism for automatically blocking malicious traffic at the network infrastructure level.

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
Telegram Notification
    │
    ▼
Cisco Response Module
    │
    ▼
Cisco Router
    │
    ▼
Dynamic ACL
```

---

# Implemented Components

- Cisco SSH configuration
- Netmiko installation
- SSH connectivity validation
- Cisco automation module (`cisco_acl_manager.py`)
- Dynamic ACL creation
- Dynamic ACL removal
- Secure environment variables (`.env`)
- Complete exception handling
- Integration with the SSH detection engine

---

# Cisco Response Workflow

```
SSH Attack

        │

        ▼

Scapy Detection

        │

        ▼

Telegram Notification

        │

        ▼

Netmiko SSH Connection

        │

        ▼

Dynamic ACL Creation

        │

        ▼

Automatic IP Blocking
```

---

# Cisco Automation Module

The developed module provides:

- Router SSH connection
- Cisco IOS command execution
- Dynamic ACL creation
- Dynamic ACL removal
- Secure credential management
- Robust exception handling

The module remains fully reusable for future project extensions.

---

# Exception Handling

To improve system robustness, all Netmiko operations are protected using:

- `try`
- `except`
- `finally`

The module correctly handles:

- Connection timeout
- Authentication failure
- Unexpected runtime errors

The SSH session is always closed properly, even when an exception occurs.

---

# Experimental Validation

The Cisco response module was validated through multiple experiments.

The validation confirmed:

- SSH connectivity
- Router information retrieval
- Dynamic ACL creation
- Dynamic ACL removal
- Exception handling
- Complete integration with the SSH detection engine

---

# Results

The developed subsystem is capable of:

- automatically connecting to the Cisco router;
- creating dynamic ACLs;
- removing ACLs when required;
- protecting the application against communication failures;
- automatically blocking detected attackers.

---

# Phase Outcome

The Automated Network Self-Defense System now supports:

```
SSH Detection

        │

        ▼

Telegram Notification

        │

        ▼

Cisco Automatic Response

        │

        ▼

Dynamic ACL Blocking
```

The complete detection and automatic response chain is now fully operational.

---

# Next Phase

The objectives of Phase 5 will be defined after the supervisor's review and recommendations.

The next development stage will extend the ANSDS architecture while preserving its modular, reusable and maintainable design.