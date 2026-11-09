"""
Consumo de energía eléctrica y tarifas por escalón: Se registra el consumo de luz en
kWh durante 6 bimestres. Si el consumo en un bimestre es menor o igual a 250
kWh, la tarifa es de $1.5 por kWh; si supera los 250 kWh, el exceso se cobra a $2.8
por kWh. Muestra el importe a pagar en cada bimestre y el gasto anual total.
"""
gasto_total = 0

    for bimestre in range(1, 7):
        consumo = float(input(f"Consumo del bimestre {bimestre} en kWh: "))

        # Los primeros 250 kWh conservan la tarifa de $1.50.
        if consumo <= 250:
            importe = consumo * 1.50
        else:
            # Solo el consumo que excede los 250 kWh usa la tarifa alta.
            importe = (250 * 1.50) + ((consumo - 250) * 2.80)

        gasto_total += importe
        print(f"Importe del bimestre {bimestre}: ${importe:.2f}")

    print(f"\nGasto total de los seis bimestres: ${gasto_total:.2f}")
