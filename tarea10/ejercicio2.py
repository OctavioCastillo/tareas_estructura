class ColaCircular:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.cola = [None] * tamaño
        self.frente = 0
        self.detras = 0
        self.size = 0

    def encolar(self, elemento):
        if self.size == self.tamaño:
            print(f"La cola está llena. Reemplazando el elemento más antiguo.")
            self.frente = (self.frente + 1) % self.tamaño
        self.cola[self.detras] = elemento
        self.detras = (self.detras + 1) % self.tamaño
        self.size = min(self.size + 1, self.tamaño)

    def desencolar(self):
        if self.size == 0:
            print("La cola está vacía. No hay elementos para desencolar.")
        else:
            elemento = self.cola[self.frente]
            self.cola[self.frente] = None
            self.frente = (self.frente + 1) % self.tamaño
            self.size -= 1
            print(f"Elemento {elemento} ha sido desencolado.")

    def mostrar_cola(self):
        if self.size == 0:
            print("La cola está vacía.")
        else:
            print("Estado actual de la cola circular:")
            for i in range(self.size):
                index = (self.frente + i) % self.tamaño
                print(self.cola[index], end=" ")
            print()

# Ejemplo de uso
cola_circular = ColaCircular(3)
cola_circular.encolar("A")
cola_circular.encolar("B")
cola_circular.encolar("C")
cola_circular.mostrar_cola()
cola_circular.encolar("D")
cola_circular.mostrar_cola()
cola_circular.desencolar()
cola_circular.mostrar_cola()
