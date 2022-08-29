"""
 Criar, ler e escrever em arquivos 
"""

# usado para fechar automaticamente o file
with open('def.txt', 'w+') as file:

    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3 ')

    file.seek(0)
    print(file.read())

# utilizando a função R = read  
with open('def.txt', 'r') as file:
    print(file.read())

# utilizando a função A = append (adicionar coisas no arquivo sem excluir)
with open('def.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())

#----------------------------------------------------------
# Trabalhando com JSON
import json

d1 = {
    'Pessoa 1': {
        'nome:': 'Luiz',
        'idade': 23,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}
# convertendo o dicionário em JSON
d1_json = json.dumps(d1, indent=True)

# guardando em um arquivo
with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)
