def insertionsort_up(numeros):
    for i in range (1, len(numeros)):
        key = numeros[i]
        j = i -1
        while j >= 0 and key < numeros[j]:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = key

def binary_search(numeros, valor):
    insertionsort_up(numeros)
    i = 0
    j = len(numeros) -1
    while i <= j:
        m = (i + j) // 2
        if valor < numeros[m]:
            j = m - 1 
        elif valor > numeros[m]:
            i = m + 1
        else:
            return m
    return -1

numeros = [5, 3, 8, 6, 2]
valor = 6
pos = binary_search(numeros, valor)

if pos >= 0:
    print(f"El valor {valor} se encontró en la posición: {pos}")
else:
    print("El valor no se encontró en el arreglo")