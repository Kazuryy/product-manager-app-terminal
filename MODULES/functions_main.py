import pandas as pd
import os
import sys
sys.path.append("menu_pro")
from menu_pro import main
import hashlib
import requests




path_user="DATA/utilisateurs.csv"
path_product="DATA/products.csv"
path_rocku="DATA/rocku.csv"
utilisateur_connecte = None


#_Creation_____________________________________________________
#_______________________________________________________________
def creation():

    if os.path.exists(path_user):
        print("Données utilisateurs trouvées 🫡")
    else:
        df=pd.DataFrame(columns=["Id", "Nom","Prenom","Login","Password"])
        df.to_csv(path_user, index=False)


    if os.path.exists(path_product):
        print("Données produits trouvées 🫡")
    else:
        df=pd.DataFrame(columns=["Name","Price","Quantity", "Id"])
        df.to_csv(path_product, index=False)





#_RockUwU_____________________________________________________
#_______________________________________________________________

#creation du fichier si no.exist
#connexion avec api have i been pwned
#ajout si mot de passe compromis

def creation_rocku():
    if os.path.exists(path_rocku):
        print("Données RockU trouvées 🫡")
    else:
        print("Le fichier RockU n'a pas été trouvé.")





#_Connexion_____________________________________________________
#_______________________________________________________________




def hashed_input(password: str) -> str:
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()




def recherche_user(username, password):
    df = pd.read_csv(path_user) # Données de la base de données sur les utilisateurs

    hashed_pw_input=hashed_input(password)
    user = df[(df['Login'] == username) & (df['Password'] == hashed_pw_input)]
    if check_info_in_file(hashed_pw_input) == True:
        print("❌ -> Ce mot de passe est compromis. Veuillez en choisir un autre.")
        modifier_utilisateur(username, password)
    elif check_password_pwned(password) == True:
        print("❌ -> Ce mot de passe est compromis. Veuillez en choisir un autre.")
        modifier_utilisateur(username, password)
    if not user.empty:
        id_user = user.iloc[0]['Id']
        main(id_user)
    else:
        print("❌ -> Erreur : Utilisateur non trouvé")




def connexion():
    print('\nVeuillez renseigner tous les champs de connexion')
    username = str(input('Login: '))
    password = str(input('Password: '))
    recherche_user(username, password)





def modifier_utilisateur(login, password):
    try:
        df = pd.read_csv(path_user)

        hashed_pw = hashed_input(password)

        # Recherche de l'utilisateur
        user_row = df[(df['Login'] == login) & (df['Password'] == hashed_pw)]
        
        if not user_row.empty:
            id_user = user_row['Id'].values[0]
            
            input_nom = str(input('Nom: '))
            input_prenom = str(input('Prenom: '))
            input_login = str(input('Login: '))
            input_password = str(input('Password: '))

            hashed_pw_input = hashed_input(input_password)
            if check_info_in_file(hashed_pw_input) == True:
                print("❌ -> Ce mot de passe est compromis. Veuillez en choisir un autre.")
                return
            
            if check_password_pwned(input_password) == True:
                print("Mot de passe compromis 😬, utilisez un autre mot de passe 😉")
                return

            # Mise à jour des informations de l'utilisateur
            df.loc[df['Id'] == id_user, 'Nom'] = input_nom
            df.loc[df['Id'] == id_user, 'Prenom'] = input_prenom
            df.loc[df['Id'] == id_user, 'Login'] = input_login
            df.loc[df['Id'] == id_user, 'Password'] = hashed_pw_input

            df.to_csv(path_user, index=False)
            print("✅ -> Utilisateur modifié avec succès.")
        else:
            print("❌ -> Utilisateur non trouvé")
        
    except FileNotFoundError:
        print("Fichier non trouvé")
        return



#_Inscription__________________________________________________
#______________________________________________________________




