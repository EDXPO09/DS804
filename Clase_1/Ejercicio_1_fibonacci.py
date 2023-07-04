# Definimos la funcion fibonacci_recursivo para obtener el valor perteneciente a la serie
def fibonacci_recursivo(n):
    if n <= 0:
        # F0 = 0
        return 0
    elif n == 1:
        # F1 = 1
        return 1
    else:
        # Fn = Fn-1 + Fn-2
        # Regresar el resultado de (n - 1) + (n - 2)
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Solicitar al usuario el valor de n
n = int(input("Ingrese el valor de n: "))

# Verificar si el valor de n es valido
if n < 0:
    print("El valor de n debe ser un número entero no negativo.")
else:
    # Llamar a la funcion fibonacci_recursivo y mostrar el resultado
    resultado = fibonacci_recursivo(n)
    print("El elemento", n, "de la serie de Fibonacci es:", resultado)
