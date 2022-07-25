"""
Faça um programa que pergunte a hora ao usuário e, baseando-se horário
descrito, exiba a saudação apropriada. EX:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""


hr = int(input('Que horas são (0-23): '))

if hr.isdigit():

    hr = int(hr)
    if hr < 0 or hr > 23:
        print('O horário deve estar entre 0 e 23.')

    if hr <= 11:
        print('Bom dia')
    elif hr <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
else: 
    print('Horário digitado inválido.')
