import sympy
import math
import msvcrt
def esperar_tecla_para_continuar():
    print("\n\tPresiona cualquier tecla para continuar... \n")
    msvcrt.getch()
    

# 1   Declara tu edad como variable Ingresea
# 2   Declara tu altura como una variable flotante
# 3   Declarar una variable que almacene un número complejo
# 4   Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y 
#     calcule el área de este triángulo (área = 0,5 xbxh).
#           Ingrese base: 20
#           Ingrese altura: 10
#           el area del el triangulo is 100
# 5   Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. 
#     Calcula el perímetro del triángulo (perímetro = a + b + c). 
#           Ingrese lado a: 5
#           Ingrese lado b: 4
#           Ingrese lado c: 3
#           el perimeter del el triangulo is 12
# 6   Obtenga la longitud y el ancho de un rectángulo usando el indicador. 
#     Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
# 7   Obtenga el radio de un círculo usando el indicador. 
#     Calcula el área (área = pi xrxr) y la circunferencia (c = 2 x pi xr) donde pi = 3,14.
# 8   Calcule la pendiente, la intersección x y la intersección y de y = 2x -2
# 9   La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la distancia euclidiana entre el punto 
#     (2, 2) y el punto (6,10)
# 10  Compara las pendientes en las tareas 8 y 9.
# 11  Calcula el valor de y (y = x^2 + 6x + 9). Trate de usar diferentes valores de x y descubra en qué valor de x y será 0
# 12  Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación falsa.
# 13  Use un operador para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
# 14  Espero que este curso no esté lleno de jerga . Use el operador in para verificar si hay jerga en la oración.
# 15  No hay 'on' tanto en dragon como en python
# 16  Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
# 17  Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?
# 18  Verifique si la división del piso de 7 por 3 es igual al valor int convertido de 2.7.
# 19  Compruebe si el tipo de '10' es igual al tipo de 10
# 20  Comprueba si int('9.8') es igual a 10
# 21  Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. 
#     ¿Calcular el salario de la persona?
#               Ingrese hours: 40
#               Ingrese rate per hour: 28
#               Your weekly earning is 1120
# 22  Escriba un script que solicite al usuario que ingrese el número de años. 
#     Calcular el número de segundos que puede vivir una persona. 
#     Supongamos que una persona puede vivir cien años. 
#               Ingrese number del years you have lived: 100
#               You have lived for 3153600000 seconds.
# 23  Escriba un script de Python que muestre la siguiente tabla 
#               1 1 1 1 1
#               2 1 2 4 8  
#               3 1 3 9 27
#               4 1 4 16 64
#               5 1 5 25 125


# 1   Declara tu edad como variable Ingresea
edad = 51
print(f"Mi edad es: {edad}")
esperar_tecla_para_continuar()

# 2   Declara tu altura como una variable flotante
altura = 1.7
print(f"mi estatura es {altura}")
esperar_tecla_para_continuar()

# 3   Declarar una variable que almacene un número complejo
num_complejo = (1 + 1j)
print(f"El valor del numero complejo es: {num_complejo}")
esperar_tecla_para_continuar()

# 4   Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y 
#     calcule el área de este triángulo (área = 0,5 x b x h).
#           Ingrese base: 20
#           Ingrese altura: 10
#           El area del triangulo sera 100
base_triangulo = float(input("Ingrese base: "))
altura_triangulo = float(input("Ingrese altura: "))
area = 0.5 * base_triangulo * altura_triangulo
print(f"El area del triangulo es: {area}")
esperar_tecla_para_continuar()


# 5   Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. 
#     Calcula el perímetro del triángulo (perímetro = a + b + c). 
#           Ingrese lado a: 5
#           Ingrese lado b: 4
#           Ingrese lado c: 3
#           el perimetro del triangulo is 12
lado_a = int(input("ingrese lado a: "))
lado_b = int(input("ingrese lado b: "))
lado_c = int(input("ingrese lado c: "))
perimetro = lado_a + lado_b + lado_c
print(f"El area del triangulo es: {perimetro}")
esperar_tecla_para_continuar()

# 6   Obtenga la longitud y el ancho de un rectángulo usando el indicador. 
#     Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
alto = int(input("Ingrese alto: "))
ancho = int(input("Ingrese ancho: "))
area = alto * ancho
perimetro = 2 * (alto + ancho)
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo: {perimetro}")
esperar_tecla_para_continuar()

# 7   Obtenga el radio de un círculo usando el indicador. 
#     Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.
radio = float(input("Radio: "))
area = round(math.pi * radio ** 2,2)
circunferencia = round(2 * math.pi * radio,2)
print(f"Area: {area}")
print(f"Circunferencia: {circunferencia}")
esperar_tecla_para_continuar()

