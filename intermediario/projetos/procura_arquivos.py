import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite o termo que deseja procurar: ')
cont = 0

# fução para formatar o tamaho de Bites
def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'   
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T' 
    else: 
        tamanho /= peta 
        texto = 'P'
    
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    # Procurando em arquivos
    for arquivo in arquivos: 
        if termo_procura in arquivo:
            try:
                cont += 1
                caminho_completo = os.path.join(raiz, arquivo)
                # separando o nome da extensão e guardo cada um em uma variável
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                # exibindo resposta ao usuário
                print()
                print('Ecnontrei arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado: ', formata_tamanho(tamanho))

            # tratamento de erro
            except PermissionError as erro:
                print('Sem permissão.')
            except FileNotFoundError as erro: 
                print('Arquivo não encontrado.')
            except Exception as erro:
                print('Erro desconhecido', erro)
    
print()
print(f'{cont} arquivo(s) encontrado(s).')
