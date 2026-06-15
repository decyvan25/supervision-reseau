import shutil
import os
from datetime import datetime

# Récupération de la date du jour au format AAAA-MM-JJ
date_jour = datetime.now().strftime("%Y-%m-%d")

# Dossier de destination des sauvegardes
dossier_sauvegarde = "sauvegardes"

# Création du dossier de sauvegarde s'il n'existe pas
if not os.path.exists(dossier_sauvegarde):
    os.makedirs(dossier_sauvegarde)

# Liste des fichiers de configuration à sauvegarder
fichiers = [
    "Configurations/switch_cisco.txt",
    "Configurations/firewall.txt"
]

# Copie de chaque fichier dans le dossier sauvegardes
for fichier in fichiers:

    # Récupération du nom du fichier
    nom_fichier = os.path.basename(fichier)

    # Suppression de l'extension .txt
    nom_sans_extension = os.path.splitext(nom_fichier)[0]

    # Création du nom du fichier sauvegardé avec la date du jour
    destination = f"{dossier_sauvegarde}/{nom_sans_extension}_{date_jour}.txt"

    # Copie du fichier source vers le fichier de sauvegarde
    shutil.copy(fichier, destination)

    # Message de confirmation
    print(f"Sauvegarde créée : {destination}")