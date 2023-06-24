def encontrar_anagramas(lista):
    # Crear un diccionario vacio para almacenar los anagramas
    anagramas = {}

    # Recorrer cada cadena en la lista
    for cadena in lista:
        
        # Ordenar los caracteres de la cadena alfabéticamente
        clave = ''.join(sorted(cadena))

        # Si la clave ya existe en el diccionario, agregar la cadena a la lista de anagramas correspondiente
        if clave in anagramas:
            anagramas[clave].append(cadena)
            
        # Si la clave no existe, crear una nueva lista con la cadena como unico elemento
        else:
            anagramas[clave] = [cadena]

    # Crear una lista de tuplas de anagramas a partir del diccionario
    resultado = [tuple(valor) for valor in anagramas.values()]

    return resultado

# Ejemplo 1
lista1 = ["apa", "oso", "paa", "soo"]
resultado1 = encontrar_anagramas(lista1)
print(resultado1)
# Salida: [('apa', 'paa'), ('oso', 'soo')]

# Ejemplo 2
lista2 = ["mama", "mimi", "momo", "maam", "oomm"]
resultado2 = encontrar_anagramas(lista2)
print(resultado2)
# Salida: [('mama', 'maam'), ('mimi',), ('momo', 'oomm')]

# Ejemplo 3 -  Definir los elementos dentro de la cadena
lista3 = [" "]
resultado3 = encontrar_anagramas(lista3)
print(resultado3)
# Salida: [(' ',)]  <- Asi estaran contenidos los elementos de la cadena definida.