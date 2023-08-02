import msvcrt
def esperar_tecla_para_continuar():
    print("\n\tPresiona cualquier tecla para continuar... \n")
    msvcrt.getch()

print(f"Lista vacia")
lista_vacia = list() # "Esto es una lista vacía, no hay elementos en la lista."
print(len(lista_vacia)) # 0

frutas = ['platano', 'naranja', 'durazno', 'limon']                     # lista de frutas
vegetales = ['Tomates', 'Papas', 'Repollo','Cebolla', 'Zanahoria']      # lista de vegetales
productos_animales = ['leche', 'carne', 'mantequilla', 'yoghurt']             # lista de productos animales
tecnoligias_web = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # lista de tecnologias web
paises = ['Finlandia', 'Estonia', 'Dinamarca', 'Suiza', 'Noruega']

# Print de listas y longitud
esperar_tecla_para_continuar()
print("Print de listas y longitud")

print('frutas:', frutas)
print('Numero de frutas:', len(frutas))
print('Vegetales:', vegetales)
print('Numero de vegetales:', len(vegetales))
print('Productos animales:',productos_animales)
print('Numero de productos animales:', len(productos_animales))
print('Tecnologias web:', tecnoligias_web)
print('Numero de tecnologias web:', len(tecnoligias_web))
print('Numero de paises:', len(paises))

# Modificando lista
esperar_tecla_para_continuar()
print("Modificando lista\n")

frutas = ['platano', 'naranja', 'durazno', 'limon'] 
primera_fruta = frutas[0] # Accedemos al primer elemento usaando index
print(primera_fruta)      # platano
segunda_fruta = frutas[1]
print(segunda_fruta)     # naranja
ultima_fruta = frutas[3]
print(ultima_fruta) # limon
# Ultimo indice
ultimo_indice = len(frutas) - 1
ultima_fruta = frutas[ultimo_indice]

# Accediendo a los items
frutas = ['platano', 'naranja', 'durazno', 'limon'] 
ultima_fruta = frutas[-1]
penultima = frutas[-2]
print(ultima_fruta)       # limon
print(penultima)      # durazno

# Slicing items
frutas = ['platano', 'naranja', 'durazno', 'limon'] 
todas_las_frutas = frutas[0:4] # "Devuelve todas las frutas"
# "Esto también da el mismo resultado que el anterior."
todas_las_frutas = frutas[0:] # "Si no especificamos dónde detenerse, toma todo el resto."
naranja_y_durazno = frutas[1:3] # "No incluye el índice final."
naranja_durazno_limon = frutas[1:]

frutas = ['platano', 'naranja', 'durazno', 'limon'] 
todas_las_frutas = frutas[-4:] # "Devuelve todas las frutas"
# "Esto también da el mismo resultado que el anterior."
naranja_y_durazno = frutas[-3:-1] # "No incluye el índice final."
naranja_durazno_limon = frutas[-3:]


frutas = ['platano', 'naranja', 'durazno', 'limon'] 
frutas[0] = 'palta' 
print(frutas)       #  ['palta', 'naranja', 'durazno', 'limon']
frutas[1] = 'manzana'
print(frutas)       #  ['palta', 'manzana', 'durazno', 'limon']
ultimo_indice = len(frutas) - 1
frutas[ultimo_indice] = 'lime'
print(frutas)        #  ['palta', 'manzana', 'durazno', 'lime']

# checking items
frutas = ['platano', 'naranja', 'durazno', 'limon']
existe = 'platano' in frutas
print(existe)  # True
existe = 'lime' in frutas
print(existe)  # False

# Append
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.append('manzana')
print(frutas)           # ['platano', 'naranja', 'durazno', 'limon', 'manzana']
frutas.append('lime')   # ['platano', 'naranja', 'durazno', 'limon', 'manzana', 'lime]
print(frutas)

# insert
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.insert(2, 'manzana') # insert manzana between naranja and durazno
print(frutas)           # ['platano', 'naranja', 'manzana', 'durazno', 'limon']
frutas.insert(3, 'lime')   # ['platano', 'naranja', 'manzana', 'durazno', 'lime','limon',]
print(frutas)

# remove
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.remove('platano')
print(frutas)  # ['naranja', 'durazno', 'limon']
frutas.remove('limon')
print(frutas)  # ['naranja', 'durazno']

# pop
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.pop()     
print(frutas)       # ['platano', 'naranja', 'durazno']

frutas.pop(0)     
print(frutas)       # ['naranja', 'durazno'] 

# del 
frutas = ['platano', 'naranja', 'durazno', 'limon']
del frutas[0]     
print(frutas)       # ['naranja', 'durazno', 'limon']

del frutas[1]     
print(frutas)       # ['naranja', 'limon']
# del frutas
print(frutas)       # "Esto debería dar como resultado: NameError: el nombre 'frutas' no está definido."

# clear
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.clear()     
print(frutas)       # []

# copying a lits

frutas = ['platano', 'naranja', 'durazno', 'limon']
copiar_fruta = frutas.copy()     
print(copiar_fruta)       # ['platano', 'naranja', 'durazno', 'limon']

# join
numeros_positivos = [1, 2, 3,4,5]
cero = [0]
numeros_negativos = [-5,-4,-3,-2,-1]
integers = numeros_negativos + cero + numeros_positivos
print(integers)
frutas = ['platano', 'naranja', 'durazno', 'limon']
vegetales = ['Tomates', 'Papas', 'Repollo','Cebolla', 'Zanahoria'] 
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)

# join con extend
num1 = [0, 1, 2, 3]
num2 = [4, 5,6]
num1.extend(num2)
print('Numeros:', num1)
numeros_negativos = [-5,-4,-3,-2,-1]
numeros_positivos = [1, 2, 3,4,5]
cero = [0]

numeros_negativos.extend(cero)
numeros_negativos.extend(numeros_positivos)
print('Integers:', numeros_negativos)
frutas = ['platano', 'naranja', 'durazno', 'limon']
vegetales = ['Tomates', 'Papas', 'Repollo','Cebolla', 'Zanahoria'] 
frutas.extend(vegetales)
print('Frutas y vegetales:', frutas )

Suiza = ['durazno', 'naranja', 'durazno', 'limon']
print(frutas.count('naranja'))   # 1
edades = [22, 19, 24, 25, 26, 24, 25, 24]
print(edades.count(24))           # 3

# index
frutas = ['platano', 'naranja', 'durazno', 'limon']
print(frutas.index('naranja'))   # 1
edades = [22, 19, 24, 25, 26, 24, 25, 24]
print(edades.index(24)) 
# Reverse
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.reverse()
print(frutas)  
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades.reverse()
print(edades) 

# sort
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.sort()
print(frutas) 
frutas.sort(reverse=True)
print(frutas)
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades.sort()
print(edades) 
edades.sort(reverse=True)
print(edades) 

# Java341@.lang