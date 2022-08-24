"""
 Map em Python
"""
from http.client import NON_AUTHORITATIVE_INFORMATION
from aula12_dados import produtos, pessoas, lista

#nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]

print(list(lista))
print(list(nova_lista))
#-----------------------------------------------

def aumenta_preco(p):#      round         2 = arredodando decimais
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p
# Map pode ser usado também para como função LAMBDA

# Método MAP recebe sempre uma função, mapeamneeto
novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
#----------------------------------------------

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)

def aumenta_idade(p):  #     aumento de 20% da idade
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

idade = map(aumenta_idade, pessoas)

for p in idade:
    print(p)
