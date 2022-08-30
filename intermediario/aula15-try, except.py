"""
 Try, Except - Tratando exceções em Python
"""

try:
    a = {}
except NameError as erro: # pega somente o NameError
    print('Erro do desenvolvedor.')
except (IndexError, KeyError) as erro: # trata dois erros
    print('Erro de índice ou chave.') 
except Exception as erro: # pega qualquer tipo de erro
    print('Ocorreu um erro inexperado.')
else: # execulta quando o bloco TRY for executado com sucesso
    print('Seu comando foi execultado com sucesso!')
    print(a) 
finally: # independente do TRY e ExCEPT será execultado
    print('finalmente.')

print('Continando...')
