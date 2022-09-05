"""
 public, protected, private
 Acesso: 
    (public_)
    (privado - _NOMECLASS__nomeatributo)

 _ = protected (Recomenda para nãoa acessar esse dado)
 __ = private (Recomenda fortemente que não seja acessado)

"""

class BaseDados:
    def __init__(self):
        self.__dados = {}

    @property  # Usado para obter um dado
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()
bd.inserir_cliente(1, 'Natan')
bd.inserir_cliente(2, 'Rafa')
bd.inserir_cliente(3, 'Ray')

print(bd.dados)
