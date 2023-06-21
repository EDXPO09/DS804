def representar_cubo(d):
    # Crear un arreglo multidimensional de tamaño (d+1) x (d+1) x (d+1)
    cubo = [[[0 for _ in range(d+1)] for _ in range(d+1)] for _ in range(d+1)]

    # Asignar valores a las posiciones requeridas
    cubo[0][0][0] = 1
    cubo[0][0][d] = 2
    cubo[0][d][0] = 3
    cubo[0][d][d] = 4
    cubo[d][0][0] = 5
    cubo[d][0][d] = 6
    cubo[d][d][0] = 7
    cubo[d][d][d] = 8

    # Mostrar los valores en las posiciones requeridas
    print("Posiciones del cubo:")
    print("●0,0,0:", cubo[0][0][0])
    print("●0,0,d:", cubo[0][0][d])
    print("●0,d,0:", cubo[0][d][0])
    print("●0,d,d:", cubo[0][d][d])
    print("●d,0,0:", cubo[d][0][0])
    print("●d,0,d:", cubo[d][0][d])
    print("●d,d,0:", cubo[d][d][0])
    print("●d,d,d:", cubo[d][d][d])

# Aplicacion del codigo
d = int(input("Ingrese el número de dimensiones del cubo: "))
representar_cubo(d)
