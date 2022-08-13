"""
 Desempacotamento em Python
"""
#          n1      n2      n3          *outra_lista         ultimo
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_ista, ultimo_da_lista = lista
    # O * armazena o resto
    # Quando não uzar o restante da lista, utilizar o *_

print(ultimo_da_lista)