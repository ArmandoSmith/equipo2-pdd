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

    Abstract Factory
    Este patron de diseno se utiliza para proporcionar una interfaz comun
    para crear una serie de objetos (productos) bajo una u otra arquitectura
    o framework.
"""

class Empleado:
    def InteractuaCon(self, Trabajo): pass

class Medico(Empleado):
    def InteractuaCon(self, Trabajo):
        print ("El medico realizo: ", Trabajo.Accion())

class Enfermera(Empleado):
    def InteractuaCon(self, Trabajo):
        print ("La enferemera realizo: ", Trabajo.Accion())

class Trabajo:
    def Accion(self): pass

class Cirugia(Trabajo):
    def Accion(self):
        print ("Cirugia")

class Consulta(Trabajo):
    def Accion(self):
        print ("Consulta")

class Curacion(Trabajo):
    def Accion(self):
        print ("Curacion")

#The Abstract Factory:
class FabHospital:
    def AccionEmpleado(self): pass
    def AccionTrabajo(self): pass

#Concrete factories:
class Atender_Paciente(FabHospital):
    def AccionEmpleado(self): return Medico()
    def AccionTrabajo(self): return Consulta()

class Realizar_Cirugia(FabHospital):
    def AccionEmpleado(self): return Medico()
    def AccionTrabajo(self): return Cirugia()

class Realizar_Curacion(FabHospital):
    def AccionEmpleado(self): return Enfermera()
    def AccionTrabajo(self): return Curacion()


class DesarrolloHospital:
    def __init__(self, fabrica):
        self.factory = fabrica
        self.e = fabrica.AccionEmpleado()
        self.t = fabrica.AccionTrabajo()
    def Paracetamol(self):
        self.e.InteractuaCon(self.t)

Med1 = DesarrolloHospital(Atender_Paciente())
Med2 = DesarrolloHospital(Realizar_Cirugia())
Enf1 = DesarrolloHospital(Realizar_Curacion())


Med1.Paracetamol()
Med2.Paracetamol()
Enf1.Paracetamol()
