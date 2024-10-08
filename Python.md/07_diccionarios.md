# `Diccionarios` ![Icon Diccionario](/assets/img/icon_21.png)

Un `diccionario` en Python es una colección de datos desordenada, mutable (puede cambiar), y indexada por llaves (`keys`) únicas. A diferencia de las listas o tuplas, que utilizan índices numéricos para acceder a los elementos, los diccionarios usan claves para acceder a los valores.

Los diccionarios se definen usando llaves `{}`, y cada elemento dentro del diccionario es un par `clave:valor`.

## `Creación de un diccionario`

Para crear un diccionario usamos **_llaves_**, **`{}`** o la función incorporado **`dict()`**

```py
# sintaxis
mi_diccionario = {}
mi_otro_diccionario = dict()

mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3",
}
```

- Las **`claves`** son únicas y pueden ser de tipo strings, números o tuplas

- Los **`valores`** pueden ser de cualquier tipo de dato: números, listas, otros diccionarios, etc.

**_Ejemplo de un diccionario_**

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar"
}

print(persona) # Imprime: {'nombre': 'Ivan', 'edad': 39, 'ciudad': 'Valledupar'}
```

En este caso, **`"nombre"`**, **`"edad"`** y **`"ciudad"`** son las claves y **`"Ivan"`**, **`39`** y **`"Valledupar"`** son los valores correspondientes.

## `Longitud del dicionario`

El método **`len()`**, comprueba el número de pares **`clave:valor`** en el diccionario.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
    "habilidades": ["HTML", "CSS", "Markdown", "GitHub", "Python"],
    "direccion": {
        "calle": 6,
        "barrio": "Mirador de la sierra 2"
    }
}
print(len(persona)) # Imprime: 6 pares

```

## `Acceso a los elementos de un diccionario`

Podemos acceder a los elementos de un diccionario haciendo referencia a su nombre de clave usando corchetes **`[]`** o el método **`get()`**.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar"
}

print(persona["edad"]) # Imprime: 39
print(persona.get("nombre")) # Imprime: Ivan

# Ejemplo cuando la clave no existe
print(persona.get("altura")) # Imprime: None
print(persona["altura"]) # Imprime: KeyError: 'altura'
```

Al acceder a un elemento por nombre de clave, se genera un error si la clave no existe. Para evitar este error primero tenemos que comprobar si existe una clave o podemos utilizar el métod **`get()`**. El método **`get()`** devuelve **`None`**, que es un tipo de datos de objeto **`NoneType`**, si la clave no existe.

## `Adición o Modificación de elementos a un diccionario`

Los diccionarios son mutables, esta propiedad nos permite argregar nuevos pares **`clave:valor`** o modificar valores existentes.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar"
}

# Agregar un nuevo par clave:valor
persona["profesión"] = "Ingeniero"

# Modificar el valor de una variable existente
persona["ciudad"] = "Medellin"

print(persona) # Imprime: {'nombre': 'Ivan', 'edad': 39, 'ciudad': 'Medellin', 'profesión': 'Ingeniero'}
```

## `Eliminación de pares clave:valor en un diccionario`

Existen varias forma para eliminar un elemento específico, estas son:

- Instrucción **`del`**, elimina un elemento con el nombre de clave especificado.
- Método **`pop()`** elimina y devuelve un elemento con el nombre de clave especificado.
- Método **`popitem()`**, elimina y devuelve el último par clave:valor agregado.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
    "habilidades": ["HTML", "CSS", "Markdown", "GitHub", "Python"]
}

del persona["ciudad"]
print(persona) # Imprime: {'nombre': 'Ivan', 'edad': 39}

persona.pop("nombre") # Imprime: Ivan
print(persona) # Imprime: {'edad': 39}

