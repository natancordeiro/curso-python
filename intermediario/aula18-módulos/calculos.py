import math
from statistics import multimode

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def mutiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

# só será executado se estiver dentro desse arquivo
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(mutiplica(lista))
    print(PI)
