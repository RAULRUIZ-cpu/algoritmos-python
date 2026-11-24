"""
5. Inventario y conteo por tipo de producto: En una bodega hay un lote de 𝑁 artículos
clasificados por su tipo mediante un código (1: Electrónica, 2: Ropa, 3: Alimentos).
Cuenta cuántos artículos hay de cada tipo y calcula el porcentaje que representa
cada categoría sobre el total.
"""
n = int(input("¿Cuántos artículos hay en el inventario? "))

# Contadores por categoría
electronica = 0
ropa = 0
alimentos = 0

# Registrar cada artículo
for i in range(1, n + 1):
    print(f"\nArtículo {i}:")
    print("  1 - Electrónica")
    print("  2 - Ropa")
    print("  3 - Alimentos")
    codigo = int(input("  Ingresa el código: "))
    if codigo == 1:
        electronica += 1
    elif codigo == 2:
        ropa += 1
    elif codigo == 3:
        alimentos += 1
    else:
        print("  Código inválido, vuelve a intentar.")

# Calcular porcentajes
porc_e = (electronica / n) * 100
porc_r = (ropa / n) * 100
porc_a = (alimentos / n) * 100

# Mostrar reporte
print(f"Electrónica: {electronica} artículos | {porc_e:.1f}%")
print(f"Ropa       : {ropa} artículos | {porc_r:.1f}%")
print(f"Alimentos  : {alimentos} artículos | {porc_a:.1f}%")
print(f"TOTAL      : {n} artículos")
