"""
Operações relacionais - == > >= < <= !=
"""
nome = input('Qual é o seu nome?')
idade = input('Qual é sua idade?')

idade = int(idade)

# Limite para pagar emprestimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar empréstimo.')
else: 
    print(f'{nome} NÃO pode pegar empréstimo')
