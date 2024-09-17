'''
Ejercicio 5 - Invertir una Cadena: Implementa una función 
recursiva que invierta una cadena de texto.La función debe 
recibir una cadena de caracteres y devolverla en orden inverso. 
Por ejemplo, si la entrada es "recursión", la salida debería ser "nóisrucer".
'''

def invertircadena(string):
    if len(string) == 0:
        return ""
    else:
        return invertircadena(string[1:]) + string[0]

print(invertircadena(input("Palabra: ")))

    