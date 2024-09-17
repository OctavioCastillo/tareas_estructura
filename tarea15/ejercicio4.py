'''
Ejercicio 4 - Potencia Recursiva:  Implementa una función recursiva 
que calcule la potencia de un número  a^b . Dado dos números a y b, 
calcula a elevado a la potencia  b  recursivamente.
'''

def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)
    
print(potencia(int(input("Dame la base: ")), int(input("Dame la potencia: "))))