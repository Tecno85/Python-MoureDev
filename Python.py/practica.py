# Obtener los valores del diccionario como una lista

alumno = {
    "nombre": "Ismael",
    "Apellido": "Madrid",
    "habilidades": ["HTML", "CSS", "Python"]
}

lista_valores = alumno.values()
print(lista_valores) # Imprime: dict_values(['Ismael', 'Madrid', ['HTML', 'CSS', 'Python']])