#1. Filtrar números primos en una lista
#Escribe una función que reciba una lista de números enteros y devuelva una lista con los números primos. Un número es primo si solo es divisible por 1 y por sí mismo.
def primo(num):
    cont = 0
    for i in range(2,num):
        if num % i == 0:
            cont += 1  
    return True if cont == 0 else False


def primos(lista):
    primos = filter(primo , lista)
    return primos

#. Contar las palabras en una cadena
#Escribe una función que reciba una cadena de texto y cuente el número de veces que aparece cada palabra en la cadena. Devuelve un diccionario donde las claves son las palabras y los valores son el número de veces que aparece cada una.

def contar_palabras(string):
    palabras = string.strip().split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

#3. Inversión de una cadena
#Escribe una función que reciba una cadena de texto y devuelva la misma cadena invertida, sin utilizar el operador de inversión [::-1].

def cadena_invertida(string):
    cadena_invertida = "".join(reversed(string))
    return cadena_invertida

def es_palindromo(string):
    cadena = cadena_invertida(string)
    if string == cadena:
        return True
    else:
        return False

def eliminar_repetidos(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva

def qsort(lista):
    if len(lista)<= 1:
        return lista
    pivot = lista[len(lista)//2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]

    return qsort(left) + middle + qsort(right)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)




if __name__ == "__main__":

    lista = [5,4,3,7,8,96,5,6,7,4,1,3,5,6,1]
    lista_ordenada = qsort(lista)

    print(lista_ordenada)
    print(fibonacci(6))
    