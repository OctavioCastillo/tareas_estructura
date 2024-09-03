class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, valor):
        self.elementos.append(valor)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise IndexError("La pila está vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

    def invertir(self, string: str):
        # Crear una pila para almacenar los caracteres
        pila = Pila()
        
        # Apilar todos los caracteres de la cadena
        for char in string:
            pila.apilar(char)
        
        # Desapilar los caracteres para construir la cadena invertida
        cadena_invertida = ''
        while not pila.esta_vacia():
            cadena_invertida += pila.desapilar()
        
        return cadena_invertida
