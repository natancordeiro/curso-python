"""
 Funções decoradoras em Python
"""
# função decoradora
def master(funcao):
    # função escrava da master
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave

# definindo ela como decorada
#fala_oi = master(fala_oi)   OU
@master
def fala_oi():
    print('Oi')

@master
def outra_funcao(msg):
    print(msg)  

outra_funcao('Olá, meu nome é Natan.')
#----------------------------------------

from time import time
from time import sleep

# Função que calcula o tempo de execução de uma outra função
def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para execultar.')
        return resultado    
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i, end='')
        sleep(1)

demora()
