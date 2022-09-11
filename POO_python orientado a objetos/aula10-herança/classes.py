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

class ClienteVIP(Cliente):
    def falar(self):
        super().falar() # se refere a função da classe principal 
        print('Outra coisa qualquer.')
        # Sobreposição / Reescrever o que o método faz
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome
        # Reescrevendo o método construtor 

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
    