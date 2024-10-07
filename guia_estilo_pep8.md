# `Guía de estilo PEP8`

```python
# Ejemplo de una clase y funciones en Python que sigue la guía PEP8

class Persona:
    """Clase para representar a una persona."""

    def __init__(self, nombre, edad):
        """Inicializa una nueva instancia de Persona."""
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """Muestra un saludo."""
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."


def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


def main():
    """Función principal."""
    persona = Persona("Ana", 30)
    print(persona.saludar())
    resultado = sumar(5, 7)
    print(f"El resultado de la suma es: {resultado}")


if __name__ == "__main__":
    main()
```

### Puntos clave de PEP8 en el ejemplo:
1. **Nombres de clases**: Deben estar en formato **CamelCase** (`Persona`).
2. **Nombres de funciones y variables**: Deben estar en **snake_case** (`saludar`, `sumar`, `persona`).
3. **Espacios alrededor de operadores**: Se deben agregar espacios alrededor de operadores como `=` y `+` (`resultado = sumar(5, 7)`).
4. **Longitud de línea**: No debe exceder de **79 caracteres** (en este caso, ninguna línea lo supera).
5. **Docstrings**: Se usan para documentar clases, métodos y funciones (utilizando `"""`).
6. **Uso de espacios**: No se usa más de un espacio entre palabras clave y paréntesis en las funciones.


## Ejemplo que incluye:

- Variables
- Funciones
- Clases y objetos
- Bucles (`for` y `while`)
- Condicionales (`if`, `elif`, `else`)
- Manejo de excepciones
- Listas, tuplas, diccionarios y sets
- Comprensiones de listas
- Uso de módulos

```python
import math


# Definición de una clase para representar a una persona
class Persona:
    """Clase que representa a una persona."""
    
    def __init__(self, nombre, edad, ciudad):
        """Inicializa una instancia de Persona."""
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __str__(self):
        """Devuelve una representación en cadena de la persona."""
        return f"{self.nombre}, {self.edad} años, de {self.ciudad}"

    def es_mayor_de_edad(self):
        """Comprueba si la persona es mayor de edad."""
        return self.edad >= 18


# Definición de una función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    if radio <= 0:
        raise ValueError("El radio debe ser mayor que 0")
    return math.pi * radio ** 2


# Definición de una función para imprimir los elementos de una lista
def imprimir_lista(lista):
    """Imprime cada elemento de una lista."""
    for elemento in lista:
        print(elemento)


def main():
    """Función principal."""
    
    # Variables
    nombre = "Carlos"
    edad = 25
    ciudad = "Bogotá"
    
    # Crear una instancia de Persona
    persona = Persona(nombre, edad, ciudad)
    
    # Imprimir la información de la persona
    print(persona)
    
    # Comprobar si es mayor de edad
    if persona.es_mayor_de_edad():
        print(f"{persona.nombre} es mayor de edad.")
    else:
        print(f"{persona.nombre} no es mayor de edad.")
    
    # Manejo de excepciones
    try:
        radio = 5
        area = calcular_area_circulo(radio)
        print(f"El área de un círculo con radio {radio} es {area:.2f}")
    except ValueError as error:
        print(f"Error: {error}")
    
    # Ejemplo de lista, tupla, diccionario y set
    lista_frutas = ["manzana", "banana", "cereza"]
    tupla_colores = ("rojo", "verde", "azul")
    diccionario_paises = {"Colombia": "Bogotá", "España": "Madrid", "Francia": "París"}
    conjunto_numeros = {1, 2, 3, 4, 5}
    
    # Imprimir lista con una función
    imprimir_lista(lista_frutas)
    
    # Bucle while
    contador = 0
    while contador < 3:
        print(f"Contador: {contador}")
        contador += 1
    
    # Comprensión de listas
    cuadrados = [x ** 2 for x in range(10)]
    print(f"Cuadrados del 0 al 9: {cuadrados}")
    
    # Recorrer diccionario
    for pais, capital in diccionario_paises.items():
        print(f"La capital de {pais} es {capital}")
    
    # Operaciones con sets
    conjunto_numeros.add(6)
    conjunto_numeros.discard(3)
    print(f"Conjunto modificado: {conjunto_numeros}")


# Ejecutar el programa
if __name__ == "__main__":
    main()
```

### Explicación del código:
1. **Variables y Clases**: Se define la clase `Persona` con atributos (`nombre`, `edad`, `ciudad`) y métodos como `es_mayor_de_edad()`.
2. **Funciones**: Se utiliza la función `calcular_area_circulo()` para realizar cálculos y la función `imprimir_lista()` para recorrer listas.
3. **Bucles**: Se incluye un bucle `for` para recorrer una lista y un bucle `while` para controlar la ejecución de un contador.
4. **Condicionales**: Se usa una estructura `if`, `elif`, `else` para verificar si una persona es mayor de edad.
5. **Manejo de Excepciones**: Se maneja un error si el radio del círculo es menor o igual a cero.
6. **Estructuras de Datos**: Se usan listas, tuplas, diccionarios y conjuntos, mostrando cómo trabajar con cada uno.
7. **Comprensiones de Listas**: Se utiliza una comprensión de listas para calcular los cuadrados de los números del 0 al 9.
8. **Módulos**: Se importa el módulo `math` para usar `pi` y realizar cálculos matemáticos.

Este código te da un buen repaso de los elementos clave del lenguaje Python. ¡Espero que te sea útil!