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

