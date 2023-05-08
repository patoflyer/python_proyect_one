print("Bienvenido al programa de cálculo de promedio y calificaciones")
nombre_alumno = input("Por favor, ingrese el nombre del alumno: ")

materias = ["Matemáticas", "Español", "Historia", "Ciencias", "Inglés", "Educación Física"]
califica = []

for materia in materias:
    calificacion = float(input(f"Ingrese la calificación en {materia}: "))
    califica.append(calificacion)

promedio = sum(califica) / len(califica)

max_calificacion = max(califica)
max_materia = materias[califica.index(max_calificacion)]

min_calificacion = min(califica)
min_materia = materias[califica.index(min_calificacion)]

print(f"El promedio de las calificaciones de {nombre_alumno} es {promedio:.2f}")
print(f"La materia con la calificación más alta es {max_materia} con una calificación de {max_calificacion}")
print(f"La materia con la calificación más baja es {min_materia} con una calificación de {min_calificacion}")