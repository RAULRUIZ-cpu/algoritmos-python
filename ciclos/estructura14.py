"""
Actualización de precios por inflación: Una lista de N productos tiene sus precios
actuales. La empresa aplicará un aumento del 5% a los productos que cuesten
menos de $100, un 8% a los que cuesten entre $100 y $500, y un 12% a los
mayores de $500. Imprime el costo anterior, el nuevo costo de cada producto y la
diferencia total sumada del ajuste.
"""
n = int(input("Cantidad de productos: "))
    diferencia_total = 0

    for i in range(1, n + 1):
        precio = float(input(f"Precio actual del producto {i}: $"))

        # Se selecciona el porcentaje de aumento según el precio original.
        if precio < 100:
            porcentaje = 0.05
        elif precio <= 500:
            porcentaje = 0.08
        else:
            porcentaje = 0.12

        aumento = precio * porcentaje
        nuevo_precio = precio + aumento
        diferencia_total += aumento

        print(f"Precio anterior: ${precio:.2f}")
        print(f"Nuevo precio: ${nuevo_precio:.2f}")
        print(f"Aumento aplicado: ${aumento:.2f}\n")

    print(f"Aumento total acumulado: ${diferencia_total:.2f}")
