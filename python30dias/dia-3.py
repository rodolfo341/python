import msvcrt
def esperar_tecla_para_continuar():
    print("Presiona cualquier tecla para continuar... \n\n")
    msvcrt.getch()




# Operadores aritméticos en Python
# Enteros (int)
esperar_tecla_para_continuar()
print("Operadores aritméticos en Python \n\n")

print('suma: 1 + 2 = ', 1 + 2)
print('Resta: 2 - 1 = ', 2 - 1)
print('Multiplicación: 2 * 3 = ', 2 * 3)
print ('División: 4 / 2 = ', 4 / 2)                         # La división en python da un número flotante
print('Division: 6 / 2 =', 6 / 2)
print('Division: 7 / 2 =', 7 / 2)
print('Division sin resto: 7 // 2 = ', 7 // 2)   # Da sin el número flotante o sin el resto
print('Módulo: 3 % 2 = ', 3 % 2)                           # Gives the modulo
print ('División sin el remanente: ', 7 // 3)
print('Exponencial: ', 3 ** 2)                     # Significa 3 * 3



# Numeros flotantes
esperar_tecla_para_continuar()
print("Numeros flotantes \n\n")

print('Numeros flotantes, PI = ', 3.14)
print('Numeros flotantes, gravedad = ', 9.81)



# Números complejos
esperar_tecla_para_continuar()
print("Números complejos \n\n")

print('Numeros complejos: 1 + 1j = ', 1 + 1j)
print('Multiplicación de números complejos: (1 + 1j) * (1-1j) = ',(1 + 1j) * (1-1j))




# Declarar la variable en la parte superior primero
esperar_tecla_para_continuar()
print("Declarar la variable en la parte superior primero \n\n")

# Operaciones aritméticas y asignación del resultado a una variable
esperar_tecla_para_continuar()
print("Operaciones aritméticas y asignación del resultado a una variable \n\n")
a = 3 # a es un nombre de variable y 3 es un tipo de datos entero
b = 2 # b es un nombre de variable y 3 es un tipo de datos entero
print("a = 3")
print("b = 2")

suma = a + b
diferencia = a - b
producto = a * b
division = a / b
modulo = a % b
division_piso = a // b
exponencial = a ** b

print(suma) # si no etiqueta su impresión con alguna cadena, nunca sabrá de dónde viene el resultado
print('a + b = ', suma)
print('a - b = ', diferencia)
print('a * b = ', producto)
print('a / b = ', division)
print('a % b = ', modulo)
print('a // b = ', division_piso)
print('a ** b = ', exponencial)





# Declarar valores y organizarlos juntos
esperar_tecla_para_continuar()
print("Declarar valores y organizarlos juntos \n\n")

numero_1 = 3
numero_2 = 4





# Operaciones aritméticas
esperar_tecla_para_continuar()
print("Operaciones aritméticas \n\n")

suma = numero_1 + numero_2
diferencia = numero_2 - numero_1
producto = numero_1 * numero_2
division = numero_2 / numero_2
modulo = numero_2 % numero_1




# Impresión de valores con etiqueta
esperar_tecla_para_continuar()
print("Impresión de valores con etiqueta \n\n")

print('suma: ', suma)
print('diferencia: ', diferencia)
print('producto: ', producto)
print('division: ', division
      )
print('modulo: ', modulo)



# Calcular el area de un círculo
esperar_tecla_para_continuar()
print("Calcular el area de un círculo \n\n")




radio = 10                                 # radio del círculo
area_del_circulo = 3.14 * radio ** 2         # dos * signo significa exponente o potencia
print('Area del círculo:', area_del_circulo)




# Calculando el area del rectangulo
esperar_tecla_para_continuar()
print("Calculando el area del rectangulo \n\n")

alto = 10
ancho = 20
area_del_rectangulo = alto * ancho
print('Area of rectangle:', area_del_rectangulo)



# Cálculo del peso de un objeto
esperar_tecla_para_continuar()
print("Cálculo del peso de un objeto \n\n")

masa = 75
gravedad = 9.81
masa = masa * gravedad
print(masa, 'N')

print(3 > 2)     # True, por que 3 es mayor que 2
print(3 >= 2)    # True, por que 3 es mayor que 2
print(3 < 2)     # False,  por que 3 es mayor que 2
print(2 < 3)     # True, por que 2 es menor que 3
print(2 <= 3)    # True, por que 2 es menor que 3
print(3 == 2)    # False, por que 3 no es igual que 2
print(3 != 2)    # True, por que 3 no es igual que 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False



# Comparación booleana
esperar_tecla_para_continuar()
print("Comparación booleana \n\n")

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)



# Comparación de otra forma
esperar_tecla_para_continuar()
print("Comparación de otra forma \n\n")

print('1 is 1', 1 is 1)                   # True - por que los valores de los datos son los mismos
print('1 is not 2', 1 is not 2)           # True - por que 1 no es 2
print('A in Rodolfo', 'A' in 'Rodolfo') # True - R encontrado en la cadena
print('B in Rodolfo', 'B' in 'Rodolfo') # False - no hay B mayúscula
print('Codificando' in 'Codificando para todos') # True - por que codificando para todos tiene la palabra codificando
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - por que ambas afirmaciones son verdaderas
print(3 > 2 and 4 < 3) # False - por que la segunda afirmación es falsa
print(3 < 2 and 4 < 3) # False - por que both statements are false
print(3 > 2 or 4 > 3)  # True - por que ambas afirmaciones son verdaderas
print(3 > 2 or 4 < 3)  # True - por que uno de los enunciados es verdadero
print(3 < 2 or 4 < 3)  # False - por que ambas afirmaciones son falsas
print(not 3 > 2)     # False - por que 3 > 2 es verdadero, entonces no verdadero da falso
print(not True)      # False - Negación, la operadora no se vuelve de verdadera a falsa
print(not False)     # True
print(not not True)  # True
print(not not False) # False