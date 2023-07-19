"""
# Formato de cadena de estilo antiguo (% operador)
esperar_tecla_para_continuar()
print("Formato de cadena de estilo antiguo (% operador)")
# Strings only
nombre = 'Rodolfo'
apellido = 'Aravena'
language = 'Python'
cadena_formateada = 'I am %s %s. I teach %s' %(nombre, apellido, language)
print(cadena_formateada)

# Strings  and numbers
radio = 10
pi = 3.14
area = pi * radio ** 2
cadena_formateada = 'El area del circulo con radio %d is %.2f.' %(radio, area) # 2 Refiere a los 2 dígitos significativos después del punto.

librerias_python = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
cadena_formateada = 'Las siguientes son librerias de python:%s' % (librerias_python)
print(cadena_formateada) # "Las siguientes son librerias de python:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

esperar_tecla_para_continuar()
# Este formato se introdujo en la versión 3 de Python. 
print("Este formato se introdujo en la versión 3 de Python. ")

nombre = 'Rodolfo'
apellido = 'Aravena'
language = 'Python'
cadena_formateada = 'Yo soy {} {}. Yo enseño {}'.format(nombre, apellido, language)
print(cadena_formateada)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
# 4 + 3 = 7
# 4 - 3 = 1
# 4 * 3 = 12
# 4 / 3 = 1.33
# 4 % 3 = 1
# 4 // 3 = 1
# 4 ** 3 = 64

# Strings  and numbers
radio = 10
pi = 3.14
area = pi * radio ** 2
cadena_formateada = 'El area de un circulo con un radio {} es {:.2f}.'.format(radio, area) # 2 digitos despues del decimal
print(cadena_formateada)
"""

print(1 / 1)



