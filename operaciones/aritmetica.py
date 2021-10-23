def run():
    a, b = 9, 4
    print("suma: ", suma(a, b))
    print("resta: ", resta(a, b))
    print("multiplicacion: ", multiplicacion(a, b))
    print("division decimales: ", divisionf(a, b))
    print("division enteros: ", division(a, b))
    print("modulo: ", modulo(a, b))
    print("cuadrado: ", square(a))
    print("potencia: ", potencia(a, b))
    print("raiz cuadrada: ", squrt(a))

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def divisionf(a, b) -> float:
    return a/b

def division(a,b) -> int:
    return a//b

def modulo(a,b):
    return a%b

def square(a):
    return a**2

def potencia(a,p):
    return a**p

def squrt(a):
    return a**(.5)

if __name__=='__main__':
    run()