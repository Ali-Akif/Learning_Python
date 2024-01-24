my_set = {1, 2, 3}
print(my_set) # {1, 2, 3}

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_set = set(liste)
print(liste_set)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

liste_set.add("bijour")
liste_set.update(["bijourV2", 10])
print(liste_set)
# {'bijour', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'bijourV2'}

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) #{1, 2, 3, 4, 5}, union
print(a & b) #{3}, intersection
print(a - b) #{1, 2}, difference, sort l'élément present dans a mais pas dans b
print(a ^ b) #{1, 2, 4, 5}, difference symetrique, ne montre pas les doublons de a et b

