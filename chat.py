food_stuff_tp = ('Apple', 'Orange', 'Pear', 'Potato', 'Onion', 'Corn', 'Horse', 'Pig', 'Duck')
food_stuff_tp = list(food_stuff_tp)  # Convierte la tupla a lista

# Calcular el índice del medio
mid_index = len(food_stuff_tp) // 2  # Índice del medio
print(mid_index)

# Obtener el elemento del medio
mid_element = food_stuff_tp[mid_index]  # Para número impar de elementos
print(mid_element)

# Para número par de elementos (accede a ambos elementos del medio)
mid_elements = food_stuff_tp[mid_index-1:mid_index+1]  # Obtiene los dos elementos del medio
print(mid_elements)

# Dividir el elemento o elementos del medio
# Para el caso impar
part1 = mid_element[:len(mid_element)//2]
part2 = mid_element[len(mid_element)//2:]
print(f"División del elemento del medio: {part1} y {part2}")

# Para el caso par
part1a = mid_elements[0][:len(mid_elements[0])//2]
part2a = mid_elements[0][len(mid_elements[0])//2:]
part1b = mid_elements[1][:len(mid_elements[1])//2]
part2b = mid_elements[1][len(mid_elements[1])//2:]

print(f"División del primer elemento del medio: {part1a} y {part2a}")
print(f"División del segundo elemento del medio: {part1b} y {part2b}")
