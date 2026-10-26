"""
Simulación de nómina semanal con horas extras: Pide las horas trabajadas cada día
durante 6 días por un empleado. Si en un día supera las 8 horas, las horas
adicionales se pagan al doble de la tarifa normal por hora. Calcula el sueldo total
semanal y el número total de horas extras trabajadas.
"""
# Declarar las variables
horas_totales = 0
horas_extras = 0
sueldo_total = 0

# Pedir el pago por hora
tarifa = float(input("Pago por hora: $"))

# Repetir durante 6 dias
for dia in range(1, 7):
    horas = float(input(f"Horas trabajadas el dia {dia}: "))

    # Calcular las horas normales y extras
    if horas > 8:
        horas_extras += horas - 8
        sueldo_total += 8 * tarifa + (horas - 8) * tarifa * 2
    else:
        sueldo_total += horas * tarifa

    # Acumular las horas trabajadas
    horas_totales += horas

# Mostrar los resultados
print("Horas trabajadas:", horas_totales)
print("Horas extras:", horas_extras)
print("Sueldo semanal: $", sueldo_total)
