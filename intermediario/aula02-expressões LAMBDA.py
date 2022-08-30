"""
 Expressões LAMBDA (Funções Anônimas) Em Python
"""

a = lambda x, y: x * y

print(a(2,4))
#-----------------------------------------
lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8]
]
# sort() usado para modificar a ordem de uma lista.
lista.sort(key=lambda item: item[1])
print(lista)

#  sorted() ordenar uma lista sem alterar a lista original.
#                                      de trás para frente
print(sorted(lista, key=lambda i: i[0], reverse=True))
#                            indice 0 = 1°obj = 'p1'..'p5'
#                            indice 1 = 2°obj =   13..8
