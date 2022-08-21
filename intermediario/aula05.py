"""
 List Comprehension em Python - (Compreensão de lista)
"""
l1 = [1,2,3,4,5,6,7,8,9]

#      Comando        Laço FOR
exp1 = [variavel for variavel in l1]

#      Comando |  Laço
exp2 = [v * 2 for v in l1]

#       Comando |  Laço 1  |      Laço 2
exp3 = [(v, v2) for v in l1 for v2 in range(3)]
#-------------------------------------------------
l2 = ['Luiz', 'Mauricio', 'Maria']
exp4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
#     invertendo os valores de lugar
exp5 = [(y, x) for x, y in tupla]
exp5 = dict(exp5)
#-------------------------------------------------
l3 = list(range(100))

# usando IF para ver somente os numeros diviziveis por 3 entre 0 e 100
exp6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

# Também possível utilizar o ELSE
exp7 = [v if v % 3 == 0 and v % 8 == 0 else "Não é" for v in l3]


print(exp7)
