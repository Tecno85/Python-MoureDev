![pythopn](./assets/img/Python_moderno.webp)

# _`print()`_ 

`print()` permite controlar cómo se separan los elementos que imprimes mediante el uso de los parámetros sep y end.

---

Parámetro `sep`

El parámetro `sep` en la función `print()` se utiliza para especificar el separador entre los elementos que estás imprimiendo. Por defecto, el separador es un espacio (`' '`), pero puedes cambiarlo a cualquier otro carácter o cadena.

Ejemplo:

```py
print('Python', 'JavaScript', 'Java', sep=' | ')
```

Salida:

```py
Python | JavaScript | Java
```

En este caso, '`|`' se utiliza como separador entre cada cadena.

---

_Parámetro_ **`end`**

El parámetro `end` controla qué se imprime al final de la llamada a `print()`. Por defecto, `print()` termina con un salto de línea `('\n')`, pero puedes cambiarlo a cualquier otro carácter o cadena, o incluso dejarlo vacío.

Ejemplo:

```py
print('Hola', end=' ')
print('Mundo')
```

Salida:

```py
Hola Mundo
```

Aquí, en lugar de un salto de línea, se coloca un espacio al final del primer `print()`, por lo que la siguiente impresión comienza en la misma línea.

---

**`Ejemplo combinado`**

Puedes combinar ambos parámetros para personalizar la salida de tus impresiones:

```py
print('Python', 'JavaScript', 'Java', sep=', ', end='.\n')
```

Salida:

```py
Python, JavaScript, Java.
```

En este ejemplo, `_sep=', '` coloca una coma y un espacio entre los elementos, y `end='.\n'` coloca un punto y luego un salto de línea al final de la impresión.

---

---

## `Formatear cadenas (strings) `

En Python, existen varias formas de formatear cadenas (strings) que facilitan la inserción de variables y expresiones dentro de texto. Formas más comunes:

### 1. **Concatenación**

Puedes concatenar cadenas con el operador `+`.

```python
nombre = "Juan"
edad = 30
mensaje = "Hola, " + nombre + ". Tienes " + str(edad) + " años."
print(mensaje)
```

### 2. **Interpolación usando el operador `%`**

Este método usa un estilo similar al del lenguaje C.

```python
nombre = "Juan"
edad = 30
mensaje = "Hola, %s. Tienes %d años." % (nombre, edad)
print(mensaje)
```

- `%s`: Para strings.
- `%d`: Para enteros.

### 3. **Método `.format()`**

El método `format()` te permite insertar valores en posiciones específicas dentro de una cadena.

```python
nombre = "Juan"
edad = 30
mensaje = "Hola, {}. Tienes {} años.".format(nombre, edad)
print(mensaje)
```

También puedes usar índices o nombres para mayor flexibilidad.

```python
mensaje = "Hola, {0}. Tienes {1} años.".format(nombre, edad)
# O con nombres
mensaje = "Hola, {nombre}. Tienes {edad} años.".format(nombre=nombre, edad=edad)
```

### 4. **f-Strings (Literales de formato)**

A partir de Python 3.6, se introdujeron los f-strings, que permiten incrustar expresiones directamente dentro de las llaves `{}`.

```python
nombre = "Juan"
edad = 30
mensaje = f"Hola, {nombre}. Tienes {edad} años."
print(mensaje)
```

También puedes realizar cálculos dentro de las llaves.

```python
precio = 100.567
mensaje = f"El precio con descuento es {precio * 0.9:.2f} euros."
print(mensaje)
```

El `.2f` especifica que quieres redondear el número a 2 decimales.

### 5. **Template Strings (módulo `string`)**

El módulo `string` proporciona una forma más segura para formatear cadenas, útil cuando se trabaja con datos externos que no deben ser manipulados de manera accidental o maliciosa.

```python
from string import Template

t = Template("Hola, $nombre. Tienes $edad años.")
mensaje = t.substitute(nombre="Juan", edad=30)
print(mensaje)
```

