"""
Una empresa tiene el registro de las horas que trabaja
diariamente un empleado durante la semana (seis días) y
requiere determinar el total de éstas, así como el sueldo
que recibirá por las horas trabajadas
"""
# Pedir el pago por hora
tarifa_hora = float(input("Ingresa el pago por hora trabajada ($): "))

horas_totales = 0

print("\nRegistro de horas - Semana (6 días)")
print("-" * 40)

# Leer horas de cada uno de los 6 días
for dia in range(1, 7):
    horas = float(input(f"Horas trabajadas el día {dia}: "))
    horas_totales += horas

# Calcular sueldo
sueldo = horas_totales * tarifa_hora

# Mostrar resultados
print("-" * 40)
print(f" Total de horas trabajadas: {horas_totales:.2f} horas")
print(f" Sueldo a recibir: ${sueldo:.2f}")
