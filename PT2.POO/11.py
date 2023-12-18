def fonction_inconnue(*parametres):
    """
    Test d'une fonction pouvant etre appelée avec un nombre variable de paramètres

    """
    print("J'ai reçu : {}.".format(parametres))

fonction_inconnue()
#print j'ai recu : ()

fonction_inconnue('a', 'b', 2)

var = 3.5
fonction_inconnue(var, [4], "...")  

for i in range(5):
    print (i)

    # print de 0 a 4

for i in range(1,5):
    print (i)

    #print de 1 a 4
