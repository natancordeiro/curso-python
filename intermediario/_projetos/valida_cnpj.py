import re

# constante (que não se pode alterar)
REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3,2]

# Função para verificar se o input é uma sequência
def sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False

# Função para validar o cnpj
def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    # tranatndo erro de sequêncnia
    try:
        if sequencia(cnpj):
            print('Inválido! É uma sequência')
            return False
    except:
        return False

    # tratando erro de sintaxe caso seja digitado letras
    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as erro:
        return False

    if novo_cnpj == cnpj:
        return True
    else: 
        return False

# Função para calcular os 2 últimos digitos
def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else: 
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    
    return f'{novo_cnpj}{digito}'

# Funão para remover os simbolos do cnpj do input
def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

#---------------------------

cnpj1 = '04.252.011/0001-10'
cnpj2 = '11.111.111/1111-11'

if valida(cnpj2):
    print(f'{cnpj2} é válido!')
else: 
    print(f'{cnpj2} é inválido!')


"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
