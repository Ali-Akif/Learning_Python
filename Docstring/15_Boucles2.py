liste = [-5, -4, 0, 1, 2]
nombres_positifs = []
for i in liste:
    if i > 0:
        nombres_positifs.append(i)
print(nombres_positifs) # [1, 2]

comprehension_de_liste = [i for i in liste]
#for i in itere sur la liste  et récupère tout

comprehension_de_liste_nb_positifs = [i for i in liste if i > 0] #rajout de la condition if
print(comprehension_de_liste_nb_positifs)#[1, 2]

nombres_positifs = [i * 2 for i in liste if i > 0] #multiplie i par 2
print(nombres_positifs)#[2, 4]

# EXERCICE
print("EXERCICE")

nombre = [1, 21, 5, 44, 4, 9, 83, 29, 31, 25, 38]
nombres_pair = [i for i in nombre if i % 2 == 0]  
# for i in nombre:
#     if i % 2 == 0:
#         nombres_pair.append(i)

print(nombres_pair)

# ________________________________________________________________

nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]
# for i in nombres:
#     if i >= 0:
#         nombres_positifs.append(i)

print(nombres_positifs)

# ________________________________________________________________

nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]
# for i in nombres:
#     nombres_doubles.append(i * 2)

print(nombres_doubles)

# ________________________________________________________________

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
# for i in nombres:
#     if i % 2 == 0:
#         nombres_inverses.append(i)
#     else:
#         nombres_inverses.append(-i)

print(nombres_inverses)

#on peut retourner ce qu'on veut, j'aurias pu faire [5 for i in nombres]....