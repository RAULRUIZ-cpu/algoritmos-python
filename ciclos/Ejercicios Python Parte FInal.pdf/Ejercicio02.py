"""
2. Categorización de ventas con montos acumulados: Procesa 𝑁 ventas realizadas en
un negocio. El programa debe determinar cuántas ventas fueron menores o iguales
a $300, cuántas entre $301 y $800, y cuántas mayores a $800. Debe mostrar la
cantidad de ventas y el monto total recaudado en cada categoría, además del total
general.
"""
# Cantidad de ventas a registrar
n = int(input("¿Cuántas ventas deseas registrar? "))

# Inicializar contadores y acumuladores
cant_bajo = 0
cant_medio = 0
cant_alto = 0
total_bajo = 0.0
total_medio = 0.0
total_alto = 0.0

# Procesar cada venta
for i in range(1, n + 1):
    monto = float(input(f"Venta {i}: $"))
    if monto <= 300:
        cant_bajo += 1
        total_bajo += monto
    elif monto <= 800:
        cant_medio += 1
        total_medio += monto
    else:
        cant_alto += 1
        total_alto += monto

# Calcular total general
total_general = total_bajo + total_medio + total_alto

# Mostrar reporte
print(f"≤ $300     : {cant_bajo} ventas | Total: ${total_bajo:.2f}")
print(f"$301 - $800: {cant_medio} ventas | Total: ${total_medio:.2f}")
print(f"> $800     : {cant_alto} ventas | Total: ${total_alto:.2f}")
print(f"VENTAS TOTALES: ${total_general:.2f}")
