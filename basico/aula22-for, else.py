"""
 For / Else em Python
"""

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'): # Começa com J
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J')
else: 
    print('Não existe uma palavra que começa com J')
