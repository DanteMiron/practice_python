# Ejercicio 2
# Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un método “cumpleaños”, que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”.
# Tendríamos que lograr ejecutar el siguiente código con la clase creada:


# class Persona():
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def cumpleaños(self):
#         self.edad +=1

# Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”. Por tanto:
# En la clase “Persona” su método __init__() debe de estar preparado para recibir nombre y apellido.
# Además, esta clase , debe tener un método para mostrar nombre_completo() el cual debe mostrar el nombre acompañado del apellido.
# La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además recibir los argumentos nombre y edad. También la clase “Estudiante”, 
# recibe el valor “carrera”, y además contar con un método mostrar_carrera(). Las dos clases son obligatorias.

class Persona():
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def nombre_completo(self):
        print(f"{self._nombre} {self._apellido}")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self._carrera = carrera

    def mostrar_carrera(self):
        print(f"{self._nombre} esta cursando al carrera {self._carrera}")
        
class Fabrica():
  def __init__(self, llantas, color, precio):
    self.llantas=llantas
    self.color=color
    self.precio=precio

class Moto(Fabrica):
  def cantidad(self):
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self.llantas,self.color,self.precio))

class Carro(Fabrica):
  def cantidad(self):
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self.llantas,self.color,self.precio))

print("OBJETO=moto")

moto=Moto(2, "Gris", "$200")
moto.cantidad()

print("OBJETO=carro")

carro=Carro(4 ,"Negro", "$600")
carro.cantidad()






  