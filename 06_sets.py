""" Sets """

my_set = set()
my_other_set = {}

print(type(my_set)) # Imprime: <class 'set'>
print(type(my_other_set)) # Imprime: <class 'dict'>

my_other_set = {"Ivan", "Madrid", 39}
print(type(my_other_set)) # Imprime: <class 'set'>

print(len(my_other_set)) # Imprime: 3

my_other_set.add("Daza")
print(my_other_set) # Imprime: {'Ivan', 'Madrid', 'Daza', 39}

# Un set no es una estructura ordenada.
# Un set no admite repetidos

print("Ivan" in my_other_set) # Imprime: True
print("Gamez" in my_other_set) # Imprime: False

my_other_set.remove("Ivan") # Elimina el elemento con el nombre de "Ivan"
print(my_other_set) # Imprime: {'Daza', 'Madrid', 39}

my_other_set.clear() # Elimina todos los elementos del set
print(my_other_set) # Imprime: set()
print(len(my_other_set)) # Imprime: 0

# del my_other_set
print(my_other_set) # Imprime: NameError: name 'my_other_set' is not defined

my_set = {"Ivan", "Madrid", 39}
my_list = list(my_set)
print(my_list) # Imprime: ['Ivan', 'Madrid', 39]
print(my_list[0]) # Imprime: "Ivan"

# No se debe de realizar este tipo de transformaciones dado que no ofrece un orden especifico en la lista, al momento de acceder a el indice de un elemento, dada la naturaleza noindexada del set, nos arroja diferentes elementos en cada una de las posiciones.

my_other_set = {"HTML", "CSS", "JavaScript", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set) # Imprime: {'JavaScript', 'Madrid', 'Python', 39, 'CSS', 'HTML', 'Ivan'}
my_new_set = my_set.union(my_other_set).union({"C#", "JAVA"})
print(my_new_set) # Imprime: {'Ivan', 'HTML', 'JavaScript', 39, 'Python', 'C#', 'CSS', 'Madrid', 'JAVA'}

print(my_new_set.difference(my_set)) # Imprime: {'Python', 'JAVA', 'C#', 'JavaScript', 'HTML', 'CSS'}
