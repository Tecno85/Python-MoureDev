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

# 12. Cambie uno de los nombres de la it_companies a mayúsculas (¡excluido IBM!)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies[1] = "GOOGLE" # Solución # 1
it_companies[2] = it_companies[2].upper() # Solución # 2
print(it_companies)


# 13. Une el it_companies con una cadena '#; '

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
combinet_companies = " - ".join(it_companies)
print(combinet_companies) # Imprime: Facebook - Google - Microsoft - Apple - IBM - Oracle - Amazon

# 14. Compruebe si existe una determinada empresa en la lista de it_companies.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
check_company = "Oracle" in it_companies
print(check_company) # Imprime: True

# 15. Ordene la lista usando el método sort()

unorder_list = [4, 7, 9, 2, 8, 6, 3, 1, 5, 10]
unorder_list.sort()
print(unorder_list) # Imprime: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 16. Invierta la lista en orden descendente usando el método reverse()

unorder_list = [4, 7, 9, 2, 8, 6, 3, 1, 5, 10]
unorder_list.sort(reverse = True)
print(unorder_list) # Imprime: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 17. Corta las 3 primeras empresas de la lista

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
some_companies = it_companies[0:3] # Solución 1
some_companies = it_companies[:3] # Solución 2
print(some_companies) # Imprime: ['Facebook', 'Google', 'Microsoft']

# 18. Elimine la empresa o empresas de TI intermedias de la lista

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

# 19. Eliminar la primera empresa de TI de la lista

# Solución 1
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(0)
print(it_companies)

# Solución 2
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove("Facebook")
print(it_companies)

# Solución 3
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[0]
print(it_companies)

# 20. Eliminar la empresa o empresas de TI intermedias de la lista

