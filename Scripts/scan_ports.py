import socket

# Demande à l'utilisateur une adresse IP ou un nom de serveur
serveur = input("Entrez une adresse IP ou un nom de serveur : ")

# Liste des ports à tester
ports = [22, 80, 443, 3306]

# Parcours de chaque port
for port in ports:

    # Création d'une socket TCP
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Temps d'attente maximal
    connexion.settimeout(2)

    # Test de connexion au port
    resultat = connexion.connect_ex((serveur, port))

    # Affichage du résultat
    if resultat == 0:
        print(f"Port {port} : ouvert")
    else:
        print(f"Port {port} : fermé")

    # Fermeture de la connexion
    connexion.close()