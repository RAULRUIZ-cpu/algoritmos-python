"""
18. Análisis de velocidad de vehículo (Multas y promedios): Un radar registra la
velocidad de 12 vehículos en una carretera donde el límite es 90 km/h. Cuenta
cuántos vehículos iban dentro del límite y cuántos cometieron infracción. De los
infractores, indica cuántos superaban los 110 km/h (multa grave).
"""
VEHICULOS = 12
LIMITE = 90
LIMITE_GRAVE = 110

dentro_limite = 0
infraccion_leve = 0
infraccion_grave = 0

# Registrar cada velocidad
for i in range(1, VEHICULOS + 1):
    velocidad = float(input(f"Vehículo {i} - Velocidad registrada (km/h): "))
    if velocidad <= LIMITE:
        dentro_limite += 1
    elif velocidad <= LIMITE_GRAVE:
        infraccion_leve += 1
    else:
        infraccion_grave += 1

# Reporte
print(f"Vehículos dentro del límite ({LIMITE} km/h): {dentro_limite}")
print(f"Vehículos con infracción leve (91-{LIMITE_GRAVE} km/h): {infraccion_leve}")
print(f"Vehículos con infracción GRAVE (>{LIMITE_GRAVE} km/h): {infraccion_grave}")
print(f"TOTAL DE VEHÍCULOS REVISADOS: {VEHICULOS}")
