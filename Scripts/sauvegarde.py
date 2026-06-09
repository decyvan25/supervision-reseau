import shutil
import os
from datetime import datetime

date_jour = datetime.now().strftime("%Y-%m-%d")

dossier_sauvegarde = "sauvegardes"

if not os.path.exists(dossier_sauvegarde):
    os.makedirs(dossier_sauvegarde)

fichiers = [
    "Configurations/switch_cisco.txt",
    "Configurations/firewall.txt"
]

for fichier in fichiers:
    nom_fichier = os.path.basename(fichier)
    nom_sans_extension = os.path.splitext(nom_fichier)[0]
    destination = f"{dossier_sauvegarde}/{nom_sans_extension}_{date_jour}.txt"

    shutil.copy(fichier, destination)
    print(f"Sauvegarde créée : {destination}")