def search_and_sort(lst, value):
    # Búsqueda lineal para encontrar el índice del valor
    index = -1
    for i in range(len(lst)):
        if lst[i] == value:
            index = i
            break

    # Si el valor no está en la lista, devolver un mensaje
    if index == -1:
        return "El valor no está presente"

    # Ordenamiento por selección si el valor se encuentra en la lista
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]

    # Devolver el índice y la lista ordenada
    return index, lst

# Prueba de la función
test_list = [23, 5, 8, 12, 45, 78, 3]
print(search_and_sort(test_list, 12))  # Salida esperada: (índice, lista ordenada)
print(search_and_sort(test_list, 100)) # Salida esperada: "El valor no está presente"