# 8   Calcule la pendiente, la intersección x y la intersección y de y = 2x -2
pendiente8 = 2
interseccion_y = -2
interseccion_x = (0 - interseccion_y) / pendiente8

print(f"La pendiente es: {pendiente8}")
print(f"La intersección y es: {interseccion_y}")
print(f"La intersección x es: {interseccion_x}")
esperar_tecla_para_continuar()

# 9   La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la distancia euclidiana entre el punto 
#     (2, 2) y el punto (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pendiente9 = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"La pendiente es: {pendiente9}")
print(f"La distancia euclidiana es: {distancia}")
esperar_tecla_para_continuar()

# 10  Compara las pendientes en las tareas 8 y 9.
print(f"Pendiente8: {pendiente8}")
print(f"Pendiente9: {pendiente9}")
esperar_tecla_para_continuar()

# 11  Calcula el valor de y (y = x^2 + 6x + 9). Trate de usar diferentes valores de x y descubra en qué valor de x y será 0
# Definición de la ecuación
def calcular_y(x):
    return x**2 + 6*x + 9

# Calculando el valor de y para diferentes valores de x
valores_x = [-5, -3, 0, 2, 4]
for x in valores_x:
    y = calcular_y(x)
    print("Cuando x =", x, ", y =", y)

# Encontrando en qué valor de x y es igual a 0 (resolviendo la ecuación cuadrática)
from sympy import symbols, Eq, solve

x = symbols('x')
ecuacion = Eq(x**2 + 6*x + 9, 0)
soluciones = solve(ecuacion, x)

print("Los valores de x donde y es igual a 0 son:", soluciones)
esperar_tecla_para_continuar()

# 12  Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación falsa.
python = len("python")
dragon = len("dragon")
print(f"python tiene : {python} letras")
print(f"dragon tiene : {dragon} letras")
print(not python == dragon)
esperar_tecla_para_continuar()

# 13  Use el operador and para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
if "on" in "python" and "on" in "drogon":
    print(f"'on' esta en 'python' y tambien en 'drogon'")
else:
    print(f"'on' no esta 'python' y tambien en 'drogon'")
esperar_tecla_para_continuar()

# 14  Espero que este curso no esté lleno de jerga . Use el operador in para verificar si hay jerga en la oración.
oracion = "Espero que este curso no esté lleno de jerga"
if "jerga" in oracion:
    print(f"'jerga' esta en la oracion")
else:
    print(f"'jerga' no esta en la oracion")
esperar_tecla_para_continuar()

# 15  No hay 'on' tanto en dragon como en python
if "on" in "python" and "on" in "drogon":
    print(f"'no hay on' 'python' como en 'drogon'")
esperar_tecla_para_continuar()

# 16  Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
longitud_python = str(float(int(len("python"))))
print(f"tipo de dato de longitud_python: {type(longitud_python)}")
esperar_tecla_para_continuar()

# 17  Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?
numero = int(input("Numero = "))
if numero % 2 == 0:
    print(f"Es par")
else:
    print(f"Es impar")
esperar_tecla_para_continuar()

# 18  Verifique si la división del piso de 7 por 3 es igual al valor int convertido de 2.7.
if 7 % 3 == int(2.7):
    print("Es igual")
else:
    print("no es igual")
esperar_tecla_para_continuar()

# 19  Compruebe si el tipo de '10' es igual al tipo de 10

#print(f": {}")
#esperar_tecla_para_continuar()

# 20  Comprueba si int('9.8') es igual a 10

#print(f": {}")
#esperar_tecla_para_continuar()

# 21  Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. 
#     ¿Calcular el salario de la persona?
#               Ingrese hours: 40
#               Ingrese rate per hour: 28
#               Your weekly earning is 1120

#print(f": {}")
#esperar_tecla_para_continuar()

# 22  Escriba un script que solicite al usuario que ingrese el número de años. 
#     Calcular el número de segundos que puede vivir una persona. 
#     Supongamos que una persona puede vivir cien años. 
#               Ingrese number del years you have lived: 100
#               You have lived for 3153600000 seconds.

#print(f": {}")
#esperar_tecla_para_continuar()

# 23  Escriba un script de Python que muestre la siguiente tabla 
#               1 1 1 1 1
#               2 1 2 4 8  
#               3 1 3 9 27
#               4 1 4 16 64
#               5 1 5 25 125

#print(f": {}")
#esperar_tecla_para_continuar()
