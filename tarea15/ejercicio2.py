'''
Ejercicio 2 - Serie de Fibonacci:  Implementa una función 
recursiva para calcular el n-ésimo número de la serie de Fibonacci.  
La secuencia de Fibonacci es una sucesión de números donde cada número 
es la suma de los dos anteriores. Los primeros dos números de la 
secuencia son 0 y 1. Por ejemplo, los primeros seis números de la secuencia 
de Fibonacci son: 0, 1, 1, 2, 3, 5, 8...
'''

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(int(input("Posición de la serie para calcular: "))))