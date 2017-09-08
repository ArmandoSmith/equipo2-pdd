'''Este patron permite el crear objetos a partir de una fuente en este caso seria una clase Persona, donde hay mas
clases que son heredadas de la clase maestra que es Persona, con esto quiero decir que se puede crear un objeto para dos clases
sin necesidad de que existan mas objetos'''

Clase persona:
class Persona(object):
    """Para nuestro caso, una persona tendra un nombre,
    una edad y un genero, por lo general
    en Java esta clase sería una 'interfaz' """
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.genero = None

    # Algunos getters ...
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_genero(self):
        return self.genero

    def __str__(self):
        return "Informacion de una persona:\n1. Nombre: {n}\n2. Edad: {e}\n3. Genero: {g}".format(
            n=self.get_nombre(), e=self.get_edad(), g=self.get_genero())

Clase Femenino:
from persona import Persona

class Femenino(Persona): 
    """Esta clase hereda de la super clase Persona,
    solo definiremos su constructor"""
    
    def __init__(self, nombre, edad, genero):
        self.nombre  = nombre
        self.edad = edad
        self.genero = genero
        print "Hola Miss "+nombre+" su edad es "+str(edad)
Clase Maculino:
from persona import Persona

class Masculino(Persona): # Heredamos de Persona
    """Esta clase hereda de la super clase Persona,
    solo definiremos su constructor"""

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        print "Hola mister "+nombre+" su edad es "+str(edad)

Clase Factoria:
from femenino import Femenino
from masculino import Masculino

class Factoria(object):
    """Esta clase es nuestra factoria, como ya sabes
    Python define un constructor sin argumentos 
    por default para cada clase, por eso no hace falta 
    escribir uno"""

    def get_persona(self, nombre, genero, edad):
        """Metodo que retorna objetos persona segun el genero"""

        #genero es el parametro usado por la factoria 
        #para elegir el obj a crear
        if (genero is 'F'): 
            return Femenino(nombre, edad, genero)
        elif (genero is 'M'):
            return Masculino(nombre, edad, genero)

Fichero Main
import factoria
if __name__ == '__main__':
    mi_factoria = factoria.Factoria()

    #Factoria, crea a una persona!
    persona = mi_factoria.get_persona('Guido Vann Rosum', 'M', 30)
    #se ha creado una persona masculina
    print persona 
    # print persona.get_nombre()
    # print persona.get_genero()

