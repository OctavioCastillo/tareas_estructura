class NodoSimple:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

def unir_listas_enlazadas(l1, l2):
    dummy = NodoSimple()
    actual = dummy

    while l1 and l2:
        if l1.valor < l2.valor:
            actual.siguiente = l1
            l1 = l1.siguiente
        else:
            actual.siguiente = l2
            l2 = l2.siguiente
        actual = actual.siguiente

    if l1:
        actual.siguiente = l1
    if l2:
        actual.siguiente = l2

    return dummy.siguiente

def eliminar_duplicados(cabeza):
    actual = cabeza
    while actual and actual.siguiente:
        if actual.valor == actual.siguiente.valor:
            actual.siguiente = actual.siguiente.siguiente
        else:
            actual = actual.siguiente
    return cabeza

def encontrar_kesimo_desde_el_final(cabeza, k):
    primero = cabeza
    segundo = cabeza

    for _ in range(k):
        if segundo is None:
            return None
        segundo = segundo.siguiente

    while segundo:
        primero = primero.siguiente
        segundo = segundo.siguiente

    return primero

def particionar_lista(cabeza, x):
    menor_dummy = NodoSimple()
    mayor_dummy = NodoSimple()

    menor = menor_dummy
    mayor = mayor_dummy

    while cabeza:
        if cabeza.valor < x:
            menor.siguiente = cabeza
            menor = menor.siguiente
        else:
            mayor.siguiente = cabeza
            mayor = mayor.siguiente
        cabeza = cabeza.siguiente

    mayor.siguiente = None
    menor.siguiente = mayor_dummy.siguiente

    return menor_dummy.siguiente
