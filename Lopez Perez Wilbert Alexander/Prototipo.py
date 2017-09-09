# -*- coding:utf-8 -*-
# 14211446 Lopez Wilbert
#Prototype
"""
Ejemplo: Tiene un objeto muy complejo que cuesta demasiado para instanciar (un árbol DOM o un objeto que lee una base de datos). 
 Luego se clona la instancia y solo se cambian los atributos según sea necesario.
"""

from copy import deepcopy

class Prototype:
    def __init__(self):
        self._objs = {}
        
    def registerObject(self, name, obj):
        """
        register an object.
        """
        self._objs[name] = obj
        
    def unregisterObject(self, name):
        """unregister an object"""
        del self._objs[name]
        
    def clone(self, name, **attr):
        """clone a registered object and add/replace attr"""
        obj = deepcopy(self._objs[name])
        obj.__dict__.update(attr)
        return obj

class A:
   pass
a=A()
prototype=Prototype()
prototype.registerObject("a",a)
b=prototype.clone("a",a=1,b=2,c=3)
print a
print b
