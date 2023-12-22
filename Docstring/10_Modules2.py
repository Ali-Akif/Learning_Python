#.callable()



#les objets callables, "appelable"
#ex : os.makedir(), tu peux l'appeler

import os
import pprint
from pprint import pprint

print(callable(pprint))
#False
print(callable(pprint))
#True avec from pprint import pprint
print(callable(os.name))
#False

#dans l'idée, tu guette tes fonctions/attribu avec os.dir, puis tu vérifie si c'est callable 