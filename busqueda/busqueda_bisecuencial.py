def bisecuencial_search(numeros, valor):
    for i in range(len(numeros)):
        for j in range(len(numeros[i])):
            if numeros[i][j] == valor:
                return i * len(numeros) + j
    return -1

binumeros = [
    [5, 3, 8],
    [6, 11, 2],
    [9, 4, 7]
]

valor = 11

pos = bisecuencial_search(binumeros, valor)

if pos >= 0:
    print(f"El valor {valor} se encuentra en la posición {pos}")
else:
    print("El valor no se encontró en la matriz")