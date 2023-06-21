import math

# Representar num complejo en forma binomica, con parte real y parte imaginaria
class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def imprimir(self):
        print(f"{self.real} + {self.imaginario}i")
    
    def multiplicar_escalar(self, escalar):
        self.real *= escalar
        self.imaginario *= escalar
    
    def modulo(self):
        return math.sqrt(self.real**2 + self.imaginario**2)
    
    def fase(self):
        return math.atan2(self.imaginario, self.real)
    
    def conjugacion(self):
        return NumeroComplejo(self.real, -self.imaginario)
    
    def convertir_a_polar(self):
        modulo = self.modulo()
        fase = self.fase()
        return (modulo, fase)

# Aplicacion de las Funciones
# 3 = Num Real
# 4 = Num imaginario
complejo = NumeroComplejo(3, 4)

# Impresion esperada: 3 + 4i
complejo.imprimir()

# Multiplicar valores por 2
complejo.multiplicar_escalar(2)

# Impresion esperada: 6 + 8i
complejo.imprimir()

# Impresion de Modulo
modulo = complejo.modulo()
print("Módulo:", modulo)

# Impresion de Fase 
fase = complejo.fase()
print("Fase:", fase)

# Conjugacion de Valores
# Impresion Esperada: 6 + -8i
conjugado = complejo.conjugacion()
conjugado.imprimir()

# Impresion de forma polar
polar = complejo.convertir_a_polar()
print("Forma polar:", polar)
