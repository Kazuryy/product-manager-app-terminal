import pandas as pd
path='DATA/products.csv'
path_user="DATA/utilisateurs.csv"


def ajout(index_user):
    try:
        name = str(input('Nom du produit'))
        price = str(input('Prix du produit'))
        quantity = str(input('Quantité du produit'))
        
        df = pd.read_csv(path)
        ligne=pd.DataFrame({"Name":[name],"Price":[price],"Quantity":[quantity], "Id": [index_user]}) # Ajouter en fonction de l'utilisateur
        df= pd.concat([df,ligne], ignore_index=True)
        df.to_csv(path, index=False)
        print("\n✅ -> Produit ajouté avec succès 🫡")
    except FileNotFoundError:
        print("\n❌ -> Erreur : le fichier n'a pas été trouvé.")

def read(index_user):
    try:
        df=pd.read_csv(path)
        df=df[df['Id']==index_user]
        print(df)
    except FileNotFoundError:
        print("❌ -> Erreur : le fichier n'a pas été trouvé.")
    except PermissionError:
        print("❌ -> Erreur : permissions insuffisantes pour ouvrir le fichier.")
    except Exception as e: 
        print(f"❌ -> Erreur inattendue : {e}")

def delete_produit(index_user):
    try:
        input_nom = str(input("Nom du produit à supprimer : "))
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(path)
        
        # Check if the product exists and remove it
        if input_nom in df['Name'].values and index_user in df['Id'].values:
            df = df[~((df['Name'] == input_nom) & (df['Id'] == index_user))] # Expliquer cette ligne
            
            # Write the updated DataFrame back to the CSV file
            df.to_csv(path, index=False)
            print("\n✅ -> Produit supprimé avec succès 🫡")
        else:
            print("\n❌ -> Produit non trouvé")
    
    except FileNotFoundError:
        print("❌ -> Erreur : Le fichier 'produits.csv' n'existe pas.")
    except PermissionError:
        print("❌ -> Erreur : Vous n'avez pas les permissions nécessaires")
    except Exception as e:
        print(f"❌ -> Une erreur s'est produite : {e}")

def search(index_user):
    try:
        input_nom = str(input("Nom du produit à rechercher : "))
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(path)
        
        # Check if the product exists and display it
        if input_nom in df['Name'].values and index_user in df['Id'].values:
            result = df[(df['Name'] == input_nom) & (df['Id'] == index_user)]
            if not result.empty:
                print("\n✅ -> Produit trouvé :")
                print(result)
            else:
                print("\n❌ -> Produit non trouvé")
        else:
            print("\n❌ -> Produit non trouvé")
    
    except FileNotFoundError:
        print("❌ -> Erreur : Le fichier 'produits.csv' n'existe pas.")
    except PermissionError:
        print("❌ -> Erreur : Vous n'avez pas les permissions nécessaires")
    except Exception as e:
        print(f"❌ -> Une erreur s'est produite : {e}")


def personalisation(index_user):
    df = pd.read_csv(path_user)
    if index_user in df['Id'].values:
        nom_user = df.loc[df['Id'] == index_user, 'Nom'].values[0]
        prenom_user = df.loc[df['Id'] == index_user, 'Prenom'].values[0]
        print(f"\n👤 -> Bienvenue dans votre espace vendeur {prenom_user} {nom_user}! 😁")
    
    else:
        print("Erreur Identification.")

def sort(index_user):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(path)
        
        choix = int(input("Trier:\n| (1) par nom 🪪|\n| (2) par prix 💲|\n| (3) par quantité 📊|"))
        # Sort the DataFrame by the 'Name' column
        if choix == 1:
            df = df.sort_values(by='Name', ascending=True)
        elif choix == 2:
            df = df.sort_values(by='Price', ascending=True)
        elif choix == 3:
            df = df.sort_values(by='Quantity', ascending=True)
        else:
            print("❌ -> Erreur : Choix invalide 😬")
            return
        
        # Write the sorted DataFrame back to the CSV file
        df.to_csv(path, index=False)
        read(index_user)
        print("\n✅ -> Produits triés avec succès 🫡")
    
    except FileNotFoundError:
        print("❌ -> Erreur : Le fichier 'produits.csv' n'existe pas.")
    except PermissionError:
        print("❌ -> Erreur : Vous n'avez pas les permissions nécessaires")
    except Exception as e:
        print(f"❌ -> Une erreur s'est produite : {e}")



def edit_product(index_user):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(path)
        
        # Ask the user for the product name to edit
        input_nom = str(input("Nom du produit à modifier : "))
        
        # Check if the product exists and edit it
        if input_nom in df['Name'].values and index_user in df['Id'].values:
            result = df[(df['Name'] == input_nom) & (df['Id'] == index_user)]
            if not result.empty:
                print("\nProduit trouvé :")
                print(result)
                
                # Ask the user for the new product information
                new_name = str(input("Nouveau nom du produit : "))
                new_price = float(input("Nouveau prix du produit : "))
                new_quantity = int(input("Nouvelle quantité du produit : "))
                
                # Update the product information
                df.loc[(df['Name'] == input_nom) & (df['Id'] == index_user), 'Price'] = new_price
                df.loc[(df['Name'] == input_nom) & (df['Id'] == index_user), 'Quantity'] = new_quantity
                df.loc[(df['Name'] == input_nom) & (df['Id'] == index_user), 'Name']  = new_name
                
                # Write the updated DataFrame back to the CSV file
                df.to_csv(path, index=False)
                print("\n✅ -> Produit modifié avec succès 🫡")
            else:
                print("\n❌ -> Produit non trouvé 😭")
    
    except FileNotFoundError:
        print("❌ -> Erreur : Le fichier 'produits.csv' n'existe pas. 🤷‍♂️")
    except PermissionError:
        print("❌ -> Erreur : Vous n'avez pas les permissions nécessaires")
    except Exception as e:
        print(f"❌ -> Une erreur s'est produite : {e}")