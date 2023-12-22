import random

print("*** Le jeu du nombre mystère ***")

essais = 5
nombre_mystere = random.randint(1,50)
print("Le nombre mystère est entre 1 et 50...")

while essais > 0:
    print(f"Il te reste {essais} essai{'s' if essais > 1 else ""}")
    essai_nombre = input("Devine le nombre : ")

    if essai_nombre.isdigit():
        if int(essai_nombre) == nombre_mystere:
            print(f"Bravo! Le nombre mystère était bien {nombre_mystere}")
            essais-=1
            print(f"Tu as trouvé en { 5 - essais} essais !")
            break

        elif int(essai_nombre) < nombre_mystere:
            essais -= 1
            if essais == 0:
                break
            else:
                print(f"Le nombre mystère est plus grand que {essai_nombre}")

        elif int(essai_nombre) > nombre_mystere:
            essais -= 1
            if essais == 0:
                break
            else:
                print(f"Le nombre mystère est plus petit que {essai_nombre}")

    else:
        print("Veuillez rentrer un nombre valide")

if essais == 0:
    print(f"Dommage! Le nombre mystère était {nombre_mystere}")
print("Fin du jeu \n")