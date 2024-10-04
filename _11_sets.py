ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(ages)) # Imprime: 8
ages_set = set(ages) # convierte la lista a set
print(type(ages_set)) # Imprime: <class 'set'>
print(ages_set) # Imprime: {19, 22, 24, 25, 26}
print(len(ages_set)) # Imprime: 5

# Nota: La lista posee una mayor longitud o cantidad de elementos que el set, dado de los set no permiten elementos duplicados
