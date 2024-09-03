class Pila:
    # Métodos anteriores...

    def sort(self):
        pila_aux = Pila()
        
        while not self.esta_vacia():
            valor = self.desapilar()
            
            while not pila_aux.esta_vacia() and pila_aux.elementos[-1] < valor:
                self.apilar(pila_aux.desapilar())
            
            pila_aux.apilar(valor)
        
        # Mover los elementos ordenados de vuelta a la pila original
        while not pila_aux.esta_vacia():
            self.apilar(pila_aux.desapilar())
