class pila:
    
# crear una pila vaci­a    
    def __init__(self):
        self.elementos = []
        
# push agregar un elemento a la pila (apilar)
    def push(self,dato):
        self.elementos.append(dato)

# pop quitar un elemento a la pila (desapilar)
    def pop(self):
        return self.elementos.pop()

# peek consultar el elemento top de la pila (sin desapilar)
    def peek(self):
        return self.elementos[len(self.elementos)-1]
        
# size dar el tamaÃ±o de la pila
    def size(slef):
        return len(self.elementos)
        
# es_vacia indica si la pila estÃ¡ vacÃ­a
    def es_vacia(self):
        return size() == 0
    
