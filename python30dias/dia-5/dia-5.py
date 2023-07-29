import msvcrt
def esperar_tecla_para_continuar():
    print("\n\tPresiona cualquier tecla para continuar... \n")
    msvcrt.getch()


lista_vacia = list() # this is an empty list, no item in the list
print(len(lista_vacia)) # 0

frutas = ['platano', 'naranja', 'durazno', 'limon']                     # list of frutas
vegetables = ['Tomates', 'Papas', 'Repollo','Cebolla', 'Zanahoria']      # list of vegetables
animal_products = ['leche', 'carne', 'mantequilla', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finlandia', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('frutas:', frutas)
print('Number of frutas:', len(frutas))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

frutas = ['platano', 'naranja', 'durazno', 'limon'] 
first_fruit = frutas[0] # we are accessing the first item using its index
print(first_fruit)      # platano
second_fruit = frutas[1]
print(second_fruit)     # naranja
last_fruit = frutas[3]
print(last_fruit) # limon
# Last index
last_index = len(frutas) - 1
last_fruit = frutas[last_index]

# Accessing items
frutas = ['platano', 'naranja', 'durazno', 'limon'] 
last_fruit = frutas[-1]
second_last = frutas[-2]
print(last_fruit)       # limon
print(second_last)      # durazno

# Slicing items
frutas = ['platano', 'naranja', 'durazno', 'limon'] 
all_frutas = frutas[0:4] # it returns all the frutas
# this is also give the same result as the above
all_frutas = frutas[0:] # if we don't set where to stop it takes all the rest
naranja_and_durazno = frutas[1:3] # it does not include the end index
naranja_durazno_limon = frutas[1:]

frutas = ['platano', 'naranja', 'durazno', 'limon'] 
all_frutas = frutas[-4:] # it returns all the frutas
# this is also give the same result as the above
naranja_and_durazno = frutas[-3:-1] # it does not include the end index
naranja_durazno_limon = frutas[-3:]


frutas = ['platano', 'naranja', 'durazno', 'limon'] 
frutas[0] = 'Avocado' 
print(frutas)       #  ['avocado', 'naranja', 'durazno', 'limon']
frutas[1] = 'apple'
print(frutas)       #  ['avocado', 'apple', 'durazno', 'limon']
last_index = len(frutas) - 1
frutas[last_index] = 'lime'
print(frutas)        #  ['avocado', 'apple', 'durazno', 'lime']

# checking items
frutas = ['platano', 'naranja', 'durazno', 'limon']
does_exist = 'platano' in frutas
print(does_exist)  # True
does_exist = 'lime' in frutas
print(does_exist)  # False

# Append
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.append('apple')
print(frutas)           # ['platano', 'naranja', 'durazno', 'limon', 'apple']
frutas.append('lime')   # ['platano', 'naranja', 'durazno', 'limon', 'apple', 'lime]
print(frutas)

# insert
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.insert(2, 'apple') # insert apple between naranja and durazno
print(frutas)           # ['platano', 'naranja', 'apple', 'durazno', 'limon']
frutas.insert(3, 'lime')   # ['platano', 'naranja', 'apple', 'durazno', 'lime','limon',]
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
del frutas
print(frutas)       # This should give: NameError: name 'frutas' is not defined

# clear
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.clear()     
print(frutas)       # []

# copying a lits

frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas_copy = frutas.copy()     
print(frutas_copy)       # ['platano', 'naranja', 'durazno', 'limon']

# join
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
frutas = ['platano', 'naranja', 'durazno', 'limon']
vegetables = ['Tomates', 'Papas', 'Repollo','Cebolla', 'Zanahoria'] 
frutas_and_vegetablelechefrutcarne vegmantequFinlandiarint(frutas_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
frutas = ['platano', 'naranja', 'durazno', 'limon']
vegetables = ['Tomates', 'Papas', 'Repollo','Cebolla', 'Zanahoria'] 
frutas.extend(vegetaleche)
prcarne'frumanteFinlandia vegetables:', frutas )

# count
frutas = ['platano', 'naranja', 'durazno', 'limon']
print(frutas.count('naranja'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
frutas = ['platano', 'naranja', 'durazno', 'limon']
print(frutas.index('naranja'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.reverse()
print(frutas)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
frutas = ['platano', 'naranja', 'durazno', 'limon']
frutas.sort()
print(frutas) 
frutas.sort(reverse=True)
print(frutas)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 

# Java341@.lang