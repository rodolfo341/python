#import math
continuar = True

while continuar:
    edad = int(input("edad: "))
    res = "puede entrar" if 50 >= edad >=15 else "no puede entrar"
    print(res)

    respuesta = input("¿Deseas continuar? (s/n): ")
    print("Continuando..." if respuesta.lower() == "s" else "Saliendo...")
    continuar = respuesta.lower() == "s"

