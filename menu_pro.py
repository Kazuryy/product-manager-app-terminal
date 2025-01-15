import pandas as pd
import sys
sys.path.append("MODULES/funtions_pro")
from MODULES.functions_pro import ajout, read, delete_produit, search, edit_product, sort, personalisation

def menu_product():
    print('\nMenu')
    print('1: Ajout de produits')
    print('2: Modifier des produits')
    print('3: Ouvrir le fichier')
    print('4: Supprimer des produits')
    print('5: Rechercher un produit')
    print('6: Trier')
    print('7: Quitter\n')




def main(id_user):
    index_user = id_user
    personalisation(index_user)
    while True:
        menu_product()
        choix = int(input('Veuillez saissir votre choix:'))
        if choix == 1:
            print('\nAjout de produits 📦')
            ajout(index_user)

        elif choix == 2:
            print('\nModification des produits 🛠️')
            edit_product(index_user)
            
        elif choix == 3:
            print('Liste des produits 📜')
            read(index_user)
            
        elif choix == 4:
            print('Suppression de produits 🗑️')
            delete_produit(index_user)

        elif choix == 5:
            print("Recherche d'un produit 🔍")
            search(index_user)

        elif choix == 6:
            print('Trier les produits 📊')
            sort(index_user)

        elif choix == 7:
            print('Déconnexion -> 🚪')
            break
        else:
            print('Choix invalide 😬')
