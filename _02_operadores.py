"""Operadores Aritméticos"""

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3) # Una división aproxima resultado a entero. 
print(2 ** 2) # Exponenciación
print(2 ** 3 + 3 -7 / 1 // 4) # Exponenciación

print("Hola " +   "python " + "¿Qué tal?") # Hola python Que tal?
print("Hola " + str(5)) # Hola 5
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
