"""
Inventario y conteo por tipo de producto: En una bodega hay un lote de N artículos
clasificados por su tipo mediante un código (1: Electrónica, 2: Ropa, 3: Alimentos).
Cuenta cuántos artículos hay de cada tipo y calcula el porcentaje que representa
cada categoría sobre el total.
"""
n = int(input("Cantidad total de articulos: "))

    # Contadores para cada tipo de producto.
    electronica = ropa = alimentos = 0

    for i in range(1, n + 1):
        print("\n1. Electronica  2. Ropa  3. Alimentos")
        tipo = int(input(f"Codigo del articulo {i}: "))

        # Se incrementa el contador según el código ingresado.
        if tipo == 1:
            electronica += 1
        elif tipo == 2:
            ropa += 1
        elif tipo == 3:
            alimentos += 1
        else:
            print("Codigo no valido; el articulo no se contabilizo.")

    # Se calcula el porcentaje solo si se registró al menos un artículo.
    if n > 0:
        print(f"\nElectronica: {electronica} ({electronica / n * 100:.2f}%)")
        print(f"Ropa: {ropa} ({ropa / n * 100:.2f}%)")
        print(f"Alimentos: {alimentos} ({alimentos / n * 100:.2f}%)")
    else:
        print("No hay articulos para contabilizar.")
