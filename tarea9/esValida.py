class Pila:
    # Métodos anteriores...

    def esValida(self, secuencia: str) -> bool:
        pila = Pila()
        
        for char in secuencia:
            if char == '{':
                pila.apilar(char)
            elif char == '}':
                if pila.esta_vacia():
                    return False
                pila.desapilar()
        
        return pila.esta_vacia()
