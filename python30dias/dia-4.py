
# Comentario de una sola línea
letra = 'P'                 # Una cadena puede ser un solo carácter o un montón de textos
print(letra)                # P
print(len(letra))           # 1
saludo = 'Hola, mundo!'     # La cadena puede ser una comilla simple o doble, "¡Hola, mundo!"
print(saludo)               # Hola, mundo!
print(len(saludo))          # 13
sentencia = "Espero que estés disfrutando de 30 días del desafío de Python."
print(sentencia)

# Cadena multilínea
# Con comillas simples
cadena_multilinea = '''Soy profesor y disfruto enseñando.
No encontré nada tan gratificante como empoderar a las personas.
Es por eso que creé 30 días de python.'''
print(cadena_multilinea)
# Otra forma de hacer lo mismo
# con comillas dobles
cadena_multilinea = """Soy profesor y disfruto enseñando.
No encontré nada tan gratificante como empoderar a las personas.
Es por eso que creé 30 días de python."""
print(cadena_multilinea)

# Concatenación de cadenas
nombre = 'Rodolfo'
apellido = 'Aravena'
espacio = ' '
nombre_completo = nombre  +  espacio + apellido
print(nombre_completo) # Rodolfo Aravena
# Verificación de la longitud de una cadena usando la función incorporada len()
print(len(nombre))                  # 8
print(len(apellido))                # 7
print(len(nombre) > len(apellido))  # True
print(len(nombre_completo))         # 15

#### desesctructurar caracteres
lenguaje = 'Python'
a,b,c,d,e,f = lenguaje              # Desestructurar caracteres de secuencia en variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Acceso a caracteres en cadenas por índice
lenguaje = 'Python'
primera_letra = lenguaje[0]
print(primera_letra) # P
segunda_letra = lenguaje[1]
print(segunda_letra) # y
ultimo_indice = len(lenguaje) - 1
ultima_letra = lenguaje[ultimo_indice]
print(ultima_letra) # n

# Si queremos comenzar desde el extremo derecho, podemos usar la indexación negativa. 
# -1 es el último índice
lenguaje = 'Python'
ultima_letra = lenguaje[-1]
print(ultima_letra) # n
pen_ultimo = lenguaje[-2]
print(pen_ultimo) # o

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

# Saltar caracteres al dividir cadenas de Python
lenguaje = 'Python'
pto = lenguaje[0:6:2] # 
print(pto) # pto

# Secuencias de escape
print('Espero que todos disfruten del desafío Python.\n ¿Y tú?') # salto de línea
print('Días\tTemas\tEjercicios')
print('Dia 1\t3\t5')
print('Dia 2\t3\t5')
print('Dia 3\t3\t5')
print('Dia 4\t3\t5')
print('Este es un símbolo de slash (\\)')                       # Para escribir una slash
print('En todo lenguaje de programación comienza con \"Hola, mundo!\"')

# Métodos de cadena
# capitalize(): Convierte el primer carácter de la cadena a letra mayúscula

desafio = 'treinta dias de python'
print(desafio.capitalize())         # 'treinta dias de python'

# count(): devuelve apariciones de subcadena en cadena, count(substring, start=.., end=..)

desafio = 'treinta dias de python'
print(desafio.count('y'))           # 3
print(desafio.count('y', 7, 14))    # 1
print(desafio.count('th'))          # 2`

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

# find(): Devuelve el índice de la primera aparición de la subcadena

desafio = 'treinta dias de python'
print(desafio.find('y'))  # 5
print(desafio.find('th')) # 0

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

# index(): Devuelve el índice de la subcadena
desafio = 'treinta dias de python'
print(desafio.find('y'))            # 5
print(desafio.find('th'))           # 0

# isalnum(): Comprueba el carácter alfanumérico

desafio = 'treinta dias de Python'
print(desafio.isalnum())            # True

desafio = '30 dias de Python'
print(desafio.isalnum())            # True

desafio = 'treinta dias de python'
print(desafio.isalnum())            # False

desafio = 'treinta dias de python 2019'
print(desafio.isalnum())            # False

# isalpha(): Comprueba si todos los caracteres son alfabetos

desafio = 'treinta dias de python'
print(desafio.isalpha())            # True
num = '123'
print(num.isalpha())                # False

# isdecimal(): Checks Decimal Characters

desafio = 'treinta dias de python'
print(desafio.find('y'))             # 5
print(desafio.find('th'))            # 0

# isdigit(): Verifica si hay digitos en un caracter

desafio = 'treinta'
print(desafio.isdigit())            # False
desafio = '30'
print(desafio.isdigit())              # True

# isdecimal():Comprueba los caracteres decimales

num = '10'
print(num.isdecimal())              # True
num = '10.5'
print(num.isdecimal())              # False


# isidentifier():Verifica el identificador válido 
# significa que verifica si una cadena es un nombre de variable válido

desafio = '30 dias de Python'
print(desafio.isidentifier())       # False, porque empieza con un numero
desafio = 'treinta_Dias_of_python'
print(desafio.isidentifier())       # True


# islower(): Comprueba si todos los caracteres en una cadena están en minúsculas

desafio = 'treinta dias de python'
print(desafio.islower())            # True
desafio = 'treinta dias de python'
print(desafio.islower())            # False

# isupper(): devuelve verdadero todos los caracteres están en mayúsculas

desafio = 'treinta dias de python'
print(desafio.isupper())            #  False
desafio = 'treinta dias de python'
print(desafio.isupper())            # True


# isnumeric(): Comprueba los caracteres numéricos

num = '10'
print(num.isnumeric())              # True
print('ten'.isnumeric())            # False

# join(): Devuelve una cadena concatenada

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
resultado = '#, '.join(web_tech)
print(resultado) # 'HTML# CSS# JavaScript# React'

# strip(): Elimina los caracteres iniciales y finales

desafio = ' treinta dias de python '
print(desafio.strip('y'))           # 5

# replace(): Reemplaza la subcadena dentro

desafio = 'treinta dias de python'
print(desafio.replace('python', 'coding')) # 'treinta Dias de codigo'

# split():Divide la cadena desde la izquierda

desafio = 'treinta dias de python'
print(desafio.split())              # ['treinta', 'Dias', 'de', 'python']

# title(): Devuelve una cadena de título en mayúsculas

desafio = 'treinta dias de python'
print(desafio.title())              # treinta dias de python

# swapcase(): Checks if String Starts with the Specified String
  
desafio = 'treinta dias de python'
print(desafio.swapcase())           # treinta dias de python
desafio = 'treinta dias de python'
print(desafio.swapcase())           # treinta dias de python

# startswith(): Comprueba si la cadena comienza con la cadena especificada

desafio = 'treinta dias de python'
print(desafio.startswith('treinta')) # True
desafio = '30 Dias of python'
print(desafio.startswith('treinta')) # False
