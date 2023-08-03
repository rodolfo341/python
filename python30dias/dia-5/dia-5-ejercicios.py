import msvcrt
def enter():
    print("\n\t\t* * * * *  Presiona cualquier tecla para continuar  * * * * *\n")
    msvcrt.getch()
    
# Declara una lista vacía.
print("Declara una lista vacía.")
lista = []
print(f"lista vacía: {lista} \n")

enter()
# Declara una lista con más de 5 elementos.
print("Declara una lista con más de 5 elementos.")
lista = [1,2,1,3,44,22,78]
print(f"lista lista: {lista}\n")


# Encuentra la longitud de tu lista.
enter()
print("Encuentra la longitud de tu lista.")
print(f"la longitud de la lista lista es: {len(lista)}\n")


# Obtén el primer elemento, el elemento del medio y el último elemento de la lista.
enter()
print("Obtén el primer elemento, el elemento del medio y el último elemento de la lista.")
print(f"primer elemento: {lista[0]}")
print(f"elemento del medio: {lista[len(lista)//2]}")
print(f"ultimo elemento: {lista[-1]}\n")

enter()
print("Declara una lista llamada \"mixed_data_types\" y agrega tu (nombre, edad, altura, estado civil, dirección).")
# Declara una lista llamada "mixed_data_types" y agrega tu (nombre, edad, altura, estado civil, dirección).
mixed_data_types = ["Rodolfo", 51, 175, "casado", "siempre viva 123"]
print(f"lista mixed_data_types: {mixed_data_types}\n") 

enter()
print("Declara una variable de lista llamada \"it_companies\" y asigna los valores iniciales: ")
print("Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.")
# Declara una variable de lista llamada "it_companies" y asigna los valores iniciales: 
# Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "apple", "IBM", "Oracle", "Amazon" ]

# Imprime la lista usando print().
print(f"it_companies: {it_companies}\n") 

enter()
print("Imprime el número de compañías en la lista.")
# Imprime el número de compañías en la lista.
print(f"numero de compañias: {len(it_companies)}\n")

enter()
print("Imprime la primera, la del medio y la última compañía.")
# Imprime la primera, la del medio y la última compañía.
primer = it_companies[0]
medio = it_companies[len(it_companies)//2]
ultimo = it_companies[-1]

print(f"primer: {primer}")
print(f"medio: {medio}")
print(f"ultimo: {ultimo}\n")

enter()
print("Imprime la lista después de modificar una de las compañías.")
# Imprime la lista después de modificar una de las compañías.
it_companies[3] = 'TikTok'
print('cambio Apple por tiktok')
print(f"it_companies: {it_companies}\n") 

enter()
print("Agrega una compañía de TI a \"it_companies\".")
# Agrega una compañía de TI a "it_companies".
it_companies.append('Borland')
print('agrego Borland')
print(f"it_companies: {it_companies}\n") 

enter()
print("Inserta una compañía de TI en el medio de la lista de compañías.")
# Inserta una compañía de TI en el medio de la lista de compañías.
medio = len(it_companies) // 2
it_companies.insert(medio, 'AliBaba')
print(f"it_companies: {it_companies}\n") 

enter()
print("Cambia uno de los nombres de las compañías de \"it_companies\" a mayúsculas (¡excluye IBM!).")
# Cambia uno de los nombres de las compañías de "it_companies" a mayúsculas (¡excluye IBM!).
print(f"Faecbook original: {it_companies[0]}") 
it_companies[0] = it_companies[0].upper()
print(f"Faecbook en mayúsculas : {it_companies[0]}\n") 

print()
# Combina las compañías de "it_companies" con un string "#; ".
print("Combina las compañías de \"it_companies\" con un string ")

it_companies_combinada = "#".join(it_companies)

print(f"lista combinada con #: {it_companies_combinada}")

enter()
print("Comprueba si una cierta compañía existe en la lista \"it_companies\".")
# Comprueba si una cierta compañía existe en la lista "it_companies".
if 'Google' in it_companies:
    print('Google esta en la lista\n')
else:
    print('Google no está en la lista\n')

enter()
print("Ordena la lista usando el método sort().")
# Ordena la lista usando el método sort().
it_companies.sort()
for companie in it_companies:
    print(companie)
print('\n')

#  la lista en orden descendente usando el método reverse().
it_reverse = it_companies[::-1]
for it in it_reverse:
    print(it)
print('\n')

# Extrae las primeras 3 compañías de la lista.
for i in it_companies[:3]:
   print(f'Compañia índice: {i}')
print('\n')

# Recorrer los últimos tres elementos con un bucle for
for i in it_companies[-3:]:
   print(f'Compañia índice: {i}')
print()

# Extrae la(s) compañía(s) de TI del medio de la lista.
# it_companies.append("kjhkjhkjhkjhkj")
if len(it_companies) % 2 == 0:
    print(f"del medio: {it_companies[len(it_companies)//2]}")
    print(f"del medio: {it_companies[len(it_companies)//2 - 1]}")
else:
    print(f"del medio: {it_companies[len(it_companies)//2]}")
print()
enter()
<<<<<<< HEAD

# Elimina la primera compañía de TI de la lista.

print(it_companies)
#"""
it_companies.pop(0)
print(it_companies)
#"""
# Elimina la(s) compañía(s) de TI del medio de la lista.
if len(it_companies) % 2 == 0:
    it_companies.pop(len(it_companies)//2)
    it_companies.pop(len(it_companies)//2 - 1)
else:
    it_companies.pop(len(it_companies)//2)
print(it_companies)
enter()

# Elimina la última compañía de TI de la lista.
print(f"lista antes: {it_companies}")
it_companies.pop()
print(f"lista despues: {it_companies}")
enter()
print()

# Elimina todas las compañías de TI de la lista.
print(it_companies)
it_companies.clear()
print(it_companies)
=======

# Elimina la primera compañía de TI de la lista.

print(it_companies)
#"""
it_companies.pop(0)
print(it_companies)
#"""
# Elimina la(s) compañía(s) de TI del medio de la lista.
if len(it_companies) % 2 == 0:
    it_companies.pop(len(it_companies)//2)
    it_companies.pop(len(it_companies)//2 - 1)
else:
    it_companies.pop(len(it_companies)//2)
print(it_companies)
enter()

# Elimina la última compañía de TI de la lista.
print(f"lista antes: {it_companies}")
it_companies.pop()
print(f"lista despues: {it_companies}")



"""
Elimina todas las compañías de TI de la lista.
>>>>>>> 317fff7cd1ffd2b385b99f22db587d00f115a4eb

#Destruye la lista de compañías de TI.
del it_companies
# print(it_companies)

# Combina las siguientes listas:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

"""
Después de combinar las listas del punto 26, copia la lista combinada y asígnala a una variable llamada "full_stack". Luego, inserta Python y SQL después de Redux.
"""