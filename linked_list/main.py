from nodo import Nodo
from linked import LinkedList



## instanciar la linked_list
linked_list = LinkedList()



## insertar los datos en la lista enlazada

linked_list.insert(Nodo(1))

linked_list.insert(Nodo(2))

linked_list.insert(Nodo(3))

linked_list.insert(Nodo(4))

linked_list.insert(Nodo(5))

linked_list.insert(Nodo(6))

linked_list.insert(Nodo(7))

## imprimir la lista enlazada
linked_list.mostrar()

print(linked_list.detectar_ciclo())

linked_list.buscar(5)

linked_list.invertir()
linked_list.mostrar

linked_list.eliminar_dato(3)

linked_list.recorrer()

linked_list.vaciar()