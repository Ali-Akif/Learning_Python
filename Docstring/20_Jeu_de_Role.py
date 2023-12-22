import random

MENU = "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
VIE = 50
VIE_ENNEMI = 50
JEU = True
POTION_STOCK = 3


while JEU:  
    attaque = random.randint(5,10)
    attaque_ennemi = random.randint(5,15)
    potion = random.randint(15,50)

    choix_joueur = input(MENU)

    if not choix_joueur.isdigit():
        continue

    if int(choix_joueur) == 1:
        VIE_ENNEMI -= attaque
        VIE -= attaque_ennemi
        print(f"Vous avez infligé {attaque} points de dégats à l'ennemi !")
        if VIE_ENNEMI <= 0:
            print("Bravo ! Vous avez vaincu l'ennemi !")
            JEU = False
        print(f"L'ennemi vous à infligé {attaque_ennemi} point de dégats.")
        if VIE <=0:
            print("Dommage... L'ennemi vous a battu.")
            JEU = False
        else:
            print(f"""Il vous reste {VIE} points de vie.
Il reste {VIE_ENNEMI} points de vie à l'ennemi.
--------------------------------------------------------------""")
     
    else:
        continue

print("Fin")