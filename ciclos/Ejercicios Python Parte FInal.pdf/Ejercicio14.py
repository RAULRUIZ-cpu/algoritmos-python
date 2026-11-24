"""
14. Actualización de precios por inflación: Una lista de 𝑁 productos tiene sus precios
actuales. La empresa aplicará un aumento del 5% a los productos que cuesten
menos de $100, un 8% a los que cuesten entre $100 y $500, y un 12% a los
mayores de $500. Imprime el costo anterior, el nuevo costo de cada producto y la
diferencia total sumada del ajuste.
"""
n = int(input("¿Cuántos productos deseas actualizar? "))

diferencia_total = 0.0

print("\n=== Actualización de Precios ===")
print(f"{'Producto':<10} {'Precio Anterior':<18} {'Precio Nuevo':<15} {'Diferencia':<12}")
print("-" * 60)

# Procesar cada producto
for i in range(1, n + 1):
    precio_anterior = float(input(f"Producto {i} - Precio actual: $"))
    
    # Determinar porcentaje de aumento
    if precio_anterior < 100:
        aumento = 0.05
    elif precio_anterior <= 500:
        aumento = 0.08
    else:
        aumento = 0.12
    
    # Cálculos
    incremento = precio_anterior * aumento
    precio_nuevo = precio_anterior + incremento
    diferencia_total += incremento
    
    print(f"{i:<10} ${precio_anterior:<17.2f} ${precio_nuevo:<14.2f} ${incremento:<11.2f}")

print(f"Suma total del ajuste de precios: ${diferencia_total:.2f}")
