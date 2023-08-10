import msvcrt
def enter():
    print("\n\t\t* * * * *  Presiona cualquier tecla para continuar  * * * * *\n")
    msvcrt.getch()
    
# Ejercicios: Nivel 1
#    Crear una tupla vacía
#    Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
#    Unir tuplas de hermanos y hermanas y asignarlas a hermanos
#    ¿Cuántos hermanos tiene usted?
#    Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members

# Ejercicios: Nivel 1
#    Crear una tupla vacía
"""
tuplaVacia = ()
print(f"tupla vacia: {tuplaVacia}")
print(f"cantidad de veces que esta el elemento: {tuplaVacia.count(2)}")
enter()
"""

#    Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
tuplaHermanos = ("Ana", "Maria", "Sofia", "Laura")
tuplaHermanas = ("Juan", "Carlos", "Andres", "Alejandro")
print(f"tupla hermanos: {tuplaHermanos}")
print(f"tupla hermanas: {tuplaHermanas}")
enter()

#    Unir tuplas de hermanos y hermanas y asignarlas a hermanos
tuplaUnion = tuplaHermanos + tuplaHermanas
print(f"tupla union: {tuplaUnion}")

#    ¿Cuántos hermanos tiene usted?
#    Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members