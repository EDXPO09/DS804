import os
import calendar

def crear_carpetas():
    year = 2023  # Cambiar el año si es necesario
    meses = [mes for mes in calendar.month_name[1:] if mes]  # Obtener nombres de los meses
    
    for mes in meses:
        num_dias = calendar.monthrange(year, meses.index(mes) + 1)[1]  # Obtener la cantidad de días del mes
        carpeta_mes = os.path.join(os.path.expanduser("~"), "Downloads", mes)  # Ruta de la carpeta del mes, Se creara en la carpeta "Downloads"
        # En caso de que desea guardarlo en un archivo especifico, especificar la ruta en la linea 10
        
        if not os.path.exists(carpeta_mes): #Comprueba existencia de la carpeta
            os.mkdir(carpeta_mes)
        
        for dia in range(1, num_dias + 1):
            carpeta_dia = os.path.join(carpeta_mes, f"Dia {dia}")  # Ruta de la carpeta del día
            
            if not os.path.exists(carpeta_dia): # Comprueba existencia de la carpeta
                os.mkdir(carpeta_dia)

crear_carpetas()
