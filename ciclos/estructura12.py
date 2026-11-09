"""
Cálculo de comisión decreciente para vendedores: Un vendedor realiza N ventas.
Por cada venta mayor a $1,500 obtiene una comisión del 10%; para ventas entre
$500 y $1,500 la comisión es del 5%, y para ventas menores a $500 no recibe
comisión. Determina el total percibido por comisiones y el monto de la mayor venta
realizada.
"""
n = int(input("Cantidad de ventas realizadas: "))
    comision_total = 0
    venta_mayor = 0

    for i in range(1, n + 1):
        venta = float(input(f"Monto de la venta {i}: $"))

        # Se actualiza el registro de la venta más alta.
        if venta > venta_mayor:
            venta_mayor = venta

        # Se determina el porcentaje de comisión correspondiente.
        if venta > 1500:
            comision = venta * 0.10
        elif venta >= 500:
            comision = venta * 0.05
        else:
            comision = 0

        comision_total += comision
        print(f"Comision de esta venta: ${comision:.2f}")

    print(f"\nTotal percibido por comisiones: ${comision_total:.2f}")
    print(f"Monto de la mayor venta: ${venta_mayor:.2f}")
