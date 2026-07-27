# Useful Commands

## Cisco IOS

### Save configuration

```cisco
write memory
```

---

### Display interfaces

```cisco
show ip interface brief
```

---

### Display routing table

```cisco
show ip route
```

---

### Display NAT translations

```cisco
show ip nat translations
```

---

### Display NAT configuration

```cisco
show running-config | section ip nat
```

---

## Ubuntu Server

### Update package list

```bash
sudo apt update
```

---

### Install OpenSSH Server

```bash
sudo apt install openssh-server -y
```

---

### Verify SSH packages

```bash
dpkg -l | grep openssh
```

---

### Check SSH status

```bash
systemctl status ssh
```

or

```bash
systemctl status ssh.socket
```

---

### Verify port 22

```bash
ss -tln | grep :22
```

---

### Display routing table

```bash
ip route
```

---

### Display DNS configuration

```bash
cat /etc/resolv.conf
```

---

## Network Tests

### Ping router

```bash
ping 192.168.10.1
```

---

### Ping Ubuntu

```bash
ping 192.168.10.10
```

---

### Ping Kali

```bash
ping 192.168.10.20
```

---

### Test Internet connectivity

```bash
ping 8.8.8.8
```

---

## SSH

### Connect from Kali

```bash
ssh imen@192.168.10.10
```

---

## Git

### Check repository status

```bash
git status
```

---

### Stage all files

```bash
git add .
```

---

### Commit

```bash
git commit -m "Commit message"
```

---

### Push

```bash
git push
```

---

### View history

```bash
git log --oneline
```

---

# Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Scapy Installation

```bash
pip install scapy
```

---

# Detector Execution

```bash
sudo ./venv/bin/python ssh_detector.py
```

---

# SSH Test

```bash
ssh imen@192.168.10.10
```

---

# SSH Brute Force Simulation

```bash
for i in {1..10}; do
    timeout 1 ssh imen@192.168.10.10 exit >/dev/null 2>&1 &
done
wait
```

# Telegram

## Create a Bot

/newbot

## Retrieve Bot Token

/token

## Start Conversation

/start

---

# Python

Install Requests

```bash
pip install requests
```

Verify Installation

```bash
pip show requests
```

Run Telegram Test

```bash
python test_telegram.py
```

Run SSH Detector

```bash
sudo $(which python) ssh_detector.py
```

---

# Network Testing

SSH Brute Force Simulation

```bash
for i in {1..15}; do
    nc -z 192.168.10.10 22
done
```

# ===========================
# Phase 4 - Netmiko
# ===========================

# Install Netmiko
pip install netmiko

# Verify installation
pip show netmiko

# Validate SSH connectivity
python test_netmiko.py

# Create a dynamic ACL
python test_acl.py

# Remove the ACL
python test_remove_acl.py

# ===========================
# Cisco IOS
# ===========================

show running-config | include hostname

show version | include Cisco IOS

show ip interface brief

show access-lists