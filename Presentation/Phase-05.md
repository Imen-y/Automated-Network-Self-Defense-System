# Phase 5 — Nmap Scan Detection and Correlated Automated Response

## 1. Objective

The objective of Phase 5 is to extend ANSDS from SSH attack detection to network reconnaissance detection.

The system detects common Nmap TCP scan techniques and correlates reconnaissance activity with subsequent SSH attack evidence.

The supported scan types are:

- TCP SYN Scan (`-sS`)
- TCP FIN Scan (`-sF`)
- TCP NULL Scan (`-sN`)
- TCP Xmas Scan (`-sX`)

---

## 2. Why Nmap Detection?

Network reconnaissance generally occurs before an attacker attempts to compromise a service.

Detecting scanning activity allows ANSDS to identify suspicious behavior earlier in the attack sequence.

The detection is based on network traffic captured directly with Scapy.

A single suspicious packet is not considered sufficient.

The detector analyses:

- Source IP
- Destination IP
- TCP flags
- Destination ports
- Number of distinct ports
- Detection time window

---

## 3. Nmap Scan Signatures

| Scan Type | Nmap Option | TCP Flags |
|-----------|-------------|-----------|
| SYN Scan | `-sS` | SYN |
| FIN Scan | `-sF` | FIN |
| NULL Scan | `-sN` | No flags |
| Xmas Scan | `-sX` | FIN + PSH + URG |

These signatures are identified directly from captured TCP packets.

---

## 4. Multi-Port Detection

The detector does not trigger an alert for a single packet.

It groups packets according to:

```text
Source IP
    +
Scan Type
    +
Multiple Destination Ports
    +
Short Time Window

The current detection parameters are:

Parameter	Value
Distinct Port Threshold	10
Detection Window	2 seconds

When the source contacts at least 10 distinct destination ports using the same scan signature within the detection window, an Nmap detection event is generated.

5. Detection Architecture
Kali Linux
    │
    │ Nmap Scan
    ▼
Network Traffic
    │
    ▼
Scapy
    │
    ▼
Nmap Detection Engine
    │
    ▼
NMAP_DETECTED

The Nmap detector is implemented as an independent detection module.

6. SSH Correlation

Nmap reconnaissance alone does not necessarily prove an intrusion attempt.

The detected source IP is therefore correlated with subsequent SSH attack evidence.

The correlation window is:

30 seconds

The resulting logic is:

NMAP_DETECTED
       ↓
Source IP stored
       ↓
SSH activity detected
       ↓
Same Source IP
       ↓
SSH_CORRELATION_CONFIRMED

This provides a second security indicator before the automated response is triggered.

7. Automated Response

Once the Nmap scan and SSH activity are correlated, ANSDS activates the existing response chain.

NMAP_DETECTED
       ↓
SSH_CORRELATION_CONFIRMED
       ↓
Telegram Alert
       ↓
Netmiko
       ↓
Cisco Router
       ↓
ANSDS-BLOCK ACL

The blocking rule is:

deny ip host <SOURCE_IP> any
8. Temporary Blocking

The Cisco blocking mechanism is temporary.

The configured blocking duration is:

60 seconds

The system automatically schedules the removal of the blocking rule.

IP_BLOCKED
     ↓
60-second Timer
     ↓
TEMPORARY_BLOCK_EXPIRED
     ↓
ACL Removed
     ↓
IP_UNBLOCKED

This prevents the attacker from remaining permanently blocked by a temporary security event.

9. Security Logging

Phase 5 introduces structured logging for the detection and response chain.

Important events include:

EVENT=NMAP_DETECTED
EVENT=SSH_CORRELATION_CONFIRMED
EVENT=TELEGRAM_ALERT_SENT
EVENT=IP_BLOCKED
EVENT=TEMPORARY_BLOCK_SCHEDULED
EVENT=TEMPORARY_BLOCK_EXPIRED
EVENT=IP_UNBLOCKED

The log provides a chronological trace of the complete security workflow.

10. Validation

The detection mechanism was tested using controlled Nmap scans from Kali Linux.

SYN Scan
nmap -sS -p 1-20 <TARGET_IP>
FIN Scan
nmap -sF -p 1-20 <TARGET_IP>
NULL Scan
nmap -sN -p 1-20 <TARGET_IP>
Xmas Scan
nmap -sX -p 1-20 <TARGET_IP>

The tests verified the identification of the different TCP scan signatures.

11. Correlation Validation

Two correlation scenarios were validated.

Nmap Only
Nmap Scan
    ↓
NMAP_DETECTED
    ↓
No SSH Correlation
    ↓
No Automated Response

This validates that reconnaissance alone does not immediately trigger the complete response chain.

Nmap + SSH Attack
Nmap Scan
    ↓
NMAP_DETECTED
    ↓
SSH Attack
    ↓
SSH_CORRELATION_CONFIRMED
    ↓
Telegram Alert
    ↓
Cisco Block

This validates the correlated attack detection mechanism.

12. Temporary Block Validation

After correlation confirmation, the Cisco router receives the dynamic ACL:

deny ip host 192.168.20.20 any

The system records:

EVENT=IP_BLOCKED
EVENT=TEMPORARY_BLOCK_SCHEDULED

After 60 seconds:

EVENT=TEMPORARY_BLOCK_EXPIRED
EVENT=IP_UNBLOCKED

The Cisco ACL is then removed automatically.

13. Phase 5 Result

Phase 5 extends the ANSDS architecture from SSH attack detection to earlier network reconnaissance detection.

The validated chain is:

Nmap Reconnaissance
        ↓
Scapy Detection
        ↓
Nmap Scan Classification
        ↓
Multi-Port Detection
        ↓
SSH Correlation
        ↓
Telegram Notification
        ↓
Cisco ACL
        ↓
Temporary Blocking
        ↓
Automatic Unblocking

The system can therefore detect reconnaissance activity, correlate it with SSH attack evidence, notify the administrator and automatically apply and remove a network-level blocking rule.