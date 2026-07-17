# Phase 02 – Développement du moteur de détection SSH

---

# Objectif

Développer le premier moteur de détection du projet **Automated Network Self-Defense System (ANSDS)** capable d'identifier automatiquement des comportements suspects visant le service SSH.

Cette phase consiste à exploiter la bibliothèque **Scapy** afin d'analyser le trafic réseau en temps réel, de détecter les paquets TCP SYN destinés au port SSH, puis d'identifier les tentatives répétées pouvant correspondre au début d'une attaque par force brute.

---

# Travail réalisé

## Préparation de l'environnement

- Installation de Python 3
- Création d'un environnement virtuel Python
- Installation de la bibliothèque Scapy
- Validation de la capture réseau

---

## Développement du détecteur

- Création du script `ssh_detector.py`
- Capture des paquets réseau avec Scapy
- Filtrage du trafic SSH (TCP port 22)
- Détection des paquets TCP SYN
- Identification des adresses IP sources
- Comptage des tentatives de connexion
- Implémentation d'un seuil de détection
- Mise en place d'une fenêtre temporelle glissante

---

## Validation

- Validation de la capture réseau
- Validation du filtrage SSH
- Validation de la détection des paquets SYN
- Validation du compteur de connexions
- Validation du seuil d'alerte
- Validation de la fenêtre temporelle
- Simulation d'une attaque SSH par connexions répétées

---

# Difficultés rencontrées

- Installation de Scapy sous Ubuntu
- Gestion de l'environnement virtuel Python
- Sélection de l'interface réseau appropriée
- Débogage de la fonction de capture Scapy
- Amélioration de la logique de comptage

---

# Solutions apportées

- Utilisation d'un environnement virtuel Python
- Identification de l'interface réseau `ens33`
- Filtrage BPF sur le port TCP 22
- Validation progressive de chaque fonctionnalité
- Remplacement du compteur cumulatif par une fenêtre temporelle glissante

---

# Résultats obtenus

- Détecteur SSH entièrement opérationnel
- Capture réseau en temps réel
- Détection des paquets TCP SYN
- Comptage des tentatives par adresse IP
- Détection automatique après dépassement du seuil
- Réduction des faux positifs grâce à la fenêtre temporelle

---

# Compétences acquises

## Programmation

- Python
- Scapy
- Structures de données
- Développement incrémental

## Réseaux

- Analyse de paquets
- TCP/IP
- TCP SYN
- Berkeley Packet Filter (BPF)

## Cybersécurité

- Détection d'intrusion
- Détection d'attaque SSH
- Analyse comportementale
- Détection de force brute

---

# Livrables de la Phase 02

- Script `Scripts/ssh_detector.py`
- Documentation technique mise à jour
- Rapport LaTeX (Chapitre 3)
- Captures de validation
- Dépôt GitHub mis à jour

---

# Transition

La phase suivante sera consacrée à l'intégration des mécanismes de notification ainsi qu'à l'automatisation de la réponse aux attaques détectées. Le détecteur Scapy sera enrichi afin d'envoyer des alertes via Telegram avant d'interagir avec le routeur Cisco pour appliquer automatiquement des règles de blocage.