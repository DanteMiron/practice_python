# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Dante", "Apellido": "Miron", "Edad":27, 1: "Python"}

my_dict = {
    "Nombre": "Dante",
    "Apellido": "Miron",
    "Edad":27,
    "Lenguajes": {"Python","Java", "C#"},
    1: 1.85
}

print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Edad"])

my_dict["Apellido"] = "Sarnago"
print(my_dict["Apellido"])

print(my_dict[1])

my_dict["Calle"] = "Salvat 3153"
print(my_dict)

del my_dict["Nombre"]
print(my_dict)

print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_list = ["River","Plate"]


my_new_dict = dict.fromkeys(("Apellido", "Edad"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Dante", "Miron"))
print(my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
