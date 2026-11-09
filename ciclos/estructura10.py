"""
Evaluación de grupo académico (Aprobados, Reprobados y Excelencia): Lee las
calificaciones finales de N estudiantes de un curso. Clasifícalos en tres categorías:

Reprobados (< 6. 0), Aprobados (6. 0 a 8. 9) y Excelencia (9. 0 a 10. 0). Muestra la
cantidad de alumnos por categoría y el promedio general del grupo.
"""
n = int(input("Cantidad de estudiantes: "))
    reprobados = aprobados = excelencia = 0
    suma_calificaciones = 0

    for i in range(1, n + 1):
        calificacion = float(input(f"Calificacion del estudiante {i}: "))

        # Se valida que la calificación esté en la escala de 0 a 10.
        if calificacion < 0 or calificacion > 10:
            print("Calificacion fuera de rango; no se contabiliza.")
            continue

        suma_calificaciones += calificacion

        if calificacion < 6:
            reprobados += 1
        elif calificacion < 9:
            aprobados += 1
        else:
            excelencia += 1

    # Se usa el número de calificaciones válidas para el promedio.
    validos = reprobados + aprobados + excelencia
    promedio = suma_calificaciones / validos if validos > 0 else 0

    print(f"\nReprobados: {reprobados}")
    print(f"Aprobados: {aprobados}")
    print(f"Excelencia: {excelencia}")
    print(f"Promedio general: {promedio:.2f}")
