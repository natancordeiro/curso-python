nome = 'Natan Cordeiro'
idade = 22  #int
altura = 1.86  #float
e_maior = idade > 18  #bool
peso = 72
imc = peso / (altura ** 2)

print( nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{2} {0} tem {1} anos de idade e seu IMC é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {imc:.2f}'.format(n=nome, i=idade, imc=imc))
