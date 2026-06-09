# Supervision-Réseau

## Présentation

Ce projet a été réalisé dans le cadre d'un TP Git, GitHub, Fork, Pull Request et GitHub Actions.

L'objectif est de mettre en place une plateforme collaborative permettant de centraliser :

* les scripts d'administration ;
* les configurations réseau ;
* les sauvegardes ;
* la documentation technique ;
* les automatisations GitHub Actions.

---

## Structure du projet

```text
supervision-reseau/
├── .github/
│   └── workflows/
│       └── test.yml
│
├── Scripts/
│   ├── scan_ports.py
│   └── sauvegarde.py
│
├── Configurations/
│   ├── switch_cisco.txt
│   └── firewall.txt
│
├── Documentations/
│   ├── procedure_installation_SSH.md
│   └── procedure_installation_DNS.md
│
├── sauvegardes/
│
└── README.md
```

---

## Fonctionnalités

### Scan de ports

Le script `scan_ports.py` permet :

* de saisir une adresse IP ou un nom de serveur ;
* de tester les ports :

  * 22 (SSH)
  * 80 (HTTP)
  * 443 (HTTPS)
  * 3306 (MySQL)

Le résultat indique si chaque port est ouvert ou fermé.

---

### Sauvegarde automatique

Le script `sauvegarde.py` :

* copie les fichiers de configuration ;
* crée automatiquement le dossier `sauvegardes` si nécessaire ;
* ajoute la date du jour au nom des fichiers ;
* affiche un message de confirmation après chaque sauvegarde.

---

## GitHub Actions

Le workflow GitHub Actions exécute automatiquement une validation lors :

* d'un Push ;
* d'une Pull Request.

Message affiché :

Validation du projet supervision-reseau

---

## Technologies utilisées

* Git
* GitHub
* GitHub Actions
* Python 3
* Socket
* Shutil
* Datetime

---

## Auteur

Yves Arnaud KOFFI
TP AIS - GESTION D'UNE INFRASTRUCTURE RESEAU AVEC GitHub
