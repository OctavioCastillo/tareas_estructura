class Pila:
    # Métodos anteriores...

    def separarParImpar(self):
        pila_pares = Pila()
        pila_impares = Pila()
        
        while not self.esta_vacia():
            numero = self.desapilar()
            if numero % 2 == 0:
                pila_pares.apilar(numero)
            else:
                pila_impares.apilar(numero)
        
        # Volver a apilar los pares
        while not pila_pares.esta_vacia():
            self.apilar(pila_pares.desapilar())
        
        # Volver a apilar los impares
        while not pila_impares.esta_vacia():
            self.apilar(pila_impares.desapilar())
