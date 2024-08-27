'''
Ejercicio 6
Programa que declare un vector de diez elementos enteros y pida números 
para rellenarlo hasta que se llene el vector o se introduzca un número 
negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
'''

# l = []
# try:
#     while len(l) < 10:
#         n = int(input("Agrega un entero: "))
#         if n < 0:
#             raise ValueError("El número no puede ser negativo")
#         else:
#             l.append(n)
    
# except ValueError as e:
#     print(f"Error: {e}, prueba de nuevo")

# finally:
#     print(l)

'''
Ejercicio 7
Queremos guardar los nombres y la edades de los alumnos de un curso. 
Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura 
de datos terminará cuando se introduzca como nombre un asterisco (*) 
Al finalizar se mostrará los siguientes datos:

   * Todos lo alumnos mayores de edad.
   * Los alumnos mayores (los que tienen más edad)
'''

# students = {}

# while True:

#     name = input("Nombre o '*' para terminar: ")
    
#     if name == "*":
#         break
#     try:
#         age = int(input("Edad: "))
#         students[name] = age
#     except ValueError:
#         print("Edad no válida")

# print(students)

# print("\nMayores de edad: ")
# for name, age in students.items():
#     if age >= 18:
#         print(f"{name}, edad: {age}")

# if students:
#     max_age = max(students.values())
    
#     print("\nAlumnos mayores:")
#     for name,age in students.items():
#         if age == max_age:
#             print(f"Nombre: {name}, Edad: {age}")
# else:
#     print("No hay alumnos registrados")

'''
Ejercicio 8
Calcule la superficie de un terreno que le corresponde a un heredero 
después de n generaciones, partiendo de una superficie inicial en la generación cero.
Se supone que hay división a partes iguales entre herederos y que el número máximo 
de generaciones con que trabajará el programa es 50. Los datos de superficie inicial, 
número de generaciones y número de herederos por generación se deben solicitar al usuario del programa.
'''

# print("***Cálculo superficie heredero***")
# g = int(input("Indique el número de generaciones (Máximo 50): "))
# if g< 0 or g > 50:
#     raise ValueError("El número máximo es 50 y mínimo 1")

# s = float(input("Indique la superficie inicial: "))

# for i in range (g):
#     h = int(input(f"Indique el número de herederos de la generación {i+1}: "))
#     s /= h

# print(f"La superficie para la generación {g} es de {s}")

'''
Ejercicio 9
De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, 
y los kilómetros que conducen cada día de la semana.

Para guardar esta información se van a utilizar dos arreglos:

Nombre: Vector para guardar los nombres de los conductores.
kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar un nuevo vector (“total_kms”) con los kilómetros totales que realza cada conductor.

Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
'''

# nombres = []
# kms = []

# def calcular_kms_totales(kms):
#     total_kms = [sum(dia) for dia in kms]
#     return total_kms

# conductores = int(input("Numero de conductores: "))

# for conductor in range(conductores):
#     nombre = input(f"Introduce el nombre del conductor {conductor+1}: ")
#     nombres.append(nombre)

#     km_dia = []
#     for dia in range(7):
#         km = float(input(f"Introduce los kms conducidos por {nombre} en el día {dia+1}: "))
#         km_dia.append(km)

#     kms.append(km_dia)


# total_kms = calcular_kms_totales(kms)

# print("Resumen")
# for i in range(conductores):
#     print(f"{nombres[i]}: {total_kms[i]:.2f} km")

'''
Ejercicio 10
Crear un programa que lea los precios de 5 artículos y las cantidades vendidas 
por una empresa en sus 4 sucursales. Informar:

Las cantidades totales de cada articulo.
La cantidad de artículos en la sucursal 2.
La cantidad del articulo 3 en la sucursal 1.
La recaudación total de cada sucursal.
La recaudación total de la empresa.
La sucursal de mayor recaudación.
'''

# def getData():

#     precios = [float(input(f"Introduce el precio del artículo {i+1}: ")) for i in range(5)]

