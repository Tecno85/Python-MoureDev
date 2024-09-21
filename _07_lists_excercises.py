""" Excercises Level 1"""

# 1. Declarar una lista vacia

my_list = []
print(my_list)

# 2. Declarar una lista con más de 5 elementos

operation = 5 * 6
fruits = ["Oranges", "Apples"]

my_list = ["ivan", True, 37, operation, fruits]
print(my_list)

# 3. Encuentra la longitud de tu lista.

operation = 5 * 6
fruits = ["Oranges", "Apples"]

my_list = ["ivan", True, 37, operation, fruits]
print(len(my_list))

# 4. Obtenga el primer elemento, el elemento del medio y el último elemento de la lista

operation = 5 * 6
fruits = ["Oranges", "Apples"]

my_list = ["ivan", True, 37, operation, fruits]
print("Primer Elemento: " + my_list[0]) # Obtengo el primer elemento
elemento_central = len(my_list) // 2
print("Elemento Central: ", my_list[elemento_central])
print("Último Elemento: ", my_list[-1]) # Obtengo el último elemento por indice negativo
print("Último Elemento: ", my_list[4]) # Obtengo el último elemento por indice positivo

# 5. Declara una lista llamada mixed_data_types, pon tu (nombre, edad, altura, estado civil, dirección)

mixed_data_types = ["Ivan", 39, 1.64, "Casado", "Mirador de la Sierra 2"]

print(len(mixed_data_types))

# 6. Declare una variable de lista denominada it_companies y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprime la lista usando print()

print(it_companies)

# 8. Imprime el número de empresas de la lista

print(len(it_companies))

# 9. Imprime la primera, la intermedia y la última empresa

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies[0]) # Imprime el primer elemento o empresa

intermediate_company = len(it_companies)  // 2
print(it_companies[intermediate_company]) # Imprime la empresa intermedia

print(it_companies[-1]) # Imprime la ultima elemento o empresa

# 10. Imprima la lista después de modificar una de las empresas

it_companies[3] = "Tesla"
print(it_companies)

# 11. Agregar una empresa de TI a it_companies

it_companies.append("Twitter")
print(it_companies)

# 11. Cambie uno de los nombres de la it_companies a mayúsculas (¡excluido IBM!)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies[1] = "GOOGLE" # Solución # 1
it_companies[2] = it_companies[2].upper() # Solución # 2
print(it_companies)


# 12. Une el it_companies con una cadena '#; '

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
combinet_companies = " - ".join(it_companies)
print(combinet_companies) # Imprime: Facebook - Google - Microsoft - Apple - IBM - Oracle - Amazon

# 13. Compruebe si existe una determinada empresa en la lista de it_companies.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
check_company = "Oracle" in it_companies
print(check_company) # Imprime: True

# 14. Ordene la lista usando el método sort()

unorder_list = [4, 7, 9, 2, 8, 6, 3, 1, 5, 10]
unorder_list.sort()
print(unorder_list) # Imprime: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 15. Invierta la lista en orden descendente usando el método reverse()

unorder_list = [4, 7, 9, 2, 8, 6, 3, 1, 5, 10]
unorder_list.sort(reverse = True)
print(unorder_list) # Imprime: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 16. Corta las 3 primeras empresas de la lista

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
some_companies = it_companies[0:3] # Solución 1
some_companies = it_companies[:3] # Solución 2
print(some_companies) # Imprime: ['Facebook', 'Google', 'Microsoft']

# 17. Elimine la empresa o empresas de TI intermedias de la lista

# Solución 1
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

middle_position = len(it_companies) // 2
delete_company = it_companies.pop(middle_position)
print(delete_company)
print(it_companies)

# Solución 2
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)
middle_position = len(it_companies) // 2
print(it_companies.pop(middle_position))
print(it_companies)

# Solución 3

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Esta solución me muestra el indice de la compañia eliminada
delete_company = len(it_companies) // 2
print(it_companies)
del it_companies[delete_company]
print(delete_company)
print(it_companies)

# Esta solución me muestra el nombre de la compañia eliminada
delete_company = it_companies[len(it_companies) // 2]
del it_companies[len(it_companies) // 2]
print(delete_company)
print(it_companies)



""" 

Eliminar la primera empresa de TI de la lista

Eliminar la empresa o empresas de TI intermedias de la lista

Eliminar la última empresa de TI de la lista

Eliminar todas las empresas de TI de la lista

Destruir la lista de empresas de TI """