# Solución 1
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
mid_company = it_companies[len(it_companies) // 2]
it_companies.remove(mid_company)
print(it_companies)

# Solución 2
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
mid_company = len(it_companies) // 2
it_companies.pop(mid_company)
print(it_companies)

# Solución 3
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
mid_company = len(it_companies) // 2
del it_companies[mid_company]
print(it_companies)

# 21. Eliminar la última empresa de TI de la lista

# Solución 1
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop()
print(it_companies)

# Solución 2
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_company = it_companies[len(it_companies) - 1]
it_companies.remove(last_company)
print(it_companies)

# Solución 3
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_company = len(it_companies) - 1
del it_companies[last_company]
print(it_companies)

# 22. Eliminar todas las empresas de TI de la lista

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

# 23. Destruir o Eliminar la lista de empresas de TI o la lista que las contiene

del it_companies

# print(it_companies)  Imprime name "it_companies" is not defined".

# 24. Une las siguientes listas:

# Solución 1
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# Solución 2
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print('str:', front_end) # Imprime la nueva lista y el tipo 
print(front_end) # Imprime solo la nueva lista sin el tipo

# Nota: 
# Solución 1: Ideal si prefieres mantener las listas originales intactas y crear una nueva lista combinada.
# Solución 2: Útil si no necesitas conservar la lista front_end original y prefieres modificarla directamente. 

# 25. Después de unirse a las listas de la pregunta 26. Copie la lista unida y asígnela a una variable full_stack. A continuación, inserte Python y SQL después de Redux.

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

new_languages = ["Python", "SQL"]

full_stack[5:5] = new_languages
print(full_stack)


""" Excercises Level 2 """ 

#* 1.La siguiente es una lista de 10 edades de estudiantes:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#* 2. Ordene la lista y encuentre la edad mínima y máxima

# Lista ordenada de menor a mayor
ages.sort()
print(ages) # Imprime la lista [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

# Edad mínima
minimum_age = ages[0]
print(minimum_age)

# Edad máxima
maximum_age = ages[-1]
print(maximum_age)

#* 3. Agregue la edad mínima y la edad máxima nuevamente a la lista

ages.insert(0, 19) # Agrega nuevamente la edad mínima
ages.append(26)
# element_position = len(ages) -1 # Se obtiene la ultima ubicación de la lista
# ages.insert(element_position, 26) # Agrega nuevamente la edad máxima
print(ages) # Imprime la lista con la edad mínima y máxima agregada

#* 4. Encuentre la edad media (un elemento del medio o dos elementos del medio divididos por dos)

ages = [80, 40, 30, 10, 70, 90, 50, 60, 20]

ages.sort()
mid_ages = ages[len(ages) // 2]
print(mid_ages)

#* 5. Encuentre la edad promedio (suma de todos los artículos dividida por su número)

ages = [80, 40, 30, 10, 70, 90, 50, 60, 20]

ages.sort()
average_age = sum(ages) / len(ages)
print(average_age)
#* Nota: En Python, puedes usar la función sum() para sumar todos los elementos de una lista y len() para obtener el número total de elementos. Así puedes calcular el promedio de manera más limpia y sencilla.

#* 6. Encuentre el rango de las edades (máx. menos mín.)

# Solución Mia - No muy optima ejeje
ages = [80, 40, 30, 10, 70, 90, 50, 60, 20]

ages.sort()
print(ages[0]) # Valor menor
print(ages[-1]) # Valor mayor

#* Nota: Python tiene las funciones min() y max() para encontrar los valores máximos y minimos en una lista. 
# Solcución 2

ages = [80, 40, 30, 10, 70, 90, 50, 60, 20]
min_age = min(ages)
max_age = max(ages)
age_range = max_age - min_age

print("El valor máximo es:", min_age)
print("El valor máximo es:", max_age)
print("El rango es:", age_range)

#* Compare el valor de (min - promedio) y (max - promedio), use el método abs()

ages = [80, 40, 30, 10, 70, 90, 50, 60, 20]

value_min = min(ages)
print(value_min)
value_max = max(ages)
print(value_max)
value_average = sum(ages) // len(ages)
print(value_average)

compare_value_min = abs(value_min - value_average)
compare_value_max = abs(value_max - value_average)

print(f"El valor (min - promedio) es: {compare_value_min} y el valor (max - promedio) es: {compare_value_max}")

#* 7. Encuentre el (los) país (s) del medio en la lista de países

# Divida la lista de países en dos listas iguales si es incluso si no hay un país más para la primera mitad.
# Si la longitud de la lista es par: Divide la lista en dos listas de igual tamaño.
# Si la longitud de la lista es impar: La primera lista debe tener un país más que la segunda. Esto significa que la primera lista contendrá un elemento adicional en comparación con la segunda.

# Solución 1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

# Calcular la longitud de la lista
mid_list_countries = len(countries) // 2

# Dividir la lista
if len(countries) % 2 == 0:
    first_list_countries = countries[:mid_list_countries]
    second_list_countries = countries[mid_list_countries:]
else:
    first_list_countries = countries[:mid_list_countries + 1]
    second_list_countries = countries[mid_list_countries + 1:]

# Imprimir las listas
print(first_list_countries)
print(len(first_list_countries))
print(second_list_countries)
print(len(second_list_countries))

# Solución 2

# Longitud de lista
list_length = len(countries)
print(f"La longitud de la lista de Países es de: {list_length} carácteres")
print()
# Longitud de la lista entre (2)
mid_len_countries = len(countries) // 2
print(f"La longitud media de los Países es de: {mid_len_countries} carácteres")
print()
# Dividir lista de países
if len(countries) % 2 == 0:
    first_lits_countries = countries[:mid_len_countries]
    second_list_countries = countries[mid_len_countries:]
else:
    first_lits_countries = countries[:mid_len_countries + 1]
    second_list_countries = countries[mid_len_countries + 1:]

print("Primera Lista de Países")
print(first_lits_countries)
print()
print("Segunda Lista de Países")
print(second_list_countries)

#* 8. ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. Desempaqueta los tres primeros países y el resto como países escandinavos.

# Solución que le di, que no es tan simplificada

countries = ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
countries_str = ' - '.join(countries)
paises_del_norte = countries[:3]
scandinavian_countries = countries[3:7]
print(paises_del_norte) 
print(scandinavian_countries) 

# Solución 2
# Se dio solución utilizando el "Desempaquetado de listas en Python"

countries = ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

[first, second, third, *scandinavian_countries] = countries

print("Los primeros paises son: ", first, second, third)
print("Los paises escandinavos son: ", scandinavian_countries)
