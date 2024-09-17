'''
Ejercicio 1 - Factorial de un Número:    Implementa una función 
recursiva que calcule el factorial de un número.    El factorial de un número 
n (denotado como n! ) es el producto de todos los enteros positivos menores o 
iguales a n. Por ejemplo, 5! = 5 x 4 x 3 x 2 x 1   
'''

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(5))