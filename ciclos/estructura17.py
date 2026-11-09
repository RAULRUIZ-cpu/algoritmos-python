"""
Tabla de amortización simplificada: Para un préstamo de valor P diferido a M meses,
calcula el pago de capital constante más un interés mensual fijo del 1.5% sobre el
saldo insoluto. Muestra la tabla mes a mes con la cuota a pagar y el saldo restante.
"""
prestamo = float(input("Valor del prestamo: $"))
    meses = int(input("Plazo en meses: "))

    # El capital se divide en partes iguales para todos los meses.
    if meses <= 0:
        print("El plazo debe ser mayor que cero.")
        return

    abono_capital = prestamo / meses
    saldo = prestamo
    tasa = 0.015

    print("\nMES | CAPITAL | INTERES | CUOTA | SALDO RESTANTE")

    for mes in range(1, meses + 1):
        # El interés se calcula sobre el saldo antes de abonar capital.
        interes = saldo * tasa
        cuota = abono_capital + interes
        saldo -= abono_capital

        # Se corrigen pequeños residuos decimales en el último mes.
        if mes == meses:
            saldo = 0

        print(f"{mes:>3} | ${abono_capital:>8.2f} | ${interes:>7.2f} | "
              f"${cuota:>8.2f} | ${saldo:>10.2f}")
