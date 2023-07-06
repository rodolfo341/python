import msvcrt
def esperar_tecla_para_continuar():#{
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
esperar_tecla_para_continuar()

# type()
print("ejemplos de type")
print(type(texto))  #str
print(type(22))     #int
print(type(2.2))    #float
print(type(True))   #bool
esperar_tecla_para_continuar()

# int()
print(type(int("11")))      # Transforma el texto de string a integer
print(int(11.11))           # Transforma el numero de flotante a integer (lo trunca)
esperar_tecla_para_continuar()

# float()
# str()
# input()


# print() 
print("imprime texto")

# len() 
texto = "ejemplo"
print("Cantida de letras de 'ejemplo:'",len(texto))
esperar_tecla_para_continuar()

# type()
print("ejemplos de type")
print(type(texto))  #str
print(type(22))     #int
print(type(2.2))    #float
print(type(True))   #bool
esperar_tecla_para_continuar()

# input()
texto = input("ingrese nuevo texto: \t")
print(f"Nuevo texto es : \t{texto}")
esperar_tecla_para_continuar()





# list()
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
esperar_tecla_para_continuar()

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
esperar_tecla_para_continuar()

nombre, apellido, pais, edad, esta_casado = 'Rodolfo', 'Aravena', 'Chile', 51, True

print(nombre, apellido, pais, edad, esta_casado)
print('Nombre:', nombre)
print('Apellido: ', apellido)
print('Pais: ', pais)
print('Edad: ', edad)
print('Esta casado: ', esta_casado)