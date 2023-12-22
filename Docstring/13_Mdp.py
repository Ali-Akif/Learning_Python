mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_court = "votre mot de passe est trop court"

if len(mdp) < 1:
    print(mdp_court.upper())
elif len(mdp) < 8:
    print(mdp_court.capitalize())
elif mdp.isdigit():
    print(mdp_court.replace("est trop court", "ne contient que des nombres"))
else:
    print("inscription terminée")

#correction:
# if len(mdp) == 0:
#     print(mdp_court.upper())
# elif len(mdp) < 8:
#     print(mdp.court.capitalize())
# elif mdp.isdigit():
#     print("Votre mot de passe ne contient que des nombres.")
# else:
#     print("Inscription terminée.")