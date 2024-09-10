'''
Ejercicio 2: Crea un programa que reciba un arreglo de 
números enteros y determine si el arreglo está ordenado de manera 
ascendente, descendente, o no está ordenado.
'''
from random import randint

ordenado = [i for i in range (10)]
descendente = [i for i in range(9,-1,-1)]
random = [randint(0,10) for i in range(10)]

print(ordenado)
print(descendente)
print(random)

def verificar_orden(lista):

    ordenado = all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))
    descendente = all(lista[i] >=lista[i + 1] for i in range(len(lista) -1))

    if ordenado:
        print("Está ordenado")
    elif descendente:
        print("Está descendente")
    else:
        print("Está desordenado")

verificar_orden(ordenado)
verificar_orden(descendente)
verificar_orden(random)    