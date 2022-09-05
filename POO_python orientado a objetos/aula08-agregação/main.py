"""
 Agregação - Quando uma class depende da outra
"""
from classes import CarrinhoDeCompa, Produto

carrinho = CarrinhoDeCompa()
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneta', 15)

carrinho.inserir(p1)
carrinho.inserir(p2)
carrinho.inserir(p3)

carrinho.lista()
print("Total:", carrinho.soma())
