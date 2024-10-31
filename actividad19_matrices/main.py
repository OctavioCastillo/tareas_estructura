import numpy as np

class Grafo:
    def __init__(self):
        # Diccionario de adyacencia para representar el grafo
        self.grafo = {}
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, nodo):
        # Agrega un nodo al grafo si no existe
        if nodo not in self.grafo:
            self.grafo[nodo] = []
            self.nodos.append(nodo)

    def eliminar_nodo(self, nodo):
        # Elimina el nodo y todas sus conexiones
        if nodo in self.grafo:
            # Elimina el nodo de las listas de adyacencia de otros nodos
            for adj in self.grafo.values():
                if nodo in adj:
                    adj.remove(nodo)
            # Elimina el nodo del grafo
            del self.grafo[nodo]
            self.nodos.remove(nodo)

    def agregar_arista(self, nodo1, nodo2):
        # Agrega una arista bidireccional entre nodo1 y nodo2
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)
            self.aristas.append((nodo1, nodo2))

    def eliminar_arista(self, nodo1, nodo2):
        # Elimina la arista entre nodo1 y nodo2
        if nodo1 in self.grafo and nodo2 in self.grafo:
            if nodo2 in self.grafo[nodo1]:
                self.grafo[nodo1].remove(nodo2)
            if nodo1 in self.grafo[nodo2]:
                self.grafo[nodo2].remove(nodo1)
            if (nodo1, nodo2) in self.aristas:
                self.aristas.remove((nodo1, nodo2))
            elif (nodo2, nodo1) in self.aristas:
                self.aristas.remove((nodo2, nodo1))

    def matriz_adyacencia(self):
        # Crear la matriz de adyacencia
        n = len(self.nodos)
        matriz = np.zeros((n, n), dtype=int)
        for i, nodo1 in enumerate(self.nodos):
            for j, nodo2 in enumerate(self.nodos):
                if nodo2 in self.grafo[nodo1]:
                    matriz[i][j] = 1
        return matriz

    def matriz_incidencia(self):
        # Crear la matriz de incidencia
        n = len(self.nodos)
        m = len(self.aristas)
        matriz = np.zeros((n, m), dtype=int)
        for j, (nodo1, nodo2) in enumerate(self.aristas):
            i1 = self.nodos.index(nodo1)
            i2 = self.nodos.index(nodo2)
            matriz[i1][j] = 1
            matriz[i2][j] = 1
        return matriz

    def mostrar_matriz_adyacencia(self):
        matriz = self.matriz_adyacencia()
        print("Matriz de Adyacencia:")
        print(matriz)

    def mostrar_matriz_incidencia(self):
        matriz = self.matriz_incidencia()
        print("Matriz de Incidencia:")
        print(matriz)

# Ejemplo de uso:
grafo = Grafo()
grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(1, 3)

# Mostrar matrices
grafo.mostrar_matriz_adyacencia()
grafo.mostrar_matriz_incidencia()
