""" TUPLAS """

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (37, 1.64, "Ivan", "Madrid", 37)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

my_tuple.count(37)
print(my_tuple.count(37.5))
print(my_tuple.index("Madrid"))
