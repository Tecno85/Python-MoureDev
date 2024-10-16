# `Ejercicios String` ![Icon String](/assets/img/icon_13.png)

**1. Concatene la cadena `'Thirty'`, `'Days'`, `'Of'`, `'Python'` en una sola cadena, `'Thirty Days Of Python'`**.

```py
thirty = "Thirty"
days = "Days"
of = "of"
python = "Python"

print(thirty + " " + days + " " + of + " " + python)  # concatenación
print("%s %s %s %s" %(thirty, days, of, python))  # interpolación con módulo (%)
print("{} {} {} {}".format(thirty, days, of, python))  # método .format
print(f"{thirty} {days} {of} {python}")  # f-string
```

**2. Concatene la cadena `'Coding'`, `'For'`, `'All'` en una sola cadena, `'Coding For All'`**.

```py
palabra_1 = "Coding"
palabra_2 = "For"
palabra_3 = "All"

print(f"{palabra_1} {palabra_2} {palabra_3}")
```

**3. Declare una variable denominada company y asígnela a un valor inicial `"Coding For All"`**.

```py
company = "Coding For ALL"
```

**4. Imprime la variable company usando `print()`**.

```py
print(company)
```

**5. Imprima la longitud de la cadena de la empresa utilizando el método `len()` y `print()`**.

```py
print(len(company))
```

**6. Cambie todos los caracteres a letras mayúsculas usando el método `upper()`**.

```py
print(company.upper())
```

**7. Cambie todos los caracteres a letras minúsculas usando el método `lower()`**.

```py
print(company.lower())
```

**8. Utilice los métodos `capitalize()`, `title()`, `swapcase()` para formatear el valor de la cadena `Coding For All`**.

```py
print(company.capitalize())
print(company.title())
print(company.swapcase())
```

**9. Corta la primera palabra de la cadena Coding For All**.

```py
company = "Coding For ALL"

first_word = company.split()[0]
print(first_word)

first_word = company.split()[2]
print(first_word)
```

**10. Compruebe si la cadena Codificación para todos contiene una palabra Codificación mediante el método `index()`, `find()` u otros métodos**.

```py
company = "Coding For ALL"
print(company.find("Coding"))

print(company.index("Coding"))
```

**11. Reemplace la palabra codificación en la cadena `'Coding For All'` a Python**.

```py
company = "Coding For ALL"

print(company.replace("Coding", "Python"))
```

**12. Cambie Python para todos a Python para todos mediante el método replace u otros métodos**.

```py
message = "Python For Everyone"
print(message.replace("Everyone", "All"))
```

**13. Divida la cadena 'Coding For All' usando el espacio como separador `(split())`**.

```py
company = "Coding For All"
print(company.split())
```

**14. `"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"` dividió la cadena en la coma**.

```py
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies)
print(companies.split(", "))
```

**16. ¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos?**.

```py
company = "Coding For All"
print(company[0])
```

**17. ¿Cuál es el último índice de la cadena Coding For All?**.

```py
company = "Coding For All"
print(len(company))

ultimo_indice = len(company) - 1
print(ultimo_indice)
```

**18.  Qué carácter está en el índice 10 en la cadena "Codificación para todos"**.

```py
company = "Coding For All"

print(company[10]) # Imprime: 

# El caracter que se encuentra en el indice 10 es un espacio en blanco.
```

**19. Crea un acrónimo o una abreviatura para el nombre `'Python For Everyone'`**.

```py
nombre = "Python For Everyone"

print(nombre.replace("Python For Everyone", "EveryForPy"))
# Imprime: EveryForPy
```

**20. Utilice el índice para determinar la posición de la primera aparición de `C` en `Coding For All`.**

```py
company = "Coding For All"
index_of_C = company.find("C")
print(index_of_C)
# Imprime: 0, la "C" está en el primer índice.
```

**21. Utilice index para determinar la posición de la primera aparición de `F` en `Coding For All`**.

```py
company = "Coding For All"
index_of_F = company.find("F")
print(index_of_F)
# Imprime: 7
```

**22. Utilice `rfind` para determinar la posición de la última aparición de `l` en `Coding For All`**.

```py
company = "Coding For All"
last_l_index = company.rfind("l")
print(last_l_index)
# Imprime: 13
```

**23. Use `index `o `find` para encontrar la posición de la primera aparición de la palabra `'porque'` en la siguiente oración**:

```py
# Solución 1:
sentence = "No se puede terminar una oración con porque porque porque es una conjunción"
first_word = sentence.index("porque")
print(first_word)
# Imprime: 37

# Solución 2:
first_word_ = sentence.find("porque")
print(first_word_)
# Imprime: 37
```

**24. Use `rindex` para encontrar la posición de la última aparición de la palabra `'porque'` en la siguiente oración: `'No puedes terminar una oración con porque porque porque porque es una conjunción'`**.

