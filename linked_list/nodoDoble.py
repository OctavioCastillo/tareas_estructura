class NodoDoble:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.tail = None

    def agregar_al_final(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.tail
            self.tail = nuevo_nodo

    def eliminar_nodo(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                if actual == self.tail:
                    self.tail = actual.anterior
                return
            actual = actual.siguiente

    def recorrer_hacia_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=' ')
            actual = actual.siguiente
        print()

    def recorrer_hacia_atras(self):
        actual = self.tail
        while actual:
            print(actual.valor, end=' ')
            actual = actual.anterior
        print()
