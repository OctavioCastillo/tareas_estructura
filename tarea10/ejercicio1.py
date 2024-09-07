class ColaBanco:
    def __init__(self):
        self.cola = []

    def llegada_cliente(self, cliente):
        self.cola.append(cliente)
        print(f"Cliente {cliente} agregado a la cola.")

    def atender_cliente(self):
        if not self.cola:
            print("La cola está vacía. No hay clientes para atender.")
        else:
            cliente = self.cola.pop(0)
            print(f"Cliente {cliente} ha sido atendido.")

    def mostrar_cola(self):
        if not self.cola:
            print("La cola está vacía.")
        else:
            print("Clientes en la cola:")
            for cliente in self.cola:
                print(cliente)

# Ejemplo de uso
banco = ColaBanco()
banco.llegada_cliente("Cliente1")
banco.llegada_cliente("Cliente2")
banco.mostrar_cola()
banco.atender_cliente()
banco.mostrar_cola()
