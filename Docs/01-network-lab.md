# Network Laboratory

## Objective

Build a realistic laboratory environment capable of simulating SSH attacks and validating an automated response system.

---

# Laboratory Architecture

```
                    Internet
                        │
                    GNS3 NAT
                        │
                FastEthernet1/0
                  Cisco Router
                FastEthernet0/0
                        │
                     Switch
                  ┌─────┴─────┐
                  │           │
          Ubuntu Server    Kali Linux
             Victim         Attacker
```

---

# Devices

## Cisco Router

Role:

- Default gateway
- Internet access (NAT/PAT)
- Future ACL deployment
- Future Netmiko automation

---

## Ubuntu Server

Role:

Victim machine.

Services:

- OpenSSH Server

IP Address:

192.168.10.10/24

Default Gateway:

192.168.10.1

---

## Kali Linux

Role:

Attacker machine.

Future tools:

- Hydra
- Nmap
- Wireshark

IP Address:

192.168.10.20/24

Default Gateway:

192.168.10.1

---

# Network

LAN

192.168.10.0/24

Gateway

192.168.10.1

WAN

Obtained automatically through DHCP using GNS3 NAT.

---

# Internet Access

Implemented using:

- GNS3 NAT
- Cisco PAT (NAT Overload)

---

# SSH

Target service:

OpenSSH Server

Listening Port:

TCP 22

Current Status:

Operational

---

# Validation

Completed tests:

- Ubuntu → Router
- Kali → Router
- Ubuntu → Kali
- Kali → Ubuntu
- SSH connection from Kali to Ubuntu

Result:

The laboratory is fully operational and ready for the attack detection phase.

# Phase 4 – Cisco Automatic Response with Netmiko

## SSH Access to the Cisco Router

Before implementing the automatic response mechanism, the Cisco router was configured to accept SSH connections.

The following validations were successfully completed:

- SSH service enabled on the Cisco router.
- Local user account created for remote authentication.
- RSA key pair generated.
- SSH Version 2 enabled.
- Successful SSH connection from the Ubuntu Server to the Cisco router.

This validated that the router was ready to accept remote management connections through Netmiko.

---

## Netmiko Connectivity Validation

A first Python test script (`test_netmiko.py`) was developed to verify SSH communication with the Cisco router.

The script successfully retrieved:

- Router hostname
- Cisco IOS version
- Interface information

This validation confirmed that Python could remotely manage the Cisco IOS device.