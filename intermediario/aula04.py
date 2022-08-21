"""
 add (adiciona) | update (atualiza) | clear | discard
 union | (une)
 intersection & (Todos os elementos presentes nos dois sets)
 difference - (elementos apenas no set da esquerda)
 symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""
# SET = Conjunto (semelhante aos dicionários, tuplas e listas)

s1 = {1, 2, 3, 4, 5, 6}

s1.add(7)
s1.discard(2)
s1.update([1,2,3,4,5], {5,6,7,8}) # adiciona de forma aleatoria as letras
#           Itens duplicados são unidos
#-----------------------------------------------------------

l1 = [1,2,3,2,1,1,1,1,1,1,1,4,5,6,6,6,6,6, 'Natan', 'Natan']
l1 = set(l1)
l1 = list(l1)
# usado para excluir itens duplicados
#-----------------------------------------------------------

s2 = {1,2,3,4,5,6, 9}
s3 = s1 | s2 # Union
s3 = s1 & s2 # Intersection
s3 = s1 - s2 # Ifference
s3 = s1 ^ s2 # Symmetric_difference


print(s3)
