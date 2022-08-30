"""
 Iteradores em Python
"""

nome = 'Natan Cordeiro'
iterador = iter(nome)
gerador = (letra for letra in nome)

try:
    print(next(iterador)) # N
    print(next(iterador)) # a
    print(next(iterador)) # t
    print(next(iterador)) # a
    print(next(iterador)) # n
    print(next(iterador)) #
    print(next(iterador)) # C
    print(next(iterador)) # o
#    print(next(iterador)) # r
#    print(next(iterador)) # d
#    print(next(iterador)) # e
#    print(next(iterador)) # i
#    print(next(iterador)) # r
#    print(next(iterador)) # o
except:
    pass

# Os iteradores CONSOMEM os valores 

print('CADÊ OS VALORES? ')
for valor in iterador:
    print(valor)

#-----------------------------------------
# Os geradores tem o mesmo comportamento
"""
print('OLHA O FOR ')
for i in gerador:
    print(i)
"""