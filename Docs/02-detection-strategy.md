# SSH Attack Detection Strategy

## Objective

Detect malicious SSH activities while minimizing false positives.

---

# Initial Idea

The first idea was to detect TCP SYN packets targeting port 22 (SSH).

Advantages:

- Early detection.
- Network-based analysis.
- Similar approach to IDS solutions such as Snort and Suricata.
- Detection before SSH authentication starts.

---

# Discussion with the Supervisor

The proposed approach was validated as technically relevant.

However, detecting a single TCP SYN packet is not sufficient because every legitimate SSH connection also starts with a TCP SYN packet.

To reduce false positives, the detection should evolve by combining multiple indicators.

---

# Detection Roadmap

## Version 1

Simple and functional implementation.

Detection

↓

Telegram Notification

↓

Automatic Cisco Blocking

Objective:

Validate the complete automation chain.

---

## Version 2

Improve the detection engine.

Possible improvements:

- Detect multiple TCP SYN packets within a short time window.
- Detect abnormal SSH connection rates.
- Detect Nmap scans.
- Correlate TCP SYN activity with SSH authentication logs.
- Reduce false positives.

---

# Final Strategy

The project will first deliver a complete working solution.

Once the entire automation chain has been validated, the detection algorithm will be progressively improved using multiple correlated indicators.

This incremental approach was recommended by the project supervisor.

---

# SSH Detection Engine

## Objective

Develop the first intrusion detection component capable of identifying repeated SSH connection attempts before integrating automated response mechanisms.

---

## Detection Principle

The detection engine is implemented using the Scapy packet manipulation framework.

Instead of analyzing SSH authentication logs, the detector observes network traffic directly and identifies TCP SYN packets targeting the SSH service (TCP port 22).

This approach allows the system to detect suspicious activity before the SSH authentication phase.

---

## Detection Algorithm

For each captured packet:

1. Capture packets from the network interface.
2. Keep only TCP packets.
3. Select packets targeting TCP destination port 22.
4. Detect TCP SYN packets.
5. Associate each SYN packet with its source IP address.
6. Store the packet timestamp.
7. Remove timestamps older than ten seconds.
8. Count remaining attempts.
9. Generate an alert when the number of attempts reaches the configured threshold.

---

## Detection Parameters

| Parameter | Value |
|-----------|-------|
| Protocol | TCP |
| Destination Port | 22 |
| Detection Event | TCP SYN |
| Time Window | 10 seconds |
| Alert Threshold | 5 attempts |

---

## Advantages

- Early detection before authentication
- Lightweight packet inspection
- Real-time monitoring
- Simple integration with automated response modules

---

# Telegram Notification Strategy

## Objective

The objective of this phase is to automatically notify the administrator immediately after an SSH brute-force attack has been detected.

The notification module is completely independent from the detection engine.

## Architecture

```
Attacker
        │
        ▼
TCP SYN Packets
        │
        ▼
Scapy Packet Capture
        │
        ▼
SSH Detection Engine
        │
        ▼
telegram_notifier.py
        │
        ▼
Telegram API
        │
        ▼
Telegram Bot
```

## Detection Workflow

1. Capture TCP SYN packets.
2. Count attempts for each source IP.
3. Apply the sliding time window.
4. Compare the number of attempts against the configured threshold.
5. Generate a professional alert.
6. Send the alert through Telegram.

## Alert Information

Each Telegram notification includes:

- Attack Type
- Severity
- Date
- Time
- Source IP
- Destination IP
- Destination Port
- Protocol
- Number of Attempts
- Time Window
- Detection Status

This information will be reused during the Cisco automatic response phase.

# Phase 4 – Automated Cisco Response

The ANSDS architecture was extended by introducing an automatic response module based on Netmiko.

The complete workflow is now:

Attacker
↓
Scapy
↓
SSH Detection
↓
Telegram Notification
↓
Netmiko
↓
Cisco Router
↓
Dynamic ACL

After Scapy detects an SSH brute-force attack, the attacker information is forwarded to the Telegram notification module.

Once the notification has been sent successfully, the Cisco module establishes an SSH connection with the router and dynamically creates an Access Control List (ACL) to immediately block the attacker.

The blocking rule follows the format:

deny ip host <SOURCE_IP> any

The Cisco module remains fully reusable and independent from the detection engine.

## Phase 5 — Nmap Scan Detection Strategy

### Objective

Phase 5 extends the ANSDS detection capabilities from SSH attack detection to network reconnaissance detection.

The objective is to identify common Nmap TCP scan techniques before a possible intrusion attempt and correlate reconnaissance activity with subsequent SSH authentication failures.

The four supported scan types are:

- TCP SYN Scan (`-sS`)
- TCP FIN Scan (`-sF`)
- TCP NULL Scan (`-sN`)
- TCP Xmas Scan (`-sX`)

The complete detection and response chain is:

