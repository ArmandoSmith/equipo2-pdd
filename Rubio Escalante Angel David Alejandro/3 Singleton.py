'''
    Singleton
    El patrón singleton es un patrón de creación (Creational Design Pattern) 
    que tiene como objetivo garantizar que una clase sólo tenga una instancia y 
    proporcionar un único punto de acceso a esa instancia. Este patrón suele ser 
    utilizado en temas de logging (entre otros) donde solo se quiere tener una 
    instancia del logger que centralice todo.
'''

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

class Jugador(Singleton):
    nombre = ""

j1 = Jugador()
j2 = Jugador()
j3 = Jugador()
j4 = Jugador()
j5 = Jugador()

j1.nombre = "Victor Mescias Valdez"
print (j1.nombre)
j2.nombre = "Angeles Torres Milan"
print (j2.nombre)
j3.nombre = "Jorge Garcia Tolome"
print (j3.nombre)
j4.nombre = "Miquel Roman Sonre"
print (j4.nombre)
j5.nombre = "Christian Ramsey Galvin"
print (j5.nombre)
