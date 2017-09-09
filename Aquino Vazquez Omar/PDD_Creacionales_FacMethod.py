# -*- coding:utf-8 -*-
# 14211402 Aquino Vazquez
#Abstract Factory

import os
from collections import deque

#Limpiar panatlla
os.system('clear')

"""
    Enfoque:
	Un hospital

    Factory Method
    Este patron de diseno es usado para permitir la creacion de una variedad
    objetos complejos desde un objeto fuente.
"""
class Empleado(object):
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.especialidad = None

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_especialidad(self):
        return self.especialidad

    def __str__(self):
        return "Informacion del empleado:\n1.Nombre: {n}\n2.Edad: {e}\n3.Especialidad: {p}".format(n=self.get_nombre(), e=self.get_edad(), p=self.get_especialidad())

class Medico(Empleado):
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        print "Hola soy {n} y yo soy el {p}".format(n=self.nombre, p=self.especialidad)

class Enfermera(Empleado):
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        print "Hola soy {n} y yo soy el {p}".format(n=self.nombre, p=self.especialidad)

class Factoria(object):
    def get_empleado(self, nombre, edad, especialidad):
        if (especialidad is 'medico'):
            return Medico(nombre, edad, especialidad)
        elif (especialidad is 'enfermera'):
            return Enfermera(nombre, edad, especialidad)
        

if __name__=='__main__':
    mi_factoria = Factoria()

empleado1 = mi_factoria.get_empleado('Ernesto Blancarte Huerta', 21, 'medico')
empleado2 = mi_factoria.get_empleado('Tania Gonzalez Arellano', 24, 'enfermera')
print empleado1
print empleado2
