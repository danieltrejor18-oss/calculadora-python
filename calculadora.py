def sumar(a,b):
    return a + b
def restar(a,b):
    return a- b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        return "Error, no se puede dividir entre 0"
    return a / b
def porcentaje(a,b):
    return (a * b) / 100
salida = " "
while salida != ("salir"):
    print("===Calculadora Simple===")
    try:
        numero1 = input("Escribe el primer numero:")
        numero2 = input("Escribe el segundo numero:")
        operacion = input("Que tipo de operacion? (Suma/Resta/Division/Multiplicar/Porcentaje):")
        numero1 = float(numero1)
        numero2 = float(numero2)
    except ValueError:
        print("Error, solo puedes ingresar numeros")
        exit()
    if operacion.lower() == ("suma") :
        resultado = sumar(numero1 , numero2)
        print("El resultado es: ", resultado)
    elif operacion.lower() == ("resta") :
        resultado = restar(numero1, numero2)
        print("El resultado es: ", resultado)
    elif operacion.lower() == ("multiplicar") :
        resultado = multiplicar(numero1, numero2)
        print("El resultado es: ", resultado)
    elif operacion.lower() == ("division") :
            resultado = dividir(numero1, numero2)
            print("El resultado es: ", resultado)
    elif operacion.lower() == ("porcentaje"):
        resultado = porcentaje(numero1, numero2)
        print("El %",numero2, "de" , numero1, "es: ", resultado)
    salida = input("Quiere salir? (escriba salir): ") .lower()