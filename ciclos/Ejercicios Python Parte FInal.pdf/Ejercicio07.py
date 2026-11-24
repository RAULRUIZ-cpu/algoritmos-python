"""
7. Registro de temperaturas extremas y promedios: Registra las temperaturas máximas
de cada día del mes (30 días). Determina cuál fue la temperatura más alta
registrada, la más baja y calcula el promedio mensual de temperatura.
"""
DIAS = 30
suma_temp = 0.0
temp_max = -999.0
temp_min = 999.0

# Leer cada temperatura
for dia in range(1, DIAS + 1):
    temp = float(input(f"Día {dia} - Temperatura máxima (°C): "))
    suma_temp += temp
    if temp > temp_max:
        temp_max = temp
    if temp < temp_min:
        temp_min = temp

# Calcular promedio
promedio = suma_temp / DIAS

# Reporte
print(f"Temperatura más alta: {temp_max:.1f}°C")
print(f"Temperatura más baja: {temp_min:.1f}°C")
print(f"Promedio mensual    : {promedio:.1f}°C")
