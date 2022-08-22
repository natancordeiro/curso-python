"""
 Geradores em Python
"""

import sys
import time

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(sys.getsizeof(l1), type(l1))
print(sys.getsizeof(l2), type(l2))
#-----------------------------------

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

for valor in g: 
    print(valor)
