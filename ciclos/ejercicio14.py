"""
Un empleado de la tienda “Tiki Taka” realiza N ventas
durante el día, se requiere saber cuántas de ellas fueron
mayores a $1000, cuántas fueron mayores a $500 pero
menores o iguales a $1000, y cuántas fueron menores o
iguales a $500. Además, se requiere saber el monto de lo
vendido en cada categoría y de forma global. Realice un
algoritmo que permita determinar lo anterior
"""
# Pedir la cantidad de ventas del día
n = int(input("¿Cuántas ventas se realizaron hoy? "))

# Inicializar contadores y acumuladores
mayor_1000_cant = 0
mayor_500_cant = 0   # >500 y ≤1000
menor_igual_500_cant = 0

mayor_1000_monto = 0.0
mayor_500_monto = 0.0
menor_igual_500_monto = 0.0

print("\nRegistro de ventas - Tienda Tiki Taka")
print("-" * 50)

# Procesar cada venta
for i in range(1, n + 1):
    monto = float(input(f"Monto de la venta {i}: $"))
    
    if monto > 1000:
        mayor_1000_cant += 1
        mayor_1000_monto += monto
    elif monto > 500:  # Aquí entra: >500 y ≤1000
        mayor_500_cant += 1
        mayor_500_monto += monto
    else:  # ≤500
        menor_igual_500_cant += 1
        menor_igual_500_monto += monto

# Calcular el total global
total_ventas = mayor_1000_monto + mayor_500_monto + menor_igual_500_monto

# Mostrar resultados
print("-" * 50)
print("📋 RESUMEN DE VENTAS DEL DÍA")
print("-" * 50)
print(f"Ventas mayores a $1000:")
print(f"  → Cantidad: {mayor_1000_cant} | Monto total: ${mayor_1000_monto:.2f}")
print(f"Ventas mayores a $500 y hasta $1000:")
print(f"  → Cantidad: {mayor_500_cant} | Monto total: ${mayor_500_monto:.2f}")
print(f"Ventas menores o iguales a $500:")
print(f"  → Cantidad: {menor_igual_500_cant} | Monto total: ${menor_igual_500_monto:.2f}")
print("-" * 50)
print(f"💰 TOTAL VENDIDO EN EL DÍA: ${total_ventas:.2f}")
