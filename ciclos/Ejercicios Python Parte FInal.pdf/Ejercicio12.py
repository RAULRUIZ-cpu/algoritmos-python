"""
12. Cálculo de comisión decreciente para vendedores: Un vendedor realiza 𝑁 ventas.
Por cada venta mayor a $1,500 obtiene una comisión del 10%; para ventas entre
$500 y $1,500 la comisión es del 5%, y para ventas menores a $500 no recibe
comisión. Determina el total percibido por comisiones y el monto de la mayor venta
realizada.
"""
n = int(input("¿Cuántas ventas se realizaron? "))

total_comisiones = 0.0
mayor_venta = 0.0

# Analizar cada venta
for i in range(1, n + 1):
    monto = float(input(f"Venta {i}: $"))
    
    # Detectar mayor venta
    if monto > mayor_venta:
        mayor_venta = monto
    
    # Calcular comisión según rango
    if monto > 1500:
        comision = monto * 0.10
    elif monto >= 500:
        comision = monto * 0.05
    else:
        comision = 0.0
    
    total_comisiones += comision
    print(f"  → Comisión: ${comision:.2f}")

# Reporte
print(f"Total percibido en comisiones: ${total_comisiones:.2f}")
print(f"La mayor venta realizada fue: ${mayor_venta:.2f}")
