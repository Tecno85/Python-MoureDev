set_1 = {"item1", "item2", "item3", "item4"}
set_2 = {"item1", "item4"}
set_difference = set_1.difference(set_2)
print(set_difference) # Imprime: {'item2', 'item3'}

numbers_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers_2 = {2, 4, 6, 8, 10}
numbers_difference = numbers_1.difference(numbers_2)
print(numbers_difference) # Imprime: {0, 1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python_difference = python.difference(dragon)
dragon_difference = dragon.difference(python)  
print(python_difference) # Imprime: {'t', 'p', 'y'}
print(dragon_difference) # Imprime: {'r', 'a', 'g', 'd'}