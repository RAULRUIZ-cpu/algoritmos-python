"""
Estadística de edades por rangos: En una encuesta aplicada a N personas, se
registra la edad de cada participante. Clasifica y cuenta cuántas personas son niños
(0-12 años), adolescentes (13-17 años), adultos (18-59 años) y adultos mayores (60
años o más).
"""
n = int(input("Cantidad de personas encuestadas: "))
    ninos = adolescentes = adultos = adultos_mayores = 0

    for i in range(1, n + 1):
        edad = int(input(f"Edad de la persona {i}: "))

        # Se clasifica cada edad dentro de un solo rango.
        if edad < 0:
            print("Edad no valida; no se contabiliza.")
        elif edad <= 12:
            ninos += 1
        elif edad <= 17:
            adolescentes += 1
        elif edad <= 59:
            adultos += 1
        else:
            adultos_mayores += 1

    print(f"\nNiños: {ninos}")
    print(f"Adolescentes: {adolescentes}")
    print(f"Adultos: {adultos}")
    print(f"Adultos mayores: {adultos_mayores}")
