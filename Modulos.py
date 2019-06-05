#importação de modulo
"""
"""
from math import pi, e
from math import sqrt
"""
    #Ou Pode ser feito assim tb

import math

e = math.e
pi = math.pi
sqrt = math.sqrt

   #Para importar todos os simpolos de um módulo de vez

#    from math import *

def func():
    from math import factorial
    print(factorial(6))
    print()

func()

print(sqrt(81))
print(pi)
print(e)
"""

from Modulos1 import *
from pprint import  pprint

#pprint(globals())


#Recarregamento de modulo

import importlib #IMPORTLIB Modulo pra manutenção de modulos

import Modulos1
del(Modulos1.bb)
Modulos1.aa = 0

print(Modulos1.aa)
#pprint(Modulos1.__dict__)
pprint( "AAAAAAAAAAAAAAAAAAAAAAAAA" )

importlib.reload(Modulos1)

print(Modulos1.aa)
#pprint(Modulos1.__dict__)
























