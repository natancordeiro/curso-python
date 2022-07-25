# índice
# 0123456789.............................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova_string = ''

inpt_usuario = input('Qual letra deseja colocar maiúscula? ')

while contador > tamanho:
    letra = frase[contador]
    if letra == inpt_usuario:
        nova_string += inpt_usuario.upper()
    else: 
        nova_string += letra
    contador += 1
print(nova_string)
