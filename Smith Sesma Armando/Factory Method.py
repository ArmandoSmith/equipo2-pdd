"""
    El enfoque que se le dara a todos los patrones de diseno sera el de
    un restaurante de pizzas
"""
"""
    Abstract Factory
    Este patron de diseno es usado para permitir la creacion de una variedad
    objetos complejos desde un objeto fuente.
    Ejemplo:
"""

class Empleado(object):
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.puesto = None

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_puesto(self):
        return self.puesto

    def __str__(self):
        return "Informacion de un empleado:\n1.Nombre: {n}\n2.Edad: {e}\n3.Puesto: {p}".format(n=self.get_nombre(), e=self.get_edad(), p=self.get_puesto())

class Cocinero(Empleado):
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        print "Hola soy {n} y yo soy el {p}".format(n=self.nombre, p=self.puesto)

class Cajero(Empleado):
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        print "Hola soy {n} y yo soy el {p}".format(n=self.nombre, p=self.puesto)

class Repartidor(Empleado):
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        print "Hola soy {n} y yo soy el {p}".format(n=self.nombre, p=self.puesto)

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

    empleado1 = mi_factoria.get_empleado('Alfredo Robles Mendez', 21, 'cocinero')
    empleado2 = mi_factoria.get_empleado('Juan Rodolfo Ramirez Fernandez', 24, 'cajero')
    empleado3 = mi_factoria.get_empleado('Armando Smith Sesma', 21, 'repartidor')
    print empleado1
    print empleado2
    print empleado3
