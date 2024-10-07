# ![Icono](/assets/img/icon_1.png) `Ejercicios Sets` ![Icono](/assets/img/icon_7.png)

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]
```

**1. Encuentre la longitud del set `it_companies`**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len_it_companies = len(it_companies)
print(len_it_companies) # Imprime: 7
```

**2. Añade 'Twitter' a `it_companies`**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add("Twitter")
print(it_companies) # Imprime: {'Amazon', 'Facebook', 'Microsoft', 'Twitter', 'Google', 'Apple', 'IBM', 'Oracle'}
```

**3. Inserte varias empresas de `TI` a la vez en el conjunto `it_companies`**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_others_companies = {"Acer", "Samsung", "LG"}
it_companies.update(it_others_companies)
print(it_companies) # Imprime: {'Amazon', 'Microsoft', 'Oracle', 'Apple', 'IBM', 'LG', 'Facebook', 'Acer', 'Google', 'Samsung'}
```

**4. Eliminar una de las empresas del conjunto `it_companies`**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies)) # imprime: 7
it_companies.pop()
print(len(it_companies)) # Imprime: 6
print(it_companies) # Imprime: {'Google', 'IBM', 'Amazon', 'Oracle', 'Apple', 'Facebook'}
```

**5. ¿Cuál es la diferencia entre el método `remove()` y `discard()`?**

El método `remove()` generará error, si el elemento que se desea eliminar no existe en el set. Mientras que el método `discard()` no genera ningún error si el elemento no está presente.

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies.discard("Git")
print(it_companies) # No genera ningún error

it_companies.remove("Duolingo")
print(it_companies) # Imprime: KeyError: 'Duolingo'
```

**6. Unir A y B**

```py
# Solución 1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A_B = A.union(B)
print(A_B) # Imprime: {19, 20, 22, 24, 25, 26, 27, 28}
# Nota: Se crea un nuevo set con los elementos de ambos sets
```

```py
# Solución 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A.update(B)
print(A) # Imprime: {19, 20, 22, 24, 25, 26, 27, 28}
# Nota: Se actualiza el set original
```

`Resumen:`

- Si necesitas un nuevo conjunto sin alterar los originales, usa `union()`.
- Si prefieres modificar A y no necesitas crear un nuevo conjunto, `usa update()`.

**7. Buscar la intersección A B**

```py
A = {19, 22, 24, 20, 25, 26, 54, 87}
B = {19, 22, 20, 25, 26, 24, 28, 27, 54}

inter_set = A.intersection(B)
print(inter_set) # Imprime: {19, 20, 54, 22, 24, 25, 26}
```

**8. Es A un subconjunto de B**

```py
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.issubset(B)) # Imprime: True
```

**9. Son conjuntos disjuntos A y B**

```py
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.isdisjoint(B)) # Imprime: False
```

**10. Unir A con B y B con A**

```py
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

union_A_B = A.union(B)
print(union_A_B) # Imprime: {19, 20, 22, 24, 25, 26, 27, 28}
union_B_A = B.union(A)
print(union_B_A) # Imprime: {19, 20, 22, 24, 25, 26, 27, 28}
```

**11. ¿Cuál es la diferencia simétrica entre A y B?**

```py
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

diferencia_simetrica = A.symmetric_difference(B)
print(diferencia_simetrica) # Imprime: {27, 28}

diferencia_simetrica_1 = A ^ B
print(diferencia_simetrica_1) # Imprime: {27, 28}
```

**12. Eliminar los conjuntos por completo**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
del it_companies
print(it_companies) # Imprime: NameError: name 'it_companies' is not defined
```

**13. Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?**

```py
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(ages)) # Imprime: 8 elementos
ages_set = set(ages) # convierte la lista a set
print(type(ages_set)) # Imprime: <class 'set'>
print(ages_set) # Imprime: {19, 22, 24, 25, 26}
print(len(ages_set)) # Imprime: 5 elementos

# Nota: La lista posee una mayor longitud o cantidad de elementos que el set, dado de los set no permiten elementos duplicados
```

**14. Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto**

![Imagen Tablas](/assets/img/Imagen%20tabla.png)

**`Diferencias`**

- **`Strings:`** son inmutables y representan secuencias de caracteres.

- **`Lists:`** son mutables, permiten duplicados y son útiles para colecciones ordenadas de datos.

- **`Tuples:`** son inmutables, útiles para datos constantes que no cambian.

- **`Sets:`** son mutables, no mantienen orden y no permiten duplicados.

**15. (I am a teacher and I love to inspire and teach people). ¿Cuántas palabras únicas se han utilizado en la oración?. Utilice los métodos de división (split()) y conjunto (set()) para obtener las palabras únicas.**

```py
# Frase Inicial
frase = "I am a teacher and I love to inspire and teach people"
print("Frase original: ", frase) # Imprime: I am a teacher and I love to inspire and teach people

# División de frase en palabras
frase_dividida = frase.split()
print("Palabras divididas: ", frase_dividida) # Imprime: ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']

# Creación de conjunto de palabras únicas
set_de_frase = set(frase_dividida)
print("Palabras únicas: ", set_de_frase) # Imprime: {'inspire', 'a', 'people', 'teach', 'I', 'to', 'am', 'love', 'teacher', 'and'}

# Conteo de palabras únicas
cantidad_unicas = len(set_de_frase)
print(cantidad_unicas) # Imprime: 10
```

---

[**`Inicio`**](./notas.md)
**-**
[**`Sets`**](./_11_sets.md)
