# Diccionarios ![Icon Diccionario](/assets/img/icon_21.png)

Un `diccionario` en Python es una colección de datos desordenada, mutable (puede cambiar), y indexada por llaves (`keys`) únicas. A diferencia de las listas o tuplas, que utilizan índices numéricos para acceder a los elementos, los diccionarios usan claves para acceder a los valores.

Los diccionarios se definen usando llaves `{}`, y cada elemento dentro del diccionario es un par `clave-valor`.

## `Creación de un diccionario`

Para crear un diccionario usamos **_llaves_**, **`{}`** o la función incorporado **`dict()`**

```py
# sintaxis
mi_diccionario = {}
m_otro_diccionario = dict()

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

El método **`len()`**, comprueba el número de pares **`clave: valor`** en el diccionario.

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

Al acceder a un elemento por nombre de clave, se genera un error si la clave no existe. Para evitar este error primero tenemos que comprobar si existe una clave o podemos utilizar el métod **`get()`**