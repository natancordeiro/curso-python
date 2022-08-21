"""
 Continuação - Dicionário em Pyhton
"""

# dicionários dentro de dicionários
clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente2': {
        'nome': 'Natan',
        'sobrenome': 'Cordeiro',
    },
}

# iterando
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

#------------------------------------------------

# Em Python, se você guardar um dicionário dentro de uma variavel
# sem utilizar a função Copy(), vai alterar tranto a varial quanto o dicionário

d1 = { 1: 'a', 2: 'b', 3: 'c', 'd': ['Natan', 'Cordeiro']}

v = d1.copy() # copia raza

import copy

v = copy.deepcopy(d1) # copia profunda
v[1] = 'Natan'
v['d'] [0] = 'Joãozinho'

print(d1)
print(v)
#------------------------------------------------------------

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]
#  Convertendo lista em dicioário
# (somente se a lista ou tupla, tiver uma dupla de valores)
dicio = dict(lista)
print(dicio)

dicio.pop('c3') # tem que dizer qual item quer excluir
dicio.popitem() # para excluir o último item

print(dicio)
