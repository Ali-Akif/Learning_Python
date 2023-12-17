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