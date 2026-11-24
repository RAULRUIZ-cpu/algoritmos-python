"""
20. Procesamiento de facturas vencidas: Un departamento de cobranza procesa 𝑁
facturas. Por cada una se lee el monto original y los días de retraso. Si los días de
retraso son mayores a 30, se le aplica un recargo del 5%; si son mayores a 60 días,
el recargo es del 12%. Muestra el importe corregido de cada factura y el monto
acumulado por penalizaciones.
"""
cantidad = int(input("¿Cuántas facturas tenemos que checar? "))

total_multas = 0

# Vamos una por una
for i in range(1, cantidad + 1):
    print(f"\n--- Factura #{i} ---")
    monto = float(input("¿Cuánto era de la factura originalmente? $"))
    dias = int(input("¿Cuántos días se atrasaron? "))

    # Según cuánto se atrasó, le ponemos el recargo
    if dias > 60:
        recargo = 0.12  # Bastante tiempo atrasado, más caro
        print("Uy, más de 60 días → 12% de recargo")
    elif dias > 30:
        recargo = 0.05  # Un poco de retraso, cobramos poquito más
        print("Más de 30 días → 5% de recargo")
    else:
        recargo = 0  # Aún está a tiempo, sin cobrar de más
        print("Sin recargo ✅")

    # Hacemos las cuentas
    monto_extra = monto * recargo
    total_final = monto + monto_extra
    total_multas += monto_extra

    # Le decimos al usuario cuánto debe en realidad
    print(f"Original: ${monto:.2f} | Recargo: ${monto_extra:.2f} → TOTAL A PAGAR: ${total_final:.2f}")

# Al final mostramos cuánto se juntó en recargos
print(f"En total cobramos ${total_multas:.2f} solo en recargos")
