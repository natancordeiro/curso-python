"""
 Listas em Python
 fatiamento 
 append, insert, pop, del, clear, extend, +
 min, max
 range
"""

#          0    1    2    3    4    5
lista = [ 'A', 'B', 'C', 'D', 'E', 10.5]

print('Lista de invertida: ', lista[::-1]) # listar de trás para frente

#------------------------------------------------

# Variáveis
l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2) # extende
print('Lista com Extend: ', l1)

l2.append('b') # insere um valor no final da lista
print('Lista com append: ', l2)

#    (indice, conteudo)
l2.insert(0, 'banana') # insere um valor em um indice especifico indicado pelo user
print('Lista com insert: ', l2)

l2.pop() # remove o último item da lista
print('Lista com o pop: ', l2)

#---------------------------------------------

# Variáveis 
#     0 1 2 3 4 5 6 7 8
l3 = [1,2,3,4,5,6,7,8,9]

del(l3[3:5]) # deleta itens selecionados a partir do indice
print('Lista com del: ' ,l3)

print('Lista com o max: ', max(l3)) # mostra o maior valor da lista
print('Lista com o min: ', min(l3)) # mostra o menor valor da lista

#--------------------------------------------------------

l4 = list(range(0, 100, 8)) # cria uma lista com um range específico
print('Criando uma lista usando o range: ', l4) 

for valor in l3:
    print(valor)   # iterando uma lista usando o laço FOR

#--------------------------------------------------------

# JOGO DA FORCA

secreto = 'perfume'
digitadas = []
chance = 3

while True:

    if chance <= 0:
        print('VOCÊ PERDEU!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('ERRO!! Digite apenas uma letra.')
        continue

    digitadas.append(letra)

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
    
    if secreto_temporario == secreto:
        print(f' PARABÉNS VOCÊ VENCEU!! A palavra secreta era {secreto_temporario}')
        break
    else: 
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto_temporario:
        chance -= 1

    print(f'Você tem {chance} chances.')