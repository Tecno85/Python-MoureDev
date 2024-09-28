fruits = ("Apple", "Orange", "Pear")
vegetables = ("Potato", "Onion", "Corn")
animals = ("Horse", "Pig", "Duck")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)


food_stuff_tp = fruits + vegetables + animals
food_stuff_lt = list(food_stuff_tp)
print(len(food_stuff_lt))
mid_index = len(food_stuff_lt) // 2
print(mid_index)
mid_element = food_stuff_lt[mid_index]
print(mid_element)
food_stuff_tp = tuple(food_stuff_lt)
print(food_stuff_tp)