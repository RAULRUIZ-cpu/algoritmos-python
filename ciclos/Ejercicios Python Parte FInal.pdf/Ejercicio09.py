"""
9. Simulador de pago de tarjeta de crédito: Una deuda inicial de $10,000 genera un
interés mensual del 2% sobre el saldo restante. Si el usuario realiza un pago fijo de
$1,000 cada mes, calcula mediante un ciclo en cuántos meses liquidará
completamente la deuda y cuánto pagó en total por concepto de intereses
"""
deuda = 10000.0
tasa_interes = 0.02
pago_mensual = 1000.0
meses = 0
total_intereses = 0.0

print("=== Tabla de Pagos Mensuales ===")
print(f"Mes | Saldo Inicial | Interés | Pago | Saldo Final")
print("-" * 60)

# Ciclo de pagos
while deuda > 0:
    meses += 1
    interes = deuda * tasa_interes
    total_intereses += interes
    saldo_inicial = deuda
    
    # Calcular pago real (último mes puede ser menor)
    if saldo_inicial + interes <= pago_mensual:
        pago_real = saldo_inicial + interes
        deuda = 0
    else:
        pago_real = pago_mensual
        deuda = saldo_inicial + interes - pago_real
    
    print(f"{meses:3} | ${saldo_inicial:12.2f} | ${interés:7.2f} | ${pago_real:6.2f} | ${deuda:11.2f}")

# Reporte final
print(f"\nLa deuda se liquidó en {meses} meses")
print(f"Total pagado en intereses: ${total_intereses:.2f}")
print(f"Total pagado: ${10000 + total_intereses:.2f}")
