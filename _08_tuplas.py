# """ TUPLAS """

# my_tuple = tuple()
# my_other_tuple = ()

# my_tuple = (37, 1.64, "Ivan", "Madrid", 37)
# my_other_tuple = (2, 1.0, "Esteban", "Madrid")
# my_tuple_2 = (8, 1.10, "Ismael", "Madrid")
# print(my_tuple)
# print(type(my_tuple))

# print(my_tuple[0])
# print(my_tuple[-1])

# my_tuple.count(37)
# print(my_tuple.count(37.5))
# print(my_tuple.index("Madrid"))

# my_sum_tuple = my_tuple + my_other_tuple + my_tuple_2
# print(my_sum_tuple)

# print(my_sum_tuple[3:6])

# my_tuple = list(my_tuple)
# print(my_tuple)
# print(type(my_tuple))

# my_tuple[4] = "M.D"
# my_tuple.insert(1, "Rojo")
# print(tuple(my_tuple))

""" Ejercicios: Nivel 1 """

# 1. Crear una tupla vacia

my_tuple = () # Forma número 1
my_other_tuple = tuple() # Forma número 2

# 2. Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)

my_tuple = ("Katerin", "Ismael", "Esteban", "Emma")

# 3. Unir tuplas de hermanos y hermanas y asignarlas a hermanos

my_brothers = ("Ismael", "Esteban")
my_sisters = ("Ketrin", "Luis")

all_my_brothers = (my_brothers + my_sisters)
print(all_my_brothers)

# 4. 'Cuántos hermanos tienes?

number_of_siblings = len(all_my_brothers)
print(number_of_siblings)

# 5. Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members

# Solución 1
all_my_brothers = list(all_my_brothers)
print(all_my_brothers)
all_my_brothers.append("Efrain")
print(all_my_brothers)
all_my_brothers.append("Emma")
print(all_my_brothers)
print(type(all_my_brothers))
all_my_brothers = tuple(all_my_brothers)
print(type(all_my_brothers))
family_members = all_my_brothers
print(family_members)
print(type(family_members))

# Solución 2
all_my_brothers = list(all_my_brothers)
all_my_brothers.insert(2, "Emma")
print(all_my_brothers)
all_my_brothers.insert(0, "Efrain")
print(all_my_brothers)
print(type(all_my_brothers))
all_my_brothers = tuple(all_my_brothers)
print(type(all_my_brothers))
family_members = all_my_brothers
print(family_members)
print(type(family_members))

# Solución 3
all_my_brothers = list(all_my_brothers)
new_elements = ["Emma", "Efrain"]
all_my_brothers[1:1] = new_elements
print(all_my_brothers)
print(type(all_my_brothers))
all_my_brothers = tuple(all_my_brothers)
print(type(all_my_brothers))
family_members = all_my_brothers
print(family_members)
print(type(family_members))

""" Ejercicios: Nivel 2 """

# 1. Desempaca a los hermanos y padres de family_members

family_members = ('Efrain', 'Emma', 'Ismael', 'Esteban', 'Katerin', 'Luis')

my_brothers = family_members[2:6]
print(my_brothers)
my_parents = family_members[0:2]
print(my_parents)

# 2. Crea tuplas de frutas, verduras y productos de origen animal. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.

fruits = ("Apple", "Orange", "Pear")
vegetables = ("Potato", "Onion", "Corn")
animals = ("Horse", "Pig", "Duck")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

# 3. Cambiar la tupla acerca de food_stuff_tp a una lista food_stuff_lt

food_stuff_tp = list(food_stuff_tp)
print(type(food_stuff_tp))

# 4. Divida el elemento o elementos del medio de la food_stuff_tp tupla o lista de food_stuff_lt.

food_stuff_tp = list(food_stuff_tp)
print(len(food_stuff_tp))
mid_index = len(food_stuff_tp) // 2
print(mid_index)
mid_element = food_stuff_tp[mid_index]
print(mid_element)
food_stuff_tp = tuple(food_stuff_tp)
print(food_stuff_tp)

# 5. Corta los tres primeros elementos y los tres últimos de food_staff_lt lista

food_stuff_tp = ('Apple', 'Orange', 'Pear', 'Potato', 'Onion', 'Corn', 'Horse', 'Pig', 'Duck')

first_elements = food_stuff_tp[:3]
print(first_elements)
last_elements = food_stuff_tp[-3:]
print(last_elements)

# 6. Elimine la tupla food_staff_tp por completo

food_stuff_tp = ('Apple', 'Orange', 'Pear', 'Potato', 'Onion', 'Corn', 'Horse', 'Pig', 'Duck')

del food_stuff_tp
# print(food_stuff_tp)

# 7. Compruebe si un elemento existe en tupla:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Comprueba si 'Estonia' es un país nórdico

# Comprueba si 'Islandia' es un país nórdico

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


""" 









"""