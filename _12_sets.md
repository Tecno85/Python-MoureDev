# `Sets` (Conjuntos) ![icon_sets](/assets/img/icon_6.png)

Un **`set`**, es una colleción desordenada de elementos únicos. A diferencia de las listas o tuplas, los **`sets`** no permiten elementos duplicados y sus elementos no están indexados, lo que significa que no es posible acceder a un elemento específico mediante un índice.

_Características de los `sets`_:

- Elementos únicos: No pueden tener elementos duplicados.

- Desordenados: No mantienen ningún orden específico.

- Mutable: Puedes agregar o eliminar elementos de un set.

- No indexado: No se puede acceder a los elementos mediante índices como en las listas o tuplas.

## `Cómo crear un` _`set`_

Para crear un `set`, se usa la función `set()` o simplemente se colocan los elementos entre llaves `{}`.

```py
# Crear un set
mi_set = {1, 2, 3, 4, 5}
print(mi_set) # Imprime: {1, 2, 3, 4, 5}
print(type(mi_set)) # Imprime el tipo: <class 'set'>

# Usando la función set()
mi_otro_set = set([1, 2, 3, 4, 5])
print(mi_otro_set) # Imprime: {1, 2, 3, 4, 5}
print(type(mi_otro_set)) # Imprime el tipo: <class 'set'>
```

## `Obtención de la longitud`

Se utiliza el método `len()` para encontrar la longitud de un `set`

```py
mi_set = {1, 2, 3, 4, 5}
len(mi_set)
print(len(mi_set)) # Imprime: 5
```

## `Acceso a los elementos`

Se accede a los elementos de un `set` mediante los bucles. El tema de bucles se trata más adelante.

## `Comprobación de elementos`

Para comprobar si un elemento está presente en un `set`, se usa el operador `in`, el cual retornará `True` si el elemento está en el `set` o `False` si no lo está.

```py
mi_set = {1, 2, 3, 4, 5}

# Se comprueba si el número 3 está en el set
print(3 in mi_set) # Imprime: True

# Se comprueba si el número 6 está en el set
print(6 in mi_set) # Imprime: False
```

También es posible comprobar si un elemento no está presente en un `set`, mediante el uso del operador `not in`. La lógica booleana se aplica de manera contraria.

```py
mi_set = {1, 2, 3, 4, 5}

# Se comprueba si el número 3 no está en el set
print(3 not in mi_set) # Imprime: False

# Se comprueba si el número 6 no está en el set
print(6 not in mi_set) # Imprime: True
```

## `Agregar un elemento al set`

Para agregar un elemento a un `set`. Utilizamos el método `add()`.

```py
mi_set = {1, 2, 3, 4, 5, 6}
mi_set.add(7)
print(mi_set) # Imprime: {1, 2, 3, 4, 5, 6, 7}
```

## `Unir dos sets`

Es posible unir dos sets usando el método `union()` o `update()`.

El método `union()` no modifica el set original. EN su lugar, retorna un nuevo set que contiene los elementos de ambos sets (sin duplicados).

```py
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
nuevo_set = set_1.union(set_2) # Se crea un nuevo set, que contiene la unión de set_1 y set_2.
print(nuevo_set) # Imprime: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
print(set_1) # El set original no se modifica.
```

Es posible agregar varios elementos a un set usando el método `update()`. El `update()` toma un argumento de lista.
El método `update()` modifica el set original añadiendo los elementos de otro set (o de cualquier iterable como una lista). No retorna un nuevo set, sino que actualiza el set original en su lugar.

```py
mi_set = {1, 2, 3, 4, 5, 6}

# Agregando un set al set
nuevo_set = {7, 8, 9 ,10, 11}
mi_set.update(nueva_tupla) # Actualiza mi_set añadiendo los elementos de nuevo_set.
print(mi_set) # Imprime: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}.

# Agregando una lista al set
nueva_lista = [12, 13, 14, 15, 16]
mi_set.update(nueva_lista)
print(mi_set) # Imprime: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

# Agregando una tupla a un set
nueva_tupla = (17, 18, 19, 20)
mi_set.update(nuevo_set)
print(mi_set) # Imprime: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

# Nota: Es posible incluir nuevos elementos en un set, los cuales pueden venir de listas, tuplas, set, etc.
```

