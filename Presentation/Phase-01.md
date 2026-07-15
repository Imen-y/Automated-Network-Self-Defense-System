# Phase 01 – Infrastructure réseau

---

# Objectif

Concevoir une infrastructure réseau stable et réaliste servant de base au développement du projet **Automated Network Self-Defense System (ANSDS)**.

Cette plateforme doit permettre de reproduire des scénarios d'attaque SSH dans un environnement entièrement contrôlé.

---

# Travail réalisé

## Conception de la topologie

- Création du laboratoire sous GNS3
- Intégration d'un routeur Cisco IOS
- Intégration d'un commutateur Cisco
- Déploiement d'un serveur Ubuntu
- Déploiement d'une machine Kali Linux
- Mise en place d'un accès Internet

---

## Configuration réseau

- Configuration des interfaces Cisco
- Configuration des adresses IP statiques
- Configuration des passerelles
- Mise en place du routage
- Configuration du NAT

---

## Validation

- Validation de la connectivité Internet
- Validation des communications ICMP
- Installation d'OpenSSH Server
- Vérification du service SSH
- Vérification du port TCP 22
- Validation d'une connexion SSH entre Kali Linux et Ubuntu

---

# Difficultés rencontrées

- Configuration des interfaces Cisco sous GNS3
- Mise en place du NAT
- Configuration réseau des machines virtuelles
- Validation complète des communications
- Installation et configuration du serveur OpenSSH

---

# Solutions apportées

- Vérification progressive de chaque équipement
- Tests de connectivité après chaque configuration
- Validation du routage avant l'installation des services
- Utilisation des commandes de diagnostic Cisco et Linux
- Vérification systématique des services réseau

---

# Résultats obtenus

- Infrastructure réseau entièrement fonctionnelle
- Communications validées entre tous les équipements
- Accès Internet opérationnel
- Service SSH fonctionnel
- Plateforme prête pour l'analyse du trafic réseau

---

# Compétences acquises

## Réseaux

- Conception d'une topologie réseau
- Configuration Cisco IOS
- Configuration NAT
- Routage IP
- Plan d'adressage

## Systèmes

- Configuration Ubuntu Server
- Configuration Kali Linux
- Installation d'OpenSSH
- Administration Linux

## Outils

- GNS3
- Cisco IOS
- VMware
- SSH

---

# Livrables de la Phase 01

- Topologie GNS3
- Infrastructure réseau opérationnelle
- Documentation technique
- Rapport LaTeX (Chapitre 2)
- Captures de validation
- Dépôt GitHub mis à jour

---

# Transition

La phase suivante portera sur l'analyse détaillée du trafic SSH à l'aide de Wireshark afin d'identifier les caractéristiques des connexions normales et des futures attaques.