"""
Formatando valores com modificadores

:s - Texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casa decimais (float) :.2f
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita 
^ - Centro
"""

nome = 'Natan'
sobrenome = 'Cordeiro'

print(' Nome {0} {1:#^30}'.format(nome, sobrenome))