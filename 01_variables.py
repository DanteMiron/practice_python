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