"""
13. Control de producción por turnos: Una fábrica registra la cantidad de piezas
producidas por 3 turnos (Mañana, Tarde y Noche) a lo largo de 7 días. Acumula la
producción total de cada turno al final de la semana e indica cuál fue el turno más
productivo.
"""
DIAS = 7
produccion_manana = 0
produccion_tarde = 0
produccion_noche = 0

# Registrar producción por día y turno
for dia in range(1, DIAS + 1):
    print(f"\nDía {dia}:")
    manana = int(input("  Piezas turno Mañana: "))
    tarde = int(input("  Piezas turno Tarde: "))
    noche = int(input("  Piezas turno Noche: "))
    
    produccion_manana += manana
    produccion_tarde += tarde
    produccion_noche += noche

# Encontrar el turno más productivo
mayor = max(produccion_manana, produccion_tarde, produccion_noche)
if mayor == produccion_manana:
    turno_mayor = "Mañana"
elif mayor == produccion_tarde:
    turno_mayor = "Tarde"
else:
    turno_mayor = "Noche"

# Reporte
print("\n=== Producción Semanal ===")
print(f"Turno Mañana: {produccion_manana} piezas")
print(f"Turno Tarde : {produccion_tarde} piezas")
print(f"Turno Noche : {produccion_noche} piezas")
print(f"El turno más productivo fue: {turno_mayor} con {mayor} piezas")
