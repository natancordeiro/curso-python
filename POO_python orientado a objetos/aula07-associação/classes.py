class Escritor:
    def __init__(self, nome): # Construtor
        self.__nome = nome  # Setter 
        self.__ferramenta = None

    @property # Getter - Utilizado para acessar o atributo fora da class
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramneta):
        self.__ferramenta = ferramneta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')
    
class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')
