# Procédure de configuration SSH

## Objectif

Permettre l'administration sécurisée à distance d'un serveur Linux via le protocole SSH.

## Installation du serveur SSH

Sous Debian ou Ubuntu :

```bash
sudo apt update
sudo apt install openssh-server -y
```

## Vérification du service

```bash
sudo systemctl status ssh
```

## Démarrage du service

```bash
sudo systemctl start ssh
sudo systemctl enable ssh
```

## Vérification de l'écoute du port 22

```bash
sudo ss -tlnp | grep 22
```

## Connexion depuis un client

```bash
ssh utilisateur@adresse_ip
```

Exemple :

```bash
ssh admin@192.168.10.10
```

## Bonnes pratiques

* Utiliser des mots de passe robustes.
* Privilégier l'authentification par clé SSH.
* Limiter les accès administrateurs.
* Mettre à jour régulièrement le serveur.
