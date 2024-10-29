def ordenamiento_burbuja(lista):
    n = len(lista)
    # Recorre la lista n veces
    for i in range(n):
        # En cada pasada, los elementos más grandes van quedando al final de la lista
        for j in range(0, n - i - 1):
            # Compara elementos adyacentes y los intercambia si están en el orden incorrecto
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Solicitar lista de números al usuario
entrada = input("Ingresa una lista de números separados por comas: ")
lista = [int(x) for x in entrada.split(",")]

# Mostrar la lista antes del ordenamiento
print("Lista original:", lista)

# Llamar a la función de ordenamiento
ordenamiento_burbuja(lista)

# Mostrar la lista después del ordenamiento
print("Lista ordenada:", lista)
