"""
 Herança simples
"""
from classes import *

c1 = Cliente('Natan', 22)
c1.falar()

a1 = Aluno('Rafa', 29)
a1.falar()

c2 = ClienteVIP('Natan', 22, 'Cordeiro')
c2.falar()
