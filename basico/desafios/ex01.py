"""2
Faça um programa que peça para o usuário para digitar um número inteiro,
informe se esse número é par ou impar. Caso o uusuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

try: 
    num = int(num)
    if num % 2 == 0:
    #PAR
        print(f'O número {num} é PAR')
    else: 
    #IMPAR
        print(f' O número {num} é IMPAR')
except:
    print('O número que você digitou não é um número inteiro')



