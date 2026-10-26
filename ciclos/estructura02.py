"""
Categorización de ventas con montos acumulados: Procesa 𝑁 ventas realizadas en
un negocio. El programa debe determinar cuántas ventas fueron menores o iguales
a $300, cuántas entre $301 y $800, y cuántas mayores a $800. Debe mostrar la
cantidad de ventas y el monto total recaudado en cada categoría, además del total
general
"""
# Pedir la cantidad de ventas
n = int(input("Cantidad de ventas: "))

# Inicializar contadores y acumuladores
cant1 = cant2 = cant3 = 0
total1 = total2 = total3 = 0

# Leer el monto de cada venta
for i in range(1, n + 1):
    venta = float(input(f"Monto de la venta {i}: $"))

    # Clasificar las ventas por monto
    if venta <= 300:
        cant1 += 1
        total1 += venta
    elif venta <= 800:
        cant2 += 1
        total2 += venta
    else:
        cant3 += 1
        total3 += venta

# Mostrar las cantidades y los montos
print("Ventas de $300 o menos:", cant1, "Total: $", total1)
print("Ventas de $301 a $800:", cant2, "Total: $", total2)
print("Ventas mayores a $800:", cant3, "Total: $", total3)
print("Total general: $", total1 + total2 + total3)
