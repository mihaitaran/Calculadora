import suma, resta

def calculadora():
    
    while True:
        n = int(input("""Introduzca qué desea hacer:
1 - Sumar
2 - Restar
3 - Salir
"""))

        if n == 3:
            print("Saliendo...")
            break

        a = int(input("Introduzca el primer número: "))
        b = int(input("Introduzca el segundo número: "))

        if n == 1:
            print("El resultado es", suma.suma(a, b))
        elif n == 2:
            print("El resultado es", resta.resta(a, b))
        else:
            print("Opción no válida")

calculadora()