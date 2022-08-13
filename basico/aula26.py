"""
 Operadores Ternários em Python
"""

logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário presica logar.'

print(msg)
#-------------------------------------------------------------------

idade = input('Qaul a sua idade?')

if not idade.isnumeric():
    print('Você precisa digitar um número.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)