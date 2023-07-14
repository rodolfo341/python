import math
import msvcrt
def espera():
    print("\tPresiona cualquier tecla para continuar...\n")
    msvcrt.getch()

#   Ejercicios: Nivel 1
# 1   Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta crea un archivo llamado variables.py
# 
# 2   Escriba un comentario de python que diga 'Día 2: 30 días de programación en python'
# Día 2: 30 días de programación en python
# 3    Declarar una variable de nombre y asignarle un valor
# 4    Declarar una variable de apellido y asignarle un valor
# 5    Declarar una variable de nombre completo y asignarle un valor
# 6    Declarar una variable de país y asignarle un valor
# 7    Declarar una variable de ciudad y asignarle un valor
# 8    Declarar una variable de edad y asignarle un valor
# 9    Declarar una variable de año y asignarle un valor
# 10    Declarar una variable is_married y asignarle un valor
# 11   Declarar una variable is_true y asignarle un valor
# 12 Declarar una variable is_light_on y asignarle un valor
# 13 Declarar múltiples variables en una línea


#   Ejercicios: Nivel 1

# 1   Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta crea un archivo llamado variables.py
# //
# 2   Escriba un comentario de python que diga 'Día 2: 30 días de programación en python'
#Día 2: 30 días de programación en python
# 3    Declarar una variable de nombre y asignarle un valor
nombre = "Manchas"
print(f"nombre = {nombre}")
espera()

# 4    Declarar una variable de apellido y asignarle un valor
apellido = "Perro"
print(f"apellido = {apellido}")
espera()

# 5    Declarar una variable de nombre completo y asignarle un valor
nombreCompleto = f"{nombre} {apellido}"
print(f"nombreCompleto = {nombreCompleto}")
espera()

# 6    Declarar una variable de país y asignarle un valor
pais = "Chile"
print(f"pais = {pais}")
espera()

# 7    Declarar una variable de ciudad y asignarle un valor
ciudad = "Santiago"
print(f"ciudad = {ciudad}")
espera()

# 8    Declarar una variable de edad y asignarle un valor
edad = 51
print(f"edad = {edad}")
espera()

# 9    Declarar una variable de año y asignarle un valor
anio = 2023
print(f"año = {anio}")
espera()

# 10    Declarar una variable is_married y asignarle un valor
is_casado = True
if is_casado == True:
    print(f"is_casado = {is_casado}")
espera()
    
# 11   Declarar una variable is_true y asignarle un valor
is_true = False
print(f"el valos de is_true es:{is_true}")
espera()

# 12 Declarar una variable is_light_on y asignarle un valor
is_light = "es una luz"
print(f"is_light = {is_light}")
espera()

# 13 Declarar múltiples variables en una línea
x, y, z =1,2,3
print(f"x = {x} y = {y} z = {z}")
espera()



#Ejercicios: Nivel 2

#  1  Verifique el tipo de datos de todas sus variables usando la función incorporada type ()
print(f"E tipo de dato de {nombre} es : {type(nombre)}")
espera()

print(f"E tipo de dato de {apellido} es : {type(apellido)}")
espera()

print(f"E tipo de dato de {nombreCompleto} es : {type(nombreCompleto)}")
espera()

print(f"E tipo de dato de {pais} es : {type(pais)}")
espera()

print(f"E tipo de dato de {ciudad} es : {type(ciudad)}")
espera()

print(f"E tipo de dato de {edad} es : {type(edad)}")
espera()

print(f"E tipo de dato de {anio} es : {type(anio)}")
espera()

print(f"E tipo de dato de {is_casado} es : {type(is_casado)}")
espera()

print(f"E tipo de dato de {is_true} es : {type(is_true)}")
espera()

print(f"E tipo de dato de {is_light} es : {type(is_light)}")
espera()

#  2  Usando la len() , encuentre la longitud de su nombre función incorporada
print(f"La longitud e mi nombre es: {len(nombre)}")
espera()

#  3  Compare la longitud de su nombre y su apellido
print(f"La longitud e mi apellido es: {len(apellido)}")
espera()
diferencia = len(nombre) - len(apellido)
print(f"La diferencia entre la longitud de nombre y apellido es: {diferencia}")
espera()

#  4  Declarar 5 como num_one y 4 como num_two
num_uno = 5
num_dos = 4
print(f"num_uno = {num_uno}")
print(f"num_dos = {num_dos}")
espera()

#      i    Agregue num_one y num_two y asigne el valor a un total variable
total = num_uno + num_dos
print(f"total = {total}")
espera()

#     ii    Reste num_two de num_one y asigne el valor a una variable diff
diferencia = num_uno - num_dos
print(f"diferencia = {diferencia}")
espera()

#    iii    Multiplique num_two y num_one y asigne el valor a un producto variable
producto = num_uno * num_dos
print(f"producto = {producto}")
espera()

#     iv    Divide num_one por num_two y asigna el valor a una división variable
cociente = num_uno / num_dos
print(f"cociente = {cociente}")
espera()

#      v    Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
modulo = num_uno % num_dos
print(f"modulo = {modulo}")
espera()
print()

#     vi    Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
exponente = num_uno ** num_dos
print(f"exponente = {exponente}")
espera()

#    vii    Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
piso = num_uno // num_dos
print(f"piso = {piso}")
espera()

#  5  El radio de un círculo es de 30 metros.
circulo = 31
print(f"circulo = {circulo}")
espera()

#      i   Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
area_del_circulo = round(math.pi * circulo ** 2,2)
print(f"el area del circulo es : {area_del_circulo}")
espera()

#     ii   Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
circunferencia_del_circulo = round(2 * math.pi * circulo,2)
print(f"La circunferencia del circulo es : {circunferencia_del_circulo}")
espera()

#    iii  Tome el radio como entrada del usuario y calcule el área.
circulo = float(input("ingresa radio del circulo: "))
area_del_circulo = round(math.pi * circulo ** 2,2)
print(f"el area del circulo es : {area_del_circulo}")
espera()

#  6  Use la función de entrada incorporada para obtener el nombre, el apellido, el país y la edad de un usuario 
#     y almacene el valor en sus nombres de variables correspondientes
#  7  Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras reservadas 
#     o las palabras clave de Python


#Ejercicios: Nivel 2

#  1  Verifique el tipo de datos de todas sus variables usando la función incorporada type ()

#  2  Usando la len() , encuentre la longitud de su nombre función incorporada
#  3  Compare la longitud de su nombre y su apellido
#  4  Declarar 5 como num_one y 4 como num_two
#      i    Agregue num_one y num_two y asigne el valor a un total variable
#     ii    Reste num_two de num_one y asigne el valor a una variable diff
#    iii    Multiplique num_two y num_one y asigne el valor a un producto variable
#     iv    Divide num_one por num_two y asigna el valor a una división variable
#      v    Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
#     vi    Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
#    vii    Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
#  5  El radio de un círculo es de 30 metros.
#      i   Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
#     ii   Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
#    iii  Tome el radio como entrada del usuario y calcule el área.
#  6  Use la función de entrada incorporada para obtener el nombre, el apellido, el país y la edad de un usuario 
#     y almacene el valor en sus nombres de variables correspondientes
#  7  Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras reservadas 
#     o las palabras clave de Python
