import time
from functools import cache


def fibonacci_sin_cache(numero):
    """
    Calcula el enésimo valor de la serie de Fibonacci sin utilizar cache.
    """
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci_sin_cache(numero - 1) + fibonacci_sin_cache(numero - 2)


@cache
def fibonacci_con_cache(numero):
    """
    Calcula el enésimo valor de la serie de Fibonacci utilizando cache.
    """
    if numero <= 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci_con_cache(numero - 1) + fibonacci_con_cache(numero - 2)


numero = 45
veces_calculo = 5

print(f"Número entero para calcular el enésimo valor de la serie de Fibonacci: {numero}")
print(f"Número de veces que desea hacer el cálculo: {veces_calculo}\n")

# Cálculo de Fibonacci sin cache
print("Cálculo de fibonacci({}) sin cache".format(numero))
tiempo_inicio = time.time()

resultado_sin_cache = fibonacci_sin_cache(numero)

tiempo_final = time.time()
tiempo_ejecucion_sin_cache = tiempo_final - tiempo_inicio
print("Tiempo de ejecución sin cache: {} segundos\n".format(tiempo_ejecucion_sin_cache))

# Cálculos de Fibonacci con cache
for i in range(veces_calculo):
    print("Cálculo {} de fibonacci({})".format(i + 1, numero))
    tiempo_inicio = time.time()

    resultado_con_cache = fibonacci_con_cache(numero)

    tiempo_final = time.time()
    tiempo_ejecucion_con_cache = tiempo_final - tiempo_inicio
    print("Tiempo de ejecución con cache: {} segundos\n".format(tiempo_ejecucion_con_cache))
