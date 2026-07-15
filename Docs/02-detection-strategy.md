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