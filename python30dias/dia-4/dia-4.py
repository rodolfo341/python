import msvcrt
def esperar_tecla_para_continuar():
    print("\n\tPresiona cualquier tecla para continuar... \n")
    msvcrt.getch()
    
    
# Comentario de una sola línea
esperar_tecla_para_continuar()
print("#Comentario de una sola linea")    
print("\"\"\"\n\tComentario \n \tmulti\n\tlinea\n\"\"\"")
esperar_tecla_para_continuar() 

letra = 'P'                 # Una cadena puede ser un solo carácter o un montón de textos
print(letra)                # P
print(len(letra))           # 1
saludo = 'Hola, mundo!'     # La cadena puede ser una comilla simple o doble, "¡Hola, mundo!"
print(saludo)               # Hola, mundo!
print(len(saludo))          # 13
sentencia = "Espero que estés disfrutando de 30 días del desafío de Python."
print(sentencia)

esperar_tecla_para_continuar()
# Cadena multilínea
# Con comillas simples
cadena_multilinea = '''Soy profesor y disfruto enseñando.
No encontré nada tan gratificante como empoderar a las personas.
Es por eso que creé 30 días de python.'''
print(cadena_multilinea)

esperar_tecla_para_continuar()
print("Otra fiorma de hacer lo mismo")
# Otra forma de hacer lo mismo
# con comillas dobles
cadena_multilinea = """Soy profesor y disfruto enseñando.
No encontré nada tan gratificante como empoderar a las personas.
Es por eso que creé 30 días de python."""
print(cadena_multilinea)

esperar_tecla_para_continuar()
print("Concatenacion de cadena\n")
# Concatenación de cadenas
nombre = 'Rodolfo'
apellido = 'Aravena'
espacio = ' '
nombre_completo = nombre  +  espacio + apellido
print(nombre_completo) # Rodolfo Aravena

esperar_tecla_para_continuar()
print("Verificación de la longitud de una cadena usando la función incorporada len()\n")
# Verificación de la longitud de una cadena usando la función incorporada len()
print(len(nombre))                  # 8
print(len(apellido))                # 7
print(len(nombre) > len(apellido))  # True
print(len(nombre_completo))         # 15

esperar_tecla_para_continuar()
print("desesctructurar caracteres\n")
#### desesctructurar caracteres
lenguaje = 'Python'
a,b,c,d,e,f = lenguaje              # Desestructurar caracteres de secuencia en variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

esperar_tecla_para_continuar()
print("Acceso a caracteres en cadenas por índice\n")
# Acceso a caracteres en cadenas por índice
lenguaje = 'Python'
primera_letra = lenguaje[0]
print(primera_letra) # P
segunda_letra = lenguaje[1]
print(segunda_letra) # y
ultimo_indice = len(lenguaje) - 1
ultima_letra = lenguaje[ultimo_indice]
print(ultima_letra) # n

esperar_tecla_para_continuar()
print("Si queremos comenzar desde el extremo derecho, podemos usar ")
print("la indexación negativa. -1 es el último índice\n")
# Si queremos comenzar desde el extremo derecho, podemos usar la indexación negativa. 
# -1 es el último índice
lenguaje = 'Python'
ultima_letra = lenguaje[-1]
print(ultima_letra) # n
pen_ultimo = lenguaje[-2]
print(pen_ultimo) # o

esperar_tecla_para_continuar()
print("Rebanar\n")
# rebanar
lenguaje = 'Python'
primeros_tres = lenguaje[0:3] # starts at zero index and up to 3 but not include 3
ultimos_tres = lenguaje[3:6]
print(ultimos_tres) # hon
# De otra manera
ultimos_tres = lenguaje[-3:]
print(ultimos_tres)   # hon
ultimos_tres = lenguaje[3:]
print(ultimos_tres)   # hon

esperar_tecla_para_continuar()
# Saltar caracteres al dividir cadenas de Python
lenguaje = 'Python'
pto = lenguaje[0:6:2] # 
print(pto) # pto

esperar_tecla_para_continuar()

# Secuencias de escape
print('Espero que todos disfruten del desafío Python.\n ¿Y tú?') # salto de línea
print('Días\tTemas\tEjercicios')
print('Dia 1\t3\t5')
print('Dia 2\t3\t5')
print('Dia 3\t3\t5')
print('Dia 4\t3\t5')
print('Este es un símbolo de slash (\\)')                       # Para escribir una slash
print('En todo lenguaje de programación comienza con \"Hola, mundo!\"')








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

esperar_tecla_para_continuar()
print("Uso de format (f)")
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')










# Métodos de cadena
# capitalize(): Convierte el primer carácter de la cadena a letra mayúscula

desafio = 'treinta dias de python'
print(desafio.capitalize())         # 'treinta dias de python'

# count(): devuelve apariciones de subcadena en cadena, count(substring, start=.., end=..)

desafio = 'treinta dias de python'
print(desafio.count('y'))           # 3
print(desafio.count('y', 7, 14))    # 1
print(desafio.count('th'))          # 2`

esperar_tecla_para_continuar()
print("\n")
# endswith(): Comprueba si una cadena termina con un final específico

desafio = 'treinta dias de python'
print(desafio.endswith('on'))   # True
print(desafio.endswith('tion')) # False

# expandtabs(): Reemplaza el carácter de tabulación con espacios, 
# el tamaño de tabulación predeterminado es 8. 
# Toma el argumento de tamaño de tabulación

