from copy import deepcopy
class Prototype:
    def __init__(self):
        self._objs = {}

    def registerObject(self, id, correo):
        
        self._objs[id] = correo

    def unregisterObject(self, id):
        """unregister an object"""
        del self._objs[id]

    def clone(self, id, **attr):
        """clone a registered object and add/replace attr"""
        obj = deepcopy(self._objs[id])
        obj.__dict__.update(attr)
        return id


class A:
    pass

a = A()
prototype = Prototype()
prototype.registerObject("a", a)
b = prototype.clone("a", a=1, b=2, c=3)
print (a)
print (c)
print(b.a, b.b, b.c)
