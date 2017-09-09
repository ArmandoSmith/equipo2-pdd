"""
    Abstract Factory
    Este patron de diseno se utiliza para proporcionar una interfaz comun
    para crear una serie de objetos (productos) bajo una u otra arquitectura
    o framework.
    Ejemplo:
"""

class Empleado:
    def interactuaCon(self, comida): pass

class Cocinero(Empleado):
    def interactuaCon(self, comida):
        print ("El cocinero a preparado el platillo: ", comida.Accion())

class Cajero(Empleado):
    def interactuaCon(self, comida):
        print ("El cajero a cobrado: ", comida.Accion())

class Repartidor(Empleado):
    def interactuaCon(self, comida):
        print ("El repartidor a entregado:  ", comida.Accion())

class Comida:
    def Accion(self): pass

class BajaRice(Comida):
    def Accion(self):
        print ("Baja Rice")

class Rollo(Comida):
    def Accion(self):
        print ("Rollo")

class Teriyaki(Comida):
    def Accion(self):
        print("Teriyaki")

class Aguachile(Comida):
    def Accion(self):
        print("Aguachile")

#The Abstract Factory:
class fabricaSushi:
    def AccionEmpleado(self): pass
    def accionComida(self): pass

#Concrete factories:
class preparar_BajaRice(fabricaSushi):
    def AccionEmpleado(self): return Cocinero()
    def accionComida(self): return BajaRice()

class preparar_Rollo(fabricaSushi):
    def AccionEmpleado(self): return Cocinero()
    def accionComida(self): return Rollo()

class preparar_Teriyaki(fabricaSushi):
    def AccionEmpleado(self): return Cocinero()
    def accionComida(self): return Teriyaki()

class preparar_Aguachile(fabricaSushi):
    def AccionEmpleado(self): return Cocinero()
    def accionComida(self): return Aguachile()


class vender_BajaRice(fabricaSushi):
    def AccionEmpleado(self): return Cajero()
    def accionComida(self): return BajaRice()

class vender_Rollo(fabricaSushi):
    def AccionEmpleado(self): return Cajero()
    def accionComida(self): return Rollo()

class vender_Teriyaki(fabricaSushi):
    def AccionEmpleado(self): return Cajero()
    def accionComida(self): return Teriyaki()

class vender_Aguachile(fabricaSushi):
    def AccionEmpleado(self): return Cajero()
    def accionComida(self): return Aguachile()


class repartir_BajaRice(fabricaSushi):
    def AccionEmpleado(self): return Repartidor()
    def accionComida(self): return BajaRice()

class repartir_Rollo(fabricaSushi):
    def AccionEmpleado(self): return Repartidor()
    def accionComida(self): return Rollo()


class repartir_Teriyaki(fabricaSushi):
    def AccionEmpleado(self): return Repartidor()
    def accionComida(self): return Teriyaki()

class repartir_Aguachile(fabricaSushi):
    def AccionEmpleado(self): return Repartidor()
    def accionComida(self): return Aguachile()



class desarrollarSushi:
    def __init__(self, fabrica):
        self.factory = fabrica
        self.e = fabrica.AccionEmpleado()
        self.c = fabrica.accionComida()
    def Producto(self):
        self.e.interactuaCon(self.c)

Cocinar1 = desarrollarSushi(preparar_BajaRice())
Cocinar2 = desarrollarSushi(preparar_Rollo())
Cocinar3 = desarrollarSushi(preparar_Teriyaki())
Cocinar4 = desarrollarSushi(preparar_Aguachile())
Vender1 = desarrollarSushi(vender_BajaRice())
Vender2 = desarrollarSushi(vender_Rollo())
Vender3 = desarrollarSushi(vender_Teriyaki())
Vender4 = desarrollarSushi(vender_Aguachile())
Repartir1 = desarrollarSushi(repartir_BajaRice())
Repartir2 = desarrollarSushi(repartir_Rollo())
Repartir3 = desarrollarSushi(repartir_Teriyaki())
Repartir4 = desarrollarSushi(repartir_Aguachile())

Cocinar1.Producto()
Vender1.Producto()
Repartir1.Producto()

Cocinar2.Producto()
Vender2.Producto()
Repartir2.Producto()

Cocinar3.Producto()
Vender3.Producto()
Repartir3.Producto()

Cocinar4.Producto()
Vender4.Producto()
Repartir4.Producto()
