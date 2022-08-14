"""
 Funções (def) em Python - *args **kwards -     
"""

#                        A partir do momento que eu seto um padrão,   
#                      todos depois  dele precisarão ter difinições padrões.
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome)

#func(1, 2, 3, 4, 5, 'Luiz')
#---------------------------------------------
def funcao(*args): # Utilizado quando não se sabe a quantidade de argumentos.
    print(args)

#funcao(1,2,3,4,5)

lista = [1,2,3,4,5]
#print(*lista, sep='-') # Separador
#  *usado para desempacotar

#--------------------------------------------
def funcao(*args): # *args vem como padrão de TUPLA
    args = list(args) # para modificar, necessário converter a TUPLA em LISTA
    args[0] = 20
    for v in args:
        print(v)

#funcao(1,2,3,4,5)
#-------------------------------------------
def funcao(*args, **kwargs): # Utilizado para identificar argumentos NOMEADOS
    print(args)

    idade = kwargs.get('idade') #.get (Verificar se existe aquele argumento)

    if idade is not None:
        print(idade)
    else: 
        print('Idade não existe')
    
lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]

funcao(*lista, *lista2, nome='Luiz', sobrenome='Miranda')
