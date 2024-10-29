def ordenamiento_insercion(lista):
    # Recorre desde el segundo elemento hasta el final de la lista
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Mueve los elementos mayores que la clave una posición adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta la clave en su posición correcta
        lista[j + 1] = clave

# Solicitar lista de números al usuario
entrada = input("Ingresa una lista de números separados por comas: ")
lista = [int(x) for x in entrada.split(",")]

# Mostrar la lista antes del ordenamiento
print("Lista original:", lista)

# Llamar a la función de ordenamiento
ordenamiento_insercion(lista)

# Mostrar la lista después del ordenamiento
print("Lista ordenada:", lista)
