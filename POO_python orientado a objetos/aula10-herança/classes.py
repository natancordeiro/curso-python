class Pessoa:
    # Função global na classe mãe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')

# Cliente está herdando de Pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando...')        

class Aluno(Pessoa):
    # Função que só funciona em seua subclasse
    def estudar(self):
        print(f'{self.nomeclasse} Estudando...')  
