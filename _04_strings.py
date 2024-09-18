"""Strings"""

# Definición de variables

my_string = "Mi string"
my_other_string = 'Mi otro string'

# Longitud de variables (Método "len")

print(len(my_string)) # 9
print(len(my_other_string)) # 14

# Concatenación

print(my_string + " " + my_other_string)
print(my_string, my_other_string)

# Salto de línea

my_new_line_string = "Este es un String con\nsalto de línea"
print(my_new_line_string)

# Tabulación

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# Cómo escapar Strings

my_scape_string = "\\tEste es un String \\nescapado"
print(my_scape_string)

# Cómo formatear los strings | Formateo

name, surname, age = "Ivan", "Madrid", 39

print(f"Mi nombre es {name} {surname} y tengo {age} años") # tipo: cadena formateada (f-string)
print("Mi nombre es " + name + " " + surname + " " + "y tengo " + str(age) + " años.") # tipo: concatenación
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age)) # tipo: método .format()
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age)) # tipo: interpolación usando operador %

"""Cadenas de Python como secuencias de carácteres"""

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # 0
print(f) # n

# Acceso a los carácteres de las cadenas por índice

lenguaje = "Python"
firts_letter = language[0]
print(firts_letter)

last_index = len(language) - 1
last_letter =language[last_index]
print(last_letter)

last_letter_2 = language[-1] # -1, el índice negativo siempre representa el último carácter
print(last_letter_2)

# Segmentación de cadenas de Python

language = "Python"
first_three = language[0:3]
print(first_three) # Pyt

last_three = language[3:6]
print(last_three) # hon

last_three = language[-3:]
print(last_three) # hon

last_three = language[3:]
print(last_three) # hon

# Invertir una cadena

greeting = "Hello World!"
print(greeting[::-1]) # !dlroW olleH

# Saltar carácteres durante la segmentación

language = "python"
salto = language[0:6:2]
print(salto) # Pto

"""Métodos"""

language = "python"
example = " Hello Python "
example_1 = "Hello Python"
variable_2 = "thirty_days_of_python"

print(language.capitalize()) # Primera letra la convierte a mayúscula
print(language.upper()) # Convierte el string a mayúscula
print(language.count("n")) # Cuenta el numero de veces que está presente una letra en una palabra
print(language.isnumeric()) # Nos dice si la variables es un número
print("1".isnumeric()) # Muestra que si
print(language.lower()) # Convierte la variable en minúscula
print(language.upper().isupper()) # True
print(language.lower().isupper()) # False - .isupper confirma si es mayúscula
print(language.startswith("py")) # Comprueba si la cadena comienza un string o letra especificada y devuelve un True or False
print(language.endswith("on")) # Comprueba si la cadena termina un string o letra especificada y devuelve un True or False
print(language.replace("python", "JavaScript")) # Reemplaza la subcadena con una dada
print(example.strip()) # Elimina todos los carácteres dados comenzando desde el principio y el final de la cadena
print(example_1.strip("Python")) # Imprime "Hello" eliminando la primera palabra o string
print(variable_2.isidentifier()) # Comprueba si hay un identificador válido: comprueba si una cadena es un nombre de variable válido. Estos inician con letras minúsculas o guión bajo.


# método join()
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " # ".join(list) # El método join() toma un string como delimitador (en este caso " # ", que incluye un hash y un espacio) y une los elementos de la lista en una única cadena, separándolos con ese delimitador. "Devuelve una cadena concatenada"
print(result)


texto = "Hola, mundo"
posicion = texto.find("mundo")
print(posicion)  # Salida: 6 Aquí, el método find() devuelve 6, que es el índice donde comienza la palabra "mundo".

""""""







