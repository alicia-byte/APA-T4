

 
"""
Generación de números aleatorios
Alicia Varón López
"""


class Aleat:
    """
    Clase iterable que genera números aleatorios usando el algoritmo LGC.

    Atributos:
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        x (int): Semilla actual.

    Métodos:
        __next__(): Devuelve el siguiente número aleatorio.
        __call__(semilla): Reinicia la secuencia con una nueva semilla.

    Pruebas unitarias:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """

    def __init__(self, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Inicializa el generador con los parámetros dados.
        Todos los argumentos deben ser pasados por clave.
        """
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
        self.x = x0

    def __next__(self):
        """
        Calcula y devuelve el siguiente número de la secuencia.
        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, semilla):
        """
        Reinicia la secuencia con la semilla indicada.
        """
        self.x0 = semilla
        self.x = semilla




"""
Implementación de la funcion que genera aleat()
"""


def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora que produce números aleatorios usando LGC.
    
    Argumentos:
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        x0 (int): Semilla inicial.

    Salida:
        Generator que produce números pseudoaleatorios.
        El método send() permite reiniciar la secuencia con una nueva semilla.

    Pruebas unitarias:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        # El yield recibe el valor enviado por send()
        semilla = yield x
        if semilla is not None:
            x = semilla

""" Ejecución de los test """
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)