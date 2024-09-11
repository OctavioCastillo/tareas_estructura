'''
Ejercicio 5: Implementa una pila, escribe funciones para convertir 
un numero decimal a hexadecimal.
'''

class Pila:

    def __init__(self) -> None:
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def add(self, new):
        self.items.append(new)

    def pop(self):
        return self.items.pop()
    
    def show(self):
        print(self.items)


def converter(num_decimal:int):

    if num_decimal == 0:
        return "0"
    
    pila = Pila()
    num_haxadecimales = "0123456789ABCEF"

    while num_decimal > 0:
        resto = num_decimal % 16
        pila.add(num_haxadecimales[resto])
        num_decimal //= 16

    hexadecimal = ""
    while not pila.empty():
        hexadecimal += pila.pop()

    return hexadecimal

print(converter(160))
print(converter(10))
print(converter(26))
