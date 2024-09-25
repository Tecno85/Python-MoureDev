# # Desempaqueta los tres primeros países y el resto como países escandinavos.

# # Se dio solución utilizando el "Desempaquetado de listas en Python"

countries = ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
countries_str = ' - '.join(countries)

[first, second, third, *paises_escandinavos] = countries

print("Los tres primeros países son: ", first, second, third)
print("Los países escandinavos son: ", paises_escandinavos)
print(countries_str)

