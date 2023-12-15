# goal, table of multiplication with user input

nb = input("quelle table de multiplication voulez vous utiliser ? : ")
nb = int(nb)
i = 0

while i < 10    :
    i+=1
    print (i, "*", nb, "=", i * nb)
        