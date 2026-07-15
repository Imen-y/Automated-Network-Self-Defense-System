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