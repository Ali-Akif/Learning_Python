print(r'c:\dossiers\thibault\nouveautes')
#permet d'échapper les anti slash
#\a (BEL) \b retour en arriere etc


#nombres entier = -5 1 15 16465258897625... on peut aussi 1_000_000
#nombres décimaux (flottants) -5.485 1.254 10.0 15.87...

#booleens 1 True 0 False
print(issubclass(bool, int))
#print True
print(bool("bonjour")) 
#print True, tout les objets ont une configuration True ou False

#les constructeurs de type natif

str() #chaine de caractères string
int() #nombres entiers integer
float() #nombres décimaux
bool() #booleens

cinq = str(5)
print(cinq)
cinq = int("2")
print(cinq)