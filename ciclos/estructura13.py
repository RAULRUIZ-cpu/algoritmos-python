"""
Control de producción por turnos: Una fábrica registra la cantidad de piezas
producidas por 3 turnos (Mañana, Tarde y Noche) a lo largo de 7 días. Acumula la
producción total de cada turno al final de la semana e indica cuál fue el turno más
productivo.
"""
manana = tarde = noche = 0

    # Cada día se registra la producción de los tres turnos.
    for dia in range(1, 8):
        print(f"\n--- Dia {dia} ---")
        produccion_manana = int(input("Piezas del turno de mañana: "))
        produccion_tarde = int(input("Piezas del turno de tarde: "))
        produccion_noche = int(input("Piezas del turno de noche: "))

        manana += produccion_manana
        tarde += produccion_tarde
        noche += produccion_noche

    print("\n--- PRODUCCION SEMANAL ---")
    print(f"Mañana: {manana} piezas")
    print(f"Tarde: {tarde} piezas")
    print(f"Noche: {noche} piezas")

    # Se compara la producción acumulada de los tres turnos.
    mayor = max(manana, tarde, noche)
    if manana == mayor:
        print("El turno de mañana fue uno de los mas productivos.")
    if tarde == mayor:
        print("El turno de tarde fue uno de los mas productivos.")
    if noche == mayor:
        print("El turno de noche fue uno de los mas productivos.")
