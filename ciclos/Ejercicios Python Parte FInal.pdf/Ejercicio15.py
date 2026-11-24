"""
15. Consumo de energía eléctrica y tarifas por escalón: Se registra el consumo de luz en
kWh durante 6 bimestres. Si el consumo en un bimestre es menor o igual a 250
kWh, la tarifa es de $1.5 por kWh; si supera los 250 kWh, el exceso se cobra a $2.8
por kWh. Muestra el importe a pagar en cada bimestre y el gasto anual total.
"""
BIMESTRES = 6
total_anual = 0.0

print("=== Consumo Bimestral de Energía ===")
for bimestre in range(1, BIMESTRES + 1):
    consumo = float(input(f"Bimestre {bimestre} - Consumo en kWh: "))
    
    # Calcular importe con tarifa escalonada
    if consumo <= 250:
        importe = consumo * 1.5
    else:
        importe = 250 * 1.5 + (consumo - 250) * 2.8
    
    total_anual += importe
    print(f"  → Importe a pagar: ${importe:.2f}\n")

# Reporte final
print(f"Gasto TOTAL ANUAL de energía: ${total_anual:.2f}")
