def cuadrado_entero(valor):
    # Calcula el cuadrado del valor flotante
    cuadrado = valor ** 2
    
    # Convierte el cuadrado a entero utilizando la técnica de decomposicion
    entero = int(cuadrado)
    
    # Devuelve el valor entero
    return entero

# Ejemplo de uso
valor_flotante = 3.14
resultado = cuadrado_entero(valor_flotante)
print("El cuadrado entero de", valor_flotante, "es:", resultado)
