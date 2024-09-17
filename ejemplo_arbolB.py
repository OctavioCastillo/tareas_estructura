# Construye la clase nodo
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Clase ArbolBinario
class ArbolBinario:
    def __init__(self) ->None:
        self.root = None

    def insertar(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertarhijo(value, self.root)
        
    def insertarhijo(self, value, current_node:Node):
        if value < current_node.data:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insertarhijo(value, current_node.left)
        else:
            if value > current_node.data:
                if current_node.right is None:
                    current_node.right = Node(value)
            else:
                self.insertarhijo(value, current_node.right)
    
    def buscar(self, nodo, valor):
        if self.root.data == valor:
            print("Valor encontrado en la raíz")
        else:
            if valor > self.root.data:
                self.buscar(self.root.right, valor)
            else:
                self.buscar(self.root.left, valor)