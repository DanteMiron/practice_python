# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))
my_other_set = {"Dante", "Miron", 27}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("DanteDev")

print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("DanteDev") # un set no admite repetidos

print(my_other_set)

print("DanteDev" in my_other_set)
print("DanteDe" in my_other_set)
