'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
'''

# materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# print(materias)

'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
'''

# materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# for materia in materias:
#     print(f"Yo estudio {materia}")

'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has 
sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada 
una de las correspondientes notas introducidas por el usuario. 
'''

# materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# calificaciones = [float(input(f"Ingrese calificaión en {materia}: ")) for materia in materias]

# for i in range(len(materias)):
#     print(f"En {materias[i]} has sacado {calificaciones[i]}")

'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa 
debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificaciones = [float(input(f"Ingrese calificaión en {materia}: ")) for materia in materias]

for i in range(len(calificaciones)-1, -1, -1): 
    if calificaciones[i] >= 6:
        materias.remove(materias[i])

print(f"Materias a repetir {materias}")