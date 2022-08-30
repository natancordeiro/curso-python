"""
 Dicionários em Python
"""

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla',
}

# deletando chave
del d1['str']

# Adicionar uma chave dentro do dicionário
d1['str'] = 'valor'

# teste se a variável exite dentro do dicionário
if d1.get('naoexiste') is not None:
    print(d1.get('naoexiste'))

print(d1)
#-----------------------------------------
# checando se uma chave existe
print('str' in d1)
print('str' in d1.keys())

# checando se um valor existe
print('valor' in d1.values())

# iterando sobre os valores
for v in d1.values():
    print(v)

# iterando sobre os objetos
for k in d1.items():
    print(k[0], k[1])

for chave, valor in d1.items():
    print(chave, valor)
#------------------------------------------