---

---

## Método `find()`

El método find() en Python se utiliza para buscar la posición (índice) de una subcadena dentro de una cadena más grande. Si la subcadena se encuentra, find() devuelve el índice de la primera aparición de dicha subcadena. Si no se encuentra, devuelve -1.

---

## El método `index()`

En Python es muy similar al método `find()`, pero con una diferencia importante: mientras que `find()` devuelve `-1` si no encuentra la subcadena, `index()` **lanza una excepción (`ValueError`)** si la subcadena no se encuentra en la cadena.

### Sintaxis:

```python
cadena.index(subcadena, inicio, fin)
```

### Parámetros:

- **subcadena**: La subcadena que estás buscando en la cadena principal.
- **inicio** (opcional): El índice desde donde se comenzará a buscar. Si no se proporciona, empieza desde el principio.
- **fin** (opcional): El índice donde se terminará la búsqueda. Si no se proporciona, busca hasta el final de la cadena.

### Ejemplos:

1. **Buscar una subcadena**:

   ```python
   texto = "Hola, mundo"
   posicion = texto.index("mundo")
   print(posicion)  # Salida: 6
   ```

   Aquí, el método `index()` devuelve `6`, que es el índice donde comienza la palabra "mundo".

2. **Subcadena no encontrada (lanzará una excepción)**:

   ```python
   texto = "Hola, mundo"
   posicion = texto.index("Python")  # Lanza ValueError
   ```

   A diferencia de `find()`, que devolvería `-1` si no encuentra la subcadena, `index()` lanzará una excepción `ValueError` porque "Python" no está en el texto.

3. **Buscar desde un índice específico**:
   ```python
   texto = "Hola, mundo, bienvenido al mundo"
   posicion = texto.index("mundo", 10)
   print(posicion)  # Salida: 25
   ```
   En este caso, se comienza la búsqueda desde el índice 10 y se encuentra "mundo" en el índice 25.

### Diferencias clave entre `find()` y `index()`:

- `find()` devuelve `-1` si no encuentra la subcadena.
- `index()` lanza una excepción si no encuentra la subcadena.

Si estás seguro de que la subcadena estará presente en la cadena, `index()` puede ser una opción, pero si no lo estás, es mejor usar `find()` para evitar errores.

---

---

# Corchetes `[]`

Se conocen comúnmente como corchetes o brackets en programación. Su uso depende del contexto, pero en muchos lenguajes, como Python y JavaScript, se utilizan para:

Listas o arrays: Para definir o acceder a elementos en una lista o array.

Ejemplo en Python: mi_lista = [1, 2, 3]
Índices: Para acceder a un elemento en una posición específica de una lista, cadena u otro tipo de colección.

Ejemplo en Python: mi_lista[0] accede al primer elemento de la lista.
Slices (corte): Para extraer porciones de una secuencia (como en tu ejemplo anterior).

Ejemplo: cadena[0:5].

## Método `round()`

Si necesitas redondear el valor de una variable `float` directamente (sin formatear la salida), puedes usar la función `round()`:

```py
mi_numero = 3.14159265359
mi_numero_redondeado = round(mi_numero, 2)  # Redondea a 2 decimales
print(mi_numero_redondeado)
```

---

---

## _`Listas`_

Una lista en Python es una estructura de datos que permite almacenar múltiples elementos en un solo contenedor o variable. Las listas son _**ordenadas**_, _**cambiales**_ y permiten elementos _**duplicados**_.

### Caracteristicas de las _`Listas`_

1. **Ordenadas**: Los elementos en una lista mantienen el orden en que se aregaron. Se acceden a los elementos usando índices, que empiezan desde 0.

1. **Cambiables**: Puedes modificar los elementos de una lista después de haberla creado. Puedes cambiar, agregar o eliminar elementos en una lista.

