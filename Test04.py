
numerateur = input("quelle est votre numerateur ?")
denominateur = input("quelle est votre denominateur ?")
 
try:
    numerateur = int(numerateur)
    denominateur = int(denominateur)
    resultat = numerateur / denominateur 
    print("votre resultat est : ", resultat)   
except NameError:
    print("var num ou den n'a pas été déf")
except TypeError:
    print("va num ou de pessede un type incompatible avec la division")
except ZeroDivisionError:
    print("var den est egale a 0")