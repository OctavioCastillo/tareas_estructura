'''
Ejercicio 3: Implementa una lista enlazada simple en la 
que puedas insertar un nodo al principio, al final, y en una 
posición específica. Crea una función que imprima todos los elementos de la lista.
'''

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insertRight(self, new_node:Node):
        if self.head:
            temp_node = self.head

            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = new_node
        else:
            self.head = new_node
    
    def insertLeft(self, new_node:Node):
        new_node.next = self.head
        self.head = new_node

    def insertAnywhere(self, new_node:Node, position):
        if position == 0:
            self.insertLeft(new_node)
        else:
            current_node = self.head
            for _ in range(position - 1):
                if current_node is None:
                    raise IndexError("Position out of list range")
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def showList(self):
        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print('None')


linked = LinkedList()

for i in range (10):
    new_node = Node(i)
    linked.insertRight(new_node)

linked.showList()
linked.insertLeft(Node('a'))
linked.showList()
linked.insertAnywhere(Node('b'), position=6)
linked.showList()