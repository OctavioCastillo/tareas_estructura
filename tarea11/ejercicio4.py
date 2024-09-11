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


def interlace_list(lista1:LinkedList, lista2:LinkedList):
    result_list = LinkedList()
    current1 = lista1.head
    current2 = lista2.head
    while current1.next is not None and current2.next is not None:
        result_list.insert(Node(current1.data))
        result_list.insert(Node(current2.data))
        current1 = current1.next
        current2 = current2.next
    
    while current1 is not None:
        result_list.insert(Node(current1.data))
        current1 = current1.next

    while current2 is not None:
        result_list.insert(Node(current2.data))
        current2 = current2.next
    
    return result_list


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

combined_list = interlace_list(lista1, lista2)
combined_list.showlist()