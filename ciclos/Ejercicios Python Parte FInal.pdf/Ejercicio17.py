"""
17. Tabla de amortización simplificada: Para un préstamo de valor 𝑃 diferido a 𝑀 meses,
calcula el pago de capital constante más un interés mensual fijo del 1.5% sobre el
saldo insoluto. Muestra la tabla mes a mes con la cuota a pagar y el saldo restante
"""
prestamo = float(input("Monto del préstamo: $"))
meses = int(input("¿A cuántos meses? "))
tasa_interes = 0.015  # 1.5% mensual

saldo_insoluto = prestamo
pago_capital = prestamo / meses  # Pago constante de capital

print(f"{'Mes':<6} {'Cuota':<15} {'Interés':<12} {'Capital':<12} {'Saldo Restante':<15}")
print("-" * 65)

for mes in range(1, meses + 1):
    interes = saldo_insoluto * tasa_interes
    cuota = pago_capital + interes
    saldo_restante = saldo_insoluto - pago_capital
    
    print(f"{mes:<6} ${cuota:<14.2f} ${interés:<11.2f} ${pago_capital:<11.2f} ${saldo_restante:<14.2f}")
    
    saldo_insoluto = saldo_restante

print(f"Total pagado: ${prestamo * (1 + tasa_interes * meses):.2f}")
