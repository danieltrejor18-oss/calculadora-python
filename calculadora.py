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
        resultado = numero1 + numero2
        print("El resultado es: ", resultado)
    elif operacion.lower() == ("resta") :
        resultado = numero1 - numero2
        print("El resultado es: ", resultado)
    elif operacion.lower() == ("multiplicar") :
        resultado = numero1 * numero2
        print("El resultado es: ", resultado)
    elif operacion.lower() == ("division") :
        try:
            resultado = numero1 / numero2
            print("El resultado es: ", resultado)
        except ZeroDivisionError:
            print("Error, no se puede dividir entre 0")
            exit()
    elif operacion.lower() == ("porcentaje"):
        resultado = (numero1 * numero2) / 100
        print("El %",numero2, "de" , numero1, "es: ", resultado)
    salida = input("Quiere salir? (escriba salir): ") .lower()