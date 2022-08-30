perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quem criou o Basquete? ',
        'respostas': {
            'a': 'Oscar Schmidt',
            'b': 'James Naismith',
            'c': 'James Cameron',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual a altura da cesta de Basquete? ',
        'respostas': {
            'a': '3,05',
            'b': '3,15',
            'c': '3,00',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'No basquete pode: ',
        'respostas': {
            'a': 'Correr com a bola na mão',
            'b': 'Andar com a bola batento e segurando',
            'c': 'Bater a bola continuamente',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Em que ano foi criado o Basquete?',
        'respostas': {
            'a': '1782',
            'b': '1892',
            'c': '1894',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Qual o limite de faltas que um jogador pode cometer?',
        'respostas': {
            'a': '4 faltas',
            'b': '6 faltas',
            'c': '5 faltas',
        },
        'resposta_certa': 'c',
    }
}
print()

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    print()

    if resposta_usuario == pv['resposta_certa']:
        print('\033[1;32mVocê acertou!\033[m')
        respostas_certas += 1
    else:
        print('\033[1;31mVocê errou!\033[m')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acertos foi {porcentagem_acerto}%.')
