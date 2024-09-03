class Cola:

    def __init__(self):
        self.elementos = []

    def estaVacia(self):
        return self.elementos == []
    
    def agregar(self, dato):
        self.elementos.append(dato)

    def salir(self):
        return self.elementos.pop()
    
    def size(self):
         return len(self.elementos)
    
    def avanzar(self):
        return self.elementos.pop(0)
    
    def mostrar(self):
        print (self.elementos)
    

# Main

cola = Cola()

string = 'abcdefghij'
for i in string:
    cola.agregar(i)

cola.mostrar()

cola.salir()
cola.mostrar()

cola.avanzar()
cola.mostrar()
