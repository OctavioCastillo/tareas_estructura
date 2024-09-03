from collections import deque

class Persona:
    def __init__(self, cartas):
        self.cartas = cartas

    def __str__(self):
        return f"Persona con {self.cartas} cartas"

class ColaCorreo:
    def __init__(self, limite_cartas_por_persona):
        self.limite_cartas_por_persona = limite_cartas_por_persona
        self.cola = deque()

    def agregar_persona(self, persona):
        self.cola.append(persona)

    def procesar_cola(self):
        while self.cola:
            persona = self.cola.popleft()
            if persona.cartas > self.limite_cartas_por_persona:
                # Si la persona tiene más cartas que el límite, se parte la carga
                cartas_restantes = persona.cartas - self.limite_cartas_por_persona
                print(f"Procesando {self.limite_cartas_por_persona} cartas de {persona}")
                # Se vuelve a agregar a la cola con las cartas restantes
                self.agregar_persona(Persona(cartas_restantes))
            else:
                # Si la persona tiene cartas dentro del límite, se procesan todas
                print(f"Procesando {persona.cartas} cartas de {persona}")


limite_cartas = 5
cola_correo = ColaCorreo(limite_cartas)

# Crear personas con diferentes cantidades de cartas
personas = [
    Persona(3),
    Persona(7),
    Persona(2),
    Persona(8)
]

# Agregar personas a la cola de correo
for persona in personas:
    cola_correo.agregar_persona(persona)

# Procesar la cola
cola_correo.procesar_cola()
