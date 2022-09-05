"""
 Relação de Associação - Uma classe se relaciona com ourta
    mas nenhuma das duas dependem uma da outra.
"""
from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor('Machado de Assis')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
