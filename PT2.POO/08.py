variable = 34

del variable #supprime la var

liste = [1, 2, 3]

del liste[1]
print(liste) #[1, 3]


liste.remove(3)
print(liste)#[1]

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0
while i < len(ma_liste):
    print(ma_liste[i])
    i +=1

for elt in ma_liste:
    print(elt) #fait la meme chose, en plus simple

for i, elt in enumerate(ma_liste):
    print("à l'indice {} se trouve {}.".format(i, elt))



for elt in enumerate(ma_liste):
    print(elt) #print (0, 'a')\n (1, 'b') etc


liste2 = [
    [1, 'a'],
    [2, 'b'],
    [3, 'c'],
]

for nb, lettre in liste2:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))

#La lettre a est la 1e de l'alphabet. \n etc