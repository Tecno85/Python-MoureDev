# """Ejercicios Operadores"""


# 1. Declara tu edad como variable entera

my_age = 39

# 2. Declara tu altura como una variable flotante

my_height = 1.64

# 3. Declarar una variable que almacena un número complejo

complex_number = 3 + 5j

# 4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule un área de este triángulo (área = 0.5 x b x h).

      # Enter base: 20
      # Enter height: 10
      # The area of the triangle is 100

triangle_base = float(input("Ingrese la base del triángulo: "))
triangle_height = float(input("Ingrese la altura del triángulo: "))

triangle_are = 0.5 * triangle_base * triangle_height

print("El área del triángulo es: ", triangle_are)

# 5. Escriba un script que solicite al usuario que escriba el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c).

# Solicitar tres lados del triángulo

print("Ingrese los valores de los tres lados del triángulo")
lado_a = float(input("Ingrese lado a: "))
lado_b = float(input("Ingrese lado b: "))
lado_c = float(input("Ingrese lado c: "))

# Cáculo del perimetro del triángulo

perimetro = lado_a + lado_b + lado_c

# Imprimir resultado

print("El perímetro del triángulo es: ", perimetro)

# 6. Obtenga la longitud y el ancho de un rectángulo usando el mensaje. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))

print("Ingrese la longitud y el ancho de un rectángulo")

longitud = float(input("Ingrese la longitud: "))
ancho = float(input("Ingrese el ancho: "))

area = longitud * ancho
perimetro = 2 * (longitud + ancho)

print("El área del rectángulo es:", area, "y el perímetro es:", perimetro)

# 7. Obtenga el radio de un círculo usando el mensaje. Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.

radio = float(input("Ingrese el radio del círculo: "))

area_circulo = 3.14 * radio * radio
circunferencia_circulo = 2 * 3.14 * radio

print(f"El área del circulo es: {area_circulo:.1f}", f"y su circunferencia es: {circunferencia_circulo:.1f}") 
# En esta línea usé le formato de cadena para poder dejar solu un número decimal

# 8. Calcula la pendiente, la intersección con el eje x y la intersección con el eje y de y = 2x -2

x = 0
y = 0
m = 2
b = -2 

y = m * x + b
y = (2 * 0) - 2
y = -2

y = 2 * x -2 
x = 1

pendiente = m
interseccion_eje_y = y
interseccion_eje_x = x

print("El valor de la pendiente es:", pendiente)
print("El valor de la intersección con el eje X es:", interseccion_eje_x)
print("El valor de la intersección con el eje y es:", interseccion_eje_y)

# 9.Encuentra la longitud de 'pitón' y 'dragón' y haz una afirmación de comparación falsa.

palabra_1 = "piton"
palabra_2 = "dragon"

print(len(palabra_1))
print(len(palabra_2))

print(not(len(palabra_2) > len(palabra_1)))

# 10. Use (and) para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'

word_one = "python"
word_two = "dragon"

print("on" in word_one and "on" in word_two)

# 11. Espero que este curso no esté lleno de jerga. Úselo en para verificar si hay jerga en la oración.

frase = "Espero que este curso no esté lleno de jerga"

print("jerga" in frase)

# 12. No hay 'on' tanto en el dragón como en la pitón

animal_one = "dragón"
animal_two = "pitón"

print("on" not in animal_one and "on" not in animal_two)

# 13. Encuentre la longitud del texto python y convierta el valor en float y conviértalo en string

text = "python"

print(len(text))
print(float(len(text)))
print(type(text))

# 14. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no usando python?

# Solución 1:

numero = int(input("Ingrese un número: "))

tipo_numero = numero % 2

print(tipo_numero == 0) # True / False

# Solución 2:

print("Vamos a comprobar si el número que va a ingresar es 'Par' o 'Impar'")

numero = int(input("Ingrese un número: "))

numero_final = "Par" * (numero % 2 == 0) + "Impar" * (numero %2 != 0)

print(f"El número ingresado es {numero} y es un número {numero_final}") 

# En la línea 146, se usó un f-string o Cadena Formateada, esta nos pemite interpolar variables directamente en la cadena. Dentro de las llaves {} podemos colocar variables o expresiones, y Python las sustituye por su valor cuando imprimas la cadena. 

# 15. Compruebe si la división del suelo de 7 por 3 es igual al valor int convertido de 2,7.

division_suelo = 7 // 3
int_convertido = int(2.7)

mensaje = "La division es igual" * (division_suelo == int_convertido) + "La división no es igual" * (division_suelo != int_convertido)

print(mensaje)

# 16. Compruebe si el tipo de '10' es igual al tipo de 10

tipo_1 = "10"
tipo_2 = 10

comparacion = "Los tipos no son iguales" * (tipo_1 != tipo_2) + "Los tipos son iguales" * (tipo_1 == tipo_2)

print(comparacion)

# 16. Comprueba si int('9.8') es igual a 10

numero_entero = int(9.8)

mensaje = "int('9.8') es igua a 10" * (numero_entero == 10) + "int('9.8') no es igual a 10" * (numero_entero != 10)

print(mensaje)

# 17. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora de trabajp. ¿Calcular el pago de la persona?

horas_trabajo = float(input("Ingrese las horas a trabajar: "))
tarifa_hora = float(input("Ingrese el valor de la hora: "))

valor_total = horas_trabajo * tarifa_hora

print("El valor total a pagar es: ", valor_total)

# 18. Escriba un script que solicite al usuario que introduzca el número de años. Calcula el número de segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años

numero_años = min(int(input("Ingrese su edad: ")))

segundos = (((numero_años * 365) * 24) * 60) * 60  

print("Tu edad en segundos es: ", segundos)

# 19. Escriba un script de Python que muestre la siguiente tabla

    # 1 1 1 1 1
    # 2 1 2 4 8
    # 3 1 3 9 27
    # 4 1 4 16 64
    # 5 1 5 25 125

print("A continuación se mostrará la siguiente tabla")

print(1, (1 // 1), 1 ** 1, 1 ** 2, 1 ** 3)
print(2, (2 // 2), 2 ** 1, 2 ** 2, 2 ** 3)
print(3, (3 // 3), 3 ** 1, 3 ** 2, 3 ** 3)
print(4, (4 // 4), 4 ** 1, 4 ** 2, 4 ** 3)
print(5, (5 // 5), 5 ** 1, 5 ** 2, 5 ** 3)

