import msvcrt
def espera():#{
    print("Presiona cualquier tecla para continuar...")
    msvcrt.getch()

# Introducción
# Dia 2 de 30 Dias del desafio Python

# Funciones integradas
# faltan los ejemplos
# print() 
print("imprime texto")

# len() 
texto = "ejemplo"
print("Cantida de letras de 'ejemplo:'",len(texto))
espera()

# type()
print("ejemplos de type")
print(type(texto))  #str
print(type(22))     #int
print(type(2.2))    #float
print(type(True))   #bool
espera()

# int()
print(type(int("11")))      # Transforma el texto de string a integer
print(int(11.11))           # Transforma el numero de flotante a integer (lo trunca)
print(int(True))            # True se transforma en 1
print(int(False))           # False se transforma en 0
#print(int("hola"))         # dará error
espera()

# float()
print(type(float("11.1")))    # Transforma el texto de string a float
print(float(11))              # Transforma el numero de int a float
print(float(True))            # True se transforma en 1.0
print(float(False))           # False se transforma en 0.0
#print(float("hola"))         # dará error
espera()

# str()
print(type(str("11.1")))    # Transforma el  de float a string
print(str(True))            # True se transforma en una cadena
print(str(False))           # False se transforma en cadena
espera()

# input()
texto = input("ingrese nuevo texto: \t")
print(f"Nuevo texto es : \t{texto}")
espera()

# list()
cadena = "Hola"
lista_caracteres = list(cadena)
print(lista_caracteres)     # Output: ['H', 'o', 'l', 'a']
espera()

rango = range(5)            # Convierte un rango en una lista
lista = list(rango)
print(lista)  # Output: [0, 1, 2, 3, 4]
espera()

# Si quieres separar las palabras usa split()
frase = "Hola a todos"
lista_palabras = frase.split()
print(lista_palabras)  # Output: ['Hola', 'a', 'todos']
espera()

# dict()
# min()
# max()
# sum()
# sorted()
# open()
# file()
# help()
# dir()

print("declaro las variables")
espera()

nombre = 'Rodolfo'
apellido = 'Aravena'
pais = 'Chile'
ciudad = 'Santiago'
edad = 51
esta_casado = True
habilidades = ['HTML', 'CSS', 'JS', 'React', 'Python']
informacion_personal = {
    'nombre':   'Rodolfo', 
    'apellido': 'Aravena', 
    'pais':     'Chile',
    'ciudad':   'Santiago'
}

# Imprimir los valores almacenados en las variables
print("Imprimo las variables")

print('Nombre:', nombre)
print('Nombre longitud(length):', len(nombre))
print('Apellido: ', apellido)
print('Apellido longitud(length): ', len(apellido))
print('Pais: ', pais)
print('Ciudad: ', ciudad)
print('Edad: ', edad)
print('Casado: ', esta_casado)
print('Habilidades: ', habilidades)
print('Informacion personalion: ', informacion_personal)

# Declarar múltiples variables en una línea
print("Declaro e imprimo variables multiples")
espera()

nombre, apellido, pais, edad, esta_casado = 'Rodolfo', 'Aravena', 'Chile', 51, True

print(nombre, apellido, pais, edad, esta_casado)
print('Nombre:', nombre)
print('Apellido: ', apellido)
print('Pais: ', pais)
print('Edad: ', edad)
print('Esta casado: ', esta_casado)