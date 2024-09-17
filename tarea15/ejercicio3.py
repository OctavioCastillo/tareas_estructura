'''
Ejercicio 3 - Suma de los Dígitos de un Número:    
Implementa una función recursiva que calcule la suma de 
los dígitos de un número entero.  Dado un número entero, 
la función debe devolver la suma de sus dígitos. Por ejemplo, 
para el número 1234, la suma de los dígitos sería 1 + 2 + 3 + 4 = 10.
'''

def sumadigitos(n):
    if n==0:
        return 0
    else:
        return n%10 + sumadigitos(n//10)
    
print(sumadigitos(int(input("Dame un número: "))))

