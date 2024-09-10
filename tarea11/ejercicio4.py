'''
Ejercicio 4: Escribe un programa que tome dos listas 
enlazadas simples, las combine en una sola lista enlazada y la imprima. 
Asegúrate de que los elementos estén intercalados entre ambas listas.
'''

class Node():
    def __init__(self, dato):
        self.data = dato
        self.next = None

class LinkedList():
    
    def __init__(self) -> None:
        self.head = None

    def insert(self, new_node:Node):
        if self.head:
            temp_node = self.head

            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = new_node
        else:
            self.head = new_node

    def showlist(self):
        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print('None')


lista1 = LinkedList()
lista2 = LinkedList()

for i in range(10):
    new_node = Node(i)
    lista1.insert(new_node)

for _ in "abcdefjhij":
    new_node = Node(_)
    lista2.insert(new_node)

lista1.showlist()
lista2.showlist()