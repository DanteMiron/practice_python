# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 25
print(my_int_variable)

my_int_to_str_variable= str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_bool_variable, str(my_int_variable), my_string_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len(my_int_to_str_variable))

# Variables en una sola línea
name, surname, alias, age = "Dante", "Miron", "Kabe", 27
print("Me llamo:",name,surname,". Mi edad es:",age,alias)

# Inputs
first_name = input ('What is your name : ')
age = input ('How old are you ? ')

print(first_name)
print(age)

# Cambiamos su tipo 
name = 35
age = "Dante"
print(name)
print(age)

# ¿Forzamos el tipo?

address: str = "Mi dirección"
address = True
address = 5
address = 1.2 
print(type(address))


 