# Tuplas

my_tuple = tuple()
my_other_tuple = (5,6,7)

my_tuple = (35, 1.85, "Dante", "Miron")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Dante"))
print(my_tuple.index("Dante"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# La tupla es inmutable, solamente tienen los metodos index y count. Se pueden sumar

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3]="River Plate"
my_tuple.insert(1,"Salomon Rondon")
my_tuple=tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))