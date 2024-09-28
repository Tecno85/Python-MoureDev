## ![fuego](/assets/img/icon_6.png) `Ejercicios` ![fuego](/assets/img/icon_6.png)

1. Crear una tupla vacia

```py
# Solución 1
my_tuple = ()

# Solución 2
my_other_tuple = tuple()
```

2. Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)

```py
my_tuple = ("Katerin", "Ismael", "Esteban", "Emma")
```

3. Unir tuplas de hermanos y hermanas y asignarlas a hermanos

```py
my_brothers = ("Ismael", "Esteban")
my_sisters = ("Ketrin", "Luis")

all_my_brothers = (my_brothers + my_sisters)
print(all_my_brothers)
```

4. ¿Cuántos hermanos tienes?

```py
number_of_siblings = len(all_my_brothers)
print(number_of_siblings)
```

5. Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a _family_members_

```py
Solución 1

all_my_brothers = list(all_my_brothers) # Cambia de tupla a lista
print(all_my_brothers)
all_my_brothers.append("Efrain") # Agrega el elemento "Efrain"
print(all_my_brothers)
all_my_brothers.append("Emma") # Agrega el elemento "Emma"
print(all_my_brothers)
print(type(all_my_brothers)) # Imprime el tipo
all_my_brothers = tuple(all_my_brothers) # Cambia de lista a tupla
print(type(all_my_brothers)) # Imprime el tipo
family_members = all_my_brothers
print(family_members)
print(type(family_members))
```

```py
Solución 2

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
```

```py
Solución 3

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
```

6. Desempaca a los hermanos y padres de _family_members_

```py
family_members = ('Efrain', 'Emma', 'Ismael', 'Esteban', 'Katerin', 'Luis')

my_brothers = family_members[2:6]
print(my_brothers)
my_parents = family_members[0:2]
print(my_parents)
```

7. Crea tuplas de frutas, verduras y productos de origen animal. Une las tres tuplas y asígnalas a una variable llamada _food_stuff_tp._

```py
fruits = ("Apple", "Orange", "Pear")
vegetables = ("Potato", "Onion", "Corn")
animals = ("Horse", "Pig", "Duck")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
```

8. Cambiar la tupla acerca de food*stuff_tp a una lista \_food_stuff_lt*

```py
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))
```

9. Divida el elemento o elementos del medio de la food*stuff_tp tupla o lista de \_food_stuff_lt.*

```py
food_stuff_tp = fruits + vegetables + animals
food_stuff_lt = list(food_stuff_tp)
print(len(food_stuff_lt))
mid_index = len(food_stuff_lt) // 2
print(mid_index)
mid_element = food_stuff_lt[mid_index]
print(mid_element)
food_stuff_tp = tuple(food_stuff_lt)
print(food_stuff_tp)
```

10. Corta los tres primeros elementos y los tres últimos de la lista _food_staff_lt_

```py
food_stuff_tp = ('Apple', 'Orange', 'Pear', 'Potato', 'Onion', 'Corn', 'Horse', 'Pig', 'Duck')

first_elements = food_stuff_tp[:3]
print(first_elements)
last_elements = food_stuff_tp[-3:]
print(last_elements)
```

11. Elimine la tupla \_food_staff_tp \_por completo

```py
food_stuff_tp = ('Apple', 'Orange', 'Pear', 'Potato', 'Onion', 'Corn', 'Horse', 'Pig', 'Duck')

del food_stuff_tp

print(food_stuff_tp) # Imprime: NameError: name 'food_stuff_tp' is not defined
                     # Imprime que la tupla no esta definida.
```

12. Compruebe si un elemento existe en tupla:

```py
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Comprueba si 'Estonia' es un país nórdico
print("Estonia" in nordic_countries)

# Comprueba si 'Islandia' es un país nórdico
print("Iceland" in nordic_countries)
```

---

[**`Inicio`**](/notas.md)
[**`-`**]()
[**`tuplas`**](/tuplas.md)