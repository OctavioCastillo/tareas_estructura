def ordenamiento_seleccion(lista):
    # Recorre cada elemento de la lista
    for i in range(len(lista)):
        # Encuentra el índice del elemento mínimo en la parte no ordenada
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        # Intercambia el elemento mínimo con el primer elemento de la parte no ordenada
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Solicitar lista de números al usuario
entrada = input("Ingresa una lista de números separados por comas: ")
lista = [int(x) for x in entrada.split(",")]

# Mostrar la lista antes del ordenamiento
print("Lista original:", lista)

# Llamar a la función de ordenamiento
ordenamiento_seleccion(lista)

# Mostrar la lista después del ordenamiento
print("Lista ordenada:", lista)
