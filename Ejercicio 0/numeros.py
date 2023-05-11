def suma_fracciones(n1, d1, n2, d2):
    # Encontrar el minimo común multiplo de los denominadores
    mcm = d1 * d2
    while d1 != d2:
        if d1 > d2:
            d1 -= d2
        else:
            d2 -= d1
    mcm = mcm // d1
    
    # Sumar los numeradores
    n = n1 * (mcm // d1) + n2 * (mcm // d2)
    
    # Encontrar el maximo común divisor del numerador y denominador
    mcd = n
    while mcd != 0:
        r = mcm % mcd
        mcm = mcd
        mcd = r
        
    # Simplificar la fraccion
    n = n // mcm
    d = mcm // d1
    
    # Devolver el resultado en formato a/b
    return f"{n}/{d}"
