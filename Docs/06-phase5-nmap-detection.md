# Phase 5 — Nmap Scan Detection and Correlation

## 1. Objective

The objective of Phase 5 is to extend the ANSDS detection capabilities beyond SSH brute-force activity by detecting network reconnaissance performed through Nmap TCP scans.

The detection mechanism focuses on four common TCP scan techniques:

- SYN Scan (`-sS`)
- FIN Scan (`-sF`)
- NULL Scan (`-sN`)
- Xmas Scan (`-sX`)

The phase also introduces event correlation between Nmap reconnaissance activity and subsequent SSH activity.

The objective is therefore not only to detect reconnaissance, but to identify a potentially malicious attack sequence and automatically trigger the existing ANSDS response chain.

The resulting workflow is:

```text
Nmap Scan
    ↓
Scapy Packet Capture
    ↓
TCP Scan Classification
    ↓
Multi-Port Scan Detection
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

## 2. Security Motivation

Network reconnaissance is generally performed before an attacker attempts to access a service.

An attacker may first scan a target host to identify open or accessible ports and then focus subsequent attacks on the discovered services.

In the ANSDS architecture, detecting this reconnaissance phase provides an opportunity to identify suspicious activity earlier than an SSH authentication-based detection mechanism alone.

However, detecting a single TCP packet with an unusual flag combination is not sufficient to classify the traffic as an Nmap scan.

The detection mechanism therefore analyses repeated packets from the same source IP targeting multiple destination ports within a short time window.

## 3. Nmap Scan Types

### 3.1 SYN Scan

The SYN scan is performed using:

nmap -sS

The scanner sends TCP packets containing the SYN flag.

The observed TCP signature is:

SYN

The detector identifies repeated SYN packets targeting different destination ports as potential reconnaissance activity.

### 3.2 FIN Scan

The FIN scan is performed using:

nmap -sF

The scanner sends TCP packets containing the FIN flag.

The observed TCP signature is:

FIN

Repeated FIN packets targeting multiple destination ports can indicate FIN-based reconnaissance.

### 3.3 NULL Scan

The NULL scan is performed using:

nmap -sN

The scanner sends TCP packets without TCP flags.

The observed TCP signature is:

No TCP flags

A sequence of packets without TCP flags targeting multiple ports is therefore considered suspicious when observed within the configured detection window.

### 3.4 Xmas Scan

The Xmas scan is performed using:

nmap -sX

The scanner activates several TCP flags simultaneously.

The observed signature is:

FIN + PSH + URG

Repeated packets with this combination targeting multiple destination ports are considered potential Xmas scan activity.

## 4. Network Signatures

The four scan types are distinguished according to their TCP flag combinations.

Scan Type	  Nmap Option	  TCP Flags
SYN Scan	  -sS	          SYN
FIN Scan	  -sF	          FIN
NULL Scan	  -sN	          No flags
Xmas Scan	  -sX	          FIN + PSH + URG

The detector uses these signatures to classify captured TCP packets before evaluating whether they form a scanning pattern.

## 5. Detection principle

The Nmap detector is implemented using Scapy.

For each captured packet, the detector analyses the IP and TCP layers and extracts:

Source IP address
Destination IP address
TCP flags
Destination port
Packet timestamp

The detector groups packets according to their source IP and scan type.

A packet is not immediately considered an Nmap scan.

Instead, the detector tracks the number of distinct destination ports contacted by the same source using the same scan signature during a short time window.

The detection model is:

Same Source IP
        +
Same Scan Type
        +
Multiple Destination Ports
        +
Short Time Window
        ↓
NMAP_SCAN_DETECTED

This approach reduces the risk of classifying isolated TCP packets as reconnaissance activity.

## 6. Detection Parameters

The Phase 5 implementation uses the following detection parameters:

Parameter	                 Value
Protocol	                 TCP
Scan Types	               SYN, FIN, NULL, Xmas
Distinct Port              Threshold	10
Nmap Detection Window	     2 seconds
SSH Correlation Window	   30 seconds
Temporary Block Duration 	 60 seconds

The Nmap detection event is generated when the configured number of distinct destination ports is reached within the detection window.

## 7. Detection Workflow

The detector follows the following processing sequence.

Step 1 — Packet Capture

Scapy captures network packets from the monitored interface.

Step 2 — TCP Filtering

Only packets containing an IP layer and a TCP layer are considered.

Step 3 — TCP Flag Classification

The detector analyses the TCP flags to determine whether the packet corresponds to one of the supported scan signatures.

Step 4 — Source Identification

The source IP address is extracted from the packet.

Step 5 — Destination Port Tracking

The destination port is stored for the corresponding source IP and scan type.

Step 6 — Time Window Management

Only packets observed during the configured detection window are retained.

Older entries are removed from the detection state.

Step 7 — Distinct Port Counting

The detector counts the number of distinct destination ports contacted by the same source IP using the same scan signature.

Step 8 — Nmap Detection

When the configured threshold is reached, the detector generates an Nmap detection event.

The event contains information such as:

Source IP
Destination IP
Scan type
Number of distinct destination ports
Detection time window

## 8. False Positive Reduction

A single TCP packet is not sufficient to identify an Nmap scan.

For example, a legitimate network connection can generate individual TCP packets containing SYN or FIN flags.

The detector therefore requires a scanning pattern involving multiple destination ports.

The following conditions are considered together:

Source IP
+
Scan signature
+
Multiple destination ports
+
Short time window

This multi-packet approach reduces false positives caused by isolated legitimate traffic.

## 9. SSH Correlation

Nmap detection alone indicates reconnaissance activity, but it does not necessarily prove that the source is attempting to compromise the SSH service.

Phase 5 therefore introduces correlation between Nmap scan events and SSH activity.

The detector keeps the Nmap detection information for a correlation period.

If SSH attack evidence is observed from the same source IP during the configured correlation window, the system generates a confirmed security event.

The correlation workflow is:

NMAP_DETECTED
        ↓
Source IP stored
        ↓
SSH activity observed
        ↓
Same Source IP
        ↓
SSH correlation confirmed
        ↓
NMAP + SSH CORRELATED

The configured SSH correlation window is:

30 seconds

This allows the system to distinguish simple reconnaissance from reconnaissance followed by suspicious SSH activity.

## 10. Telegram Notification

Once the Nmap reconnaissance and SSH activity are correlated, the event is transmitted to the Telegram notification module.

The Telegram module is responsible only for notification.

The detector passes the relevant security information to the notification component.

The resulting workflow is:

Nmap Detection
      ↓
SSH Correlation
      ↓
Security Event
      ↓
Telegram Notification

The logging system records the notification event using:

EVENT=TELEGRAM_ALERT_SENT
## 11. Automatic Cisco Response

After the security event has been confirmed, the ANSDS system invokes the Cisco response module.

The Cisco module uses Netmiko to establish an SSH connection with the Cisco router.

The source IP identified during the detection process is then used to dynamically create an ACL rule.

The blocking rule follows the format:

deny ip host <SOURCE_IP> any

The ACL used by the system is:

ANSDS-BLOCK

The response workflow is:

Confirmed Security Event
        ↓
Netmiko
        ↓
Cisco Router
        ↓
ANSDS-BLOCK ACL
        ↓
deny ip host <SOURCE_IP> any
## 12. Temporary Blocking

The Phase 5 implementation introduces temporary blocking.

The objective is to prevent the attacker from continuing the activity while avoiding permanent modification of the router configuration.

When the source IP is blocked, the system schedules an automatic unblock operation.

The configured temporary blocking duration is:

60 seconds

The logging system records the scheduling operation as:

EVENT=TEMPORARY_BLOCK_SCHEDULED
## 13. Automatic Unblocking

After the temporary blocking period expires, the system automatically removes the corresponding ACL rule.

The system first identifies the temporary block associated with the source IP and then removes the Cisco ACL configuration.

The expiration event is recorded as:

EVENT=TEMPORARY_BLOCK_EXPIRED

The successful restoration of network access is recorded as:

EVENT=IP_UNBLOCKED

The complete mechanism is therefore:

Attack Confirmed
      ↓
IP Blocked
      ↓
60-second Timer
      ↓
Temporary Block Expired
      ↓
ACL Removed
      ↓
IP Unblocked
## 14. Security Event Logging

Phase 5 introduces structured security logging through the ANSDS logging module.

The log records the major events generated during the detection and response process.

Examples include:

EVENT=NMAP_DETECTED
EVENT=SSH_CORRELATION_CONFIRMED
EVENT=TELEGRAM_ALERT_SENT
EVENT=IP_BLOCKED
EVENT=TEMPORARY_BLOCK_SCHEDULED
EVENT=TEMPORARY_BLOCK_EXPIRED
EVENT=IP_UNBLOCKED

Each event contains contextual information such as the source IP, destination IP, scan type, number of distinct ports, time window, ACL and interface when applicable.

The log therefore provides a chronological record of the complete security response.

## 15. Experimental Validation

The Phase 5 implementation was validated using controlled Nmap scans generated from the Kali Linux machine.

The validation was performed for the four supported scan types.

15.1 SYN Scan Validation

The SYN scan was generated using:

nmap -sS -p 1-20 <TARGET_IP>

The detector identified the SYN packets targeting multiple destination ports and generated an Nmap detection event.

15.2 FIN Scan Validation

The FIN scan was generated using:

nmap -sF -p 1-20 <TARGET_IP>

The detector identified the FIN packet signature and tracked the contacted destination ports.

15.3 NULL Scan Validation

The NULL scan was generated using:

nmap -sN -p 1-20 <TARGET_IP>

The detector identified packets without TCP flags and evaluated their multi-port scanning behavior.

15.4 Xmas Scan Validation

The Xmas scan was generated using:

nmap -sX -p 1-20 <TARGET_IP>

The detector identified the FIN + PSH + URG TCP signature and evaluated the resulting scanning pattern.

15.5 Legitimate Traffic Validation

Legitimate TCP traffic was also observed to verify that isolated packets do not automatically trigger an Nmap detection event.

The objective of this experiment was to validate the multi-port and time-window conditions used by the detector.

15.6 Nmap Without SSH Correlation

An Nmap scan was executed without subsequent suspicious SSH activity.

This experiment validates that reconnaissance activity alone does not automatically produce the final correlated attack event.

The detector records the Nmap activity while waiting for the corresponding SSH evidence during the correlation window.

15.7 Nmap With SSH Correlation

A combined scenario was then executed in which Nmap reconnaissance was followed by suspicious SSH activity from the same source IP.

The system successfully correlated the two events.

The resulting sequence was:

NMAP_DETECTED
        ↓
SSH_CORRELATION_CONFIRMED
        ↓
TELEGRAM_ALERT_SENT
        ↓
IP_BLOCKED

This experiment validates the complete correlation mechanism.

15.8 Temporary Block Validation

After the security event was confirmed, the Cisco router received the dynamically generated ACL.

The system recorded:

EVENT=IP_BLOCKED

and:

EVENT=TEMPORARY_BLOCK_SCHEDULED

The ACL was verified directly on the Cisco router.

15.9 Automatic Unblock Validation

After the configured temporary blocking period expired, the system automatically removed the ACL.

The system recorded:

EVENT=TEMPORARY_BLOCK_EXPIRED

followed by:

EVENT=IP_UNBLOCKED

This confirmed that the router configuration was automatically restored after the temporary response period.

## 16. Experimental Results

The Phase 5 experiments demonstrate that the ANSDS architecture can detect several types of network reconnaissance and correlate this activity with subsequent SSH attack evidence.

The validation confirmed the following capabilities:

SYN scan detection
FIN scan detection
NULL scan detection
Xmas scan detection
Multi-port scanning analysis
Time-window based detection
SSH correlation
Telegram security notification
Dynamic Cisco ACL creation
Temporary IP blocking
Automatic ACL removal
Security event logging

The resulting architecture provides an earlier detection point than SSH authentication monitoring alone while maintaining the existing automated response mechanism developed during the previous phases.

## 17. Phase 5 Architecture

The complete Phase 5 architecture can be represented as follows:

                    Attacker
                       │
                       ▼
                 Nmap Scanning
                       │
                       ▼
                Scapy Packet Capture
                       │
                       ▼
              TCP Flag Classification
                       │
                       ▼
             Multi-Port Detection
                       │
                       ▼
                NMAP_DETECTED
                       │
                       ▼
                SSH Correlation
                       │
              ┌────────┴────────┐
              │                 │
        No correlation    Correlation confirmed
              │                 │
              │                 ▼
              │          Telegram Alert
              │                 │
              │                 ▼
              │          Netmiko / Cisco
              │                 │
              │                 ▼
              │          ANSDS-BLOCK ACL
              │                 │
              │                 ▼
              │         Temporary Blocking
              │                 │
              │                 ▼
              │         Automatic Unblock
              │
              ▼
        Continue Monitoring
## 18. Conclusion

Phase 5 extends the ANSDS system from SSH attack detection toward broader network reconnaissance detection.

The implementation identifies SYN, FIN, NULL and Xmas scan signatures using Scapy and evaluates their behavior across multiple destination ports within a short time window.

The introduction of SSH correlation provides an additional security indicator by distinguishing reconnaissance activity from reconnaissance followed by suspicious SSH behavior.

Once the correlation is confirmed, the existing ANSDS response chain is activated. The system sends a Telegram notification, dynamically creates a Cisco ACL through Netmiko, temporarily blocks the source IP and automatically removes the blocking rule after the configured period.

The resulting architecture provides a complete detection, correlation, notification and automated response workflow while maintaining the modular design of the ANSDS project.