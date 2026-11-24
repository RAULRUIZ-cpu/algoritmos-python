"""
10. Evaluación de grupo académico (Aprobados, Reprobados y Excelencia): Lee las
calificaciones finales de 𝑁 estudiantes de un curso. Clasifícalos en tres categorías:
Reprobados (< 6. 0), Aprobados (6. 0 a 8. 9) y Excelencia (9. 0 a 10. 0). Muestra la
cantidad de alumnos por categoría y el promedio general del grupo.
"""
n = int(input("¿Cuántos estudiantes hay en el grupo? "))

reprobados = 0
aprobados = 0
excelencia = 0
suma_calif = 0.0

# Registrar cada calificación
for i in range(1, n + 1):
    calif = float(input(f"Estudiante {i} - Calificación: "))
    suma_calif += calif
    if calif < 6.0:
        reprobados += 1
    elif calif <= 8.9:
        aprobados += 1
    else:
        excelencia += 1

# Cálculos
promedio_grupo = suma_calif / n

# Reporte
print(f"Reprobados : {reprobados}")
print(f"Aprobados  : {aprobados}")
print(f"Excelencia : {excelencia}")
print(f"Promedio general del grupo: {promedio_grupo:.2f}")

