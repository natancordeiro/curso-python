"""
 Argumentos padrão mutáveis em função

Mutável: Lista, dicionário
Imutável: Tupla, string, número, True, False, None
"""
#                              argumento mutável
def lista_cliente(cliente_iteravel, lista=[]):
    lista.extend(cliente_iteravel)
    return lista

clientes1 = ['João', 'Maria', 'José']
clientes2 = ['Marcos', 'Rafael', 'André']
clientes3 = ['Cludio', 'Natan']

print(clientes1)
print(clientes2)
