class Nodo:
    def __init__(self, data):
        self.data = data
        self.izquierdo = None
        self.derecho = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, data):
        if self.raiz is None:
            self.raiz = Nodo(data)
        else:
            self._insertar_recursivo(self.raiz, data)

    def _insertar_recursivo(self, nodo, data):
        if data < nodo.data:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(data)
            else:
                self._insertar_recursivo(nodo.izquierdo, data)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(data)
            else:
                self._insertar_recursivo(nodo.derecho, data)

    def buscar(self, data):
        return self._buscar_recursivo(self.raiz, data)

    def _buscar_recursivo(self, nodo, data):
        if nodo is None:
            return None
        if nodo.data == data:
            return nodo
        elif data < nodo.data:
            return self._buscar_recursivo(nodo.izquierdo, data)
        else:
            return self._buscar_recursivo(nodo.derecho, data)

    def inorder(self):
        return self._inorder_recursivo(self.raiz)

    def _inorder_recursivo(self, nodo):
        resultado = []
        if nodo:
            resultado.extend(self._inorder_recursivo(nodo.izquierdo))
            resultado.append(nodo.data)
            resultado.extend(self._inorder_recursivo(nodo.derecho))
        return resultado


arbol = Arbol()
datos = [5, 3, 7, 2, 4, 6, 8]
for dato in datos:
    arbol.insertar(dato)

print("Recorrido inorden:", arbol.inorder())
nodo_buscado = arbol.buscar(4)
if nodo_buscado:
    print("Nodo encontrado:", nodo_buscado.data)
else:
    print("Nodo no encontrado")
