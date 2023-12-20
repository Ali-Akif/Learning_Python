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

