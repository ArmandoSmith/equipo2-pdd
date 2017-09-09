'''
  Factory Method
  Factory Method es un patrón de diseño que define una interfaz para crear un objeto,
  pero deja que sean las subclases quienes decidan qué clase instanciar. 
  Permite que una clase delegue en sus subclases la creación de objetos.
'''

class Empleado(object):
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.puesto = None

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_puesto(self):
        return self.puesto

    def __str__(self):
        return "Informacion de un empleado:\n1.Nombre: {n}\n 2.Apellido {a}\n2.Edad: {e}\n3.Puesto: {p}".format(n=self.get_nombre(), a=self.get_apellido(), e=self.get_edad(), p=self.get_puesto())

class Cocinero(Empleado):
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        print ("{p}: {n} {a}".format(n=self.nombre, p=self.puesto,a=self.apellido))

class Cajero(Empleado):
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        print("{p}: {n} {a}".format(n=self.nombre, p=self.puesto, a=self.apellido))

class Repartidor(Empleado):
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        print("{p}: {n} {a}".format(n=self.nombre, p=self.puesto, a=self.apellido))

class Factoria(object):
    def get_empleado(self, nombre, edad, puesto):
        if (puesto is 'cocinero'):
            return Cocinero(nombre, edad, puesto)
        elif (puesto is 'cajero'):
            return Cajero(nombre, edad, puesto)
        elif (puesto is 'repartidor'):
            return Repartidor(nombre, edad, puesto)

if __name__=='__main__':
    mi_factoria = Factoria()

    empleado1 = mi_factoria.get_empleado('Roberto Estrada Meza', 26, 'Cocinero')
    empleado2 = mi_factoria.get_empleado('Rafael Castillo Perez', 22, 'Cajero')
    empleado3 = mi_factoria.get_empleado('Andres Jaramillo Izquia', 21, 'Repartidor')
    print (empleado1)
    print (empleado2)
    print (empleado3)