`Diferencias clave`:

1. Modificación del set original:

- `union()`: No modifica el set original, retorna un nuevo set.
- `update()`: Modifica el set original directamente.

1. Retorno:

- `union()`: Retorna un nuevo set con la unión de los elementos.
- `update()`: No retorna nada (retorna None), solo actualiza el set original.

## `Eliminación de elementos del set`

El método `remove()`, elimina un elemento del set. Si no se encuentra el elemento, el método `remove()` genererá errores, por lo que es bueno verificar si el elemento esta presente en el `set`.

```py
mi_set = {1, 2, 3, 4, 5}

# Cuando se conoce el elemento
mi_set.remove(3)
print(mi_set) # Imprime: {1, 2, 4, 5}

# Cuando se elimina un elemento inexistente
mi_set.remove(6)
print(mi_set) # Imprime: KeyError/Errordeclave: 6
```

El método `discard()`, elimina un elemento del set, pero no genera error si el elemento no existe.

```py
# Cuando se conoce el elemento
mi_set = {1, 2, 3, 4, 5}
mi_set.discard(4)
print(mi_set) # Imprime: {1, 2, 3, 5}

# Cuando se elimina un elemento inexistente
mi_set = {1, 2, 3, 4, 5}
mi_set.discard(6)
print(mi_set) # Imprime: {1, 2, 3, 4, 5}
```

El método `clear()`, elimina o vacia todos los elementos del set.

```py
mi_set = {1, 2, 3, 4, 5}
mi_set.clear()
print(mi_set) # Impirme un set vacío: set()
```

El método `pop()` elimina un elemento aleatorio de la lista y devuelve el elemento eliminado.

```py
mi_set = {1, 2, 3, 4, 5}
print(mi_set.pop()) # Imprime: 1
print(mi_set) # Imprime: {2, 3, 4, 5}
```

El operador `del`, elimina el set completamente de la memoria.

```py
mi_set = {1, 2, 3, 4, 5}
del mi_set
# Intentar acceder al set después de eliminarlo, generará un error porque el set ya no existe
print(mi_set) # Imprime: NameError: name 'mi_set' is not defined
```

## `Convertir una lista en set`

Es posible convertir una `lista` en un `set` y un `set` en una `lista`. Al convertir la `lista` en `set`, se eliminan los duplicados y solo se reservarán los elementos únicos.

```py
mi_lista = [1, "Carlos", 3, "Carlos", 4, 3, 5.5]
print(type(mi_lista)) # Impime: <class 'list'>
mi_set = set(mi_lista)
print(type(mi_set)) # Imprime: <class 'set'>
print(mi_set) # Imprime: {1, 3, 4, 5.5, 'Carlos'}
```

## `Intercepción de elementos`

Retorna un nuevo set con los elementos comunes a ambos sets.

```py
set_1 = {"Carlos", "Maria", "Santiago", 45, 90}
set_2 = {90, 34, 89, "Carlos", "Maria"}
inter_set = set_1.intersection(set_2)
print(inter_set) # Imprime: {'Carlos', 90, 'Maria'}
```

```py
python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "a", "g", "r", "o", "n"}
interset = python.intersection(dragon)
print(interset) # Imprime: {'n', 'o'}
```

## `Comprobación de subset y supersets`

En Python, los conceptos de subsets (subconjuntos) y supersets (superconjuntos) se relacionan con las comparaciones entre sets para determinar si uno es un subconjunto o un superconjunto de otro.

### `Subsets (Subconjuntos)`

Un set A es un subconjunto de un set B si todos los elementos de A están también en B. En otras palabras, A está contenido en B.

Podemos verificar si un `set` es un subconjnto de otro usando el método `issubset()` o el operador `<=`.

```py
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

# Verificar si setA es un subconjunto de setB
print(setA.issubset(setB))  # True

# Usando el operador <=
print(setA <= setB)  # True
```

