"""
 @property - Getters e Setters em Python
"""
class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # desconto por porcentagem
    def desconto(self, porcentagem_desconto):
        self.preco = self.preco - (self.preco * (porcentagem_desconto / 100))

    # Getter 
    @property
    def preco(self):
        return self._preco

    # Setter 
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
        self._preco = valor

p1 = Produto('Camisa', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)
