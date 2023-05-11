# '{}' = Es para indicar que queremos reemplazar este valor con uno formateado
# ':02X' = Formatear el valor como un numero hexadecimal de 2 digitos
# format = Es una funcion python que nos ayudara a convertir valores Decimales a su equivalente en Hexadecimal
# La "X" dentro de '{:02X}' significa que queremos que sea en mayusculas la conversion
def rgb_a_hexadecimal(r, g, b):
    # Convertimos los valores RGB a su equivalente en hexadecimal
    r_hex = '{:02X}'.format(r)
    g_hex = '{:02X}'.format(g)
    b_hex = '{:02X}'.format(b)
    
    # Combinamos los valores hexadecimales en una cadena de texto y la devolvemos
    return '#' + r_hex + g_hex + b_hex

# Convertir el color RGB (255, 0, 0) a hexadecimal
# Rojo = (255, 0, 0)
# Verde = (0, 255, 0)
# Azul = (0, 0, 255)
hexadecimal = rgb_a_hexadecimal(255, 0, 0)
print(hexadecimal) # Imprime "#FF0000" que seria rojo



# Fuente: Como Formatear Valores en Python
# https://es.stackoverflow.com/questions/178990/cómo-puedo-dar-formato-de-números-en-python-con-separador-de-miles-y-de-decima

# Selector de Color para obtener los RGB
# https://www.google.com/search?client=opera-gx&q=%2300FF00&sourceid=opera&ie=UTF-8&oe=UTF-8