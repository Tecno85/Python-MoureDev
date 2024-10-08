# Crea un diccionario vacío llamado perro

perro = {}
print(perro)
# Imprime: {}
mi_perro = dict()
print(perro)
# Imprime: {}

# * Agregue nombre, color, raza, patas, edad al diccionario de perros

perro = {"nombre": "Tony", "color": "Negro", "raza": "Pastor Aleman", "edad": 10}
print(perro)
# Imprime: {'nombre': 'Tony', 'color': 'Negro', 'raza': 'Pastor Aleman', 'edad': 10}

# * Cree un diccionario de estudiante y agregue first_name, last_name, sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario

estudiante = {
    "firts_name": "Ismael",
    "last_name": "Madrid",
    "sexo": "Masculino",
    "edad": 8,
    "país": "Colombia",
    "ciudad": "Valledupar",
    "habilidades": ["HTML", "CSS", "JavaScript", "Python"],
}

# * Obtener la longitud del diccionario del alumno

print(len(estudiante))

# * Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista

print(type(estudiante["habilidades"]))

# * Modifique los valores de las habilidades agregando una o dos habilidades

estudiante["habilidades"].extend(["JAVA", "GitHub"])
estudiante["habilidades"] += ["JAVA", "GitHub"]
print(estudiante)

# * Obtener las claves del diccionario como una lista

claves_diccionario = estudiante.keys()
print(claves_diccionario)

# * Obtener los valores del diccionario como una lista

valores_diccionarios = estudiante.values()
print(valores_diccionarios)

# * Cambie el diccionario a una lista de tuplas usando el método items()

estudiante.items()
print(estudiante.items())
list_estudiante = list(estudiante.items())
print(list_estudiante)
print(type(list_estudiante))

# * Eliminar uno de los elementos del diccionario

print(estudiante)
estudiante.pop("firts_name")
print(estudiante)

estudiante.popitem()
print(estudiante)

del estudiante["last_name"]
print(estudiante)

estudiante.clear()
print(estudiante)

# * Eliminar uno de los diccionarios

estudiante = {
    "firts_name": "Ismael",
    "last_name": "Madrid",
    "sexo": "Masculino",
    "edad": 8,
    "país": "Colombia",
    "ciudad": "Valledupar",
    "habilidades": ["HTML", "CSS", "JavaScript", "Python"],
    "gato": {"nombre": "Mishu", "peso": 10},
}

print(estudiante)
del estudiante["gato"]
print(estudiante)
