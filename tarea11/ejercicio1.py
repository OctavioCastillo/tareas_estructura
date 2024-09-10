'''
Ejercicio 1: Escribe un programa que tome un arreglo de enteros y 
encuentre el elemento máximo y el mínimo sin utilizar funciones predefinidas. 
Debe imprimir el valor máximo y el mínimo junto con sus índices en el arreglo.
'''

from random import randint

lista = [randint(0,10) for i in range(5)]

def maxValue(lista):
    highest = 0
    for i in lista:
        if highest < i:
            highest = i
    return highest

def minValue(lista):
    minimum = lista[0]
    for i in lista:
        if minimum > i:
            minimum = i
    return minimum

print(lista)
print(maxValue(lista))
print(minValue(lista))