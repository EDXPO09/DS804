# Definimos la funcion para invertir la cadena de texto
def invertir_cadena(cadena):
    
    # Caso base: cadena vacia
    if len(cadena) == 0:  
        return ""
    else:
        # Primer caracter de la cadena
        primer_caracter = cadena[0] 
        
        # Resto de la cadena (sin el primer caracter) 
        resto_cadena = cadena[1:]  
        
        # Inversión recursiva del resto de la cadena
        inverso_resto = invertir_cadena(resto_cadena) 
        
        # Concatenacion del inverso del resto con el primer caracter 
        return inverso_resto + primer_caracter  


# Palabras a Invertir
print(invertir_cadena("hola"))  # Resultado: aloh
print(invertir_cadena("Python"))  # Resultado: nohtyP
print(invertir_cadena("Edmundo"))  # Resultado: odnumdE
