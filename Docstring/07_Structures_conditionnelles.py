#if, elif, else



age = 15

if age >= 18:
    print("t'es majeur")
elif age < 18:
    print("mineur")

utilisateur = "admin"
if utilisateur == "admin":
    print("Accès autorisé")
elif utilisateur == "root":
    print("Accès autorisé")
else:
    print("Accès refusé")

#opérateurs ternaires
majeur = True if age >= 18 else False
print(bool(age))

#les opérateurs logique and or not
mot_de_passe = utilisateur
if utilisateur == "admin" and mot_de_passe == "admin":
    print("Accès autorisé")

if 5 > 2 and 5 < 10 or 5 > 15:
    print("ouii") #print ouii, avec or, si ou moins une des conditions est vrai alors le résultat est vrai

if 5 > 2 and (5 < 10 or 5 > 15):
    print("ouiii") #print ouii car () is true and ( > 2 true)

if not utilisateur == "admin":
    print("no")#print r car ut == admin