```py
sentence = "No se puede terminar una oración con porque porque porque es una conjunción"
# Solución 1:
last_word = sentence.rfind("porque")
print(last_word)
# Imprime: 51

# Solución 2:
last_word_ = sentence.rindex("porque")
print(last_word_)
# Imprime: 51
```

**25. Corta la frase `"porque porque porque"` en la siguiente oración: `"No puedes terminar una oración con porque porque porque porque es una conjunción"`**.

```py
# Solución 1:
sentence = ("No puedes terminar una oración con porque porque porque porque es una conjunción")
antes, separador, despues = sentence.partition("porque porque porque porque")
print(antes.strip() + " " + despues.strip())
# imprime: No puedes terminar una oración con es una conjunción

# Solución 2:
sentence = ("No puedes terminar una oración con porque porque porque porque es una conjunción")
new_sentence = sentence.replace("porque porque porque porque","").replace("  ", " ")
print(new_sentence.strip())
# imprime: No puedes terminar una oración con es una conjunción
```

**26. Halla la posición de la primera aparición de la palabra `'porque'` en la siguiente oración: `'No puedes terminar una oración con porque porque porque porque es una conjunción'`**.

```py
# Solución 1:
sentence = (
    "No puedes terminar una oración con porque porque porque porque es una conjunción"
)
new_posicion = sentence.index("porque")
print(new_posicion)

# Solución 2:
new_posicion = sentence.find("porque")
print(new_posicion)
```

# 27. Corta la frase "porque porque porque" en la siguiente oración: "No puedes terminar una oración con porque porque porque porque es una conjunción"

sentence = (
    "No puedes terminar una oración con porque porque porque porque es una conjunción"
)
antes, separador, despues = sentence.partition("porque porque porque porque")
print(antes.strip() + " " + despues.strip())

new_partition = sentence.replace("porque porque porque porque",
                                 "").replace("  ", " ")
print(new_partition.strip())

# 28. ¿'Coding For All' comienza con una subcadena Coding?

sentence = "Coding For All"
new_sentence = sentence.startswith("Coding")
print(new_sentence)  # True

# 29. ¿'Codificación para todos' termina con una codificación de subcadena?

sentence = "Coding For All"
new_sentence = sentence.endswith("Coding")
print(new_sentence)

# 30. ' Coding For All ', elimine los espacios finales izquierdo y derecho en la cadena dada.

sentence = " Coding For All "
new_sentence = (
    sentence.strip()
)  # No es necesario colocar las comillas y el espacio (" "), para que el método los elimine
print(new_sentence)  # Imprime Coding For All, sin espacios inciales y finales

# 31. ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier():

variable_1 = "30DaysOfPython"
variable_2 = "thirty_days_of_python"

print(variable_1.isidentifier())
print(variable_2.isidentifier())

# 32. La siguiente lista contiene los nombres de algunas de las bibliotecas de python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con cadena de espacio.

libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
result_libraries = " # ".join(libraries)
print(result_libraries)

# 33. Utilice la nueva secuencia de escape de línea para separar las siguientes oraciones.

# \n = es la secuencia de escape de líne nueva

sentence_1 = "I am enjoying this challenge"
sentence_2 = "I just wonder what is next"

new_sentence_1 = "I am\nenjoying this cahllange"  # No son necesarios los espacios antes y despues de \n
new_sentence_2 = "I just\nwonder what\nis next "

print(new_sentence_1)
print(new_sentence_2)

# 34. Utilice una secuencia de escape de tabulación para escribir las siguientes líneas.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")

# 35. Utilice el método de formato de cadena para mostrar lo siguiente:

radius = 10
area = 3.14 * radius**2  # Número permanece como flotante

# The area of a circle with radius 10 is 314 meters square.

new_string = f"The area of a circle with radius {radius} is {area:.0f} meters square"
# Nota: {area:.0f} = Esto es muy útil cuando deseas mantener el valor como un número flotante internamente, pero mostrarlo sin decimales.
print(new_string)

# 36. Realice lo siguiente utilizando métodos de formato de cadena:

# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

x = 8
y = 6

print(f"{x} + {y} = {x + y}")  # Método f-string
print("{} - {} = {}".format(x, y, x - y))  # Método str.format
print("%d * %d = %d" % (x, y, x * y))  # Método interpolación usando operador %
print(
    str(x) + " " + "/" + " " + str(y) + " " + "=" + " " +
    str(round(x / y, 2)))  # Método concatenación
print(f"{x} % {y} = {x % y}")  # Método f-string
print("{} // {} = {}".format(x, y, x // y))  # Método str.format
print("%d ** %d = %d" % (x, y, x**y))  # Método interpolacion usando operador %




[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

> [!IMPORTANT]
>

> [!WARNING]
> Este es un ejemplo

> Note: `--Ivan` es un desarrollador excelente.