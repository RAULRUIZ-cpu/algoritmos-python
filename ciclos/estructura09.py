"""
Simulador de pago de tarjeta de crédito: Una deuda inicial de $10,000 genera un
interés mensual del 2% sobre el saldo restante. Si el usuario realiza un pago fijo de
$1,000 cada mes, calcula mediante un ciclo en cuántos meses liquidará
completamente la deuda y cuánto pagó en total por concepto de intereses.
"""
deuda = 10000
    tasa_mensual = 0.02
    pago_fijo = 1000
    intereses_totales = 0
    meses = 0

    # Se repite hasta que el saldo quede liquidado.
    while deuda > 0:
        # Primero se agrega el interés mensual al saldo.
        interes = deuda * tasa_mensual
        deuda += interes
        intereses_totales += interes
        meses += 1

        # El último pago se ajusta para no pagar más de lo que se debe.
        pago = min(pago_fijo, deuda)
        deuda -= pago

        print(f"Mes {meses}: interes ${interes:.2f}, pago ${pago:.2f}, saldo ${deuda:.2f}")

    print(f"\nLa deuda se liquido en {meses} meses.")
    print(f"Total pagado por intereses: ${intereses_totales:.2f}")
