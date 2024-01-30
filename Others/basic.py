print("Bienvenue dans la calculatrice simple !")

# Demander à l'utilisateur de saisir deux nombres
num1 = float(input("Veuillez entrer le premier nombre : "))
num2 = float(input("Veuillez entrer le deuxième nombre : "))

# Afficher les options d'opération
print("\nChoisissez une opération :")
print("1. Addition (+)")
print("2. Soustraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Demander à l'utilisateur de choisir une opération
operation = input("\nEntrez le numéro de l'opération choisie (1/2/3/4) : ")

# Définir un dictionnaire pour mapper les opérations aux opérateurs
operations = {
    '1': '+',
    '2': '-',
    '3': '*',
    '4': '/'
}

# Vérifier si l'opération est valide, sinon afficher une erreur
if operation in operations:
    resultat = eval(f"{num1} {operations[operation]} {num2}")
else:
    resultat = "Erreur : Opération invalide"

# Afficher le résultat
print(f"Résultat : {num1} {operations.get(operation, '')} {num2} = {resultat}")