#     cantidades = []
#     for i in range (4):
#         print(f"\nIngresa las cantidades vendidas por la sucursal {i+1}: ")
#         cantidades_sucursal = []
#         for articulo in range(5):
#             cantidad = int(input(f"Ingresa la cantidad del artículo {articulo+1}: "))
#             cantidades_sucursal.append(cantidad)
#         cantidades.append(cantidades_sucursal)
    
#     return precios, cantidades

# def cantidades_por_articulo(cantidades):
#     articulos_totales = []

#     for i in cantidades:
#         sucursal = 0    
#         for j in i:
#             sucursal += j
#         articulos_totales.append(sucursal)
        
#     return articulos_totales

# def articulos_sucursal2(cantidades):
#     return sum(cantidades[1])
    
# def get_articulo3_sucursal1(cantidades):
#     return cantidades[0][2]

# def recaudacion_total_por_sucursal(cantidades, precios):
#     lista_total = []

#     for tienda in cantidades:
#         total_sucursal = 0
#         for j in tienda:
#             item = j*precios[j]
#             total_sucursal += item


#         lista_total.append(total_sucursal)
#     return lista_total

# def recaudacion_empresa(func, cantidades, precios):
#     sucursales = func(cantidades, precios)
#     return sum(sucursales)

# def sucursal_mayor_recaudacion(func, cantidades, precios):
#     sucursales = func(cantidades, precios)
#     ganancia_max = max(sucursales)
#     mayores = []
#     for i in range(4):
#         if sucursales[i] == ganancia_max:
#             mayores.append(i+1)
#     return mayores, ganancia_max

    
# precios, cantidades = getData()
# print(f"Artículos por sucursal: {cantidades}, Precios: {precios} ")

# articulos_totales  = cantidades_por_articulo(cantidades)
# print(f"Articulos totales por sucursal: {articulos_totales}")

# articulos_totales_sucursal2 = articulos_sucursal2(cantidades)
# print(f"Articulos totales en sucursal 2: {articulos_totales_sucursal2}")

# articulo3_sucursal1 = get_articulo3_sucursal1(cantidades)
# print(f"Hay {articulo3_sucursal1} unidades del artículo 3 en la sucursal ")

# total_por_sucursal = recaudacion_total_por_sucursal(cantidades, precios)
# print(f"Recaudación total por sucursal: {total_por_sucursal}")

# total_empresa = recaudacion_empresa(recaudacion_total_por_sucursal, cantidades, precios)
# print(f"Total recaudado por la empresa {total_empresa}")

# sucursal_max, ganancia_max = sucursal_mayor_recaudacion(recaudacion_total_por_sucursal, cantidades, precios)
# print(f"Sucursal o sucursales con más ganancias: {sucursal_max} con un total de {ganancia_max}")

'''
Ejercicio 11
Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. 
Para ello vamos a utilizar dos tablas:

Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos 
de cada partido. En la quiniela se indican 15 partidos.
Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, 
en la primera se guarda el número de goles del equipo que está guardado en la primera columna 
de la tabla anterior, y en la segunda los goles del otro equipo.
El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, 
a continuación se imprimirá la quiniela de esa jornada.
'''

# equipos = [["" for _ in range(2)] for _ in range(15)]
# resultados = [[0, 0] for _ in range(15)]

# print("Bienvenido al gestor de quiniela de fútbol.")
# print("Ingresa los nombres de los equipos y los resultados de cada partido.")

# for i in range(15):
#     print(f"\nPartido {i + 1}:")
#     equipo1 = input("Nombre del primer equipo: ")
#     equipo2 = input("Nombre del segundo equipo: ")
#     goles_equipo1 = int(input(f"Resultado del {equipo1}: "))
#     goles_equipo2 = int(input(f"Resultado del {equipo2}: "))
    
#     equipos[i][0] = equipo1
#     equipos[i][1] = equipo2
#     resultados[i][0] = goles_equipo1
#     resultados[i][1] = goles_equipo2

# print("\nQuiniela de la jornada:")
# for i in range(15):
#     equipo1, equipo2 = equipos[i]
#     goles_equipo1, goles_equipo2 = resultados[i]
#     print(f"Partido {i + 1}: {equipo1} {goles_equipo1} - {goles_equipo2} {equipo2}")