```text
Nmap Scan
    ↓
Scapy Packet Capture
    ↓
TCP Scan Classification
    ↓
Multi-Port Detection
    ↓
SSH Correlation
    ↓
Telegram Alert
    ↓
Cisco ACL
    ↓
Temporary Block
    ↓
Automatic Unblock

Nmap Scan Identification

The detector identifies Nmap scans according to their TCP flag signatures.

Scan Type	Nmap Option	TCP Flags
SYN Scan	-sS	SYN
FIN Scan	-sF	FIN
NULL Scan	-sN	No flags
Xmas Scan	-sX	FIN + PSH + URG

The TCP flags are extracted using Scapy and compared with the expected signatures.

A packet that does not match one of the supported scan signatures is ignored by the Nmap detection mechanism.

Detection Principle

A single TCP packet is not considered sufficient evidence of an Nmap scan.

The detector analyses repeated packets originating from the same source IP and using the same scan signature.

The detection criteria are:

Same Source IP
        +
Same Scan Type
        +
Multiple Distinct Destination Ports
        +
Short Time Window
        ↓
NMAP_DETECTED

This approach reduces false positives caused by isolated legitimate TCP packets.

Detection Parameters

The implemented Nmap detection mechanism uses:

Parameter	Value
Protocol	TCP
Scan Types	SYN, FIN, NULL, Xmas
Distinct Port Threshold	10
Detection Window	2 seconds

The detector maintains a sliding window for each source IP and scan type.

Only packets observed inside the configured detection window are retained.

The detector then counts the distinct destination ports contacted by the source IP.

When the number of distinct destination ports reaches the configured threshold, an Nmap detection event is generated.

Detection Workflow

For each captured packet, the detector performs the following operations:

Capture the packet using Scapy.
Verify that the packet contains IP and TCP layers.
Extract the source IP address.
Extract the destination IP address.
Analyse the TCP flags.
Identify the corresponding scan type.
Store the destination port and timestamp.
Remove packets older than the detection window.
Count the distinct destination ports.
Generate an Nmap detection event when the threshold is reached.

The detection event contains:

Source IP
Destination IP
Scan type
Number of distinct destination ports
Detection window
SSH Correlation

Nmap reconnaissance alone does not necessarily indicate an attempt to compromise the target.

Phase 5 therefore introduces correlation between Nmap reconnaissance and SSH authentication activity.

After an Nmap scan is detected, the source IP is temporarily stored as a pending security event.

The detector then searches for SSH authentication failures generated by the same source IP.

The correlation logic is:

NMAP_DETECTED
        ↓
Source IP stored
        ↓
SSH authentication activity
        ↓
Same Source IP
        ↓
SSH correlation confirmed
        ↓
NMAP + SSH CORRELATED

The correlation mechanism provides an additional indicator of malicious intent and reduces the possibility of reacting to reconnaissance activity alone.

Correlated Security Response

Once Nmap reconnaissance and SSH authentication failures are correlated, the system activates the existing ANSDS response chain.

The response sequence is:

NMAP + SSH CORRELATED
        ↓
Telegram Notification
        ↓
Cisco Response
        ↓
Dynamic ACL
        ↓
Temporary IP Block

The Telegram notification contains the main information related to the detected security event, including the source IP, destination IP, scan type and correlation status.

Dynamic Cisco Response

After the correlated event is confirmed, the source IP is transmitted to the Cisco response module.

The Cisco module uses Netmiko to establish an SSH connection with the router and dynamically creates the blocking rule:

deny ip host <SOURCE_IP> any

The ACL used for the ANSDS response is:

ANSDS-BLOCK

This allows the system to transform the detection event into an automatic network-level response.

Temporary Blocking

The Phase 5 response mechanism uses temporary IP blocking rather than leaving the attacker permanently blocked.

After the ACL is applied, the system schedules an automatic unblock operation.

The configured temporary blocking duration is:

60 seconds

The temporary response follows:

IP BLOCKED
    ↓
60-second Timer
    ↓
Temporary Block Expired
    ↓
ACL Removed
    ↓
IP Unblocked

This mechanism allows the system to restore the network state automatically after the response period.

Security Logging

Phase 5 also introduces structured logging for the main detection and response events.

The logging mechanism records events such as:

EVENT=NMAP_DETECTED
EVENT=SSH_CORRELATION_CONFIRMED
EVENT=TELEGRAM_ALERT_SENT
EVENT=IP_BLOCKED
EVENT=TEMPORARY_BLOCK_SCHEDULED
EVENT=TEMPORARY_BLOCK_EXPIRED
EVENT=IP_UNBLOCKED

The log provides a chronological record of the detection, correlation and automated response process.

False Positive Considerations

The detector does not classify an isolated TCP packet as an Nmap scan.

Instead, detection requires a combination of:

Source IP
Scan type
Multiple destination ports
Short detection window

The additional SSH correlation step provides another layer of validation before the automated response is triggered.

This multi-stage approach is designed to distinguish isolated legitimate traffic from reconnaissance followed by suspicious authentication activity.

Phase 5 Validation

The implementation was validated using controlled Nmap scans generated from Kali Linux.

The following scan types were tested:

SYN Scan
FIN Scan
NULL Scan
Xmas Scan

Additional scenarios were also validated:

Legitimate traffic
Nmap reconnaissance without SSH correlation
Nmap reconnaissance followed by SSH authentication failures
Telegram notification
Dynamic Cisco ACL creation
Temporary IP blocking
Automatic ACL removal
Security event logging

The validation confirms the complete detection and response workflow:

Nmap Reconnaissance
        ↓
Nmap Detection
        ↓
SSH Correlation
        ↓
Security Alert
        ↓
Cisco Blocking
        ↓
Temporary Response
        ↓
Automatic Unblocking
Implementation Status

The Nmap detection mechanism is implemented as an independent detection component within the ANSDS architecture.

The implementation uses:

Scapy for packet capture and TCP analysis
Python for detection logic
SSH authentication logs for correlation
Telegram for security notification
Netmiko for Cisco automation
Cisco ACL for network-level blocking
ANSDS logging for event traceability

The resulting architecture preserves the modular design established during the previous phases while extending the detection capabilities of the system to the reconnaissance stage of an attack.