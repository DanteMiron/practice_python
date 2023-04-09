# Strings

my_string = "Mi string"
my_other_string = 'Mi string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Dante", "Miron", 27


print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

# División

laguage_slice = language[1:3]
print(laguage_slice)
laguage_slice = language[1:]
print(laguage_slice)
laguage_slice = language[-2]
print(laguage_slice)
laguage_slice = language[0:6:3]
print(laguage_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) # mayuscula primera letra
print(language.upper()) 
print(language.count("t")) 
print(language.isnumeric())
print("123".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))