# Nota: Este print nos devuelve el último elemento eliminado("habilidades") por popitem()
print(persona.popitem()) # Imprime: ('habilidades', ['HTML', 'CSS', 'Markdown', 'GitHub', 'Python'])
print(persona) # Imprime: {'edad': 39, 'es_casado': True}
```

## `Eliminar un diccionario`

Si no usamos el diccionario podemos eliminarlo por completo mediante la instrucción **`del`**

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
}

del persona
print(persona) # Imprime: NameError: name 'persona' is not defined
```

## `Borrar un diccionario`

Si no queremos los elementos de un diccionario, podemos borrarlos usando el método **`clear()`**

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
}

print(persona.clear()) # Imprime: None
```

## `Copiar un diccionario`

Podemos copiar un diccionario usando un método **`copy()`**. Con este método podemos evitar la mutación del diccionario original.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
}

copia_persona = persona.copy()
print(copia_persona) # Imprime: {'nombre': 'Ivan', 'edad': 39, 'ciudad': 'Valledupar', 'es_casado': True}
```

## `Comprobación de claves en un diccionario`

El operador **`in`** se utiliza para verificar si existe una clave en un diccionario.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
    "habilidades": ["HTML", "CSS", "Markdown", "GitHub", "Python"]
}

print("nombre" in persona) # Imprime: True
print("estatura" in persona) # Imprime: False
print("es_casado" in persona) # Imprime: True
```

## `Cambiar el diccionario a una lista de elementos`

El método **`items()`** cambia el diccionario a una lista de tuplas con pares **`clave:valor`**.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
}

print(persona.items()) # Imprime: dict_items([('nombre', 'Ivan'), ('edad', 39), ('ciudad', 'Valledupar'), ('es_casado', True)])
```

Cuando llamas al método `items()` en un diccionario, no se devuelve una lista directamente, sino un objeto especial llamado **`dict_items`**. Este tipo de objeto es una **vista** de los pares `(clave, valor)` del diccionario.

Una **vista** en Python es un objeto que refleja los datos del diccionario de manera eficiente, sin duplicarlos en memoria. Es una representación dinámica: si el diccionario cambia, la vista también reflejará esos cambios.

### Características principales

1. **No es una lista**: Aunque parece una lista de tuplas, es un tipo de objeto especial que puedes iterar, pero no es modificable como una lista normal.
   
2. **Dinamismo**: Si modificas el diccionario, el objeto `dict_items` cambiará automáticamente para reflejar esos cambios.
   
3. **Iterabilidad**: Puedes recorrerlo con un bucle `for`, igual que harías con una lista.

```python
mi_diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Obtener una vista dict_items
items_vista = mi_diccionario.items()

print(items_vista)
# Imprime: dict_items([('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Madrid')])
```

### `¿Por qué no es directamente una lista?`

La razón por la que `items()` devuelve un `dict_items` en lugar de una lista es por **eficiencia**. Como los diccionarios pueden ser muy grandes, la vista `dict_items` es más ligera en términos de memoria porque no duplica el contenido del diccionario, solo lo "refleja".

### Convertir `dict_items` a lista:

Si realmente necesitas trabajar con una lista (por ejemplo, si deseas modificarla o acceder a los elementos por índices), puedes convertir el `dict_items` a una lista con el constructor `list()`.

```python
lista_tuplas = list(mi_diccionario.items())
print(lista_tuplas)
# Imprime: [('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Madrid')]
```

## `Obtener claves de diccionario como un lista`

El método **`keys()`** nos da todas las claves de un diccionario como una lista.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
}

claves = persona.keys()
print(claves) # Imprime: dict_keys(['nombre', 'edad', 'ciudad', 'es_casado'])
```

## `Obtener valores de diccionario como un lista`

El método **`values()`** nos da todas los valores de un diccionario como una lista.

```py
persona = {
    "nombre": "Ivan",
    "edad": 39,
    "ciudad": "Valledupar",
    "es_casado": True,
}

valores = persona.values()
print(valores) # Imprime: dict_values(['Ivan', 39, 'Valledupar', True])
```


