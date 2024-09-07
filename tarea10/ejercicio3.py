import heapq

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def agregar(self, elemento, prioridad):
        heapq.heappush(self.cola, (-prioridad, elemento))

    def atender(self):
        if not self.cola:
            print("La cola de prioridad está vacía.")
        else:
            prioridad, elemento = heapq.heappop(self.cola)
            print(f"Elemento {elemento} con prioridad {-prioridad} ha sido atendido.")

    def mostrar_cola(self):
        if not self.cola:
            print("La cola de prioridad está vacía.")
        else:
            print("Estado actual de la cola de prioridad:")
            for prioridad, elemento in sorted(self.cola, reverse=True):
                print(f"Elemento: {elemento}, Prioridad: {-prioridad}")

# Ejemplo de uso
cola_prioridad = ColaPrioridad()
cola_prioridad.agregar("Tarea1", 2)
cola_prioridad.agregar("Tarea2", 1)
cola_prioridad.agregar("Tarea3", 3)
cola_prioridad.mostrar_cola()
cola_prioridad.atender()
cola_prioridad.mostrar_cola()
