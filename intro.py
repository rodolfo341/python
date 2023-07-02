# #import math
# `continuar = True
# while continuar:
    

#     respuesta = input("¿Deseas continuar? (s/n): ")
#     print("Continuando..." if respuesta.lower() == "s" else "Saliendo...")
#     continuar = respuesta.lower() == "s"`

comando = ""
 
def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1]
    return palabra_invertida
 # Ejemplo de uso
palabra_ingresada = input("Ingresa una palabra: ")
palabra_invertida = invertir_palabra(palabra_ingresada)
print("Palabra invertida:", palabra_invertida)
