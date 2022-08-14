def saudacao(comprimento, nome):
    print(comprimento, nome)

saudacao('Olá', 'Natan')

#--------------------------------------
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(1, 4, 7)

#--------------------------------------
def calculo(numero, percentual):
    percentual = numero * (percentual / 100)
    return print(numero + percentual)

calculo(1000, 50)

#--------------------------------------
def fizz_buzz(numero):
    
    if numero % 5 == 0 and numero % 3 == 0:
        return print('FizzBuzz')
    elif numero % 5 == 0:
        return print('Buzz')
    elif numero % 2 == 0:
        return print('Fizz')
    else:
        return print(numero)

fizz_buzz(30)