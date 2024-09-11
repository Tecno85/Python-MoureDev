""" Ejercicios Strings """

# 1. Concatene la cadena 'Thirty', 'Days', 'Of', 'Python' en una sola cadena, 'Thirty Days Of Python'.

thirty = "Thirty"
days = "Days"
of = "of"
python = "Python"

print(thirty + " " + days + " " + of + " " + python) # concatenación
print("%s %s %s %s" %(thirty, days, of, python)) # interpolación con módulo (%)
print("{} {} {} {}".format(thirty, days, of, python)) # método .format
print(f"{thirty} {days} {of} {python}") # f-string

# 2. Concatene la cadena 'Coding', 'For', 'All' en una sola cadena, 'Coding For All'.

palabra_1 = "Coding"
palabra_2 = "For"
palabra_3 = "All" 

print(f"{palabra_1} {palabra_2} {palabra_3}")

# 3. Declare una variable denominada company y asígnela a un valor inicial "Coding For All".

company = "Coding For ALL"

# 4. Imprime la variable company usando print().

print(company)

# 5. Imprima la longitud de la cadena de la empresa utilizando el método len() y print().

print(len(company))

# 6. Cambie todos los caracteres a letras mayúsculas usando el método upper().

print(company.upper())


# 7. Cambie todos los caracteres a letras minúsculas usando el método lower().

print(company.lower())

# 8. Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Corta la primera palabra de la cadena Coding For All.

company = "Coding For ALL"

first_word = company.split()[0]
print(first_word)

first_word = company.split()[2]
print(first_word)

# 10. Compruebe si la cadena Codificación para todos contiene una palabra Codificación mediante el método index, find u otros métodos.

company = "Coding For ALL"
print(company.find("Coding"))

print(company.index("Coding"))

# 11. Reemplace la palabra codificación en la cadena 'Coding For All' a Python.

company = "Coding For ALL"

print(company.replace("Coding", "Python"))


"""




.


Reemplace la palabra codificación en la cadena 'Coding For All' a Python.
Cambie Python para todos a Python para todos mediante el método replace u otros métodos.
Divida la cadena 'Coding For All' usando el espacio como separador (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" dividió la cadena en la coma.
¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos?
¿Cuál es el último índice de la cadena Coding For All?
Qué carácter está en el índice 10 en la cadena "Codificación para todos".
Crea un acrónimo o una abreviatura para el nombre 'Python For Everyone'.
Crea un acrónimo o una abreviatura para el nombre 'Coding For All'.
Utilice el índice para determinar la posición de la primera aparición de C en Codificación para todos.
Utilice index para determinar la posición de la primera aparición de F en Coding For All.
Utilice rfind para determinar la posición de la última aparición de l en Codificación para todas las personas.
Use index o find para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No se puede terminar una oración con porque porque porque es una conjunción'
Use rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción'
Corta la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque porque es una conjunción"
Halla la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque porque es una conjunción'
Corta la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque porque es una conjunción"
¿''Coding For All' comienza con una subcadena Coding?
¿'Codificación para todos' termina con una codificación de subcadena?
' Codificación para todos ', elimine los espacios finales izquierdo y derecho en la cadena dada.
¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():
30DaysOfPython
thirty_days_of_python
La siguiente lista contiene los nombres de algunas de las bibliotecas de python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con cadena de espacio.

"""