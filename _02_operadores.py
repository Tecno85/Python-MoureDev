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
print(10 % 3)
print(10 // 3) # Una división aproxima resultado a entero. 
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
