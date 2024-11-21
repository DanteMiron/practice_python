#fibonacci

def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a+b
    
    return secuencia

def contar_palabra(nombre_archivo,palabra):
    
    try:
        with open(nombre_archivo, "r") as file:
            contenido = file.read()
            cont = contenido.lower().count(palabra.lower())
            print("La palabra no se encuentra en el texto") if cont==0 else print(cont)
    except FileNotFoundError:
        print("Error el archivo no se encuentra")
    except IOError:
        print("Error: hubo un error al leer el archivo")
    finally: 
        print("Se termino la lectura del archivo")    
        
    pass

def persomas_mas_joven(personas):
    personas.sort(key=lambda x : x ["edad"])
    print(personas[0]["nombre"])
    pass

def cuadrados_pares(lista):
    cuadrado_pares = map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, lista)) 
    return list(cuadrado_pares)

def verify_user(usuarios):
    error_users = [];
    for user in usuarios:
        if len(user["username"]) < 5:
            error_users.append({"username" : user["username"], "error" : "Username tiene menos de 5 letras"})
        if len(user["password"]) < 8:
            error_users.append({"username" : user["username"], "error" : "Password  tiene menos de 8 letras"})
        if "@" not in user["email"] or "." not in user["email"]:
            error_users.append({"username" : user["username"], "error" : "email invalido"})

    return error_users

if __name__ == '__main__':

   usuarios = [
    {"username": "ana", "password": "1234567", "email": "ana@example.com"},
    {"username": "luis123", "password": "password123", "email": "luis@example.com"},
    {"username": "maria", "password": "pass", "email": "mariaexample.com"}
    ]   
   
   error_users = verify_user(usuarios)
   print(list(error_users))

