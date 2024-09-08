"""Operadores de Asignación"""

# Asignan valores a las variables

x = 10 # Asignación simple
x += 5 # Asignación con suma: Equivale a x = x + 5
x -= 3 # Asignación con resta: Equivale a x = x - 3
x *= 2 # Asignación con multiplicación: Equivale a x = x * 2
x /= 2 # Asignación con división: Equivale a x = x / 2
x %= 3 # Asignación con módulo: Equivale a x = x % 3
x **= 2 # Asignación con exponenciación: Equivale a x = x ** 2
x //= 3 # Asignación con división entera: Equivale a x = x // 3

"""Operadores Aritméticos"""

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # módulo o resto
print(10 // 3) # División del suelo (floor division): Una división que aproxima el resultado al mayor entero de la división. 
print(2 ** 2) # Exponenciación
print(2 ** 3 + 3 -7 / 1 // 4) # Exponenciación

# Operaciones con cadenas de texto 

print("Hola " +   "python " + "¿Qué tal?") # Hola python Que tal?
print("Hola " + str(5)) # Hola 5

# Operaciones mixtas
print("Hola " * (2 ** 3)) # Hola Hola Hola Hola Hola Hola Hola Hola  

my_float = 2.5 * 2
print("Hola " * int(my_float)) # Hola Hola Hola Hola Hola 

"""Operadores de Comparación"""

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print("Escribo este texto para separar en la salida de la terminal")

# Operadores con cadenas de texto
print("Hola" > "Python") # Esta comparando el orden alfabético
print(len("Hola") >= len("Zola")) # Esta comparando la cantidad de caracteres
print("Hola" < "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

"""Operadotes Lógicos""" 

print("Espacio para resultados de Operadores Lógicos")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" < "Python")
print(3 > 4 or ("Hola" < "Python" and 4 == 4))
print(not(3 < 4 and "Hola" < "Python"))

"""Operadores de Pertenencia"""

# Son utiles para verificar la presencia o ausencia de elementos en diferentes tipos de colecciones

# Operador "in" Verifica si un valor está presente en una secuencia o colección
# Operador "not in" Verifica si un valor no está presente en uns secuencia o colección

# Ejemplo: cadenas de texto

cadena = "Hello Word"
print("Hello" in cadena) # True, dado que si está presente
print("goobye" not in cadena) # True, dado que no está presente

# Ejemplo: listas

lista = [10, 20, 30]
print(20 in lista) # True
print(30 not in lista) # False





