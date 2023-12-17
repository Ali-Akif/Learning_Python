prenom = "Akif"
nom = "Gunacar"
age = 21
print("Je m'appelle {0} {1} et j'ai {2} ans.".format( prenom, nom, age ))

#.format({0}{1}{2})

nouvelle_chaine = "Je m'appelle {0} {1} et j'ai {2} ans. ".format(prenom, nom, age)

print("Je m'appelle {0} {1} ({3} {0} pour les intimes) et j'ai {2} ans.".format(prenom,nom,age,nom.upper()))  #important ça

date = "17 décembre 2023"
heure = "19:34"

print("Cela à été écrit le {}, à {}.".format(date,heure))
#ça aussi



adresse = """ 
{no_rue}, {nom_rue}
    {code_postal} {nom_ville} ({pays})""".format(no_rue=55, nom_rue="rue d'Amsterdam", code_postal=67000, nom_ville = "Strasbourg", pays="France")
print(adresse)
#Au lieu des numéros, on donne le nom des var qui seront dans les accolades

message = "Bonjour"

chaine_complete = message + " " + prenom
print(chaine_complete) 

#voila comment concaténer des chaines frérot

message = "J'ai " + str(age) + " ans."
print(message)

#on appelle str() pour convertir un objet en chaine de caractere, car age n'est pas entre " ", il aurait réussi sinon le frérot