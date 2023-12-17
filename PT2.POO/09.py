tuple_vide = ()
tuple = (1,) #faut mettre une virgule, sinon c'est juste une var
fausse_tuple = (1)

print(fausse_tuple)#print 1
print(tuple)#print (1,)

a, b = 3, 4

print (a) #3

a, b = b, a
print(a)#4

def decomposer(entier, divise_par):
    """

    Cette fonction retourne la partie entère et le reste de entier / diviser_par

    """
    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste

partie_entière, reste = decomposer(20, 3)

print (partie_entière)
print (reste)
# print 6 et 3 car 20 divisé par 3 = 6.67, mais avec modulo il reste 2