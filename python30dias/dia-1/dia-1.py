
import msvcrt

def esperar_tecla_para_continuar():
    print("Presiona cualquier tecla para continuar...")
    msvcrt.getch()

# Introducción
# Dia 1 de 30 Dias del desafio Python

print("Operaciones básicas")
print("suma",2 + 3)                 # Suma(+) 5
print("Resta",3 - 1)                # Resta(-) 2
print("Multiplicación",2 * 3)       # Multiplicación(*) 6
print("División",3 / 2)             # División(/) 1.5
print("Exponeciación",5 ** 3)       # Eexponenciación(**) 125
print("Módulo",3 % 2)               # Moduo(%) 1
print("División redondeo",3 // 2)   # División redondeo(//) 1

esperar_tecla_para_continuar()
# Comprobar de tipos de datos

print(type(10))                     # Int
print(type(3.14))                   # Float
print(type(1 + 3j))                 # Complex
print(type('Rodolfo'))              # String
print(type([1, 2, 3]))              # List
print(type({'Nombre':'Aravena'}))   # Dictionary
print(type({9.8, 3.14, 2.7}))       # Set
print(type((9.8, 3.14, 2.7)))       # Tuple