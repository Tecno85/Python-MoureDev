# ![tuplas_icon](./assets/img/python_icon_2.png) `TUPLAS` ![tuplas_icon](./assets/img/python_icon_4.png)

Una tupla es una estructura de datos en Python que permite almacenar una colección de elementos ordenados e inmutables. Esto significa que, una vez que se crea una tupla, no se pueden modificar, agregar o eliminar elementos de ella.

_Características principales de las tuplas_:

- _Ordenadas_: Los elementos dentro de una tupla tienen un orden definido, lo que significa que puedes acceder a ellos usando índices, igual que en las listas.

- _Inmutables_: A diferencia de las listas, no puedes cambiar el contenido de una tupla una vez creada. No se pueden añadir, eliminar o modificar elementos.

- _Permiten elementos duplicados_: Al igual que las listas, una tupla puede contener elementos duplicados.

- _Heterogéneas_: Pueden contener elementos de diferentes tipos de datos (números, cadenas, listas, etc.).

## `Sintaxis`

Las `tuplas` se definen usando **paréntesis** `()` y separando los elementos con **comas**.

```py
my_tuple = (1, 2, 3, "a", "b", "c") # Forma recomendada, clara y explícita.
print(type(my_tuple)) # Imprime <class 'tuple'>

my_other_tuple = tuple([1, 3]) # Otra forma de definir tuplas usando una lista.
print(type(my_tuple)) # Imprime <class 'tuple'>
```

También es posible crear tuplas sin paréntesis, simplementet separando los elementos con comas, no es una buena práctica, es usada sobre todo en el desempaquetado de variables.

```py
my_tuple = 1, 2, 3 # Válida pero menos clara.
print(type(my_tuple)) # Imprime <class 'tuple'>
```

## `Longitud`

Usamos el método `len()` para obtener la longitud de una tupla.

```py
my_tuple = (1, 2, 3, "a", "b", "c")
len(my_tuple)
print(len(my_tuple)) # La longitud de la tupla es de: "6" elementos.
```

## `Acceso a elementos`

Es posible acceder a los elementos de una tupla mediante su índice, empezando desde 0, para acceder al primer elemento en la indexación positiva y desde -1 en la indezaxión negativa. El -1 representa el ultimo número de la tupla en la indexación negativa. Dado que esta comienza la indexación desde el final de la tupla.

```py
my_tuple = (10, 20, 30)
print(my_tuple[0]) # Imprime: 10. Representa indexación positiva.
print(my_tuple[-2]) # Imprime: 10. Representa indexación negativa.
```

## `Inmutabilidad`

No se puede cambiar los elementos en una tupla

```py
my_tuple = (10, 20, 30)
my_tuple[1] = 40
print(my_tuple[1]) # Imprime error dado que la tuplas no son modificables.
                   # TypeError: 'tuple' object does not support item assignment
```

## `Cambiar tuplas a listas`

Podemos cambiar de tuplas a listas y de listas a tuplas. La tupla es inmutable, si deseamos modificar una tupla debemos cambiarla por una lista.

```py
my_tuple = (10, 20, 30)
my_tuple = list(my_tuple) # Utilizo el método list() para cambiar la tupla a lista y agregar un elemento nuevo.
my_tuple[1] = 40 # Agregando un nuevo elemento a la lista.
print(my_tuple) # Imprime la lista: [10, 40, 30]
my_tuple = tuple(my_tuple) # Utilizo el método tuple() para convertir nuevamente la lista a tupla.
print(my_tuple) # Imprime la tupla: (10, 40, 30)
```

## `Segmentación de tuplas`

Podemos dividir una subtupla especificando un rango de índice donde comenzar y dónde terminar en la tupla, el valor devuelto será una nueva tupla con los elementos especifícados.

```py
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

first_issues = numbers[:5]
print(first_issues) # Imprime: (1, 2, 3, 4, 5)
second_issues = numbers[5:]
print(second_issues) # Imprime: (6, 7, 8, 9, 10)
numbers_segment = numbers[2:7]
print(numbers_segment) # Imprime: (3, 4, 5, 6, 7)
last_number = numbers[-1]
print(last_number) # Imprime mediante índice negativo el último elemento: 10
```

## `Comprobación de un elemento en una tupla`

Podemos comprobar si un elemento existe o no en una `tupla`, usando el operador de pertenencia `in`, el cuál tiene como función verificar si un elemento está presente en una secuencia (tuplas, listas o cadenas), devolviendo `True` si está y `False` si no está

```py
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(11 in numbers) # Imprime "False"
print(4 in numbers) # Imprime "True"
```

## `Concatenación o Unión de tuplas`

Podemos unir dos o más `tuplas` usando el operador `+`

```py
tupla_1 = (1, 2)
tupla_2 = (3, 4, 5, 6)
tupla_concatenada = tupla_1 + tupla_2   # Concatenación de tuplas
print(tupla_concatenada) # Imprime: (1, 2, 3, 4, 5, 6)
```

## `Repetición de elementos en tuplas`

Es posible multiplicar una `tupla` por un número entero para repetir sus elementos

```py
my_tupla = (1, 2) * 3
print(my_tupla) # Imprime: (1, 2, 1, 2, 1, 2)
```

## `Desempaquetado de tuplas`

El desempaquetado de `tuplas`, permite asignar los valores de una `tupla` a variables separadas

```py
my_tupla = (1, 2, 3, 4)
a, b, c, d = my_tupla
print(a) # Imprime: 1
print(b) # Imprime: 2
print(c) # Imprime: 3
print(d) # Imprime: 4
```

## `Eliminación de tuplas`

No es posible eliminar elementos de una tupla, pero es porible eliminar la tupla usando la instrucción o palabra reservada `del`

```py
my_tupla = (1, 2, 3, 4)
del my_tupla
print(my_tupla) # Imprime: NameError: name 'my_tupla' is not defined
                # 'del' elimina la variable y nos dice que no existe.
```

## `Método` _`count()`_

Este método nos permite devolver las veces que aparece un elemento específico en la tupla.

```py
my_tupla = (1, 2, 2, 2, 3, 4, 5, 5, 6, 7)

print(my_tupla.count(2)) # Imprime: 3
print(my_tupla.count(4)) # Imprime: 1
print(my_tupla.count(5)) # Imprime: 2
```

## `Método` _`index()`_

Este método devuelve el índice del primer elemento cuyo valor sea igual al que se pasa como argumento

```py
my_tupla = (1, 2, 3, 4)
print(my_tupla.index(4)) # Imprime: "3", este corresponde al elemento "4", el cuál está ubicado en el indice "3".
```

## `¿Cuándo usar tuplas?`

- Cuando necesitas un conjunto de elementos que no deben cambiar durante la ejecución del programa.

- Cuando quieres un rendimiento optimizado, ya que las tuplas ocupan menos espacio y son más rápidas que las listas para operaciones que no requieren modificaciones.

## `Ejercicios: Nivel 1`

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

Unir tuplas de hermanos y hermanas y asignarlas a hermanos

```py
my_brothers = ("Ismael", "Esteban")
my_sisters = ("Ketrin", "Luis")

all_my_brothers = (my_brothers + my_sisters)
print(all_my_brothers)
```

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

---

[**`Contendio`**](/notas.md)
