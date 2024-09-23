class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._agregar_recursivo(self.raiz, dato)

    def _agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.izquierdo, dato)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.derecho, dato)

    def buscar(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        elif dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierdo, dato)
        else:
            return self._buscar_recursivo(nodo.derecho, dato)

    def recorrido_inorden(self):
        return self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo):
        resultado = []
        if nodo:
            resultado.extend(self._recorrido_inorden_recursivo(nodo.izquierdo))
            resultado.append(nodo.dato)
            resultado.extend(self._recorrido_inorden_recursivo(nodo.derecho))
        return resultado

    def recorrido_preorden(self):
        return self._recorrido_preorden_recursivo(self.raiz)

    def _recorrido_preorden_recursivo(self, nodo):
        resultado = []
        if nodo:
            resultado.append(nodo.dato)
            resultado.extend(self._recorrido_preorden_recursivo(nodo.izquierdo))
            resultado.extend(self._recorrido_preorden_recursivo(nodo.derecho))
        return resultado

    def recorrido_postorden(self):
        return self._recorrido_postorden_recursivo(self.raiz)

    def _recorrido_postorden_recursivo(self, nodo):
        resultado = []
        if nodo:
            resultado.extend(self._recorrido_postorden_recursivo(nodo.izquierdo))
            resultado.extend(self._recorrido_postorden_recursivo(nodo.derecho))
            resultado.append(nodo.dato)
        return resultado

    def imprimir(self):
        niveles = []
        self._imprimir_recursivo(self.raiz, niveles, 0)
        for nivel in niveles:
            print(" ".join(map(str, nivel)))

    def _imprimir_recursivo(self, nodo, niveles, nivel):
        if nodo is None:
            return
        if len(niveles) == nivel:
            niveles.append([])
        niveles[nivel].append(nodo.dato)
        self._imprimir_recursivo(nodo.izquierdo, niveles, nivel + 1)
        self._imprimir_recursivo(nodo.derecho, niveles, nivel + 1)



arbol = ArbolBinario()
datos = [5, 3, 7, 2, 4, 6, 8]
for dato in datos:
    arbol.agregar(dato)

print("Recorrido inorden:", arbol.recorrido_inorden())
print("Recorrido preorden:", arbol.recorrido_preorden())
print("Recorrido postorden:", arbol.recorrido_postorden())
print("Buscar 4:", arbol.buscar(4))
print("Buscar 9:", arbol.buscar(9))
print("Imprimir árbol:")
arbol.imprimir()
