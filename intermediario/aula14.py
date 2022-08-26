"""
 Reduce em Python
"""
from functools import reduce
from aula12_dados import produtos, pessoas, lista

#                       acumulador        inicio = 0
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)
#-----------------------------------------------------

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
media = soma_precos / len(produtos)

print(f'A média do preço dos produtos é: R${round(media, 2)}')
#---------------------------------------------------------

idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
media = idade / len(produtos)

print(f'A média do idade das pessoas é de {media}')
