class LinkedList:

    def __init__(self):

        ## inicializar la cabeza con None
        self.head = None

    def insert(self, nuevo_nodo):

        ## comprueba si la cabeza está vacía o no
        if self.head:

            ## obtener el último nodo
            ultimo_nodo = self.head

            while ultimo_nodo.next != None:

                ultimo_nodo = ultimo_nodo.next

            ## asignar el nuevo nodo al puntero siguiente del último nodo
            ultimo_nodo.next = nuevo_nodo

        else:

            ## head está vacío
            ## asignar el nodo a cabeza
            self.head = nuevo_nodo
        
    def mostrar(self):

        ## variable para iteración
        temp_node = self.head

        ## iterar hasta llegar al final de la lista enlazada
        while temp_node != None:

            ## imprimiendo los datos del nodo
            print(temp_node.datos, end='->')

            ## pasar al siguiente nodo
            temp_node = temp_node.next

        print('Nulo')

    def invertir(self):

        anterior = None
        actual = self.head

        while actual is not None:
            temp = actual.next  # Guarda el siguiente nodo
            actual.next = anterior  # Invertir el puntero 'next' del nodo actual
            anterior = actual  # Mueve el puntero 'anterior' al nodo actual
            actual = temp  # Mueve el puntero 'actual' al siguiente nodo en la lista original

        self.head = anterior  # Ajusta el head de la lista a la nueva cabeza

    
    def detectar_ciclo(self):
        tortuga = self.head
        liebre = self.head
        
        while liebre and liebre.next:
            tortuga = tortuga.next  # Mueve tortuga un paso
            liebre = liebre.next.next  # Mueve liebre dos pasos
            
            if tortuga == liebre:
                return True  # Hay un ciclo
        
        return False  # No hay ciclo


    def eliminar_dato(self, dato):

        actual = self.head
        previo = None

        while actual is not None and actual.datos != dato:
            previo = actual
            actual = actual.next

        if actual is None:

            print(f"Dato {dato} no encontrado en la lista.")
            return

        if previo is None:
            self.head = actual.next

        else:
            previo.next = actual.next

        print(f"Dato {dato} eliminado de la lista.")

    def recorrer(self):

        temp_node = self.head

        if not temp_node:
            print("La lista está vacía.")
            return 0
        
        while temp_node is not None:
            print(temp_node.datos, end=' -> ')
            temp_node = temp_node.next
        print('Nulo')

    def buscar(self, dato):

        temp_node = self.head

        while temp_node is not None:

            if temp_node.datos == dato:

                print(f"Dato {dato} encontrado en la lista.")
                return 0
            
            temp_node = temp_node.next
        print(f"Dato {dato} no encontrado en la lista.")

    def vaciar(self):

        self.head = None

        print("Lista vaciada.")
        self.mostrar()