def inscription_ajout(nom, prenom, login, password): 
    
    df = pd.read_csv(path_user)
    
    # Vérifier si la colonne ID existe, sinon l'ajouter
    if 'Id' not in df.columns:
        df['Id'] = range(1, len(df) + 1)
    
    if login in df['Login'].values:
        print(f"❌ -> Le login '{login}' existe déjà. Veuillez en choisir un autre.")
        return
    
    # Calculer le nouvel ID
    new_id = df['Id'].max() + 1 if not df.empty else 1
    hashed_pw = hashed_input(password)
    if check_info_in_file(hashed_pw) == True:
        print("❌ -> Ce mot de passe est compromis. Veuillez en choisir un autre.")
        return
    
    if check_password_pwned(password) == True:
        print("❌ -> Ce mot de passe est compromis. Veuillez en choisir un autre.")
        return
    
    else:
        hashed_pw = hashed_input(password)
        ligne = pd.DataFrame({"Id": [new_id], "Nom": [nom], "Prenom": [prenom], "Login": [login], "Password": [hashed_pw]})
        print("\nNouvelle ligne à ajouter:")
        print(ligne)
    
        df = pd.concat([df, ligne], ignore_index=True)
    
        df.to_csv(path_user, index=False)
        print("Fichier mis à jour avec succès. 🫡")




def inscription():
    print('\nVeuillez renseigner tous les champs de connexion')
    nom=str(input('Nom:'))
    prenom=str(input('Prenom:'))
    login=str(input('Login:'))
    password=str(input('Password:'))

    inscription_ajout(nom, prenom, login, password)




#_Suppression_Compte___________________________________________
#______________________________________________________________

def delete_account():
    confirmation = input(" 🚨 Are you sure you want to delete your account?\n| YES ✅ |\n| NO  ❌ |\nChoice:")

    if confirmation.lower() in ['yes', 'y']:
        input_login = input('🧔‍♂️ Identifiant: ')
        input_password = input('🔑 Mot de passe: ')

        # Charger les utilisateurs
        df_users = pd.read_csv(path_user)
        hashed_pw = hashed_input(input_password)

        # Trouver l'utilisateur correspondant
        user_row = df_users[(df_users['Login'] == input_login) & (df_users['Password'] == hashed_pw)]
        if not user_row.empty:
            id_user = user_row['Id'].values[0]

            # Charger les produits et supprimer ceux de l'utilisateur
            df_products = pd.read_csv(path_product)
            if id_user in df_products['Id'].values:
                df_products = df_products[df_products['Id'] != id_user]
                df_products.to_csv(path_product, index=False)
                print("\n✅ -> Produits supprimés avec succès 🫡")

            # Supprimer l'utilisateur
            df_users = df_users[df_users['Id'] != id_user]
            df_users.to_csv(path_user, index=False)
            print("✅ -> Utilisateur supprimé avec succès 🫡")
        else:
            print("❌ Identifiant ou mot de passe incorrect.")

    else:
        print("❌ Suppression annulée.")



#_Mot_de_passe_compromis_______________________________________
#______________________________________________________________

def check_info_in_file(password):
    try:
        df = pd.read_csv(path_rocku, encoding='utf-8')
        if password in df.values:
            print(f"Information found: {password}")
            return True
        else:
            print("Information not found in the file.")
            return False
    except FileNotFoundError:
        print(f"The file {path_rocku} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")



def check_password_pwned(password: str) -> bool:
    """Vérifie si un mot de passe est compromis via Have I Been Pwned."""
    
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]  # Les 5 premiers caractères du hash
    suffix = sha1_hash[5:]  # Le reste du hash

    # Appeler l'API de HIBP
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Erreur lors de la requête à l'API HIBP : {response.status_code}")

    # Vérifier si le suffixe est dans la réponse
    hashes = response.text.splitlines()
    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            print(f"😨 Mot de passe compromis ! Trouvé {count} fois. Veulliez en choisir un autre 💡.")
            return True

    print("✅ Mot de passe sûr. Pas trouvé dans les bases de données compromises.")
    return False