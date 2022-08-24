"""
 Count - Itertools
"""
from itertools import count

contador = count(start=-1, step=-1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break
#-------------------------------------

indice = count()
lista = ['Luiz', 'Natan', 'João', 'Maria', 'Eduardo']

lista = zip(indice, lista)
print(list(lista))
