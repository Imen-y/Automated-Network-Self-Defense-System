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