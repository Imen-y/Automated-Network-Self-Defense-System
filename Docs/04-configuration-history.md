# Configuration History

This document contains every configuration performed during the project.

Configurations are recorded chronologically.

---

# Cisco Router Configuration

## LAN Interface

```cisco
enable

configure terminal

interface FastEthernet0/0

ip address 192.168.10.1 255.255.255.0

no shutdown

exit
```

---

## WAN Interface

```cisco
configure terminal

interface FastEthernet1/0

ip address dhcp

no shutdown

exit
```

---

## NAT Configuration

```cisco
configure terminal

interface FastEthernet0/0
 ip nat inside
 exit

interface FastEthernet1/0
 ip nat outside
 exit

access-list 1 permit 192.168.10.0 0.0.0.255

ip nat inside source list 1 interface FastEthernet1/0 overload

end

write memory
```

---

# Ubuntu Server Configuration

## Netplan

```yaml
network:
  version: 2
  renderer: networkd

  ethernets:
    ens4:
      dhcp4: no
      addresses:
        - 192.168.10.10/24
      routes:
        - to: default
          via: 192.168.10.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 1.1.1.1
```

Apply configuration

```bash
sudo netplan apply
```

---

## OpenSSH Server

Install

```bash
sudo apt update

sudo apt install openssh-server -y
```

Verification

```bash
dpkg -l | grep openssh

systemctl status ssh.socket

ss -tln | grep :22
```

---

# Kali Linux Configuration

Configure static IP

```bash
nmcli connection modify "Wired connection 1" \
ipv4.addresses 192.168.10.20/24 \
ipv4.gateway 192.168.10.1 \
ipv4.dns "8.8.8.8 1.1.1.1" \
ipv4.method manual

nmcli connection down "Wired connection 1"

nmcli connection up "Wired connection 1"
```

---

# Network Validation

Ubuntu

```bash
ping 192.168.10.1

ping 192.168.10.20
```

Kali

```bash
ping 192.168.10.1

ping 192.168.10.10
```

SSH

```bash
ssh imen@192.168.10.10
```

---

# Git

Repository initialization

```bash
git init

git branch -M main

git remote add origin <repository-url>
```

First commit

```bash
git add .

git commit -m "Initialize project structure and complete network infrastructure"

git push -u origin main
```

---

# Phase 03 Configuration

Operating System:
- Ubuntu Server 24.04 LTS

Python:
- Python 3.12

Virtual Environment:
- Python venv

Packet Library:
- Scapy 2.7.0

Monitored Interface:
- ens33

Detection Port:
- TCP 22

Detection Threshold:
- 5 SYN packets

Sliding Time Window:
- 10 seconds

# Phase 3 Configuration History

## Telegram Bot

- Telegram Bot created using BotFather.
- Bot Token generated.
- Chat ID retrieved.

---

## Python Environment

- requests installed inside the virtual environment.

---

## Telegram Module

Created:

- telegram_notifier.py

Functions:

- send_notification()

---

## SSH Detector

Integrated Telegram notifications.

Detection pipeline:

TCP SYN Detection

↓

Threshold Verification

↓

Professional Alert Generation

↓

Telegram Notification

---

## Final Parameters

SSH Port

22

Threshold

5 attempts

Sliding Time Window

10 seconds

Notification

Automatic

# Phase 4 Configuration Changes

## New directory

Scripts/Cisco/

## New modules

- cisco_acl_manager.py
- test_netmiko.py
- test_acl.py
- test_remove_acl.py

## New environment variables

ROUTER_HOST
ROUTER_USERNAME
ROUTER_PASSWORD

## Security Improvements

- Cisco credentials moved to the .env file.
- Added .env.example for GitHub.
- Added requirements.txt.
- Added complete Netmiko exception handling.
- Integrated Cisco automatic response into ssh_detector.py.