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
"""

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

class Hospital(Singleton):
    nombre = ""

h1 = Hospital()
h2 = Hospital()
h3 = Hospital()

h1.nombre = "Del Prado"
print h1.nombre
h2.nombre = "Angeles"
print h2.nombre
h3.nombre = "San Francisco"
print h3.nombre
