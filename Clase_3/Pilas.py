class Pila:
    def __init__(self):
        self.items = []

    def agregar(self, elemento):
        self.items.append(elemento)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def buscar(self, elemento):
        if elemento in self.items:
            return True
        else:
            return False
    # Comprobar si tiene contenido
    def esta_vacia(self):
        return len(self.items) == 0


# Ejemplo de uso
pila = Pila()

# Elementos dentro de "pila"
pila.agregar(5)
pila.agregar(10)
pila.agregar(15)

print(pila.buscar(10))  # True
print(pila.buscar(20))  # False

print(pila.eliminar())  # 15
print(pila.eliminar())  # 10
print(pila.eliminar())  # 5
print(pila.eliminar())  # None (pila vacía)
