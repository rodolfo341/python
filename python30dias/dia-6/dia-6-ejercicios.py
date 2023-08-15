import msvcrt
def enter():
    print("\n\t\t* * * * *  Presiona cualquier tecla para continuar  * * * * *\n")
    msvcrt.getch()
    
# Ejercicios: Nivel 1
#  1  Crear una tupla vacía
#  2  Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
#  3  Unir tuplas de hermanos y hermanas y asignarlas a hermanos
#  4  ¿Cuántos hermanos tiene usted?
#  5  Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members

# Ejercicios: Nivel 1
#   1 Crear una tupla vacía
"""
tuplaVacia = ()
print(f"tupla vacia: {tuplaVacia}")
print(f"cantidad de veces que esta el elemento: {tuplaVacia.count(2)}")
enter()
"""

# 2 Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
tuplaHermanos = ("Ana", "Maria", "Sofia", "Laura")
tuplaHermanas = ("Juan", "Carlos", "Andres", "Alejandro")
print(f"tupla hermanos: {tuplaHermanos}")
print(f"tupla hermanas: {tuplaHermanas}")
enter()


# 3 Unir tuplas de hermanos y hermanas y asignarlas a hermanos
tuplaUnion = tuplaHermanos + tuplaHermanas
print(f"tupla union: {tuplaUnion}")
enter()

# 4 ¿Cuántos hermanos tiene usted?
totalHermanos = len(tuplaUnion)
print(f"El total de hermanos es: {totalHermanos}")
enter()

# 5 Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members

family_members = tuplaUnion + ("mama","papa")
print(f"totalHermanos + mama y papa: {family_members}")

# Ejercicios: Nivel 2

# 1 Desempaquetar hermanos y padres de family_members
# 2 Cree tuplas de frutas, verduras y productos animales. 
#       Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
# 3 Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
# 4 Rebane el artículo o artículos del medio de la tupla food_stuff_tp o la lista food_stuff_lt.
# 5 Cortar los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt
# 6 Eliminar completamente la tupla food_staff_tp
# 7 Compruebe si existe un elemento en la tupla:
#       Comprobar si 'Estonia' es un país nórdico
#       Comprobar si 'Islandia' es un país nórdico
#           nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')


# Ejercicios: Nivel 2

# 1 Desempaquetar hermanos y padres de family_members
hijo1, hijo2, hijo3, hijo4, hijo5, hijo6, hijo7, hijo8, mama, papa = family_members
print(f"Hijo1: {hijo1}") 
print(f"Hijo2: {hijo2}") 
print(f"Hijo3: {hijo3}") 
print(f"Hijo4: {hijo4}") 
print(f"Hijo5: {hijo5}") 
print(f"Hijo6: {hijo6}") 
print(f"Hijo7: {hijo7}") 
print(f"Hijo8: {hijo8}")
print(f"Mama: {mama}")
print(f"Papa: {papa}") 

# 2 Cree tuplas de frutas, verduras y productos animales. 
#       Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
tuplaFrutas = ("manzana", "pera", "naranja")
tuplaVerduras = ("papa", "zapallo")
tuplaUnion = tuplaFrutas + tuplaVerduras
print(f"Tupla union: {tuplaUnion}")

# 3 Cambie la tupla about food_stuff_tp a una lista food_stuff_lt


# 4 Rebane el artículo o artículos del medio de la tupla food_stuff_tp o la lista food_stuff_lt.


# 5 Cortar los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt


# 6 Eliminar completamente la tupla food_staff_tp


# 7 Compruebe si existe un elemento en la tupla:
#       Comprobar si 'Estonia' es un país nórdico
#       Comprobar si 'Islandia' es un país nórdico
#           nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

