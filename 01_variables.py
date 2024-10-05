"""variables""" 

# Nombres de Variables:

"""
Para nombrar variables y funciones en Python se utiliza la convención snale_case, donde las palabras estan en minúscula y separados por guiones bajos(_). Los nombre deben comenzar por letras o guion bajo
"""

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print

print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas Funciones del sistema

print(len(my_string_variable)) # (18) Nos dice el número de caracteres que tiene la variable

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!

my_name, last_name, age, alias = "Ivan", "Madrid", 39, "IvanCho"
print("Mi nombre es:", my_name, last_name,". tengo", age, "y me dicen", alias)


# Inputs
"""name = input('¿Cual es tu nombre? ')
age = input('¿Cual es tu edad? ')
print(name)
print(age)"""

# Cambiamos su nombre
name = 35
age = "Ivan"
print(name)
print(age)

# Forzamos el tipo
address: str = "Mi direccion"
print(address)
print(type(address))
address = "Ivan"
address = 1.5
address = True
print(address)
print(type(address))
