import sys
sys.path.append('..')
sys.setrecursionlimit(200000000)

from structures.chronometer import Chronometer

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    if n < 0:
        raise ValueError("n no puede ser negativo")
    
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_recursivo(n):
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    if n < 0:
        raise ValueError("n no puede ser negativo")
    
    def recursivo(m):
        if m == 1:
            return 1

        return m * recursivo(m - 1)
    
    return n * recursivo(n-1)

if __name__ == '__main__':
    cro = Chronometer()
    n = 1000

    cro.start()
    v1 = factorial(n)
    step_time_1 = cro.stop()
    print(step_time_1)

    cro.start()
    v2 = factorial_recursivo(n)
    step_time_2 = cro.stop()
    print(step_time_2)

    print((100 / step_time_1) * step_time_2)