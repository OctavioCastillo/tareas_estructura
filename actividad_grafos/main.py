class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        """Añade un nodo al grafo si no existe."""
        if nodo not in self.grafo:
            self.grafo[nodo] = []
            print(f"Nodo {nodo} agregado.")
        else:
            print(f"Nodo {nodo} ya existe.")

    def agregar_arista(self, nodo1, nodo2):
        """Crea una arista entre nodo1 y nodo2."""
        if nodo1 not in self.grafo:
            self.agregar_nodo(nodo1)
        if nodo2 not in self.grafo:
            self.agregar_nodo(nodo2)
        
        if nodo2 not in self.grafo[nodo1]:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)  # Grafo no dirigido
            print(f"Arista entre {nodo1} y {nodo2} agregada.")
        else:
            print(f"Arista entre {nodo1} y {nodo2} ya existe.")

    def eliminar_nodo(self, nodo):
        """Elimina el nodo y todas las aristas relacionadas."""
        if nodo in self.grafo:
            # Eliminar todas las aristas relacionadas
            for vecino in self.grafo[nodo]:
                self.grafo[vecino].remove(nodo)
            del self.grafo[nodo]
            print(f"Nodo {nodo} eliminado.")
        else:
            print(f"Nodo {nodo} no existe.")

    def eliminar_arista(self, nodo1, nodo2):
        """Elimina la arista entre nodo1 y nodo2."""
        if nodo1 in self.grafo and nodo2 in self.grafo[nodo1]:
            self.grafo[nodo1].remove(nodo2)
            self.grafo[nodo2].remove(nodo1)  # Grafo no dirigido
            print(f"Arista entre {nodo1} y {nodo2} eliminada.")
        else:
            print(f"No existe una arista entre {nodo1} y {nodo2}.")

grafo = Grafo()

# Agregando nodos
grafo.agregar_nodo('A')
grafo.agregar_nodo('B')
grafo.agregar_nodo('C')

# Agregando aristas
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')

# Mostrando el grafo
print("Grafo actual:", grafo.grafo)

# Eliminando un nodo
grafo.eliminar_nodo('B')

# Mostrando el grafo después de eliminar un nodo
print("Grafo después de eliminar nodo B:", grafo.grafo)