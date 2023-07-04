def buscar_valor(lista_ordenada, valor):
    return busqueda_binaria_recursiva(lista_ordenada, valor, 0, len(lista_ordenada) - 1)

"""" 
Esta función toma la lista ordenada, el valor a buscar 
y los límites izquierda y derecha de la sublista actual.
"""
def busqueda_binaria_recursiva(lista_ordenada, valor, izquierda, derecha):
    if izquierda > derecha:
        return None

    medio = (izquierda + derecha) // 2

    if lista_ordenada[medio] == valor:
        return medio
    elif lista_ordenada[medio] < valor:
        return busqueda_binaria_recursiva(lista_ordenada, valor, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista_ordenada, valor, izquierda, medio - 1)
"""
La funcion anterior comprueba si izquierda es mayor que derecha,
lo cual indica que el valor no está presente en la lista, y devuelve None en ese caso.
"""


lista = [1, 3, 5, 7, 9, 11, 13, 15, 17]
valor_buscado = 9

indice = buscar_valor(lista, valor_buscado)

if indice is not None:
    print(f"El valor {valor_buscado} se encuentra en el índice {indice} de la lista.")
else:
    print(f"El valor {valor_buscado} no está en la lista.")

""""
El valor 9 se encuentra en el índice 4 de la lista.
"""