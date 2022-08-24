"""
    ITERTOOLS
 Combinations - Permutations e Product 

 Combinação - Ordem não importa
 Permutação - Ordem importa 
Ambos não repetem valores únicos
 Produto - Ordem importa e repete valores 
"""
from itertools import combinations, permutations, product

pessoas = ['Natan', 'Rafaela', 'Emile', 'Rayane', 'Waldemir', 'Gil']

#           Mostra as combinações
for grupo in combinations(pessoas, 2):
    print(grupo)
#           Ordem não importa
for grupo in permutations(pessoas, 2):
    print(grupo)
#           Repete os mesmos valores tbm
for grupo in product(pessoas, repeat=2):
    print(grupo)
