import math

def soma(a,b):
    return a + b

def subtração(a,b):
    return a - b

def multiplicação(a,b):
    return a * b

def divisão(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "\033[1;31mNenhum pois não é possível dividir por 0\033[m"

def potenciação(a,b):
    return a ** b

def raiz(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "\033[1;31mNenhum pois não é possível calcular raiz quadrada de número negativo!\033[m"