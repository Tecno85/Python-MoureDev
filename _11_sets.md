# `Sets` ![icon_sets](/assets/img/icon_6.png)

Un **`set`**, es una colleción desordenada de elementos únicos. A diferencia de las listas o tuplas, los **`sets`** no permiten elementos duplicados y sus elementos no están indexados, lo que significa que no es posible acceder a un elemento específico mediante un índice.

_Características de los `sets`_:

- Elementos únicos: No pueden tener elementos duplicados.

- Desordenados: No mantienen ningún orden específico.

- Mutable: Puedes agregar o eliminar elementos de un set.

- No indexado: No se puede acceder a los elementos mediante índices como en las listas o tuplas.

### `Cómo crear un` _`set`_

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

### `Obtención de la longitud`

Se utiliza el método `len()` para encontrar la longitud de un `set`

```py
mi_set = {1, 2, 3, 4, 5}
len(mi_set)
print(len(mi_set)) # Imprime: 5
```

### `Acceso a los elementos`

Se accede a los elementos de un `set` mediante los bucles. El tema de bucles se trata más adelante.

### `Comprobación de elementos`

Para comprobar si un elemento está presente en un `set`, se usa el operador `in`, el cual retornará `True` si está el elemento en el `set` o `False` si no lo está.

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

### `Agregar elementos al set`

Para agregar elementos a un `set`. Utilizamos el método `add()`.

```py
mi_set = {1, 2, 3, 4, 5}
mi_set.add(6) # Agega el número 6
print(mi_set) # Imprime: {1, 2, 3, 4, 5, 6}
```
