'''
Ejercicio 6: Escribe un programa que utilice una pila para 
verificar si una expresión matemática con paréntesis está balanceada. 
La expresión puede contener paréntesis redondos `()`, cuadrados `[]`, y llaves `{}`.
'''

from ejercicio5 import Pila

def verificar_parentesis(cadena:str):
    pila = Pila()
    balanced = True
    index = 0
    while index < len(cadena) and balanced:
        simbolo = cadena[index]
        if simbolo == "(":
            pila.add(simbolo)
        else:
            if pila.empty():
                balanced = False
            else:
                pila.pop()
        
        index += 1

    if balanced and pila.empty():
        return True
    
    else:
        return False
    
print(verificar_parentesis('((()))'))
print(verificar_parentesis('(())'))
print(verificar_parentesis('((())'))
