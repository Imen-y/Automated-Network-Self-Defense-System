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