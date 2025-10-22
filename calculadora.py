import suma, resta, multiplicacion

def calculadora():
    
    while True:
        n = int(input("""Introduzca qué desea hacer:
1 - Sumar
2 - Restar
3 - Multiplicación
4 - Salir
"""))

        if n == 4:
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
        else:
            print("Opción no válida")

calculadora()