"""
1. Simulación de nómina semanal con horas extras: Pide las horas trabajadas cada día
durante 6 días por un empleado. Si en un día supera las 8 horas, las horas
adicionales se pagan al doble de la tarifa normal por hora. Calcula el sueldo total
semanal y el número total de horas extras trabajadas.
"""
# Definir tarifa normal 
tarifa_normal = float(input("Ingresa la tarifa normal por hora: $"))

# Inicializar acumuladores
total_horas_extras = 0
sueldo_total = 0

# Ciclo para 6 días de trabajo
for dia in range(1, 7):
    horas = float(input(f"Día {dia} - Horas trabajadas: "))
    
    # Clasificar horas normales y extras
    if horas > 8:
        horas_normales = 8
        horas_extras = horas - 8
        total_horas_extras += horas_extras
    else:
        horas_normales = horas
        horas_extras = 0
    
    # Calcular pago del día
    pago_dia = horas_normales * tarifa_normal + horas_extras * tarifa_normal * 2
    sueldo_total += pago_dia

# Mostrar resultados
print(f"Total horas extras: {total_horas_extras:.2f}")
print(f"Sueldo total a pagar: ${sueldo_total:.2f}")
