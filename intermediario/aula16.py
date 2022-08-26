"""
 Levantando exceções 
"""
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        return False

#---------------------------------------------
def divid(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1 / n2

print(divid(2, 0))
