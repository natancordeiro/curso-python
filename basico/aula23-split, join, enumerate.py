"""
 Split, Join, Enumerate em Python

 * Split - Dividir uma string # str
 * Join - Juntar uma lista # str
 Enumerate - Enumerar elementos da lista # list

"""

string = 'O Brasil é o país do futebol, o Brasil é penta.'

lista1 = string.split(' ') # Separa nos espaços
lista2 = string.split(',') # Separa na vírgula

for valor in lista2:
    print(valor.strip().capitalize()) 
                # Remove os espaços antes e depois

#-------------------------------------------------------

string1 = 'O Brasil é penta.'
lista = string1.split(' ')

string2 = ','.join(lista) # Juntar elementos de uma lista em String

print(string2)

#--------------------------------------------------------

for indice, valor in enumerate(lista):  # Enumera os valores
    print(indice, valor)


