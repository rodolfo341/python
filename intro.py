#import math
continuar = True

while continuar:
    
    el_numero = 3
    for iterador in range(20):
       print(iterador)
       if iterador == 7:
          print("encontrado")
    

    respuesta = input("¿Deseas continuar? (s/n): ")
    print("Continuando..." if respuesta.lower() == "s" else "Saliendo...")
    continuar = respuesta.lower() == "s"

 
