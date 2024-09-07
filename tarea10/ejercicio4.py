class ColaTareas:
    def __init__(self):
        self.cola = []

    def agregar_tarea(self, tarea, tiempo):
        self.cola.append((tarea, tiempo))
        print(f"Tarea '{tarea}' agregada con tiempo de ejecución {tiempo}.")

    def ejecutar_tarea(self):
        if not self.cola:
            print("No hay tareas para ejecutar.")
        else:
            tarea, tiempo = self.cola.pop(0)
            print(f"Ejecutando tarea '{tarea}' que tarda {tiempo} segundos.")
            # Simular el tiempo de ejecución
            import time
            time.sleep(tiempo)

    def mostrar_cola_tareas(self):
        if not self.cola:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for tarea, tiempo in self.cola:
                print(f"Tarea: '{tarea}', Tiempo: {tiempo}")

# Ejemplo de uso
cola_tareas = ColaTareas()
cola_tareas.agregar_tarea("Tarea1", 2)
cola_tareas.agregar_tarea("Tarea2", 3)
cola_tareas.mostrar_cola_tareas()
cola_tareas.ejecutar_tarea()
cola_tareas.mostrar_cola_tareas()