Si A es un subconjunto estricto de `B` (es decir, `A` está contenido en `B` pero `B` tiene elementos adicionales), puedes usar el operador `<:`

```py
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

# Verificar si setA es un subconjunto estricto de setB
print(setA < setB)  # True
```

### `Supersets (Superconjuntos)`

Un set `A` es un superconjunto de un set `B` si `A` contiene todos los elementos de `B`. En otras palabras, `A` es más grande o igual a `B`.

Podemos verificar si un set es un superconjunto de otro usando el método `issuperset()` o el operador `>=`.

```py
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}

# Verificar si setA es un superconjunto de setB
print(setA.issuperset(setB))  # True

# Usando el operador >=
print(setA >= setB)  # True
```

Si `A` es un superconjunto estricto de `B` (es decir, `A` tiene elementos adicionales), puedes usar el operador `>:`

```py
setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}

# Verificar si setA es un superconjunto estricto de setB
print(setA > setB)  # True
```

## `Diferencia entre sets`

El método `difference()`, devuelve la diferencia entre dos `sets`

```py
set_1 = {"item1", "item2", "item3", "item4"}
set_2 = {"item1", "item4"}
set_difference = set_1.difference(set_2)
print(set_difference) # Imprime: {'item2', 'item3'}

numbers_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers_2 = {2, 4, 6, 8, 10}
numbers_difference = numbers_1.difference(numbers_2)
print(numbers_difference) # Imprime: {0, 1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python_difference = python.difference(dragon)
dragon_difference = dragon.difference(python)  
print(python_difference) # Imprime: {'t', 'p', 'y'}
print(dragon_difference) # Imprime: {'r', 'a', 'g', 'd'}
```

## `Diferencia simétrica entre sets`

La diferencia simétrica entre dos `sets` `A` y `B` es el conjunto de los elementos que están en `A` o en `B`, pero no en ambos. Es decir, excluye los elementos que están en ambos `sets`.

Podemos usar el método `symmetric_difference()` o el operador `^`.

```py
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Hallar la diferencia simétrica entre setA y setB
diferencia_simetrica = setA.symmetric_difference(setB)
print(diferencia_simetrica)  # {1, 2, 5, 6}

# Usando el operador '^'
diferencia_simetrica = setA ^ setB
print(diferencia_simetrica)  # {1, 2, 5, 6}
```

En este caso, la diferencia simétrica contiene los elementos que están en setA o setB, pero no en ambos (1, 2, 5, 6). 

`Diferencia simétrica:` A ^ B (elementos que no se comparten entre A y B).

## `Sets disjuntos`

El método `isdisjoint()` se utiliza para comprobar si dos `sets`(o un `set` y cualquier otro iterable) son disjuntos, es decir, si no tiene elementos en común. 

- Si los `sets` no tienen ningún elemento en común, entonces son `disjuntos`, y el método `isdisjoint()` devolverá `True.`

- Si tiene al menos un elemento en común, devolverá `False`

```py
setA = {1, 2, 3}
setB = {4, 5, 6}
setC = {2, 4, 6}

# Comprobar si setA y setB son disjuntos
print(setA.isdisjoint(setB))  # True, no tienen elementos en común

# Comprobar si setA y setC son disjuntos
print(setA.isdisjoint(setC))  # False, tienen en común el número 2
```

`¿Se puede usar con otros iterables?`

Sí, es posible usar `isdisjoint()` con otros tipos de iterables (como listas, tuplas, etc.), no solo con sets.

```py
setA = {1, 2, 3}
lista = [4, 5, 6] # Ejemplo con lista

print(setA.isdisjoint(lista))  # True, no tienen elementos en común
```

`Nota:`

Los sets en Python son útiles cuando necesitas colecciones de elementos únicos y no te importa el orden de los mismos. Son perfectos para realizar operaciones como uniones, intersecciones y diferencias entre colecciones.

[**`Inicio`**](./README.md)
**-**
[**`Ejercicios Sets`**](./_12_sets_ejercicios.md)