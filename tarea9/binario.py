class Pila:
    # Métodos anteriores...

    def binario(self, numero: int):
        if numero == 0:
            return "0"
        
        pila = Pila()
        
        while numero > 0:
            pila.apilar(numero % 2)
            numero = numero // 2
        
        binario_str = ''
        while not pila.esta_vacia():
            binario_str += str(pila.desapilar())
        
        return binario_str
