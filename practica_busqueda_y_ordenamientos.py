def search_and_sort(lst, value):
    # Búsqueda lineal del valor en la lista
    for i in range(len(lst)):
        if lst[i] == value:
            # Si se encuentra el valor, aplicamos ordenamiento por selección
            for j in range(len(lst)):
                min_idx = j
                for k in range(j + 1, len(lst)):
                    if lst[k] < lst[min_idx]:
                        min_idx = k
                lst[j], lst[min_idx] = lst[min_idx], lst[j]  # Intercambiar elementos
            return i, lst  # Devolver índice y lista ordenada
    # Si no se encuentra el valor
    return "El valor no está presente"

# Prueba la función
test_list = [23, 5, 8, 12, 45, 78, 3]
print(search_and_sort(test_list, 12))  # Salida esperada: (índice, lista ordenada)
print(search_and_sort(test_list, 100))  # Salida esperada: "El valor no está presente"
