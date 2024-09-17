'''
Ejercicio 7: Implementa una cola utilizando una lista enlazada. 
Escribe funciones para simular un centro de atención a clientes de 
Telcel donde las personas llegan y son atendidas en orden de llegada. 
El programa debe permitir tomar un turno, indicar el turno que está 
atendiendo  y el próximo turno
'''

class Node:

    def __init__(self, data:str) -> None:
        self.data = data
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.lenght = 0

    def empty(self):
        return self.head is None
    
    def add_to_queue(self, value):
        new_node = Node(value)
        if self.empty():
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        self.lenght += 1
    
    def attend(self):
        if self.empty():
            raise IndexError("La cola está vacía")
            
        value = self.head.data
        self.head = self.head.next
        self.lenght -= 1
        return value
    
    def current_turn(self):
        if self.empty():
            raise IndexError("La cola está vacía")
        return self.head.data   
        


    
