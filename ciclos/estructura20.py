"""
Procesamiento de facturas vencidas: Un departamento de cobranza procesa N
facturas. Por cada una se lee el monto original y los días de retraso. Si los días de
retraso son mayores a 30, se le aplica un recargo del 5%; si son mayores a 60 días,
el recargo es del 12%. Muestra el importe corregido de cada factura y el monto
acumulado por penalizaciones.
"""
n = int(input("Cantidad de facturas: "))
    penalizaciones_total = 0

    for i in range(1, n + 1):
        monto = float(input(f"Monto original de la factura {i}: $"))
        dias = int(input("Dias de retraso: "))

        # Se evalúa primero el rango mayor para aplicar el recargo correcto.
        if dias > 60:
            porcentaje = 0.12
        elif dias > 30:
            porcentaje = 0.05
        else:
            porcentaje = 0

        penalizacion = monto * porcentaje
        importe_corregido = monto + penalizacion
        penalizaciones_total += penalizacion

        print(f"Penalizacion: ${penalizacion:.2f}")
        print(f"Importe corregido: ${importe_corregido:.2f}\n")

    print(f"Total acumulado por penalizaciones: ${penalizaciones_total:.2f}")
