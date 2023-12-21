#reversed()

# EXERCICE

for i in range(10):
    print(f"Utilisateur {i+1}")


mot = "Python"
for i in reversed(mot):
    print(i)

# mot = "Python"
# print(reversed(mot)) ça veut pass
# print(list(reversed(mot)) ça sort une liste avec ['n', 'o', 'h', 't', 'y', 'P']
    
continuer = "o"
while continuer == "o":
    print("On continue !")
    resultat = input("Voulez vous continuer ? o/n ")
    if resultat == "n":
        break
    else:
        continue