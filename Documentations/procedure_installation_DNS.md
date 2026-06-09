# Procédure de configuration DNS

## Objectif

Mettre en place un service DNS permettant la résolution de noms dans le réseau.

## Installation du serveur DNS

Sous Debian ou Ubuntu :

```bash
sudo apt update
sudo apt install bind9 -y
```

## Vérification du service

```bash
sudo systemctl status bind9
```

## Fichier principal de configuration

```bash
sudo nano /etc/bind/named.conf.local
```

## Exemple de zone directe

```text
zone "entreprise.local" {
    type master;
    file "/etc/bind/db.entreprise.local";
};
```

## Redémarrage du service

```bash
sudo systemctl restart bind9
```

## Vérification

Depuis un client :

```bash
nslookup serveur.entreprise.local
```

ou

```bash
dig serveur.entreprise.local
```

## Bonnes pratiques

* Sauvegarder les fichiers de configuration.
* Documenter les zones DNS.
* Contrôler régulièrement les journaux du service.
