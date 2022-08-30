"""
 Filter em Pyhton
"""
from aula12_dados import produtos, pessoas, lista

# função filter retorna True ou False
# nova_lista = filter(lambda x: x > 5, lista)

nova_lista = [x for x in lista if x > 5]

print(list(nova_lista))
#--------------------------------------------
#                      retorna produtos maior que 50,00
lista_prod = filter(lambda p: p['preco'] > 50, produtos)

for produto in lista_prod:
    print(produto)
#--------------------------------------------
print(f'\n')


def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else: 
        return False
    
nova_idade = filter(filtra, pessoas)

for pessoa in nova_idade:
    print(pessoa)
