"""
Rendimiento de un vehículo por trayecto: En un viaje de 8 etapas, se registra la
distancia recorrida (en km) y el combustible consumido (en litros) de cada etapa.
Calcula el consumo promedio (km/l) de cada etapa, el total de km recorridos y el
rendimiento promedio total del viaje.
"""
distancia_total = 0
    combustible_total = 0

    for etapa in range(1, 9):
        distancia = float(input(f"Distancia de la etapa {etapa} en km: "))
        litros = float(input(f"Combustible de la etapa {etapa} en litros: "))

        distancia_total += distancia
        combustible_total += litros

        # El rendimiento se expresa en kilómetros por litro.
        if litros > 0:
            rendimiento = distancia / litros
            print(f"Rendimiento de la etapa {etapa}: {rendimiento:.2f} km/l")
        else:
            print("No se puede calcular el rendimiento: litros igual a cero.")

    # El rendimiento total se calcula con distancia total / litros totales.
    if combustible_total > 0:
        rendimiento_total = distancia_total / combustible_total
    else:
        rendimiento_total = 0

    print(f"\nDistancia total: {distancia_total:.2f} km")
    print(f"Combustible total: {combustible_total:.2f} litros")
    print(f"Rendimiento promedio total: {rendimiento_total:.2f} km/l")
