import sys
import time
sys.path.append("MODULES/funtions_main")
from MODULES.functions_main import  creation, creation_rocku, connexion, inscription, modifier_utilisateur, delete_account


def menu_login():
    while True:
        print('Menu')
        print('|1. Connexion|')
        print('|2. Inscription|')
        print('|3. Modification de compte|')
        print('|4. Suppression de compte|')
        print('|5. Quitter|')

        choix = input('Veuillez saissir votre choix:')
        
        if int(choix) == 1:
            print('Connexion 🔑')
            connexion()
            time.sleep(1)
            
        
        elif int(choix) == 2:
            print('Inscription 📝')
            inscription()
            time.sleep(1)
        
        elif int(choix) == 3:
            print('Modification de compte 🛠️')
            print('Veuillez rensiegner votre identifiant et mot de passe:')
            login = str(input('🧔‍♂️ Identifiant:'))
            password = input(('🔑 Mot de passe:'))
            modifier_utilisateur(login, password)
            time.sleep(1)
        
        elif int(choix) == 4:
            print('Suppression de compte 🗑️')
            print('Veuillez rensiegner votre identifiant et votre mot de passe:\n')
            delete_account()
        
        elif int(choix) == 5:
            print('Au revoir 👋')
            break
        else:
            print('Choix invalide 😬')

creation()
creation_rocku()
menu_login()
