from scapy.all import sniff, IP, TCP
import time

# -----------------------------
# Configuration
# -----------------------------
SSH_PORT = 22
THRESHOLD = 5          # Maximum SYN packets allowed
TIME_WINDOW = 10       # Time window in seconds

# Dictionary:
# Key   -> Source IP
# Value -> List of timestamps for detected SYN packets
attempts = {}


def packet_callback(packet):
    """
    Process each captured packet.
    Detect repeated TCP SYN packets targeting the SSH service.
    """

    # Verify that the packet contains IP and TCP layers
    if not (packet.haslayer(IP) and packet.haslayer(TCP)):
        return

    ip_src = packet[IP].src
    ip_dst = packet[IP].dst
    tcp = packet[TCP]

    # Detect only TCP SYN packets sent to SSH
    if tcp.dport != SSH_PORT or tcp.flags != "S":
        return

    current_time = time.time()

    # Create entry for a new source IP
    if ip_src not in attempts:
        attempts[ip_src] = []

    # Store timestamp
    attempts[ip_src].append(current_time)

    # Keep only timestamps inside the time window
    attempts[ip_src] = [
        t for t in attempts[ip_src]
        if current_time - t <= TIME_WINDOW
    ]

    count = len(attempts[ip_src])

    print(
        f"[SSH SYN] {ip_src} -> {ip_dst} | "
        f"Attempts (last {TIME_WINDOW}s): {count}"
    )

    # Trigger alert if threshold is reached
    if count >= THRESHOLD:

        print("=" * 60)
        print("[ALERT] Possible SSH Brute Force detected!")
        print(f"Source IP   : {ip_src}")
        print(f"Destination : {ip_dst}")
        print(f"Attempts    : {count}")
        print(f"Time Window : {TIME_WINDOW} seconds")
        print("=" * 60)


print("[*] Starting packet capture...")

sniff(
    iface="ens33",
    filter="tcp port 22",
    prn=packet_callback,
    store=False
)