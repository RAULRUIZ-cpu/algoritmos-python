"""
8. Rendimiento de un vehículo por trayecto: En un viaje de 8 etapas, se registra la
distancia recorrida (en km) y el combustible consumido (en litros) de cada etapa.
Calcula el consumo promedio (km/l) de cada etapa, el total de km recorridos y el
rendimiento promedio total del viaje.
"""
ETAPAS = 8
total_km = 0.0
total_litros = 0.0

print("=== Consumo por Etapa ===")
for etapa in range(1, ETAPAS + 1):
    km = float(input(f"Etapa {etapa} - Distancia en km: "))
    litros = float(input(f"Etapa {etapa} - Combustible en litros: "))
    consumo = km / litros
    print(f"  → Consumo etapa {etapa}: {consumo:.2f} km/l\n")
    total_km += km
    total_litros += litros

# Cálculos finales
rendimiento_total = total_km / total_litros

# Reporte
print(f"Distancia total recorrida: {total_km:.2f} km")
print(f"Combustible total consumido: {total_litros:.2f} L")
print(f"Rendimiento promedio total: {rendimiento_total:.2f} km/l")
