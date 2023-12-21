# choisissez parmi les 5 options suivantes:
# 1: ajouter un élément a la liste
# 2: Retirer un élément de la liste
# 3: Afficher la liste
# 4: Vider la liste
# 5: quitter
#     Votre choix:

continuer = 1
liste = []

while continuer == 1:

    reponse = input("""----------------------------------------------------
Choisissez parmi les 5 options suivantes:
1: ajouter un élément a la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
     Votre choix : """)
    
    if not reponse.isdigit():
        print("Il faut rentrer un chiffre.")
        continue
    elif 0> int(reponse) or int(reponse) > 5:
        print("Merci de rentrer une commande recevable.")
    
    elif int(reponse) == 1:
        ajout = input("Ecrivez l'élément que vous voulez ajouté à la liste : ").lower().capitalize()
        liste.append(ajout)
        print(f"L'élément {ajout} à bien été ajouté à votre liste.")

    elif int(reponse) == 2:
        retirer = input("Entrez le nom d'un élément à retirer de la liste de courses : ").lower().capitalize()
        if retirer in liste:    
            liste.remove(retirer)
            print(f"L'élément {retirer} à bien été retiré de votre liste.")
        else:
            print(f"L'élément {retirer} n'est pas dans la liste.")
            print(f"Les éléments dans votre liste sont : ")
            for i in range(len(liste)):
                print(f"{i + 1}. {liste[i]}")

    elif int(reponse) == 3:
        if (len(liste)) > 0:
            print("Les éléments dans votre liste sont : ")
            for i in range(len(liste)):                      #pouvait etre fait avec for i item in enumerate(liste, 1): print(f"{i}. {item}")
                print(f"{i + 1}. {liste[i]}")
        else:
            print("Votre liste ne contient aucun élément.")

    elif int(reponse) == 4:
        liste.clear()
        print("La liste à été vidée de son contenu.")
    
    elif int(reponse) == 5:
        print("A bientôt !")
        continuer = 2
    
    