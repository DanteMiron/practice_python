# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 45, 12, 85 , 695 , 45, 5]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'Dante', 'Miron']
print(type(my_other_list))

print(my_other_list[1])
print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count(35))
print(my_list.count(45))
#print(my_other_list[-5])  IndexError
#print(my_other_list[4])   IndexError

age, height, name, surname = my_other_list


print(my_list + my_other_list)

my_other_list.append("aguante river")
print(my_other_list)

my_other_list.insert(1, "sabelo perro")
print(my_other_list)

my_other_list.remove("aguante river")
print(my_other_list)

print(my_other_list.pop())
print(my_other_list)

del my_other_list[0]
print(my_other_list)

my_other_list.insert(1, "blue")
print(my_other_list)

my_other_list[1] = "red"
print(my_other_list)

my_new_list = my_other_list.copy()
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_other_list.clear()
print(my_other_list)


my_list = "Hola Python"
print(my_list)
print(type(my_list))