1. **Permiten Duplicados**: Las listas pueden contener elementos duplicados. Los elementos en una lista no tienen que ser únicos.

1. **Heterogéneas**: Una lista puede contener elementos de diferentes tipos, como números, cadenas, booleanos, otras listas, etc.

### Sintaxis

Las listas se crean usando cohorchetes **`[]`**, y los elementos se separan por comas. Ejemplo:

```py
my_list = [1, 2, 3, "four", 5.0]
```

### Acceso a los Elementos

Puedo acceder a los elementos de una lista usando índices:

```py
first_element = my_list[0] # Accedo al primer elemento (1)
last_element = my_list[-1] # Accedo al último elemento (5.0)
```

### Modificación de Elementos

Puedes cambiar el valor de un elemento en una lista:

```py
my_list = [1, 2, 3, "four", 5.0]

my_list[3] = "Four Modified"
print(my_list) # Imprime [1, 2, 3, "Four Modified", 5.0]
```

### Métodos Comunes

- `append()`: Agrega un elemento al final de la lista.

```py
my_list = [1, 2, 3, "four", 5.0]
my_list.append(6)
my_list = [1, 2, 3, "four", 5.0, 6] # Agrega el número "6" al final de la lista.
```

- `insert()`: Inserta un elemento en una posición específica de la lista.

```py
my_list = [1, 2, 3, "four", 5.0]
my_list.insert(3, "Hello Ismael")
my_list = [1, 2, 3, "four", "Hello Ismael", 5.0] # Inserto "Hello Ismael" en la posición 4.
```

- `remove()`: Elimina un elemento específico de una lista.

```py
my_list = [1, 2, 3, "four", 5.0]
my_list.remove(3)
my_list = [1, 2, "four", 5.0] # Eliminó el número "3"
```

- `pop()`: Elimina el índice espedificado( o el último elemento si no se especifica el índice).

```py
lst = ['item1', 'item2']
lst.pop()       # last item
```
## **`slice (rebanado)`**

En Python, puedes usar el método **`insert()`** para agregar un solo elemento en una posición específica, pero si quieres agregar **varios elementos** a una lista en una posición determinada, una buena opción es utilizar el ***slice* (rebanado)** para insertar una lista de varios elementos en una posición específica.

Aquí te dejo un ejemplo de cómo hacerlo:

### Ejemplo:
```python
# Lista inicial
mi_lista = [1, 2, 3, 7, 8]

# Elementos a agregar
nuevos_elementos = [4, 5, 6]

# Agregar los nuevos elementos en la posición 3 (antes del 7)
mi_lista[3:3] = nuevos_elementos

print(mi_lista)
```

### Resultado:
```python
[1, 2, 3, 4, 5, 6, 7, 8]
```

### Explicación:
- `mi_lista[3:3]` selecciona la **posición 3** (justo antes del número 7) sin eliminar ningún elemento existente.
- Luego, asignamos `nuevos_elementos` en esa posición, lo que inserta los nuevos elementos sin reemplazar los actuales.

De esta forma, puedes agregar varios elementos en la posición específica de la lista.

## `La sintaxis [5:5]`

En Python se refiere a un slice (rebanado) de la lista, y aquí está la explicación:

- full_stack[5:5]:

  - El primer número (5) es el índice de inicio y el segundo (también 5) es el índice final.

  - Este slice no selecciona ningún elemento de la lista, porque el inicio y el final son iguales. Esto significa que estás eligiendo una posición vacía en la lista donde puedes insertar nuevos elementos.

**¿Por qué se repite?**

- Usar el mismo índice en el inicio y el final es una forma de indicar una posición vacía. Así que cuando haces full_stack[5:5] = new_languages, estás insertando los elementos de new_languages en esa posición vacía, sin reemplazar nada.

En resumen, la repetición de los índices es necesaria para indicar que quieres insertar elementos sin eliminar nada existente.

---
`Quéde en Tiempo: 4:04`
