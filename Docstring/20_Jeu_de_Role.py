import random

VIE = 50
VIE_ENNEMI = 50
POTIONS = 3
SKIP_TURN = False

while True:
    #Jeu du joueur
    if SKIP_TURN == True:
        print("Vous passez votre tour...")
        SKIP_TURN = False
    else:
        choix = ""
        while choix not in ["1", "2"]:
            choix = input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")

        if choix == "1": # Attaque
            degats = random.randint(5,10)
            VIE_ENNEMI -= degats
            print(f"Vous avez infligé {degats} points de dégats à l'ennemi{" !!!" if degats == 10 else "."}⚔️")
        elif choix == "2" and POTIONS > 0: # Potion
                popo = random.randint(15,50)
                VIE += popo
                POTIONS -= 1
                SKIP_TURN = True
                print(f"Vous récupérez {popo} points de vie ❤️ ( {POTIONS} potions restante{"s" if POTIONS > 1 else ""})")
        else:
            print("Vous n'avez plus de potions...")
            continue


    if VIE_ENNEMI <= 0:
        print("Bravo, tu as gagné !")
        break
    
    # Attaque de l'ennemi
    degats = random.randint(5,15)
    VIE -= degats
    print(f"L'ennemi vous a infligé {degats} points de dégats{" !" if degats > 10 else "."} ⚔️")

    if VIE <= 0:
        print("Dommage, tu as perdu...")
        break
    
    #Stats
    print(f"Il vous reste {VIE} point{"s" if VIE > 1 else ""} de vie.")
    print(f"Il reste {VIE_ENNEMI} point{"s" if VIE_ENNEMI > 1 else ""} de vie à l'ennemi.")
    print("-" * 50)
    
print("Fin du jeu.\n")