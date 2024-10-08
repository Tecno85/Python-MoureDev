# ![Icono Diccionario](/assets/img/icon_22.png) Ejercicios Diccionarios ![Icono Diccionario](/assets/img/icon_22.png)

**1. Crea un diccionario vacío llamado perro**.

```py
perro = {}
mi_perro = dict()

print(type(perro)) # Imprime: <class 'dict'>
print(type(mi_perro))  # Imprime: <class 'dict'>
```

**2. Agregue nombre, color, raza, patas, edad al diccionario de perros**.

```py
perro = {
    "nombre": "Tony",
    "color": "Negro",
    "raza": "Pastor Aleman",
    "patas": 4,
    "edad": 6
    }

print(perro) # Imprime: {'nombre': 'Tony', 'color': 'Negro', 'raza': 'Pastor Aleman', 'patas': 4, 'edad': 6}
```

**3. Cree un diccionario de estudiante y agregue first_name, last_name, país y ciudad como claves para el diccionario**.

```py
estudiante = dict(
    nombre="Ivan",
    apellido="Madrid",
    pais="Colombia",
    ciudad="Valledupar",
)

#  Imprime: {'nombre': 'Ivan', 'apellido': 'Madrid', 'pais': 'Colombia', 'ciudad': 'Valledupar'}
print(estudiante)
```

**4. Obtener la longitud del diccionario del alumno**.

```py
alumno = dict(
    nombre="Ivan",
    apellido="Madrid",
    pais="Colombia",
    ciudad="Valledupar",
)

print(len(alumno)) #  Imprime: 4 pares
```

**5. Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista**.

```py
alumno = {
    "nonmbre": "Ismael",
    "Apellido": "Madrid",
    "habilidades": ["HTML", "CSS", "Python"]
}

print(alumno["habilidades"]) # Imprime: ['HTML', 'CSS', 'Python'] 
print(type(alumno["habilidades"])) # Imprime: <class 'list'>
```

**6. Modifique los valores de las habilidades agregando una o dos habilidades**.

```py
alumno = {
    "nombre": "Ismael",
    "Apellido": "Madrid",
    "habilidades": ["HTML", "CSS", "Python"]
}

# Agregando un elemento
alumno["habilidades"].append("JavaScript")
print(alumno["habilidades"])
# Imprime: ['HTML', 'CSS', 'Python', 'JavaScript']

# Agregando dos o más elementos
alumno["habilidades"].extend(["Markdown", "GitHub"])
print(alumno["habilidades"])
# Imprime: ['HTML', 'CSS', 'Python', 'JavaScript', 'Markdown', 'GitHub']

# Otra forma de Agregar dos o más elementos, usando el operador `+=`
alumno["habilidades"] += ["VSC", "GitBash"]
print(alumno["habilidades"])
# Imprime: ['HTML', 'CSS', 'Python', 'JavaScript', 'Markdown', 'GitHub', 'VSC', 'GitBash']
```

**7. Obtener las claves del diccionario como una lista**.

```py
alumno = {
    "nombre": "Ismael",
    "Apellido": "Madrid",
    "habilidades": ["HTML", "CSS", "Python"]
}

lista_claves = alumno.keys() 
print(lista_claves) # Imprime: dict_keys(['nombre', 'Apellido', 'habilidades'])
```

**8. Obtener los valores del diccionario como una lista**.

```py
alumno = {
    "nombre": "Ismael",
    "Apellido": "Madrid",
    "habilidades": ["HTML", "CSS", "Python"]
}

lista_valores = alumno.values()
print(lista_valores) # Imprime: dict_values(['Ismael', 'Madrid', ['HTML', 'CSS', 'Python']])
```

**9. Cambie el diccionario a una lista de tuplas usando el método items()**.

```py
alumno = {
    "nombre": "Ismael",
    "Apellido": "Madrid",
    "habilidades": ["HTML", "CSS", "Python"]
}

print(type(alumno)) 
# Imprime: <class 'dict'>
print(alumno)  
# Imprime: {'nombre': 'Ismael', 'Apellido': 'Madrid', 'habilidades': ['HTML', 'CSS', 'Python']} 
lista_tuplas = alumno.items()
print(lista_tuplas)
# Imprime: dict_items([('nombre', 'Ismael'), ('Apellido', 'Madrid'), ('habilidades', ['HTML', 'CSS', 'Python'])])
print(type(lista_tuplas)) 
# Imprime: <class 'dict_items'>

# Convertir la vista dict_item a una lista con el constructor "list"
lista_tuplas = list(alumno.items())
print(lista_tuplas) 
# Imprime: [('nombre', 'Ismael'), ('Apellido', 'Madrid'), ('habilidades', ['HTML', 'CSS', 'Python'])]
print(type(lista_tuplas))
# Imprime: <class 'list'>
```

**10. Eliminar uno de los elementos del diccionario**.

```py
alumno = {
    "nombre": "Ismael",
    "Apellido": "Madrid",
    "sexo": "Masculino",
    "habilidades": ["HTML", "CSS", "Python"],
    "estatura": 1.64
}

del alumno["estatura"]
print(alumno)
# Imprime: {'nombre': 'Ismael', 'Apellido': 'Madrid', 'sexo': 'Masculino', 'habilidades': ['HTML', 'CSS', 'Python']}

alumno.pop("habilidades")
print(alumno)
# Imprime: {'nombre': 'Ismael', 'Apellido': 'Madrid', 'sexo': 'Masculino'}

alumno.popitem()
print(alumno)
# Imprime: {'nombre': 'Ismael', 'Apellido': 'Madrid'}
```

**11. Eliminar uno de los diccionarios**.

```py
alumno = {
    "nombre": "Ismael",
    "Apellido": "Madrid",
    "sexo": "Masculino",
    "habilidades": ["HTML", "CSS", "Python"],
    "estatura": 1.64,
    "familia": {"hijo_menor": "Esteban", "hijo_mayor": "Ismael", "Esposa": "Katerin", "mama": "Emma"}
}

del alumno["familia"]
print(alumno)
# Imprime: {'nombre': 'Ismael', 'Apellido': 'Madrid', 'sexo': 'Masculino', 'habilidades': ['HTML', 'CSS', 'Python'], 'estatura': 1.64}
```