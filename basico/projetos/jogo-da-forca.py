# JOGO DA FORCA

# Variáveis globais
secreto = 'perfume'
digitadas = []
chance = 3

while True:
    
    # Contador de chances
    if chance <= 0:
        print('VOCÊ PERDEU!!')
        break

    letra = input('Digite uma letra: ')

    # Teste de erro (mais de uma letra digitada)
    if len(letra) > 1:
        print('ERRO!! Digite apenas uma letra.')
        continue

    # Incremento da letra na variável
    digitadas.append(letra)

    # Verificação de acerto
    if letra in secreto:
        print(f'UHUUULLL, a letra "{letra}" existe na palavra secreta.')
    else: 
        print(f'AAAFFF, a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()
    

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    # Verificação de Game Over
    if secreto_temporario == secreto:
        print(f' PARABÉNS VOCÊ VENCEU!! A palavra secreta era {secreto_temporario}')
        break
    else: 
        print(f'A palavra secreta está assim: {secreto_temporario}')

    # Decressão do contador de chances
    if letra not in secreto_temporario:
        chance -= 1
    print(f'Você tem {chance} chances.')
