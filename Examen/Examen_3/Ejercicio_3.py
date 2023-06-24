def encontrar_suma(lista, X):
    # Diccionario para almacenar los índices de los elementos
    indice_map = {}  
    
    for i, num in enumerate(lista):
        
        # Calcula el complemento necesario para que la suma sea X
        complemento = X - num  
        
        if complemento in indice_map:
            
             # Retorna los índices si se encuentra una coincidencia
            return (indice_map[complemento], i) 
        
        # Guarda el índice del elemento actual en el diccionario
        indice_map[num] = i  
        
    # Retorna una tupla vacía si no se encuentra ninguna coincidencia
    return ()  

# Ejemplo 1 
# Entrada: [1, 2, 3, 4], 5
lista1 = [1, 2, 3, 4]
# 5 Es el numero que se desea obtener con la suma de dos elementos dentro de la funcion
X1 = 5
resultado1 = encontrar_suma(lista1, X1)
print(resultado1)  
# Salida: (1, 2)

# Ejemplo 2
# Entrada: [8, 1, 7], 9
lista2 = [8, 1, 7]
# 9 Es el numero que se desea obtener con la suma de dos elementos dentro de la funcion
X2 = 9
resultado2 = encontrar_suma(lista2, X2)
print(resultado2)  
# Salida: (0, 1)

# Ejemplo 3
# Entrada: [1, 3, 1], 5
lista3 = [1, 3, 1]
# 5 Es el numero que se desea obtener con la suma de dos elementos dentro de la funcion
X3 = 5
resultado3 = encontrar_suma(lista3, X3)
print(resultado3)  
# Salida: () <- Dado que se necesitan mas de 2 elementos, no regresa resultados