'''
    Object Pool
    Object pool es un patrón de diseño de software que usa un conjunto de objetos inicializados preparados para su uso.
    Esto es más efectivo que estar creando y destruyendo los objetos según se ocupe. Un cliente del pool le pedirá un 
    objeto para realizar las operaciones con el objeto. Cuando el cliente termina retorna el objeto al pool para que 
    lo retenga hasta que vuelva a necesitar usarse. Es decir, los objetos no se crean (salvo la primera vez) ni se destruyen, 
    simplemente se van reciclando.
'''

class piscinaObjetos:
    """
    Manage Reusable objects for use by Client objects.
    """

    def __init__(self, size):
        self._reusables = [Reusable() for _ in range(size)]

    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


class Reusable:
balavx += 10
balavy +=0.5
gravedad += 2
    pass

def main():
    reusable_pool = ReusablePool(50)
    reusable = reusable_pool.acquire()
    reusable_pool.release(reusable)


if __name__ == "__main__":
    main()
