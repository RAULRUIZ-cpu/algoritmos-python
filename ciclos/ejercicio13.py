# Realice un algoritmo para generar e imprimir los números pares que se encuentran entre 0 y 100.
print("Números pares entre 0 y 100:")
print("-" * 30)

# Opción 1: Recorriendo de 2 en 2 (más eficiente)
for numero in range(0, 101, 2):
    print(numero)

print("-" * 30)
print(f"Total de números pares: {len(range(0, 101, 2))}")
