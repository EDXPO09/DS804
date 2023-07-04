from sys import argv

class Archivos:
    """ Clase Archivos con metodo para leer e imprimir el contenido de un archivo"""

    """
        Inicia el atributo con el nombre del archivo a utilizar.
    """
    def __init__(self):
        self.archivo = None
        self.contenido = None

        """
        Abre el archivo especificado, lee su contenido y lo imprime por pantalla.
        """
    def imprimir_contenido(self, archivo):

        self.archivo = open(archivo, 'r')
        self.contenido = self.archivo.read()
        print(self.contenido)
        self.archivo.close()


        """
        Abre el archivo especificado, lee su contenido línea por línea y imprime la columna especificada de cada línea.
        El contenido del archivo debe estar separado por comas.
        :param archivo: Nombre del archivo.
        :param columna: Nombre de la columna a imprimir.
        """
    def imprimir_columna(self, archivo, columna):
        
        self.archivo = open(archivo, 'r')
        self.contenido = self.archivo.readlines()
        for linea in self.contenido:
            if columna == 'colA':
                print(linea.split(',')[0])
            if columna == 'colB':
                print(linea.split(',')[1])
            if columna == 'colC':
                print(linea.split(',')[2])
            if columna == 'colD':
                print(linea.split(',')[3])

    def reescribir_columna_4(self, archivo, numero):
        """
        Abre el archivo especificado, lee su contenido línea por línea y reescribe la cuarta columna de cada línea
        con el número especificado.
        Luego guarda los cambios en el archivo.
        :param archivo: Nombre del archivo.
        """
        self.archivo = open(archivo, 'r')
        self.contenido = self.archivo.readlines()
        nuevo_contenido = ''
        for linea in self.contenido:
            array_linea = linea.split(',')[0:3]
            nueva_linea = f'{array_linea[0]},{array_linea[1]},{array_linea[2]},{numero}\n'
            nuevo_contenido = nuevo_contenido + nueva_linea
        self.archivo.close()

        self.archivo = open(archivo, 'w')
        self.archivo.write(nuevo_contenido)
        self.archivo.close()



""""  Crea una instancia de la clase Archivos llamada archivo1 y muestra el contenido original del archivo. 
Luego, llama al método reescribir_columna_4 para modificar la cuarta columna del archivo con el número especificado.
Finalmente, muestra el contenido del archivo después de la edición."""

nombre_archivo = argv[1]
numero = argv[2]
archivo1 = Archivos()

print(f'Contenido del archivo antes de la edicion')
archivo1.imprimir_contenido(archivo=nombre_archivo)
archivo1.reescribir_columna_4(archivo=nombre_archivo, numero=numero)

print(f'\n\nContenido del archivo despues de la edicion')
archivo1.imprimir_contenido(archivo=nombre_archivo)