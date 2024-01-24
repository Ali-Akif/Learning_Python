dico = {'a': 1, 'b':2, 'c':3 }

for key, value in dico.items():
    print(key, value)

import os

file_path = os.path.dirname(os.path.abspath(__file__)) #path.abspath renvoi le chemin absolu jusqu'au fichier, path.dirname enleve le nom du fichier executé actuellement

print(file_path)

folders = os.listdir(file_path)

print(folders)