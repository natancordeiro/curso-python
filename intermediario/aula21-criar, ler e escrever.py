"""
 Criar, ler e escrever em arquivos - Básico
"""
# criando arquivo
file = open('abc.txt', 'w+')

# escrevendo...
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# Posicionando cursor de volta para o inicio
file.seek(0, 0)

# lendo tudo
print('Lendo linhas:')
print(file.read())

print('------------------')

# lendo linha a linha
file.seek(0, 0)
print(file.readline(), end='') # Linha 1
print(file.readline(), end='') # Linha 2
print(file.readline(), end='') # Linha 3

print('------------------')


file.seek(0, 0) # readlines() cria uma lista contendo as linhas como conteúdo
for linha in file.readlines():
    print(linha, end='')

# fechando arquivo
file.close()
