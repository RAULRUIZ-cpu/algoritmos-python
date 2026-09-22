"""
El director de una escuela está organizando un viaje de estudios y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.

La forma de cobrar es la siguiente:

Si son 100 alumnos o más, el costo por cada alumno es de $65.00.
De 50 a 99 alumnos, el costo es de $70.00.
De 30 a 49 alumnos, el costo es de $95.00.
Si son menos de 30 alumnos, el costo de la renta del autobús es de $4000.00, sin importar el número de alumnos.
alumnos = int(input("Ingresa el número de alumnos: "))

if alumnos >= 100:
    costo_alumno = 65
    total = alumnos * costo_alumno

elif alumnos >= 50:
    costo_alumno = 70
    total = alumnos * costo_alumno

elif alumnos >= 30:
    costo_alumno = 95
    total = alumnos * costo_alumno

else:
    total = 4000
    costo_alumno = total / alumnos

print("Costo por alumno: $", costo_alumno)
print("Total a pagar: $", total)
"""
