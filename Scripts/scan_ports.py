import socket

serveur = input("Entrez une adresse IP ou un nom de serveur : ")

ports = [22, 80, 443, 3306]

for port in ports:
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion.settimeout(2)

    resultat = connexion.connect_ex((serveur, port))

    if resultat == 0:
        print(f"Port {port} : ouvert")
    else:
        print(f"Port {port} : fermé")

    connexion.close()