desafio = 'treinta\tDias\tde\tpython'
print(desafio.expandtabs())   # 'treinta  Dias    de      python'
print(desafio.expandtabs(10)) # 'treinta    Dias      de        python'

esperar_tecla_para_continuar()
print("\n")
# find(): Devuelve el índice de la primera aparición de la subcadena

desafio = 'treinta dias de python'
print(desafio.find('y'))  # 5
print(desafio.find('th')) # 0

esperar_tecla_para_continuar()
print("\n")
# format()	formatea la cadena en una salida más agradable    
nombre = 'Rodolfo'
apellido = 'Aravena'
trabajo = 'profesor'
pais = 'Chile'
sentencia = 'Yo soy {} {}. Soy un {}. Vivo {}.'.format(nombre, apellido, trabajo, pais)
print(sentencia) # Yo soy Rodolfo Aravena. Soy un profesor. Vivo en Chile.

radio = 10
pi = 3.14
area = pi                           # radio ## 2
resultado = 'El área del círculo con radio de {} es {}'.format(str(radio), str(area))
print(resultado) # The area of circle con radio de 10 is 314.0

esperar_tecla_para_continuar()
print("\n")
# index(): Devuelve el índice de la subcadena
desafio = 'treinta dias de python'
print(desafio.find('y'))            # 5
print(desafio.find('th'))           # 0

esperar_tecla_para_continuar()
print("\n")
# isalnum(): Comprueba el carácter alfanumérico

desafio = 'treinta dias de Python'
print(desafio.isalnum())            # True

desafio = '30 dias de Python'
print(desafio.isalnum())            # True

desafio = 'treinta dias de python'
print(desafio.isalnum())            # False

desafio = 'treinta dias de python 2019'
print(desafio.isalnum())            # False

esperar_tecla_para_continuar()
print("\n")
# isalpha(): Comprueba si todos los caracteres son alfabetos

desafio = 'treinta dias de python'
print(desafio.isalpha())            # True
num = '123'
print(num.isalpha())                # False

esperar_tecla_para_continuar()
print("\n")
# isdecimal(): Checks Decimal Characters

desafio = 'treinta dias de python'
print(desafio.find('y'))             # 5
print(desafio.find('th'))            # 0

esperar_tecla_para_continuar()
print("\n")
# isdigit(): Verifica si hay digitos en un caracter

desafio = 'treinta'
print(desafio.isdigit())            # False
desafio = '30'
print(desafio.isdigit())              # True

esperar_tecla_para_continuar()
print("\n")
# isdecimal():Comprueba los caracteres decimales

num = '10'
print(num.isdecimal())              # True
num = '10.5'
print(num.isdecimal())              # False

esperar_tecla_para_continuar()
print("\n")
# isidentifier():Verifica el identificador válido 
# significa que verifica si una cadena es un nombre de variable válido

desafio = '30 dias de Python'
print(desafio.isidentifier())       # False, porque empieza con un numero
desafio = 'treinta_Dias_of_python'
print(desafio.isidentifier())       # True

esperar_tecla_para_continuar()
print("\n")
# islower(): Comprueba si todos los caracteres en una cadena están en minúsculas

desafio = 'treinta dias de python'
print(desafio.islower())            # True
desafio = 'treinta dias de python'
print(desafio.islower())            # False

esperar_tecla_para_continuar()
print("\n")
# isupper(): devuelve verdadero todos los caracteres están en mayúsculas

desafio = 'treinta dias de python'
print(desafio.isupper())            #  False
desafio = 'treinta dias de python'
print(desafio.isupper())            # True

esperar_tecla_para_continuar()
print("\n")
# isnumeric(): Comprueba los caracteres numéricos

num = '10'
print(num.isnumeric())              # True
print('ten'.isnumeric())            # False

esperar_tecla_para_continuar()
print("\n")
# join(): Devuelve una cadena concatenada

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
resultado = '#, '.join(web_tech)
print(resultado) # 'HTML# CSS# JavaScript# React'

esperar_tecla_para_continuar()
print("\n")
# strip(): Elimina los caracteres iniciales y finales

desafio = ' treinta dias de python '
print(desafio.strip('y'))           # 5

esperar_tecla_para_continuar()
print("")
# replace(): Reemplaza la subcadena dentro

desafio = 'treinta dias de python'
print(desafio.replace('python', 'coding')) # 'treinta Dias de codigo'

esperar_tecla_para_continuar()
print("")
# split():Divide la cadena desde la izquierda

desafio = 'treinta dias de python'
print(desafio.split())              # ['treinta', 'Dias', 'de', 'python']

esperar_tecla_para_continuar()
print("")
# title(): Devuelve una cadena de título en mayúsculas

desafio = 'treinta dias de python'
print(desafio.title())              # treinta dias de python

esperar_tecla_para_continuar()
print("swapcase(): Checks if String Starts with the Specified String\n")
# swapcase(): Checks if String Starts with the Specified String
  
desafio = 'treinta dias de python'
print(desafio.swapcase())           # treinta dias de python
desafio = 'treinta dias de python'
print(desafio.swapcase())           # treinta dias de python

esperar_tecla_para_continuar()
print("startswith(): Comprueba si la cadena comienza con la cadena especificada\n")
# startswith(): Comprueba si la cadena comienza con la cadena especificada


desafio = 'treinta dias de python'
print(desafio.startswith('treinta')) # True
desafio = '30 Dias of python'
print(desafio.startswith('treinta')) # False
