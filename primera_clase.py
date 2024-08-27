'''
Ejercicio 1
Realizar un programa que defina un vector llamado “vector_numeros” de 10 enteros,
a continuación lo inicialice con valores aleatorios (del 1 al 10) y posteriormente 
muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.
'''

from random import randint

lista1 = [randint(1,10) for i in range (10)]

print(lista1)
print("   Numeros      Cuadrado      Cubo")
for i in lista1:
    print(f'     {i}           {i*i}             {i*i*i}')


'''
Ejercicio 2
Se quiere realizar un programa que lea por teclado las 5 notas
obtenidas por un alumno (comprendidas entre 0 y 10). A continuación
debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
'''

calif = []
while len(calif) <= 4:
    n = int(input('Ingrese calificaión: '))
    if n < 0 or n > 10:
        print("Las calificaciones deben estan entre 0 y 10")
    elif n >= 0 and n <= 10:
        calif.append(n)
    else:
        print("Solo se aceptan números")

print(f'Calificaciones = {calif}')
print(f'Más alta = {max(calif)}')
print(f'Más baja = {min(calif)}')

'''
Ejercicio 3
Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector 
con datos leídos por el teclado. Copia los elementos del vector en otro vector 
pero en orden inverso, y muéstralo por la pantalla.
'''

palabras = [input("Ingresa la palabra: ") for i in range(5)]
inv = palabras[::-1]

print(palabras)
print(inv)
    

'''
Ejercicio 4
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y 
diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar un vector. 
Para simplificarlo vamos a suponer que febrero tiene 28 días.
'''

meses = ['Enero', 'Febrero', 'Marzo', 'Abirl', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
         'Octubre', 'Noviembre', 'Diciembre']

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30 , 31, 30, 31]

num = int(input("Ingresa un número del 1 al 12: "))

print(f"Numero: {num}, mes: {meses[num-1]}, días: {dias[-1]}")

'''
Ejercicio 5
Hacer un programa que inicialice un vector de números con valores aleatorios, 
y posterior ordene los elementos de menor a mayor
'''
from random import randint

lista5 = [randint(0,20) for i in range(randint(3,10))]
print(lista5)
lista5.sort()
print(lista5)