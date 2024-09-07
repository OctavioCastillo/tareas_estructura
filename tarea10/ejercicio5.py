class ColaImpresora:
    def __init__(self):
        self.cola = []

    def agregar_documento(self, documento):
        self.cola.append(documento)
        print(f"Documento '{documento}' agregado a la cola de impresión.")

    def imprimir_documento(self):
        if not self.cola:
            print("La cola de impresión está vacía.")
        else:
            documento = self.cola.pop(0)
            print(f"Imprimiendo documento '{documento}'.")

    def mostrar_cola_impresion(self):
        if not self.cola:
            print("No hay documentos en la cola de impresión.")
        else:
            print("Documentos pendientes de impresión:")
            for documento in self.cola:
                print(documento)

# Ejemplo de uso
cola_impresora = ColaImpresora()
cola_impresora.agregar_documento("Documento1")
cola_impresora.agregar_documento("Documento2")
cola_impresora.mostrar_cola_impresion()
cola_impresora.imprimir_documento()
cola_impresora.mostrar_cola_impresion()
