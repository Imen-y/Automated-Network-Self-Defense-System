from datetime import datetime, timedelta

from scapy.all import IP, TCP, sniff

from Scripts.Telegram.telegram_notifier import send_notification
from Scripts.Cisco.cisco_acl_manager import block_ip

# -----------------------------
# Configuration
# -----------------------------
SSH_PORT = 22
THRESHOLD = 5
TIME_WINDOW = 10

# Dictionary:
# Key   -> Source IP
# Value -> List of timestamps
attempts = {}


def packet_callback(packet):
    """
    Process captured packets and detect SSH brute-force attempts.
    """

    # Verify IP and TCP layers
    if not (packet.haslayer(IP) and packet.haslayer(TCP)):
        return

    ip_src = packet[IP].src
    ip_dst = packet[IP].dst
    tcp = packet[TCP]

    # Detect only TCP SYN packets targeting SSH
    if tcp.dport != SSH_PORT or tcp.flags != "S":
        return

    current_time = datetime.now()

    # Create an entry for a new source IP
    if ip_src not in attempts:
        attempts[ip_src] = []

    # Store current timestamp
    attempts[ip_src].append(current_time)

    # Keep only timestamps inside the time window
    attempts[ip_src] = [
        timestamp
        for timestamp in attempts[ip_src]
        if current_time - timestamp <= timedelta(seconds=TIME_WINDOW)
    ]

    count = len(attempts[ip_src])

    print(
        f"[SSH SYN] {ip_src} -> {ip_dst} | "
        f"Attempts (last {TIME_WINDOW}s): {count}"
    )

    # Trigger alert only once when the threshold is reached
    if count == THRESHOLD:

        alert_message = f"""
==================================================
               ANSDS SECURITY ALERT
==================================================

Attack Type      : SSH Brute Force

Severity         : HIGH

Date             : {current_time.strftime('%Y-%m-%d')}
Time             : {current_time.strftime('%H:%M:%S')}

Source IP        : {ip_src}
Destination IP   : {ip_dst}

Destination Port : {SSH_PORT}
Protocol         : TCP

Attempts         : {count}
Time Window      : {TIME_WINDOW} seconds

Status           : Detection threshold reached

==================================================
"""

        print("=" * 60)
        print("SSH Brute Force detected!")

        if send_notification(alert_message):
            print("[+] Telegram notification sent successfully.")

            block_ip(ip_src)

        else:
            print("[-] Failed to send Telegram notification.")

        print("=" * 60)


print("[*] Starting packet capture...")

sniff(
    iface="ens33",
    filter=f"tcp port {SSH_PORT}",
    prn=packet_callback,
    store=False
)