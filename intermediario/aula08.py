"""
 Zip - Unindo iteráveis 
 Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

# ZIP usado para unir iteráveis. Une até a ultima da menor lista
cidades_estados = zip(indice, estados, cidades)

# Para incluir a maior lista, usa o Zip_longest | ao inves de NONE preencher com filtro
cidade_estados = zip_longest(estados, cidades, fillvalue='Estado')

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
