'''
Ejercicio 6 - Torres de Hanói (Desafío):   Implementa una función recursiva para resolver 
el clásico problema de las Torres de Hanói. Las Torres de Hanói es un rompecabezas matemático 
en el que tienes tres varillas y varios discos de diferentes tamaños que pueden deslizarse 
sobre cualquiera de las varillas. El rompecabezas comienza con los discos apilados en orden 
de tamaño en una varilla, con el disco más pequeño en la parte superior. El objetivo es mover 
toda la pila a otra varilla, respetando las siguientes reglas:
   - Solo se puede mover un disco a la vez.
   - Solo puedes mover el disco superior de una pila.
   - Un disco más grande no puede ser colocado sobre uno más pequeño.
'''

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen)

hanoi(3, 'A', 'C', 'B')


def hanoi_moves(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi_moves(n - 1) + 1

n_discs = 3
print(f"El número de movimientos necesarios para {n_discs} discos es: {hanoi_moves(n_discs)}")

