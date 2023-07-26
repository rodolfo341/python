import msvcrt
def esperar_tecla_para_continuar():
    print("\n\tPresiona cualquier tecla para continuar... \n")
    msvcrt.getch()
""""
#   1  Concatene la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.
#   2  Concatene la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'.
#   3  Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".
#   4  Imprime la empresa variable usando print() .
#   5  Imprima la longitud de la cadena de caracteres de la empresa utilizando el método len() e print() .
#   6  Cambie todos los caracteres a letras mayúsculas usando el método upper() .
#   7  Cambie todos los caracteres a letras minúsculas usando el método lower() .
#   8  Use los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena "Codificacion para todos" .
#   9  Corte (corte) la primera palabra de la cadena "Codificacion para todos" .
#  10  Verifique si la cadena "Codificacion para todos" contiene una palabra Coding usando el método index, find u otros métodos.
#  11  Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.
#  12  Cambie Python para todos a Python para todos usando el método de reemplazo u otros métodos.
#  13  Divida la cadena 'Codificación para todos' usando el espacio como separador (split()) .
#  14  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma.
#  15  ¿Cuál es el carácter en el índice 0 en la cadena "Codificacion para todos" ?
#  16  ¿Cuál es el último índice de la cadena "Codificacion para todos" ?
#  17  Qué carácter está en el índice 10 en la cadena "Codificación para todos".
#  18  Cree un acrónimo o una abreviatura para el nombre 'Python For Everyone'.
#  19  Cree un acrónimo o una abreviatura para el nombre 'Codificación para todos'.
#  20  Use index para determinar la posición de la primera aparición de C en "Codificacion para todos".
#  21  Utilice el índice para determinar la posición de la primera aparición de F en "Codificacion para todos".
#  22  Use rfind para determinar la posición de la última aparición de l en "Codificacion para todos" People.
#  23  Use índice o busque para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente #      oración: 'No puede terminar una oración con porque porque porque es una conjunción'
#  24  Use rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No #      puede terminar una oración con porque porque porque es una conjunción'
#  25  Corta la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque porque #      porque es una conjunción'
#  26  Encuentre la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puede terminar #      una oración con porque porque porque es una conjunción'
#  27  Corta la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque porque #      porque es una conjunción'
#  28  ¿'"Codificacion para todos"' comienza con una subcadena Coding ?
#  29  ¿'Codificación para todos' termina con una codificación de subcadena ?
#  30  ' Codificación para todos ', elimine los espacios finales izquierdo y derecho en la cadena dada. 
#  31  ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():
#           30DíasDePython
#           treinta_dias_de_python
#  32  La siguiente lista contiene los nombres de algunas de las bibliotecas de Python: ['Django', 'Flask', 'Bottle', #      'Pyramid', 'Falcon']. Únase a la lista con un hash con cadena de espacio. 
#  33  Use la secuencia de escape de nueva línea para separar las siguientes oraciones. 
#           I am enjoying this challenge.
#           I just wonder what is next.
#  34  Use una secuencia de escape de tabulación para escribir las siguientes líneas. 
#           Name      Age     Country   City
#           Asabeneh  250     Finland   Helsinki
#  35  Utilice el método de formato de cadena para mostrar lo siguiente: 
#           radius = 10
#           area = 3.14 * radius ** 2
#           The area of a circle with radius 10 is 314 meters square.
#  36  Haga lo siguiente usando métodos de formato de cadena: 
#           8 + 6 = 14
#           8 - 6 = 2
#           8 * 6 = 48
#           8 / 6 = 1.33
#           8 % 6 = 2
#           8 // 6 = 1
#           8 ** 6 = 262144





#   1  Concatene la cadena 'Treinta', 'Días', 'De', 'Python' en una sola cadena, 'Treinta días de Python'.
_30 = "Treinta"
d = "Días"
de = "De"
p = "Python"
print("Concatenacion")
print('Treinta ' 'Días ' 'De ' 'Python')
print('Treinta ' + 'Días ' + 'De ' + 'Python')
print('Treinta', 'Días', 'De', 'Python')
print(f"{_30} {d} {de} {p}")
#print('Treinta' 'Días' 'De' 'Python')
#print('Treinta' 'Días' 'De' 'Python')

#   2  Concatene la cadena 'Codificación', 'Para', 'Todos' en una sola cadena, 'Codificación para todos'.
esperar_tecla_para_continuar()
print(f"concatenacion")
print('Codificación', 'Para', 'Todos')

#   3  Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".
esperar_tecla_para_continuar()
print("Crear la variable 'empresa' con el valor \"Codificacion para todos\"")
"""
empresa = "Codificación para todos"
"""
#   4  Imprime la empresa variable usando print() .
esperar_tecla_para_continuar()
print("Imprime a: 'empresa'")
print(empresa)

#   5  Imprima la longitud de la cadena de caracteres de la empresa utilizando el método len() e print() .
esperar_tecla_para_continuar()
empresa_len = len(empresa)
print(f"Metodo 'len()' \"{empresa_len}\"")

#   6  Cambie todos los caracteres a letras mayúsculas usando el método upper() .
esperar_tecla_para_continuar()
empresa_upper = empresa.upper()
print(f"Metodo 'upper()' \"{empresa_upper}\"")

#   7  Cambie todos los caracteres a letras minúsculas usando el método lower() .
esperar_tecla_para_continuar()
empresa_lower = empresa.lower()
print(f"Metodo 'lower()' \"{empresa_lower}\"")

#   8  Use los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena "Codificacion para todos".
esperar_tecla_para_continuar()
empresa_capitalize = empresa.capitalize()
print(f"Metodo 'capitalize()' \"{empresa_capitalize}\"")

esperar_tecla_para_continuar()
empresa_title = empresa.capitalize()
print(f"Metodo 'title()' \"{empresa_title}\"")

esperar_tecla_para_continuar()
empresa_swapcase = empresa.swapcase()
print(f"Metodo 'swapcase()' \"{empresa_swapcase}\"")

#   9  Corte(slice) la primera palabra de la cadena "Codificacion para todos".
rebanada1 = slice(0,12)
rebanada2 = slice(13,17)
rebanada3 = slice(18,22)
print(empresa[rebanada1])
print(empresa[rebanada2])
print(empresa[rebanada3])

#  10  Verifique si la cadena "Codificacion para todos" contiene una palabra "Codificacion" usando el método index, find u otros métodos.
esperar_tecla_para_continuar()
aparicion = empresa.index("Codificación")
print(f"la primera aparicion de \"Codificacion\" es en el indice [{aparicion}]")

#  11  Reemplace la palabra "codificación" en la cadena 'Codificación para todos' por Python.
nueva_empresa = empresa.replace("Codificación","Natación")
print(f"Nueva cadena = {nueva_empresa}")
esperar_tecla_para_continuar()

#  12  Cambie "Python para cada uno" a "Python para todos" usando el método de reemplazo u otros métodos.
cadena_original = "Python para cada uno"
print(f"cadena_original = {cadena_original}")
cadena_nueva = cadena_original.replace("cada uno","todos")
print(f"cadena_nueva = {cadena_nueva}")
esperar_tecla_para_continuar()

#  13  Divida la cadena 'Codificación para todos' usando el espacio como separador (split()) .
separador = empresa.split("-")
print(separador)

#  14  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma.
lista_empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
separador = lista_empresas.split(",")
print(separador)
esperar_tecla_para_continuar()

#  15  ¿Cuál es el carácter en el índice 0 en la cadena "Codificacion para todos" ?
caracter_0 = empresa[0]
print(caracter_0)
esperar_tecla_para_continuar()

#  16  ¿Cuál es el último índice de la cadena "Codificacion para todos" ?
caracter_0 = empresa[-1]
print(caracter_0)
esperar_tecla_para_continuar()

#  17  Qué carácter está en el índice 10 en la cadena "Codificación para todos".
caracter_0 = empresa[10]
print(caracter_0)
esperar_tecla_para_continuar()

#  18  Cree un acrónimo o una abreviatura para el nombre 'Python para cada uno'.
texto = "Python Para Cada Uno"
palabras = texto.split()
primeras_letras = ""

for palabra in palabras:
    primera_letra = palabra[0]
    primeras_letras += primera_letra    

print(f"Acrónimo de \"Python Para Cada Uno\" = {primeras_letras}")
esperar_tecla_para_continuar()

#  19  Cree un acrónimo o una abreviatura para el nombre 'Codificación Para Todos'.
texto = "Codificación Para Todos"
palabras = texto.split()
primeras_letras = ""

for palabra in palabras:
    primera_letra = palabra[0]
    primeras_letras += primera_letra    

print(f"Acrónimo de \"Codificación Para Todos\" = {primeras_letras}")
esperar_tecla_para_continuar()

#  20  Use index para determinar la posición de la primera aparición de C en "Codificacion para todos".
texto = "Codificacion para todos"
letra = "C"
posicion = texto.index("C")
print(f"La letra 'C' esta en la posición: {posicion}")
esperar_tecla_para_continuar()

#  21  Utilice el índice para determinar la posición de la primera aparición de T en "Codificacion para todos".
texto = "Codificacion para todos"
letra = "t"
posicion = texto.index("t")
print(f"La letra 'C' esta en la posición: {posicion}")
esperar_tecla_para_continuar()

#  22  Use rfind para determinar la posición de la última aparición de "a" en "Codificacion para todos" People.
texto = "Codificacion para todos"
largo_cadena = texto.rfind("") - 1 # longitud de la cadena
indice = texto.rfind("a",0,largo_cadena)
print(f"Ultima aparicion de la letra \"a\" en la cadena es en el indice: {indice}")
esperar_tecla_para_continuar()

#  23  Use índice o busque para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente 
#  oración: 'No puede terminar una oración con porque porque porque es una conjunción'
texto = "No puede terminar una oración con porque porque porque es una conjunción"
posicion = texto.find("porque")
print(f"la posicion de la palabra \"porque\" esta en el indice [{posicion}]")
esperar_tecla_para_continuar()


#  24  Use rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 
# 'No puede terminar una oración con porque porque porque es una conjunción'
oracion = "No puede terminar una oración con porque porque porque es una conjunción"
palabra = "porque"
ultim_indice = oracion.rindex(palabra)
print(f"La ultima vez que aparece {palabra} es en el indice {ultim_indice}")
esperar_tecla_para_continuar()

#  25  Corta la frase 'porque porque porque' en la siguiente oración: 
# 'No puedes terminar una oración con porque porque porque es una conjunción'
oracion = "No puedes terminar una oración con porque porque porque es una conjunción"
palabra = "porque"
partes = oracion.split(palabra)
print(partes)

#  26  Encuentre la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 
# 'No puede terminar una oración con porque porque porque es una conjunción'
texto = "No puede terminar una oración con porque porque porque es una conjunción"
posicion = texto.find("porque")
print(f"la posicion de la palabra \"porque\" esta en el indice [{posicion}]")
esperar_tecla_para_continuar()

#  27  Corta la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque porque #      porque es una conjunción'
oracion = "No puedes terminar una oración con porque porque porque es una conjunción"
palabra = "porque"
partes = oracion.split(palabra)
print(partes)
esperar_tecla_para_continuar()

#  28  ¿'"Codificacion para todos"' comienza con una subcadena Codificacion ?
oracion = "Codificacion para todos"
palabra = "Codificacion"
posicion = oracion.find(palabra)
if posicion == 0:
    print(f"La palabra {palabra} es al comienzo ")
else:
    print(f"La palabra {palabra} no es al comienzo ")
esperar_tecla_para_continuar()

#  29  ¿'Codificación para todos' termina con una codificación de subcadena Codificacion ?
oracion = "Codificacion para todos-"
palabra = "Codificacion"

if oracion.endswith(palabra):
    print(f"La palabra {palabra} esta al final")
else:
    print(f"La palabra {palabra} no esta al final")
esperar_tecla_para_continuar()

#  30  ' Codificación para todos ', elimine los espacios finales izquierdo y derecho en la cadena dada. 
oracion = " Codificación para todos "
oracion_sin_espacios = oracion.strip()
print(f"Oracion sin espacios \"{oracion_sin_espacios}\"")
esperar_tecla_para_continuar()

#  31  ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():
#           30DíasDePython
#           treinta_dias_de_python
cadena1 = "30DíasDePython"
cadena2 = "treinta_dias_de_python"
print(cadena1.isidentifier())
print(cadena2.isidentifier())
esperar_tecla_para_continuar()


#  32  La siguiente lista contiene los nombres de algunas de las bibliotecas de Python: 
#      ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
#      Únase a la lista con un hash con cadena de espacio. 
lista = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = " ".join(lista)
print(resultado)
esperar_tecla_para_continuar()
"""

#  33  Use la secuencia de escape de nueva línea para separar las siguientes oraciones. 
#           I am enjoying this challenge.
#           I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

#  34  Use una secuencia de escape de tabulación para escribir las siguientes líneas. 
#           Name      Age     Country   City
#           Asabeneh  250     Finland   Helsinki
print("Name Age Country City Asabeneh 250 Finland Helsinki")


#  35  Utilice el método de formato de cadena para mostrar lo siguiente: 
#           radius = 10
#           area = 3.14 * radius ** 2
#           The area of a circle with radius 10 is 314 meters square.


#  36  Haga lo siguiente usando métodos de formato de cadena: 
#           8 + 6 = 14
#           8 - 6 = 2
#           8 * 6 = 48
#           8 / 6 = 1.33
#           8 % 6 = 2
#           8 // 6 = 1
#           8 ** 6 = 262144


