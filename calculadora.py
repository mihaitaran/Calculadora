import suma, resta, multiplicacion, division

def calculadora():
    
    while True:
        n = int(input("""Introduzca qué desea hacer:
1 - Sumar
2 - Restar
3 - Multiplicación
4 - División
5 - Salir
"""))

        if n == 5:
            print("Saliendo...")
            break

        a = int(input("Introduzca el primer número: "))
        b = int(input("Introduzca el segundo número: "))

        if n == 1:
            print("El resultado es", suma.suma(a, b))
        elif n == 2:
            print("El resultado es", resta.resta(a, b))
        elif n == 3:
            print("El resultado es", multiplicacion.multiplicacion(a, b))
        elif n == 4:
            if b == 0:
                print("No divida números por 0")
                continue
            print("El resultado es", division.division(a, b))
        else:
            print("Opción no válida")

calculadora()