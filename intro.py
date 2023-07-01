#import math
continuar = True

while continuar:
    
    for numero in range(20):
        print(numero)

    respuesta = input("¿Deseas continuar? (s/n): ")
    print("Continuando..." if respuesta.lower() == "s" else "Saliendo...")
    continuar = respuesta.lower() == "s"

